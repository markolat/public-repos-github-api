
// Gets cookie by name from browser

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// On-document-ready section//

$(function () {

  // Ajax setup //

  $.ajaxSetup({
    beforeSend: function (xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
  });

  // Ajax api call - fetch repositories//

  $("#load-data-btn").on("click", function (e) {

    e.preventDefault();

    if (!$("#username-input")[0].checkValidity()) {
      $("#username-input")[0].reportValidity();
      return;
    }

    $('.loader').css('display', 'block');
    $('#message-index').html('');

    var username = $("#username-input").val();

    $.ajax({
      url: `/api/repositories`,
      method: 'GET',
      data: {
        'username': username,
      },
      success: (response) => {
        $('.loader').css('display', 'none');
        $('#message-index').html(
          `<article class="message">
                        <div class="message-body">
                            ${response.message}
                        </div>
                    </article>
                    <div>
                        <a class="button" href="repositories">List repositories</a>
                        <a class="button" href="repositories/change-name">Change repository name</a>
                    </div>`
        );
      },
      error: (xhr, response) => {
        $('.loader').css('display', 'none');
        $('#message-index').html(
          `<article class="message">
                        <div class="message-body">
                            Error while collecting data
                        </div>
                    </article>`
        );
      },
    });

  });

  // Ajax api call - change repo name //

  $("#change-name-btn").on("click", function (e) {

    e.preventDefault();

    if (!$("#repository-id-input")[0].checkValidity()) {
      $("#repository-id-input")[0].reportValidity();
      return;
    }

    if (!$("#new-name-input")[0].checkValidity()) {
      $("#new-name-input")[0].reportValidity();
      return;
    }

    var id = $("#repository-id-input").val();
    var newName = $("#new-name-input").val();

    $.ajax({
      url: `/api/repositories/change-name`,
      method: 'POST',
      data: {
        'id': id,
        'new-name': newName
      },
      success: (response) => {

        $('#message-change-repo-name').html(
          `<article class="message">
                        <div class="message-body">
                            Repository name changed successfuly
                        </div>
                    </article>`
        );

      },
      error: (response) => {
        var message = 'Something went wrong. Repository name unchanged!'
        if (response.status == 404) {
          message = 'Repository with that id not found.'
        }
        $('#message-change-repo-name').html(
          `<article class="message">
                        <div class="message-body">
                            ${message}
                        </div>
                    </article>`
        );
      },
    });

  });

});