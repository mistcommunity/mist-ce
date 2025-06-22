import '@polymer/polymer/polymer-legacy.js';
import '@polymer/paper-input/paper-input.js';
import '@polymer/paper-button/paper-button.js';
import '@polymer/paper-icon-button/paper-icon-button.js';
import '@polymer/paper-spinner/paper-spinner.js';
import '@polymer/paper-material/paper-material.js';
import '@polymer/iron-form/iron-form.js';
import '@polymer/iron-icon/iron-icon.js';
import '@polymer/iron-icons/iron-icons.js';
import '@polymer/iron-icons/social-icons.js';
import '@polymer/iron-ajax/iron-ajax.js';
import '@polymer/iron-flex-layout/iron-flex-layout.js';

import { Polymer } from '@polymer/polymer/lib/legacy/polymer-fn.js';
import { html } from '@polymer/polymer/lib/utils/html-tag.js';



Polymer({
  _template: html`
    <style>
      :host {
        background-color: #fff;
        padding-top: 100px;
      }

      [hidden] {
        display: none !important;
      }

      h1 {
        text-align: center;
        font-weight: var(--form-h1-weight);
        font-family: Roboto, sans;
        font-size: 36px;
      }

      a {
        color: var(--link-color);
        cursor: pointer;
        text-decoration: none;
      }

      paper-button {
        width: 100%;
        margin-top: 8px;
        color: #bbb;
        font-weight: 500;
        font-size: 16px;
        margin: 24px auto 16px;
        text-align: center;
        height: 46px;
        display: block;
        width: 305px;
        padding-left: 4px;
      }

      paper-button > iron-icon {
        padding: 7px;
        background-color: #fff;
        float: left;
        margin-top: -7px;
      }

      .textBtn {
        padding-left: 7px;
      }

      paper-button > span {
        width: 100%;
      }

      paper-spinner {
        width: 16px;
        height: 16px;
        margin: 0 auto;
      }

      paper-button[disabled] {
        opacity: var(--form-button-opacity-disabled, 1);
      }

      paper-button:not([disabled]) {
        background-color: var(--app-accent-color);
        color: #fff;
      }

      paper-button.white:not([disabled]) {
        background-color: #fff;
        color: #424242;
      }

      paper-button.white.ldap-selected.true:not([disabled]) {
        background-color: transparent;
        box-shadow: 0 0 0 0 transparent;
        background-color: transparent;
        padding-left: 0;
        margin: 0 0 0 -3px;
      }

      paper-button > span > iron-icon.users {
        color: #444;
        background-color: transparent;
        padding: 7px 2px 7px 12px;
        float: left;
        margin-top: -5px;
      }

      div.output {
        text-align: center;
      }

      paper-material {
        background-color: var(--form-background);
        display: block;
        padding: 8px 32px 32px;
        @apply (--form-elevation);
        width: 300px;
        margin: 0 auto;
        box-shadow: var(--form-box-shadow);
      }

      div.logo-solo {
        width: 220px;
        display: block;
        margin: 0 auto;
        text-align: center;
      }

      div.logo-solo paper-icon-button {
        width: 160px;
        height: 160px;
        padding: 32px;
      }

      div.or {
        margin: 32px auto 0px;
        width: 100px;
        text-align: center;
        text-transform: uppercase;
        font-size: 15px;
        font-weight: 500;
        color: #888;
        display: block;
      }
      .error {
        color: #d96557;
      }
      .success {
        color: #69b46c;
      }
      .forbidden-error {
        font-size: 0.9em;
        margin-bottom: 24px;
      }
      paper-button#logo {
        background-image: var(--vertical-logo);
        background-color: transparent !important;
        background-repeat: no-repeat;
        background-position: center center;
        width: 160px;
        height: 160px;
        padding: 32px;
        border-radius: 50%;
      }
    </style>

    <div id="container">

      <div class="logo-solo">
        <a href="/"><paper-button id="logo" on-tap="_logoClicked"></paper-button></a>
      </div>

      <iron-form id="signInForm">
        <paper-material elevation="1">
          <form
            method="post"
            action="/login"
            enctype="application/json"
            id="form"
          >
            <paper-input
              name="email"
              id="signin-email"
              label="Email"
              auto-validate
              autofocus
              type="email"
              on-focus="_autoSelect"
            >
            </paper-input>

            <paper-input
              name="password"
              id="signin-password"
              label="Password"
              type="password"
              required=""
              auto-validate=""
              on-focus="_autoSelect"
            ></paper-input>

            <paper-button
              raised=""
              on-tap="_submitButtonHandler"
              disabled=""
              id="signInSubmit"
            >
              <paper-spinner
                id="spinner"
                hidden$="[[!loading]]"
                active="[[loading]]"
              ></paper-spinner>
              <div class="output" hidden$="[[loading]]">
                Sign in
              </div>
            </paper-button>

          </form>
        </paper-material>
      </iron-form>

    </div>
  `,

  is: 'auth-sign-in',

  properties: {
    loading: {
      type: Boolean,
      value: false,
    },
    csrfToken: {
      type: String,
      value: '',
    },
  },

  attached() {
    const that = this;

    const validate = event => {
      const ret = that.$.signInForm.validate();
      that.$.signInSubmit.disabled = !ret;
      const outputDiv = that.$.signInForm.querySelector('.output');

      if (!that.loading && outputDiv && outputDiv.innerHTML !== 'Sign in') {
        outputDiv.innerHTML = 'Sign in';
      }
      return ret;
    };

    this.$.signInForm.addEventListener('change', validate);

    this.$.signInForm.addEventListener('keyup', event => {
      const submitDisabled = that.$.signInSubmit.disabled;
      if (validate(event) && !submitDisabled && event.key === 'Enter') {
        that._submitButtonHandler()
      };
    });

    this.$.signInForm.addEventListener('iron-form-error', event => {
      that.loading = false;
      let statusCode = event.detail.request.xhr.status
      let errorMsg = event.detail.error;
      let msg = ''

      switch(statusCode) {
        case 400:
          msg = 'Bad Request';
          break;
        case 401:
          msg = 'Unauthorized';
          break;
        case 403:
          msg = 'Forbidden';
          break;
        case 502:
          msg = 'Bad Gateway';
          break;
        default:
          msg = errorMsg
      }
      that.$.signInForm.querySelector('.output').innerHTML = msg;
    });

    this.$.signInForm.addEventListener('iron-form-response', event => {
      that.loading = false;
      that.$.signInForm.querySelector('.output').innerHTML = 'SUCCESS!';
      window.location = event.detail.response.redirect;
    });

    this.$.signInForm.addEventListener('iron-form-presubmit', () => {
      that.$.signInForm.headers['Csrf-Token'] = this.csrfToken;
    });
  },

  _submitButtonHandler() {
    // this.set('showRequestWhitelist', false);
    this.loading = true;
    this.$.signInSubmit.disabled = true;
    this.$.signInForm.querySelector('.output').innerHTML = '';
    this.$.signInForm.submit();
  },

  _logoClicked() {
    this.fire('user-action', 'logo click on sign-in');
  },

  _autoSelect(event) {
    event.target._focusableElement.select();
  },
});
