$(function() {
  $(".card:first").hide()
  $.ajax({
    url: "/static/json/info_teacher.json",
    success: function(result) {
      $.each(result, function(index, item) {
      for (i = 0; i < item.length; i++){
        var cards = $(".card:first").clone()
        var full_name = item[i].full_name;
        var post = item[i].post;
        var department = item[i].department;
        var id = item[i].index;
        var elms = document.querySelectorAll("[id='id']");

        if (i === item.length - 1) {
            elms[i].value = item[0].index;
        } else {
            elms[i].value = item[i+1].index;
            }
<<<<<<< HEAD
        $(cards).find(".full_name").html(full_name);
        $(cards).find(".post_department").html(department + ", " + post);
=======
        $(cards).find(".card-title").html(full_name);
        $(cards).find(".card-text").html(department + ", " + post);
>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873
        $(cards).show()
        $(cards).appendTo($(".info_teacher"))
        }
      });
    }
  });
});