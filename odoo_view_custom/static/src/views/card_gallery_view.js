/** @odoo-module **/

import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {Component, useState} from "@odoo/owl";
import {listView} from "@web/views/list/list_view";
import {ListController} from "@web/views/list/list_controller";

export class CardGalleryController extends ListController {
    setup() {
        super.setup();
        this.notification = useService("notification");
    }

    async onClickMyCustomButton() {
        this.notification.add("This is your custom controller acting!", { type: "success" });
    }
}

export class CardGalleryRenderer extends Component {
    static template = "odoo_view_custom.CardGalleryRenderer";
    static props = ["*"];

    get records() {
        return this.props.list.records;
    }

    getImageSrc(record) {
        const id = record.resId;
        const model = record.resModel ?? "product.template";
        if (record.data.image_128 || record.data.image_1920) {
            return `/web/image/${model}/${id}/image_128`;
        }
        return "/web/static/img/placeholder.png";
    }

    getStars(value = 0, max = 5) {
        return Array.from({length: max}, (_, i) => ({
            index: i + 1,
            filled: i < value,
        }));
    }

    formatPrice(record) {
        const price = record.data.list_price;
        const currency = record.data.currency_id;
        if (price === undefined) return null;
        const symbol = currency ? currency[1] : "$";
        return `${symbol} ${parseFloat(price).toFixed(2)}`;
    }

    async onCardClick(record) {
        await this.props.openRecord(record);
    }
}

export class CardGalleryArchParser extends listView.ArchParser {
    parse(xmlDoc, models, modelName) {
        const listDoc = xmlDoc.ownerDocument.createElement("list");
        for (const attr of xmlDoc.attributes) {
            listDoc.setAttribute(attr.name, attr.value);
        }
        while (xmlDoc.firstChild) {
            listDoc.appendChild(xmlDoc.firstChild);
        }
        
        return super.parse(listDoc, models, modelName);
    }
}

export const CardGalleryView = {
    ...listView,
    type: "card_gallery",
    display_name: "Card Gallery",
    icon: "oi-view-kanban",
    Controller: CardGalleryController,
    ArchParser: CardGalleryArchParser,
    Renderer: CardGalleryRenderer,
    buttonTemplate: "odoo_view_custom.CardGalleryButtons",
};

registry.category("views").add("card_gallery", CardGalleryView);