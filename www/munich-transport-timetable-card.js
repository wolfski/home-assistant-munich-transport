// Munich Transport Timetable Card

class MunichTransportTimetableCard extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({
            mode: 'open'
        });
    }

    /* This is called every time sensor is updated */
    set hass(hass) {

        const config = this.config;
        const maxEntries = config.max_entries || 10;
        const showStopName = config.show_stop_name || true;
        const entityIds = config.entity ? [config.entity] : config.entities || [];
        const directionMaxLen = config.direction_name_max_length || 30;

        let content = "";

        for (const entityId of entityIds) {
            const entity = hass.states[entityId];
            if (!entity) {
                throw new Error("Entity State Unavailable");
            }

            if (showStopName) {
                content += `<div class="stop">${entity.attributes.friendly_name}</div>`;
            }
            /*
                    <div class="line-icon" style="background-color: ${departure.color}">${departure.line_name}</div>
             */
            const timetable = entity.attributes.departures.slice(0, maxEntries).map((departure) =>
                `<div class="departure">
                    <div class="line">
                    <div class="line-icon ${departure.line_code} ${departure.line_code}_${departure.line_name}">${departure.line_name}</div>
                    </div>
                    <div class="direction">${(departure.direction.length > directionMaxLen)
                    ? departure.direction.slice(0, directionMaxLen - 3) + '...'
                    : departure.direction}</div>
                    <div class="departure_time">${departure.departure_time}</div>
                    <div class="time">${departure.time}</div>

                </div>`
            );

            content += `<div class="departures">` + timetable.join("\n") + `</div>`;
        }

        this.shadowRoot.getElementById('container').innerHTML = content;
    }

    /* This is called only when config is updated */
    setConfig(config) {
        const root = this.shadowRoot;
        if (root.lastChild) root.removeChild(root.lastChild);

        this.config = config;

        const card = document.createElement('ha-card');
        const content = document.createElement('div');
        const style = document.createElement('style')

        style.textContent = `
            .container {
                padding: 10px;
                font-size: 130%;
                line-height: 1.5em;
            }
            .stop {
                opacity: 0.6;
                font-weight: 400;
                width: 100%;
                text-align: left;
                padding: 10px 10px 5px 5px;
            }      
            .departures {
                width: 100%;
                font-weight: 400;
                line-height: 1.5em;
                padding-bottom: 20px;
            }
            .departure {
                padding-top: 10px;
                display: flex;
                flex-direction: row;
                flex-wrap: nowrap;
                align-items: flex-start;
                gap: 20px;
            }
            .line {
                min-width: 70px;
                text-align: right;
            }
            .line-icon {
                display: inline-block;
                padding: 7px 10px 5px;
                font-size: 120%;
                font-weight: 700;
                line-height: 1em;
                color: #FFFFFF;
                background-color: #FF6666;
                text-align: center;
            }

            .S {
                border-radius: 20px;
            }
            .U {
                border-radius: 5px;
            }
            .M {
                border-radius: 0px;
            }
            .BUS {
                border-radius: 0px;
                background-color: #3300CC;
                color: #FFFFFF;
                border: 1px solid #FFFFFF;
            }

            .U_U1 {
                background-color: #336633;
            }
            .U_U2 {
                background-color: #CC0033;
            }
            .U_U3 {
                background-color: #FF6633;
            }
            .U_U4 {
                background-color: #339966;
            }
            .U_U5 {
                background-color: #996600;
            }
            .U_U6 {
                background-color: #3366CC;
            }
            .U_U7 {
                background-color: #336600;
            }
            .U_U8 {
                background-color: #CC0033;
            } 

            .S_S1 {
                background-color: #57B7E2;
            }
            .S_S2 {
                background-color: #84B645;
            }
            .S_S3 {
                background-color: #89277D;
            }
            .S_S4 {
                background-color: #D12D26;
            }
            .S_S6 {
                background-color: #429564;
            }
            .S_S7 {
                background-color: #89392C;
            }
            .S_S8 {
                background-color: #000000;
                color: #FFCB01;
            }
            .S_S20 {
                background-color: #FF3366;
            }

            .M_12 {
                background-color: #993399;
            }
            .M_16 {
                background-color: #0066CC;
            }
            .M_17 {
                background-color: #663333;
            }       
            .M_18 {
                background-color: #009933;
            }
            .M_19 {
                background-color: #FF0033;
            }
            .M_20 {
                background-color: #0099CC;
            } 
            .M_21 {
                background-color: #996600;
            }       
            .M_23 {
                background-color: #99CC33;
            }
            .M_25 {
                background-color: #CC6666;
            }
            .M_27 {
                background-color: #FF9900;
            }             
            .M_28 {
                background-color: #FFFFFF;
                color: #FF9900;
            }       
            .M_29 {
                background-color: #FFFFFF;
                color: #CC0000;
            }
            .M_E7 {
                background-color: #FFFFFF;
                color: #000000;
            }
            .M_N17 {
                background-color: #656565;
                color: #FDEE00; 
            }
            .M_N19 {
                background-color: #656565;
                color: #FDEE00; 
            }
            .M_N20 {
                background-color: #656565;
                color: #FDEE00; 
            }
            .M_N27 {
                background-color: #656565;
                color: #FDEE00; 
            }

            .direction {
                align-self: center;
                flex-grow: 1;
            }
            .time {
                align-self: flex-start;
                font-weight: 700;
                line-height: 2em;
                padding-right: 10px;
            }
            .departure_time {
                align-self: center;
                font-weight: 700;
                line-height: 2em;
                padding-right: 10px;
            }
        `;

        content.id = "container";
        content.className = "container";
        card.header = config.title;
        card.appendChild(style);
        card.appendChild(content);

        root.appendChild(card);
    }

    // The height of the card.
    getCardSize() {
        return 5;
    }
}

customElements.define('munich-transport-timetable-card', MunichTransportTimetableCard);
