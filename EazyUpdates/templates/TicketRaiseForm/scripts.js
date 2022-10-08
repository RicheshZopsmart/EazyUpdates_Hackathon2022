$(document).ready(function() { //wait until body loads

    var testimonial_ok = false; //keeps track of whether the testimonial box is filled out
  
    //Inputs that determine what fields to show
    var rating = $('#live_form input:radio[name=rating]');
    var testimonial = $('#live_form input:radio[name=testimonial]');
  
    //Wrappers for all fields
    var bad = $('#live_form textarea[name="feedback_bad"]').parent();
    var ok = $('#live_form textarea[name="feedback_ok"]').parent();
    var great = $('#live_form textarea[name="feedback_great"]').parent();
    var testimonial_parent = $('#live_form #div_testimonial');
    var thanks_anyway = $('#live_form #thanks_anyway');
    var all = bad.add(ok).add(great).add(testimonial_parent).add(thanks_anyway); //shortcut for all wrapper elements
  
    rating.change(function() { //when the rating changes
      var value = this.value;
      all.addClass('hidden'); //hide everything and reveal as needed
  
      if (value == 'return') {
        ok.removeClass('hidden'); //show feedback_ok	
      } else if (value == 'replace') {
        testimonial_parent.removeClass('hidden'); //show testimonial question
  
        //if testimonial has already been answered
        if (testimonial_ok == 'yes') {
          great.removeClass('hidden');
        } else if (testimonial_ok == 'no') {
          thanks_anyway.removeClass('hidden');
        }
      }
    });
  
  
    testimonial.change(function() {
      //hide all except testimonial question
      all.addClass('hidden');
      testimonial_parent.removeClass('hidden');
  
      testimonial_ok = this.value;
  
      if (testimonial_ok == 'yes') { //if user willing to write testimonial
        great.removeClass('hidden'); //show feedback_great
      } else {
        thanks_anyway.removeClass('hidden'); //show thanks message
      }
  
    });
  });
  