$(document).ready(function(){

    $('#sign_up_link').click(function(){

        $('#sign_up').css('display', 'block');
        $('#login').hide();
    });

     $('#login_link').click(function(){

        $('#login').show();
        $('#sign_up').css('display', 'none');
    });

    var x = 1; // Counter for ingredients
    var y = 1; // Counter for method steps
    var maxIngre = 15; // Maximum number of ingredients they can add
    var maxSteps = 20; // Maximum number of steps they can add
    var ingreHtml = '<div class="input-field"><input name="ingredient" id="ingredient" class="extra_ingre" type="text"/></div>'; // Ingredient html input field
    var methodHtml = '<div class="input-field"><input name="method" id="method" class="extra_method" type="text"/></div>'; // Method html input field

    // Add another line under ingredient when the plus button is clicked
    $('#add_ingredient').click(function(){

            if (x < maxIngre) {
            x++;
            $('.ingre_wrapper').append(ingreHtml)
            }
    });

    // Add another line under method when the plus button is clicked
    $('#add_method').click(function(){

        if (y < maxSteps) {
        y++;
        $('.method_wrapper').append(methodHtml)
        }
    });

    // Remove ingredient
    $('#remove_ingredient').click(function(){
        $('.extra_ingre').last().remove();
    });

     // Remove method
    $('#remove_method').click(function(){
        $('.extra_method').last().remove();
    });

});