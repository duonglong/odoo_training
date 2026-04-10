/** @odoo-module **/


import { registry }             from "@web/core/registry";
import { standardFieldProps }   from "@web/views/fields/standard_field_props";
import { Component }            from "@odoo/owl";

const MAX_STARS = 5;

export class StarRatingField extends Component {
    static template = "odoo_view_custom.StarRatingField";

    static props = {
        ...standardFieldProps,
        // Optional per-field override: options="{'max': 10}" in the arch
        max: { type: Number, optional: true },
    };

    static defaultProps = {
        max: MAX_STARS,
    };

    get currentValue() {
        return Number(this.props.record.data[this.props.name]) || 0;
    }

    get maxStars() {
        return this.props.max ?? MAX_STARS;
    }

    get stars() {
        const val = this.currentValue;
        return Array.from({ length: this.maxStars }, (_, i) => ({
            index: i + 1,
            filled: i < val,
        }));
    }

    onStarClick(index) {
        if (this.props.readonly) return;
        const newValue = index === this.currentValue ? 0 : index;
        // Odoo 19: write via record.update(), NOT this.props.update()
        this.props.record.update({ [this.props.name]: newValue });
    }

    onStarKeyDown(ev, index) {
        if (this.props.readonly) return;
        if (ev.key === " " || ev.key === "Enter") {
            ev.preventDefault();
            this.onStarClick(index);
        }
    }
}

export const starRatingField = {
    component: StarRatingField,
    supportedTypes: ["integer"],
    displayName: "Star Rating",
    extractProps: ({ attrs, options }) => ({
        max: options.max ? Number(options.max) : MAX_STARS,
    }),
};

registry.category("fields").add("star_rating", starRatingField);
