
  document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'timeGridWeek',
      headerToolbar: {
<<<<<<< HEAD
        left: 'prev',
        center: 'title',
        right: 'next'
      },
      height: 'auto',
      editable: false,
      selectable: false,
      selectMirror: true,
      nowIndicator: true,
      eventSources: [
    {
      url: 'static/json/answer.json'
    }]
    });
=======
        left: '',
        center: 'title',
        right: ''
      },
      height: 'auto',
      editable: true,
      selectable: false,
      selectMirror: true,
      nowIndicator: true,
        eventSources: [
    {
      url: 'static/json/answer.json'
    }
  ]
    });

>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873
    calendar.render();
  });

