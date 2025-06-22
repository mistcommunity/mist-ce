const documentContainer = document.createElement('template');

documentContainer.innerHTML = `<dom-module id="shared-styles">
    <template>
        <style>
    :host > * {
      font-size: 16px;
      font-weight: 400;
      -ms-text-size-adjust: 100%;
      -webkit-text-size-adjust: 100%;
      -webkit-font-smoothing: antialiased;
      box-sizing: border-box;
    }

    :host > *, :after, :before {
      box-sizing: inherit; 
    }
    @media only screen and (min-width: 0) {
      :host > * {
        font-size: 14px;
      }
    }

    @media only screen and (min-width: 992px) {
      :host > * {
        font-size: 14.5px;
      }
    }

    @media only screen and (min-width: 1200px) {
      :host > * {
        font-size: 15px;
      }
    }
    :host > *, .section {
        font-size: 18px !important;
        line-height: 1.5;
    }
    h1, h2, h3, h4, h5, h6 {
      font-weight: 300;
      line-height: 1.1;
    }

    h5, h6, p {
      font-weight: 400;
    }

    h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
      font-weight: inherit;
    }

    h1 {
      font-size: 4.2rem;
      line-height: 110%;
      margin: 2.1rem 0 1.68rem 0;
    }

    h2 {
      font-size: 3.56rem;
      line-height: 110%;
      margin: 1.78rem 0 1.424rem 0;
    }

    h3 {
      font-size: 2.92rem;
      line-height: 110%;
      margin: 1.46rem 0 1.168rem 0;
    }

    h4 {
      font-size: 2.28rem;
      line-height: 110%;
      margin: 1.14rem 0 0.912rem 0;
    }

    h5 {
      font-size: 1.64rem;
      line-height: 110%;
      margin: 0.82rem 0 0.656rem 0;
    }

    h6 {
      font-size: 1rem;
      line-height: 110%;
      margin: 0.5rem 0 0.4rem 0;
    }
    .with-shadow {
      @apply(--shadow-elevation-2dp);
    }
    
    a {
      text-decoration: none;
      color: #09c !important;
      outline: none;
    }

    img {
      max-width: 100%;
    }

    marked-element::content a {
      text-decoration: none !important;
      color: #09c !important; 
    }

    [slot="marked-element"] a {
      text-decoration: none;
      color: var(--app-accent-color) !important;
    }

    sub,
    sup {
      font-size: 75%;
      line-height: 0;
      position: relative;
      vertical-align: baseline;
    }

    sup {
      top: -0.5em;
    }

    sub {
      bottom: -0.25em;
    }

    paper-dialog-scrollable {
      display: block;
      overflow-y: scroll;
    }

    @media only screen and (max-width: 993px) {
      body {
        font-size: 16px !important;
      }
    }

    paper-button {
      letter-spacing: .5px;
    }

    .w200 {
      font-weight: 200;
    }

    .w300 {
      font-weight: 300;
    }

    .w400 {
      font-weight: 400;
    }

    .w500 {
      font-weight: 500;
    }

    .line1 {
      line-height: 1em;
      margin: 0;
    }

    .right {
      float: right;
    } 
    .right-align {
        text-align: right;
    }
    .indent-40 {
        text-indent: 40px;
    }

    .text-center {
      text-align: center;
    }

    .valign-wrapper {
      display: -webkit-flex;
      display: -ms-flexbox;
      display: flex;
      -webkit-align-items: center;
          -ms-flex-align: center;
              align-items: center;
    }

    .valign-wrapper .valign {
      display: block;
    }

    .section > * {
      max-width: 1180px;
      margin: 0 auto;
      padding: 48px 0;
      width: 90%;
      box-sizing: border-box;
    }

    .section.grey {
      background-color: var(--app-background-color);
      color: var(--app-section-primary-color);
    }

    .section.white {
      background-color: var(--app-background-secondary-color);
      color: var(--app-section-secondary-color);
    }

    .section.dark {
      background-color: var(--app-background-highlight-color);
      color: var(--app-highlight-color);
    }

    .row {
      margin-bottom: 24px;
    }

    .row:after {
      content: "";
      display: table;
      clear: both;
    }

    .decorated {
      position: relative;
    }

    .decorated:after {
      content: "";
      position: absolute;
      display: inline-block;
      width: 80px;
      border-bottom: 2px solid;
      border-color: inherit;
      bottom: -20px;
      margin: 0 auto;
      left: 0;
      right: 0;
      transition: all .3s ease-in-out;
    }

    .decorated:hover:after {
      width: 160px;
    }

    .secondary {
      -webkit-font-smoothing: antialiased;
      font-size: 14px;
      font-weight: 400;
      line-height: 20px;
      color: #737373;
    }

    .items-center {
      align-items: center;
    }

    .fluid {
      margin-right: auto;
      margin-left: auto;
      padding-right: 2rem;
      padding-left: 2rem;
    }

    .grid-row {
      box-sizing: border-box;
      display: -webkit-flex;
      display: -ms-flexbox;
      display: -webkit-box;
      display: flex;
      -webkit-flex: 0 1 auto;
      -ms-flex: 0 1 auto;
      -webkit-box-flex: 0;
      flex: 0 1 auto;
      -webkit-flex-direction: row;
      -ms-flex-direction: row;
      -webkit-box-orient: horizontal;
      -webkit-box-direction: normal;
      flex-direction: row;
      -webkit-flex-wrap: wrap;
      -ms-flex-wrap: wrap;
      flex-wrap: wrap;
      margin-right: -1rem;
      margin-left: -1rem;
    }

    .grid-row.reverse {
      -webkit-flex-direction: row-reverse;
      -ms-flex-direction: row-reverse;
      -webkit-box-orient: horizontal;
      -webkit-box-direction: reverse;
      flex-direction: row-reverse;
    }

    .grid-col.reverse {
      -webkit-flex-direction: column-reverse;
      -ms-flex-direction: column-reverse;
      -webkit-box-orient: vertical;
      -webkit-box-direction: reverse;
      flex-direction: column-reverse;
    }

    .xs,
    .xs1,
    .xs2,
    .xs3,
    .xs4,
    .xs5,
    .xs6,
    .xs7,
    .xs8,
    .xs9,
    .xs10,
    .xs11,
    .xs12 {
      box-sizing: border-box;
      -webkit-flex: 0 0 auto;
      -ms-flex: 0 0 auto;
      -webkit-box-flex: 0;
      flex: 0 0 auto;
      padding-right: 1rem;
      padding-left: 1rem;
    }

    .xs {
      -webkit-flex-grow: 1;
      -ms-flex-positive: 1;
      -webkit-box-flex: 1;
      flex-grow: 1;
      -ms-flex-preferred-size: 0;
      -webkit-flex-basis: 0;
      flex-basis: 0;
      max-width: 100%;
    }

    .xs1 {
      -ms-flex-preferred-size: 8.333%;
      -webkit-flex-basis: 8.333%;
      flex-basis: 8.333%;
      max-width: 8.333%;
    }

    .xs2 {
      -ms-flex-preferred-size: 16.667%;
      -webkit-flex-basis: 16.667%;
      flex-basis: 16.667%;
      max-width: 16.667%;
    }

    .xs3 {
      -ms-flex-preferred-size: 25%;
      -webkit-flex-basis: 25%;
      flex-basis: 25%;
      max-width: 25%;
    }

    .xs4 {
      -ms-flex-preferred-size: 33.333%;
      -webkit-flex-basis: 33.333%;
      flex-basis: 33.333%;
      max-width: 33.333%;
    }

    .xs5 {
      -ms-flex-preferred-size: 41.667%;
      -webkit-flex-basis: 41.667%;
      flex-basis: 41.667%;
      max-width: 41.667%;
    }

    .xs6 {
      -ms-flex-preferred-size: 50%;
      -webkit-flex-basis: 50%;
      flex-basis: 50%;
      max-width: 50%;
    }

    .xs7 {
      -ms-flex-preferred-size: 58.333%;
      -webkit-flex-basis: 58.333%;
      flex-basis: 58.333%;
      max-width: 58.333%;
    }

    .xs8 {
      -ms-flex-preferred-size: 66.667%;
      -webkit-flex-basis: 66.667%;
      flex-basis: 66.667%;
      max-width: 66.667%;
    }

    .xs9 {
      -ms-flex-preferred-size: 75%;
      -webkit-flex-basis: 75%;
      flex-basis: 75%;
      max-width: 75%;
    }

    .xs10 {
      -ms-flex-preferred-size: 83.333%;
      -webkit-flex-basis: 83.333%;
      flex-basis: 83.333%;
      max-width: 83.333%;
    }

    .xs11 {
      -ms-flex-preferred-size: 91.667%;
      -webkit-flex-basis: 91.667%;
      flex-basis: 91.667%;
      max-width: 91.667%;
    }

    .xs12 {
      -ms-flex-preferred-size: 100%;
      -webkit-flex-basis: 100%;
      flex-basis: 100%;
      max-width: 100%;
    }

    @media only screen and (min-width: 48em) {
      .grid {
        width: 46rem;
      }

      .s,
      .s1,
      .s2,
      .s3,
      .s4,
      .s5,
      .s6,
      .s7,
      .s8,
      .s9,
      .s10,
      .s11,
      .s12 {
        box-sizing: border-box;
        -webkit-flex: 0 0 auto;
        -ms-flex: 0 0 auto;
        -webkit-box-flex: 0;
        flex: 0 0 auto;
        padding-right: 1rem;
        padding-left: 1rem;
      }

      .s {
        -webkit-flex-grow: 1;
        -ms-flex-positive: 1;
        -webkit-box-flex: 1;
        flex-grow: 1;
        -ms-flex-preferred-size: 0;
        -webkit-flex-basis: 0;
        flex-basis: 0;
        max-width: 100%;
      }

      .s1 {
        -ms-flex-preferred-size: 8.333%;
        -webkit-flex-basis: 8.333%;
        flex-basis: 8.333%;
        max-width: 8.333%;
      }

      .s2 {
        -ms-flex-preferred-size: 16.667%;
        -webkit-flex-basis: 16.667%;
        flex-basis: 16.667%;
        max-width: 16.667%;
      }

      .s3 {
        -ms-flex-preferred-size: 25%;
        -webkit-flex-basis: 25%;
        flex-basis: 25%;
        max-width: 25%;
      }

      .s4 {
        -ms-flex-preferred-size: 33.333%;
        -webkit-flex-basis: 33.333%;
        flex-basis: 33.333%;
        max-width: 33.333%;
      }

      .s5 {
        -ms-flex-preferred-size: 41.667%;
        -webkit-flex-basis: 41.667%;
        flex-basis: 41.667%;
        max-width: 41.667%;
      }

      .s6 {
        -ms-flex-preferred-size: 50%;
        -webkit-flex-basis: 50%;
        flex-basis: 50%;
        max-width: 50%;
      }

      .s7 {
        -ms-flex-preferred-size: 58.333%;
        -webkit-flex-basis: 58.333%;
        flex-basis: 58.333%;
        max-width: 58.333%;
      }

      .s8 {
        -ms-flex-preferred-size: 66.667%;
        -webkit-flex-basis: 66.667%;
        flex-basis: 66.667%;
        max-width: 66.667%;
      }

      .s9 {
        -ms-flex-preferred-size: 75%;
        -webkit-flex-basis: 75%;
        flex-basis: 75%;
        max-width: 75%;
      }

      .s10 {
        -ms-flex-preferred-size: 83.333%;
        -webkit-flex-basis: 83.333%;
        flex-basis: 83.333%;
        max-width: 83.333%;
      }

      .s11 {
        -ms-flex-preferred-size: 91.667%;
        -webkit-flex-basis: 91.667%;
        flex-basis: 91.667%;
        max-width: 91.667%;
      }

      .s12 {
        -ms-flex-preferred-size: 100%;
        -webkit-flex-basis: 100%;
        flex-basis: 100%;
        max-width: 100%;
      }
    }

    @media only screen and (min-width: 62em) {
      .grid {
        width: 61rem;
      }

      .m,
      .m1,
      .m2,
      .m3,
      .m4,
      .m5,
      .m6,
      .m7,
      .m8,
      .m9,
      .m10,
      .m11,
      .m12 {
        box-sizing: border-box;
        -webkit-flex: 0 0 auto;
        -ms-flex: 0 0 auto;
        -webkit-box-flex: 0;
        flex: 0 0 auto;
        padding-right: 1rem;
        padding-left: 1rem;
      }

      .m {
        -webkit-flex-grow: 1;
        -ms-flex-positive: 1;
        -webkit-box-flex: 1;
        flex-grow: 1;
        -ms-flex-preferred-size: 0;
        -webkit-flex-basis: 0;
        flex-basis: 0;
        max-width: 100%;
      }

      .m1 {
        -ms-flex-preferred-size: 8.333%;
        -webkit-flex-basis: 8.333%;
        flex-basis: 8.333%;
        max-width: 8.333%;
      }

      .m2 {
        -ms-flex-preferred-size: 16.667%;
        -webkit-flex-basis: 16.667%;
        flex-basis: 16.667%;
        max-width: 16.667%;
      }

      .m3 {
        -ms-flex-preferred-size: 25%;
        -webkit-flex-basis: 25%;
        flex-basis: 25%;
        max-width: 25%;
      }

      .m4 {
        -ms-flex-preferred-size: 33.333%;
        -webkit-flex-basis: 33.333%;
        flex-basis: 33.333%;
        max-width: 33.333%;
      }

      .m5 {
        -ms-flex-preferred-size: 41.667%;
        -webkit-flex-basis: 41.667%;
        flex-basis: 41.667%;
        max-width: 41.667%;
      }

      .m6 {
        -ms-flex-preferred-size: 50%;
        -webkit-flex-basis: 50%;
        flex-basis: 50%;
        max-width: 50%;
      }

      .m7 {
        -ms-flex-preferred-size: 58.333%;
        -webkit-flex-basis: 58.333%;
        flex-basis: 58.333%;
        max-width: 58.333%;
      }

      .m8 {
        -ms-flex-preferred-size: 66.667%;
        -webkit-flex-basis: 66.667%;
        flex-basis: 66.667%;
        max-width: 66.667%;
      }

      .m9 {
        -ms-flex-preferred-size: 75%;
        -webkit-flex-basis: 75%;
        flex-basis: 75%;
        max-width: 75%;
      }

      .m10 {
        -ms-flex-preferred-size: 83.333%;
        -webkit-flex-basis: 83.333%;
        flex-basis: 83.333%;
        max-width: 83.333%;
      }

      .m11 {
        -ms-flex-preferred-size: 91.667%;
        -webkit-flex-basis: 91.667%;
        flex-basis: 91.667%;
        max-width: 91.667%;
      }

      .m12 {
        -ms-flex-preferred-size: 100%;
        -webkit-flex-basis: 100%;
        flex-basis: 100%;
        max-width: 100%;
      }
    }

    @media only screen and (min-width: 75em) {
      .grid {
        width: 71rem;
      }

      .l,
      .l1,
      .l2,
      .l3,
      .l4,
      .l5,
      .l6,
      .l7,
      .l8,
      .l9,
      .l10,
      .l11,
      .l12 {
        box-sizing: border-box;
        -webkit-flex: 0 0 auto;
        -ms-flex: 0 0 auto;
        -webkit-box-flex: 0;
        flex: 0 0 auto;
        padding-right: 1rem;
        padding-left: 1rem;
      }

      .l {
        -webkit-flex-grow: 1;
        -ms-flex-positive: 1;
        -webkit-box-flex: 1;
        flex-grow: 1;
        -ms-flex-preferred-size: 0;
        -webkit-flex-basis: 0;
        flex-basis: 0;
        max-width: 100%;
      }

      .l1 {
        -ms-flex-preferred-size: 8.333%;
        -webkit-flex-basis: 8.333%;
        flex-basis: 8.333%;
        max-width: 8.333%;
      }

      .l2 {
        -ms-flex-preferred-size: 16.667%;
        -webkit-flex-basis: 16.667%;
        flex-basis: 16.667%;
        max-width: 16.667%;
      }

      .l3 {
        -ms-flex-preferred-size: 25%;
        -webkit-flex-basis: 25%;
        flex-basis: 25%;
        max-width: 25%;
      }

      .l4 {
        -ms-flex-preferred-size: 33.333%;
        -webkit-flex-basis: 33.333%;
        flex-basis: 33.333%;
        max-width: 33.333%;
      }

      .l5 {
        -ms-flex-preferred-size: 41.667%;
        -webkit-flex-basis: 41.667%;
        flex-basis: 41.667%;
        max-width: 41.667%;
      }

      .l6 {
        -ms-flex-preferred-size: 50%;
        -webkit-flex-basis: 50%;
        flex-basis: 50%;
        max-width: 50%;
      }

      .l7 {
        -ms-flex-preferred-size: 58.333%;
        -webkit-flex-basis: 58.333%;
        flex-basis: 58.333%;
        max-width: 58.333%;
      }

      .l8 {
        -ms-flex-preferred-size: 66.667%;
        -webkit-flex-basis: 66.667%;
        flex-basis: 66.667%;
        max-width: 66.667%;
      }

      .l9 {
        -ms-flex-preferred-size: 75%;
        -webkit-flex-basis: 75%;
        flex-basis: 75%;
        max-width: 75%;
      }

      .l10 {
        -ms-flex-preferred-size: 83.333%;
        -webkit-flex-basis: 83.333%;
        flex-basis: 83.333%;
        max-width: 83.333%;
      }

      .l11 {
        -ms-flex-preferred-size: 91.667%;
        -webkit-flex-basis: 91.667%;
        flex-basis: 91.667%;
        max-width: 91.667%;
      }

      .l12 {
        -ms-flex-preferred-size: 100%;
        -webkit-flex-basis: 100%;
        flex-basis: 100%;
        max-width: 100%;
      }
    }
    .padding {
      padding: 24px;
    }
    .padding-bottom {
        padding-bottom: 24px;
    }
    .padding-top {
        padding-top: 24px;
    }
    .padding-left {
        padding-left: 24px;
    }
    .padding-right {
        padding-right: 24px;
    }
    .margin {
      margin: 24px;
    }
    .margin-top {
        margin-top: 24px;
    }
    .margin-bottom {
        margin-bottom: 24px;
    }
    .margin-left {
        margin-left: 24px;
    }
    .margin-right {
        margin-right: 24px;
    }

/* ABOUT */

paper-material {
  @apply(--shadow-elevation-2dp);
}

:host {
  display: block;
}

.text-center {
  text-align: center;
}

a {
  text-decoration: none;
}

#placeholder {
  opacity: 0;
  background-color: grey;
  @apply(--layout-fit);
  z-index: -1;
}

marked-element {
  padding-top: 0 !important;
  margin-bottom: 50px !important;
}

landing-providers .provider {
  padding: 48px !important;
}

.about .title {
  margin-bottom: 0;
}

.page {
  padding-top: 130px;
}

.provider img {
    opacity: .4;
    max-width: 180px;
    filter: grayscale(100%);
    -webkit-filter: grayscale(100%);
    -webkit-transition: all .2s ease-in-out;
    transition: all .2s ease-in-out;
}
.provider:hover img {
    opacity: 1;
    filter: grayscale(0);
    -webkit-filter: grayscale(0);
}
.providers {
    justify-content: center;
    padding: 24px;
}
landing-person img {
    width: 100%;
}

/* PRODUCT */

.page paper-button {
  background-color: var(--app-accent-color) !important;
  color: #fff;
  font-size: 18px;
  height: 54px;
  padding: 0 2rem !important;
  margin: 0 8px 40px !important;
  font-weight: 500;
}

a {
  text-decoration: none;
}

.col {
  width: 50%;
  box-sizing: border-box;
}

.pad {
  padding: 16px;
}

img.with-shadow {
  max-width: 100%;
  display: block;
}

#placeholder {
    opacity: 0;
    background-color: grey;
    @apply(--layout-fit);
    z-index: -1;
}

.product .title {
  margin-bottom: 0;
}

/* FEATURES */

.features iron-icon {
    width: 48px;
    height: 48px;
}

.feature {
    position: relative;
    /*padding: 24px;*/
}

.image,
.desc {
    padding: 24px;
}

img {
    max-width: 100%;
}

.feature h3 {
    font-size: 2.92rem;
    margin: 1.46rem 0 1.168rem;
}

.white {
    background-color: #fff;
}

.prod-label {
    background-color: #444;
    color: #fff;
    font-size: 0.8em;
    border-radius: 2px;
    padding: 4px 6px;
    width: 100px;
    font-style: normal;
}

.product-feature ul, .feature ul {
    padding: 0;
}

.product-feature ul li, .feature ul li {
    line-height: 2em;
    list-style-type: disc;
    list-style-position: inside;
}

.product-feature ul ul, .feature ul ul {
    margin-left: 70px;
}

/* EDITIONS */

h5 {
    font-weight: 400;
    font-size: 1.64rem;
    margin: .82rem 0 .656rem;
}
.edition iron-icon {
    color: #09c;
    width: 48px;
    height: 48px;
}
.edition {
    max-width: 235px;
    margin: 0 auto;
    position: relative;
}

/* FAQ */

.faqitem h5 {
    font-weight: 400;
    font-size: 1.64rem;
    margin: .82rem 0 .656rem;
}
.faqitem {
    margin: 0 auto;
    position: relative;
}
.faqitem a {
    text-decoration: none !important;
    color: #09c !important;
}

/* SUMMURY */

paper-material {
  width: 80%;
  display: block;
  margin: 0 auto;
}

paper-material img {
  display: block;
}

a {
  text-decoration: none;
}

.col {
  display: block;
  box-sizing: border-box;
  padding-bottom: 80px;
}

img.with-shadow {
  max-width: 100%;
  display: block;
}

.landing-summary-p {
  height: 81px;
}

.icon {
  background-color: #424242;
  color: #fff;
  border-radius: 50%;
  padding: 8px;
  font-weight: bold;
  font-size: 1.2em;
  text-align: center;
  flex: none;
  display: block;
  margin: 0 auto 24px auto;
  width: 24px;
  height: 24px;
}

@media (max-width: 991px) {
  .landing-summary-p {
      height: auto;
  }
}

@media (max-width: 767px) {
  h2 {
    margin: 24px 0;
  }
}

/* WHATS NEW */

#whatsnew {
    display: block;            
}

#whatsnew[hidden] {
    display: none;
}

#whatsnew  h4 {
  font-size: 2.28rem;
  margin: 1.14rem 0 .912rem;
}

#whatsnew  h5 {
  line-height: 140%;
  font-size: 1.64rem;
  margin: .82rem 0 .656rem;
}

#whatsnew  h6 {
  font-size: 1rem;
}

#whatsnew paper-material {
    @apply(--shadow-elevation-2dp);
    display: block;
}

#whatsnew paper-material img {
    display: block;
}

#whatsnew paper-button {
  background-color: var(--app-accent-color);
  color: #fff;
  font-size: 18px;
  height: 54px;
  padding: 0 50px;
  margin: 40px 0;
  font-weight: 500;
}

#whatsnew {
  /*background-color: var(--app-accent-color);*/
  font-weight: 400 !important;
  background-color: #444;
  color: #fff;
}
#whatsnew h4.title {
  font-weight: 400 !important;
  line-height: 110%;
}

.light {
    font-weight: 400 !important;
}
#whatsnew .promtext {
    margin: 8px 0 24px 0;
}

#whatsnew .promtext.top {
    margin-top: 1.14em;
}

#whatsnew .promtext h6 {
    line-height: 150%;
    margin: 1rem 0 1rem 0;
}

#whatsnew .right-alligned {
    text-align: right;
}

@media screen and (max-width: 993px) {
    #whatsnew .right-alligned {
        text-align: left;
    }
    #whatsnew br.widescreens {
        display: none;
    }
}

#whatsnew .emph {
    /*color: #37B8D2;*/
    color: #A0DDEB;
}

#whatsnew h4 {
    padding: 0.112rem 0 0.912rem 0 !important;
}

#whatsnew a {
    color: #acd !important;
    cursor: pointer;
}

#whatsnew .join {
    display: inline-block;
}

#whatsnew .join img {
    vertical-align: middle;
    margin: 0 8px;
    height: 30px;
}

#whatsnew .person {
    margin-bottom: 8px;
}

#whatsnew .people > *,
#whatsnew .person > * {
    vertical-align: middle;
    margin-right: 8px;
    display: inline-block;
    line-height: 1.2em;
}

#whatsnew .person-img {
    border-style: solid;
    border-width: 2px;
    border-color: #fff;
    border-radius: 69px;
    width: 60px;
    height: 60px;
    float: left;
}

#whatsnew .people .comp {
    opacity: 0.54;
    font-size: .9em;
}

#whatsnew .people .name {
    padding-top: 8px;
}

/* FEATURES */

.features iron-icon {
    width: 48px;
    height: 48px;
}
.feature {
    max-width: 300px;
    margin: 0 auto;
    position: relative;
}
.new-feature {
    position: absolute;
    top: 42px;
    background-color: #09c;
    color: #fff;
    border-radius: 2px;
    padding: 0;
    width: 58px;
    left: calc(50% - 29px);
    font-size: 0.8em;
    font-weight: 400;
}

/* TESTIMONIALS */

#testimonials {
    position: relative;
    display: block;
} 
.client {
    font-size: 16px;
}
img.client-image {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background-color: #fefefe;
    border: 3px solid #444;
}
.job-title {
    color: #7f7f7f;
    line-height: 130%;
    font-weight: 300;
    margin: 0;
}
h5.client-name {
    font-weight: 400; 
}
h6.job-title {
    line-height: 130%;
    color: #7f7f7f;
    font-weight: 400;
}
hr {
    max-width: 66%;
    margin-top: 20px;
    margin-bottom: 20px; 
    opacity: .3;
}
.client-testimonial {
    max-width: 75%;
    margin: 0 auto;
}
#testimonials {
    position: relative;
    min-height: 300px;
}
.testimonial {
    position: absolute;
    width: 100%;
    top: 0;
    transition: 100ms opacity ease-in;
    opacity: 0;
}
.testimonial[active] {
    opacity: 1;
}
#controls {
    text-align: center;
    left: 0;
    right: 0;
    bottom: 0;
    margin: 0;
}
#controls .control-item {
    display: inline-block;
    cursor: pointer;
    height: 16px;
    width: 16px;
    margin: 0 12px;
    background-color: #e0e0e0;
    transition: background-color .3s;
    border-radius: 50%;
    font-size: 0;
}
#controls .control-item[active] {
    background-color: #09c;
}

/* PRICING */

:host {
    --paper-tooltip: {
        font-size: 14px;
        line-height: 24px;
    }
}
:host paper-tooltip {
    max-width: 200px;
    text-align: center;
}

span#vcpus, span#datapoints, span#rulechecks, span#apirequests, span#retention {
    border-bottom: 1px dashed #999;
}

#pricing paper-material {
    @apply --shadow-elevation-2dp;
}

#pricing .hero {
    padding: 48px 0;
}

:host {
    display: block;
}

.text-center {
    text-align: center;
}

#pricing paper-button {
    background-color: var(--app-accent-color) !important;
    color: #fff;
    font-size: 18px;
    height: 54px;
    padding: 0 2rem !important;
    margin: 0 40px 40px !important;
    font-weight: 500;
}

#pricing paper-button.hero-button {
    margin: 40px 40px 16px !important;
}

#pricing a {
    text-decoration: none;
}

#pricing .col {
    width: 50%;
    box-sizing: border-box;
}

#pricing .pad {
    padding: 16px;
}

#pricing #placeholder {
    opacity: 0;
    background-color: grey;
    @apply(--layout-fit);
    z-index: -1;
}

#pricing .plan {
    background-color: #fff;
    margin-bottom: 50px;
    overflow: auto;
    @apply(--shadow-elevation-4dp);
}

#pricing .plan, #pricing .plan > * {
    box-sizing: border-box;
    margin: 0;
}

#pricing .title {
    color: #fff;
    text-transform: uppercase;
    padding: 20px 0;
    font-size: 18px;
}

#pricing .plan paper-button {
    margin: 0 !important;
    font-size: 14px;
    height: 2rem;
    width: auto;
}

#pricing .bg-0 {
    background-color: #999;
}

#pricing .bg-1 {
    background-color: #777;
}

#pricing .bg-2 {
    background-color: #555;
}

#pricing .bg-3 {
    background-color: #222;
}

#pricing .plan-body-item {
    padding: 30px 10px 50px 10px;
}

@media only screen and (max-width: 600px) {
    #pricing .plan-body-item {
        min-height: 50px;
    }
}

#pricing .plan-body-item + #pricing .plan-body-item {
    border-top: 1px solid #d4d4d4;
}

#pricing .plan-body-item:last-child {
    border-bottom: 1px solid #d4d4d4;
}

#pricing .plan-body-item.highlight {
    background-color: var(--app-background-color);
}

#pricing .plan-body-item * {
    width: 100%;
}

#pricing .plan-body-item:not(:first-child) {
    padding: 0 10px;
}

#pricing .plan-body-item:last-child p {
    font-weight: bold;
}

#pricing .valign {
    display: block;
}

#pricing .price {
    font-weight: 700;
    line-height: 1;
    padding: 0;
    margin: 8px;
}

#pricing .price sub,
#pricing .price sup {
    font-size: 18px;
    font-weight: 300;
    vertical-align: middle;
}

#pricing .price sup {
    font-size: 24px;
    padding: 0 5px;
}

#pricing paper-button#enterpriseBtn {
    background-color: #4caf50;
    /*green*/
    display: block-inline;
    line-height: 54px;
    margin-left: 0 !important;
    margin-right: 0 !important;
}
#pricing ul {
    padding: 0;
    margin: 0;
}
#pricing ul li {
    margin-left: 15px;
    clear: both;
    list-style: none;
}
#pricing .block-center {
    margin: 0 auto;
}
#pricing .payg-rate {
    justify-content: center;
}
#pricing .plus-rate > span {
    background-color: #424242;
    color: #fff;
    border-radius: 50%;
    padding: 8px;
    font-weight: bold;
    font-size: 1.2em;
    text-align: center;
    flex: none;
    display: block;
    margin: 0 auto;
    width: 52px;
    height: 52px;
    line-height: 52px;
}
#pricing .plus-rate .plus {
    font-weight: normal;
    font-size: 0.8em;
}
#pricing .plus-per {
    text-align: center;
}
@media screen and (max-width: 768px){
    #pricing .includes > div {
        text-align: center;
    }
    #pricing .includes ul, #pricing .includes li {
        margin: 0;
        padding: 0;
    }
}

#pricing p.free {
    max-width: 540px;
    margin: 32px auto;
    line-height: 32px;
}
#pricing .small {
    font-size: 14px;
    margin: 0 32px 32px;
}

/* ORCHESTRATION */
.orchestration paper-button {
  color: #fff;
  font-size: 18px;
  height: 54px;
  padding: 0 2rem !important;
  margin: 0 8px 40px !important;
  font-weight: 500;
}

a {
  text-decoration: none;
}

.col {
  width: 50%;
  box-sizing: border-box;
}

.pad {
  padding: 16px;
}

img.with-shadow {
  max-width: 100%;
  display: block;
}

#placeholder {
    opacity: 0;
    background-color: grey;
    @apply(--layout-fit);
    z-index: -1;
}

/* RBAC */

.rbac .icon-bg {
  background-color: #ccc;
  border-radius: 50%;
  width: 95px;
  margin: 40px auto 20px;
  height: 95px;
  box-sizing: border-box;
}

.rbac iron-icon {
  width: 60px;
  height: 60px;
  padding: 14px 0 0 0 !important;
}

.rbac .offset-m3 {
  margin-left: 25%; 
}

@media screen and (max-width: 991px) {
  .rbac .offset-m3 {
    margin-left: 24px; 
    margin-right: 24px; 
  }
}

.rbac .conclusion {
  padding-bottom: 120px;
}

/* RBAC STEPS */

.step {
    position: relative;
    padding: 24px;
    width: 100%;
}

.step .image,
.step .desc {
    padding: 24px;
}

.step h3 {
    font-size: 2.92rem;
    margin: 1.46rem 0 1.168rem;
}

.step .image-wrapper {
    border-radius: 50%;
    width: 220px;
    height: 220px;
    overflow: hidden;
    cursor: pointer;
    margin: 0 auto;
}

/* GET STARTED */

#get-started .hero {
    padding: 48px 0;
}

#get-started .center {
    margin: 0 auto;
}

#get-started .text-center {
    text-align: center;
}

#get-started paper-button {
    background-color: var(--app-accent-color);
    color: #fff;
    font-size: 18px;
    height: 54px;
    font-weight: 500;
}
#get-started paper-button a {
    color: #fff !important;
}
#get-started .plan paper-button {
    width: 80% !important;
    margin-top: 24px;
}

#get-started a {
    font-weight: 400 !important;
    text-decoration: none;
}

#get-started .col {
    width: 50%;
    box-sizing: border-box;
}

#get-started .pad {
    padding: 16px;
}

@media only screen and (max-width: 943px) {
    #get-started typed-text {
        display: block;
    }
}

#get-started .contains > .grid-row {
    align-items: flex-start;
}

#get-started #placeholder {
    opacity: 0;
    background-color: grey;
    /*@apply(--layout-fit);*/
    z-index: -1;
}

#get-started .plan {
    margin-top: 50px;
    margin-bottom: 50px;
    overflow: auto;
    background-color: #fff;
    /*@apply(--shadow-elevation-4dp);*/
    box-shadow: 0 4px 5px 0 rgba(0, 0, 0, 0.14),
                0 1px 10px 0 rgba(0, 0, 0, 0.12),
                0 2px 4px -1px rgba(0, 0, 0, 0.4);
}
#get-started .plan .icon {
    border-radius: 50%;
    background-color: #fff;
    width: 48px;
    padding: 8px;
    height: 48px;
}
#get-started .plan-head {
    padding: 2rem 0;
    border-bottom: 4px solid;
}

#get-started .green .plan-head  {
    border-color: green;
}

#get-started .purple .plan-head {
    border-color: purple;
}

#get-started .blue .plan-head {
    border-color: #3F51B5;
}
#get-started .plan, #get-started .plan > * {
    box-sizing: border-box;
    margin: 0;
}

#get-started .title {
    color: #fff;
    text-transform: uppercase;
    padding: 20px 0;
    font-size: 24px;
}

#get-started .plan-body-item {
    padding: 16px;
}

@media only screen and (max-width: 600px) {
    #get-started .plan-body-item {
        min-height: 50px;
    }
}

#get-started .plan-body-item + .plan-body-item {
    border-top: 1px solid #d4d4d4;
}

#get-started .plan-body-item:last-child {
    border-bottom: 1px solid #d4d4d4;
}

#get-started .plan-body-item.highlight {
    background-color: var(--app-background-color);
}

#get-started .plan-body-item:first-child{
    min-height: 115px;
    max-height: 120px;
}

#get-started .plan-body-item > * {
    width: 100%;
}

#get-started .valign {
    display: block;
}

#get-started .price {
    font-weight: 700;
    line-height: 1;
    padding: 0;
    margin: 8px 0;
}

#get-started .price sub,
#get-started .price sup {
    font-size: 18px;
    font-weight: 300;
    vertical-align: middle;
}

#get-started sub > sub {
    font-size: 12px !important;
    display: block;
    margin-top: 8px;
}

#get-started .price sup {
    font-size: 24px;
    padding: 0 5px;
}

#get-started .price sub.month {
    margin-left: -54px;
    top: 6px;
}

#get-started .price sup.vcpu {
    top: -15px;
}

#get-started .plan-head sub iron-icon {
    width: 32px;
    height: 32px;
    top: -2px;
    left: -2px;
}

#get-started paper-button#enterpriseBtn {
    background-color: #4caf50;
    /*green*/
    display: block-inline;
    line-height: 54px;
    margin-left: 0 !important;
    margin-right: 0 !important;
}
#get-started ul {
    padding: 0;
    margin: 0;
}
#get-started ul li {
    margin-left: 15px;
    clear: both;
    list-style: none;
}
#get-started .bold {
    font-weight: 500;
}
#get-started ul.feature-list {
    display: block;
    margin: 1em auto;
}
#get-started ul.feature-list li {
    margin-left: 0;
    text-align: left;
    cursor: pointer;
    line-height: 1.8em;
    display: flex;
    align-items: center;
    margin-bottom: 16px;
}
#get-started ul.feature-list li .li-text {
    line-height: 1.4em
}
#get-started ul.feature-list li p {
    height: 0;
    opacity: 0;
    margin: 0;
    font-size: 0.8em;
    padding-left: 55px;
    transform: translate3d(-100%, 0);
    transition: all 100ms ease-in;
}
#get-started ul.feature-list li p.visible {
    height: auto;
    margin-top: 4px;
    margin-bottom: 16px;
    opacity: 0.87;
    transform: translate3d(0, 0);
    transition: all 300ms linear;
}
#get-started ul.feature-list li iron-icon {
    opacity: 0.54;
    margin: 0 16px;
    width: 1em;
    height: 1em;
}
@media screen and (min-width: 768px) and (max-width: 1024px) {
    #get-started ul.feature-list li {
        font-size: 0.9em;
    }
    #get-started ul.feature-list li iron-icon {
        margin: 0 16px;
    }
}
@media screen and (max-width: 768px){
    #get-started .includes > div {
        text-align: center;
    }
    #get-started .includes ul, .includes li {
        margin: 0;
        padding: 0;
    }
}

#get-started h4.pricetext {
    line-height: 2.36em;
}

#get-started .grey {
    background-color: var(--app-background-color);
}

#get-started div.back {
    float: left;
    margin-top: 24px;
    text-transform: uppercase;
    font-size: 0.8em;
    cursor: pointer;
}

#get-started div.back span {
    line-height: 4.5em;
    vertical-align: middle;
    color: #000 !important;
}

#get-started h2.decorated {
    margin-left: 32px;
    margin-right: 32px;
}
        </style>
    </template>
</dom-module>`;

document.head.appendChild(documentContainer.content);
