class CKEditorHelper {

    prefix = "";
    elementName = "";

    get elementId() {
        return `${this.prefix}_${this.elementName}`;
    }

    get elementButtonId() {
        return `${this.prefix}_button`;
    }

    get elementValidationId() {
        return `${this.elementId}_validation`
    }

    get elementFormId() {
        return `${this.prefix}_form`;
    }

    createEditor(prefix, elementName){

        this.prefix = prefix;
        this.elementName = elementName;

        ClassicEditor
            .create(document.getElementById(this.elementId), {
                toolbar: {
                    items: [
                        'undo', 'redo',
                        '|', 'heading',
                        '|', 'bold', 'italic',
                        '|', 'link', 'blockQuote',
                        '|', 'bulletedList', 'numberedList','outdent', 'indent'
                    ],
                    //shouldNotGroupWhenFull: false
                }
            })
            .then(editor => {
                document.getElementById(this.elementButtonId)
                    .addEventListener('click', (e) => this.handleFormSubmit(e, editor));
    
                editor.model.document.on('change:data', () => {
                    const editorData = editor.getData();

                    let validationElement = document.getElementById(this.elementValidationId);
                    if (editorData.trim() && !validationElement.classList.contains("d-none")) {
                        validationElement.classList.add("d-none");
                    }
                });
            })
            .catch( error => {
                console.error( error );
            });
    }
    
    handleFormSubmit(event, editor){
        const editorData = editor.getData();
    
        // Check if the editor data is empty
        if (!editorData.trim()) {
            event.preventDefault();
            document.getElementById(this.elementValidationId).classList.remove("d-none");
            return false;
        }
    
        // Update the hidden field value just before submitting
        document.getElementById(this.elementId).value = editorData;
    
        // Submit the form
        document.getElementById(this.elementFormId).submit();
    }

}