# Rainbow Runners - Testing
![Image](resources/mockup.png)
***
**Contents**
- [Rainbow Runners - Testing](#rainbow-runners---testing)
  - [Responsiveness](#responsiveness)
  - [Validations](#validations)
    - [W3C Validator](#w3c-validator)
    - [JSHint](#jshint)
    - [Python Linter](#python-linter)
    - [Validation Summary](#validation-summary)
  - [Lighthouse](#lighthouse)
  - [Wave](#wave)
  - [Browser Compatibility](#browser-compatibility)
***
## Responsiveness
This website has been tested on a wide range of screen sizes from various manufacturers to account for the differences between them. It’s crucial to test website responsiveness due to the web being mostly accessed using mobile devices. A responsive website guarantees a uniform user experience across different screen sizes and resolutions, making it easy for visitors to access and navigate the site, regardless of the device they’re using. Additionally, responsive design enhances search engine optimization (SEO), as search engines prioritize mobile-friendly sites in their rankings. The testing has been carried out using the device list on the chrome developer tools.
<br>
<br>
The resolutions tested as as follows:<br>
Galaxy S III: 360 x 640<br>
Iphone SE: 375 x 667<br>
Iphone 12 Pro: 390 x 844<br>
Moto G Power: 412 x 823<br>
Ipad Air: 768 x 1024<br>
Nexus 10: 800 x 1280<br>
Desktop 1080p: 1920 x 1080<br>


***
## Validations
### W3C Validator
Testing has been completed using the W3C code validators to ensure that the code used is clean, consistent and adheres to best practices. No warnings or errors were found and the results can be found below.<br>
<br>
1. [Home Page Validation](resources/validations/home-page.PNG)
2. [About Us Page Validation](resources/validations/about-us.PNG)
3. [Contact Us Page Validation](resources/validations/contact-us.PNG)
4. [Resources Page Validation](resources/validations/resources.PNG)
5. [Club Shop Page Validation](resources/validations/club-shop.PNG)
6. [Product Details Page Validation](resources/validations/product-detail.PNG)
7. [Add Product Page Validation](resources/validations/add-product.PNG)
8. [Edit Product Page Validation](resources/validations/edit-product.PNG)
9. [Edit Product Info Page Validation](resources/validations/edit-product-info.PNG)
10. [Checkout Page Validation](resources/validations/checkout.PNG)
11. [Checkout Success Page Validation](resources/validations/checkout-success.PNG)
12. [Shopping Basket Page Validation](resources/validations/shopping-basket.PNG)
13. [Log In Page Validation](resources/validations/login.PNG)
14. [Sign Up Page Validation](resources/validations/sign-up.PNG)
15. [View Questions Page Validation](resources/validations/view-questions.PNG)
16. [Club Posts Page Validation](resources/validations/club-posts.PNG)
17. [Comments Page Validation](resources/validations/comments.PNG)
18. [Profile Page Validation](resources/validations/profile.PNG)
19. [CSS Validation](resources/validations/css-validation.PNG)
<br>
### JSHint
Quality testing of the JavaScript code has been carried out using [JSHint](https://jshint.com/). Before testing please ensure the checkboxes next to "New JavaScript features (ES6)" and "jQuery" have been turned on. To do this please click "CONFIGURE" and if needed click "New JavaScript features (ES6)" and "jQuery".

**_script.js_**<br>
![Image](resources/validations/scripts.PNG)

**_ckeditor.js_**<br>   
![Image](resources/validations/ckeditor.PNG)

**_quantity_input_script_**<br>
![Image](resources/validations/quantity-input.PNG)                                           

**_stripe_elements.js_**<br>
![Image](resources/validations/stripe.PNG)

### Python Linter                                                   
The Code Institute Python Linter has been used to validate the python code. No errors were found and the results can be seen by clicking the links below.<br>
1. [template_env.py](resources/validations/python-linter/template_env.PNG)
2. [rainbow-runners/urls.py](resources/validations/python-linter/urls.PNG)
3. [profiles/views.py](resources/validations/python-linter/profiles-views.PNG)
4. [profiles/urls.py](resources/validations/python-linter/profiles-urls.PNG)
5. [profiles/models.py](resources/validations/python-linter/profiles-models.PNG)
6. [profiles/forms.py](resources/validations/python-linter/profiles-forms.PNG)
7. [profiles/apps.py](resources/validations/python-linter/profiles-apps.PNG)
8. [profiles/role_context_processor.py](resources/validations/python-linter/role_context_processor.PNG)
9. [products/widgets.py](resources/validations/python-linter/products-widgets.PNG)
10. [products/views.py](resources/validations/python-linter/products-views.PNG)
11. [products/urls.py](resources/validations/python-linter/products-urls.PNG)
12. [products/models.py](resources/validations/python-linter/products-models.PNG)
13. [products/forms.py](resources/validations/python-linter/products-forms.PNG)
14. [products/admin.py](resources/validations/python-linter/products-admin.PNG)
15. [posts/views.py](resources/validations/python-linter/posts-views.PNG)
16. [posts/urls.py](resources/validations/python-linter/posts-urls.PNG)
17. [posts/models.py](resources/validations/python-linter/posts-models.PNG)
18. [posts/forms.py](resources/validations/python-linter/posts-forms.PNG)
19. [posts/admin.py](resources/validations/python-linter/posts-admin.PNG)
20. [home/views.py](resources/validations/python-linter/home-views.PNG)
21. [home/urls.py](resources/validations/python-linter/home-urls.PNG)
22. [contact/views.py](resources/validations/python-linter/contact-views.PNG)
23. [contact/urls.py](resources/validations/python-linter/contact-urls.PNG)
24. [contact/forms.py](resources/validations/python-linter/contact-forms.PNG)
25. [checkout/webhooks.py](resources/validations/python-linter/checkout-webhooks.PNG)
26. [checkout/webhook_handler.py](resources/validations/python-linter/checkout-webhook-handler.PNG)
27. [checkout/views.py](resources/validations/python-linter/checkout-views.PNG)
28. [checkout/urls.py](resources/validations/python-linter/checkout-urls.PNG)
29. [checkout/signals.py](resources/validations/python-linter/checkout-signals.PNG)
30. [checkout/models.py](resources/validations/python-linter/checkout-models.PNG)
31. [checkout/forms.py](resources/validations/python-linter/checkout-forms.PNG)
32. [checkout/apps.py](resources/validations/python-linter/checkout-apps.PNG)
33. [checkout/admin.py](resources/validations/python-linter/checkout-admin.PNG)
34. [bag/views.py](resources/validations/python-linter/bag-views.PNG)
35. [bag/urls.py](resources/validations/python-linter/bag-urls.PNG)
36. [bag/contexts.py](resources/validations/python-linter/bag-contexts.PNG)          

### Validation Summary
![Image](resources/validations/validation-summary.PNG)
***
## Lighthouse                                             
The lighthouse results can be found for each page below.                        

![Image](resources/lighthouse/lighthouse-test-one.PNG)                   
![Image](resources/lighthouse/lighthouse-test-two.PNG)                         
![Image](resources/lighthouse/lighthouse-test-three.PNG)                         
![Image](resources/lighthouse/lighthouse-test-four.PNG)                          
![Image](resources/lighthouse/lighthouse-test-five.PNG)                           
***
## Wave
The Wave tool has been completed with no errors or contrast errors found.                              
                                   
![Image](resources/wave/wave-results-one.PNG)
![Image](resources/wave/wave-results-two.PNG)
![Image](resources/wave/wave-results-three.PNG)
![Image](resources/wave/wave-results-four.PNG)
![Image](resources/wave/wave-results-five.PNG)
![Image](resources/wave/wave-results-six.PNG)
![Image](resources/wave/wave-results-severn.PNG)
***
## Browser Compatibility
Testing has been carried out on the browsers within the below table as these browsers are most used, but in addition to this Firefox uses Gecko rendering engine while the others use WebKit. This helps identify any inconsistencies or rendering discrepancies that may arise due to variations in the rendering engines.        
                                                                    
![Image](resources/browser-compatibility.PNG)
***


