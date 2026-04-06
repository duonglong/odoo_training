import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("student_record_tour", {
    // url: "/odoo/action-90",
    steps: () => [
        {
            trigger:  ".o_list_view",
            content:  "Student Records list view is loaded",
            run: () => {},
        },
        {
            trigger: ".o_list_button_add",
            content: "Let's add a new visitor.",
            tooltipPosition: "bottom",
            run: "click",
        },
        {
            trigger:  ".o_form_view",
            content:  "Form view is open and ready",
            run: () => {},
        },
        {
            trigger:  ".o_field_widget[name='name'] input",
            content:  "Step 4 — Type the student's name",
            run:      "edit Duong Long",
        },

        {
            trigger:  ".o_field_widget[name='date_of_birth'] input",
            content:  "Type a description",
            run:      "edit 15/06/1993",
        },

        {
            trigger:  ".o_form_button_save",
            content:  "Save the record",
            run:      "click",
        },
        {
            trigger:  ".o_form_saved",
            content:  "Record saved successfully (form is in view mode)",
            run: () => {},
        }
    ]
});