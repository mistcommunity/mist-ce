import '@polymer/polymer/polymer-legacy.js';
import '@polymer/app-route/app-location.js';
import '@polymer/app-route/app-route.js';
import '@polymer/iron-pages/iron-pages.js';

import { Polymer } from '@polymer/polymer/lib/legacy/polymer-fn.js';
import { html } from '@polymer/polymer/lib/utils/html-tag.js';

import './auth-sign-in.js';
import './shared-styles.js';
import './mist-theme.js'



Polymer({
  _template: html`
    <style>
      :host {
        display: block;
        width: 100%;
        height: 100vh;
        box-sizing: border-box;
      }
    </style>

    <app-location
      route="{{route}}"
    ></app-location>

    <app-route
      route="{{route}}"
      pattern="/:page"
      data="{{routeData}}"
    ></app-route>

    <iron-pages
      selected="{{page}}"
      attr-for-selected="name"
      fallback-selection="sign-in"
      role="main"
    >
    
    <auth-sign-in
      name="sign-in"
      route="[[route]]"
      sign-in-email=[[config.features.signin_email]]
      csrf-token="[[csrfToken]]"
    ></auth-sign-in>

    </iron-pages>
  `,

  is: 'auth-app',

  properties: {
    route: Object,
    routeData: Object,
    page: {
      type: String,
      reflectToAttribute: true,
      value: 'sign-in'
    },
    config: {
      type: Object,
      value() {
        return {};
      }
    }
  },

  observers: [
    '_routePageChanged(routeData.page)'
  ],

  _routePageChanged(page) {
    this.page = page || 'sign-in';
  }
});