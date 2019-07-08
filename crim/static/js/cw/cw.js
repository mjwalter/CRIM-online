!function(t){var e={};function r(i){if(e[i])return e[i].exports;var o=e[i]={i:i,l:!1,exports:{}};return t[i].call(o.exports,o,o.exports,r),o.l=!0,o.exports}r.m=t,r.c=e,r.d=function(t,e,i){r.o(t,e)||Object.defineProperty(t,e,{configurable:!1,enumerable:!0,get:i})},r.r=function(t){Object.defineProperty(t,"__esModule",{value:!0})},r.n=function(t){var e=t&&t.__esModule?function(){return t.default}:function(){return t};return r.d(e,"a",e),e},r.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},r.p="",r(r.s=2)}([function(t,e,r){r(1),t.exports=self.fetch.bind(self)},function(t,e){!function(t){"use strict";if(!t.fetch){var e={searchParams:"URLSearchParams"in t,iterable:"Symbol"in t&&"iterator"in Symbol,blob:"FileReader"in t&&"Blob"in t&&function(){try{return new Blob,!0}catch(t){return!1}}(),formData:"FormData"in t,arrayBuffer:"ArrayBuffer"in t};if(e.arrayBuffer)var r=["[object Int8Array]","[object Uint8Array]","[object Uint8ClampedArray]","[object Int16Array]","[object Uint16Array]","[object Int32Array]","[object Uint32Array]","[object Float32Array]","[object Float64Array]"],i=function(t){return t&&DataView.prototype.isPrototypeOf(t)},o=ArrayBuffer.isView||function(t){return t&&r.indexOf(Object.prototype.toString.call(t))>-1};d.prototype.append=function(t,e){t=a(t),e=h(e);var r=this.map[t];this.map[t]=r?r+","+e:e},d.prototype.delete=function(t){delete this.map[a(t)]},d.prototype.get=function(t){return t=a(t),this.has(t)?this.map[t]:null},d.prototype.has=function(t){return this.map.hasOwnProperty(a(t))},d.prototype.set=function(t,e){this.map[a(t)]=h(e)},d.prototype.forEach=function(t,e){for(var r in this.map)this.map.hasOwnProperty(r)&&t.call(e,this.map[r],r,this)},d.prototype.keys=function(){var t=[];return this.forEach(function(e,r){t.push(r)}),u(t)},d.prototype.values=function(){var t=[];return this.forEach(function(e){t.push(e)}),u(t)},d.prototype.entries=function(){var t=[];return this.forEach(function(e,r){t.push([r,e])}),u(t)},e.iterable&&(d.prototype[Symbol.iterator]=d.prototype.entries);var s=["DELETE","GET","HEAD","OPTIONS","POST","PUT"];b.prototype.clone=function(){return new b(this,{body:this._bodyInit})},y.call(b.prototype),y.call(g.prototype),g.prototype.clone=function(){return new g(this._bodyInit,{status:this.status,statusText:this.statusText,headers:new d(this.headers),url:this.url})},g.error=function(){var t=new g(null,{status:0,statusText:""});return t.type="error",t};var n=[301,302,303,307,308];g.redirect=function(t,e){if(-1===n.indexOf(e))throw new RangeError("Invalid status code");return new g(null,{status:e,headers:{location:t}})},t.Headers=d,t.Request=b,t.Response=g,t.fetch=function(t,r){return new Promise(function(i,o){var s=new b(t,r),n=new XMLHttpRequest;n.onload=function(){var t,e,r={status:n.status,statusText:n.statusText,headers:(t=n.getAllResponseHeaders()||"",e=new d,t.replace(/\r?\n[\t ]+/g," ").split(/\r?\n/).forEach(function(t){var r=t.split(":"),i=r.shift().trim();if(i){var o=r.join(":").trim();e.append(i,o)}}),e)};r.url="responseURL"in n?n.responseURL:r.headers.get("X-Request-URL");var o="response"in n?n.response:n.responseText;i(new g(o,r))},n.onerror=function(){o(new TypeError("Network request failed"))},n.ontimeout=function(){o(new TypeError("Network request failed"))},n.open(s.method,s.url,!0),"include"===s.credentials?n.withCredentials=!0:"omit"===s.credentials&&(n.withCredentials=!1),"responseType"in n&&e.blob&&(n.responseType="blob"),s.headers.forEach(function(t,e){n.setRequestHeader(e,t)}),n.send(void 0===s._bodyInit?null:s._bodyInit)})},t.fetch.polyfill=!0}function a(t){if("string"!=typeof t&&(t=String(t)),/[^a-z0-9\-#$%&'*+.\^_`|~]/i.test(t))throw new TypeError("Invalid character in header field name");return t.toLowerCase()}function h(t){return"string"!=typeof t&&(t=String(t)),t}function u(t){var r={next:function(){var e=t.shift();return{done:void 0===e,value:e}}};return e.iterable&&(r[Symbol.iterator]=function(){return r}),r}function d(t){this.map={},t instanceof d?t.forEach(function(t,e){this.append(e,t)},this):Array.isArray(t)?t.forEach(function(t){this.append(t[0],t[1])},this):t&&Object.getOwnPropertyNames(t).forEach(function(e){this.append(e,t[e])},this)}function f(t){if(t.bodyUsed)return Promise.reject(new TypeError("Already read"));t.bodyUsed=!0}function c(t){return new Promise(function(e,r){t.onload=function(){e(t.result)},t.onerror=function(){r(t.error)}})}function l(t){var e=new FileReader,r=c(e);return e.readAsArrayBuffer(t),r}function p(t){if(t.slice)return t.slice(0);var e=new Uint8Array(t.byteLength);return e.set(new Uint8Array(t)),e.buffer}function y(){return this.bodyUsed=!1,this._initBody=function(t){if(this._bodyInit=t,t)if("string"==typeof t)this._bodyText=t;else if(e.blob&&Blob.prototype.isPrototypeOf(t))this._bodyBlob=t;else if(e.formData&&FormData.prototype.isPrototypeOf(t))this._bodyFormData=t;else if(e.searchParams&&URLSearchParams.prototype.isPrototypeOf(t))this._bodyText=t.toString();else if(e.arrayBuffer&&e.blob&&i(t))this._bodyArrayBuffer=p(t.buffer),this._bodyInit=new Blob([this._bodyArrayBuffer]);else{if(!e.arrayBuffer||!ArrayBuffer.prototype.isPrototypeOf(t)&&!o(t))throw new Error("unsupported BodyInit type");this._bodyArrayBuffer=p(t)}else this._bodyText="";this.headers.get("content-type")||("string"==typeof t?this.headers.set("content-type","text/plain;charset=UTF-8"):this._bodyBlob&&this._bodyBlob.type?this.headers.set("content-type",this._bodyBlob.type):e.searchParams&&URLSearchParams.prototype.isPrototypeOf(t)&&this.headers.set("content-type","application/x-www-form-urlencoded;charset=UTF-8"))},e.blob&&(this.blob=function(){var t=f(this);if(t)return t;if(this._bodyBlob)return Promise.resolve(this._bodyBlob);if(this._bodyArrayBuffer)return Promise.resolve(new Blob([this._bodyArrayBuffer]));if(this._bodyFormData)throw new Error("could not read FormData body as blob");return Promise.resolve(new Blob([this._bodyText]))},this.arrayBuffer=function(){return this._bodyArrayBuffer?f(this)||Promise.resolve(this._bodyArrayBuffer):this.blob().then(l)}),this.text=function(){var t,e,r,i=f(this);if(i)return i;if(this._bodyBlob)return t=this._bodyBlob,e=new FileReader,r=c(e),e.readAsText(t),r;if(this._bodyArrayBuffer)return Promise.resolve(function(t){for(var e=new Uint8Array(t),r=new Array(e.length),i=0;i<e.length;i++)r[i]=String.fromCharCode(e[i]);return r.join("")}(this._bodyArrayBuffer));if(this._bodyFormData)throw new Error("could not read FormData body as text");return Promise.resolve(this._bodyText)},e.formData&&(this.formData=function(){return this.text().then(m)}),this.json=function(){return this.text().then(JSON.parse)},this}function b(t,e){var r,i,o=(e=e||{}).body;if(t instanceof b){if(t.bodyUsed)throw new TypeError("Already read");this.url=t.url,this.credentials=t.credentials,e.headers||(this.headers=new d(t.headers)),this.method=t.method,this.mode=t.mode,o||null==t._bodyInit||(o=t._bodyInit,t.bodyUsed=!0)}else this.url=String(t);if(this.credentials=e.credentials||this.credentials||"omit",!e.headers&&this.headers||(this.headers=new d(e.headers)),this.method=(r=e.method||this.method||"GET",i=r.toUpperCase(),s.indexOf(i)>-1?i:r),this.mode=e.mode||this.mode||null,this.referrer=null,("GET"===this.method||"HEAD"===this.method)&&o)throw new TypeError("Body not allowed for GET or HEAD requests");this._initBody(o)}function m(t){var e=new FormData;return t.trim().split("&").forEach(function(t){if(t){var r=t.split("="),i=r.shift().replace(/\+/g," "),o=r.join("=").replace(/\+/g," ");e.append(decodeURIComponent(i),decodeURIComponent(o))}}),e}function g(t,e){e||(e={}),this.type="default",this.status=void 0===e.status?200:e.status,this.ok=this.status>=200&&this.status<300,this.statusText="statusText"in e?e.statusText:"OK",this.headers=new d(e.headers),this.url=e.url||"",this._initBody(t)}}("undefined"!=typeof self?self:this)},function(t,e,r){"use strict";r.r(e);var i=r(0),o=r.n(i);window.CrimViewer=class{constructor(t){this.omas=t.omas?t.omas:"http://mith.umd.edu/ema/",this.meiUrl=t.mei,this.ema=t.ema,this.fullEma=`${this.omas}${encodeURIComponent(this.meiUrl)}/${this.ema}/highlight`,this.div=document.getElementById(t.div),this.controls=document.getElementById(t.controls),this.vrv=t.vrv,this.meiData="",this.curPage=0,this.startPage=1,this.highlightedIds=[]}getMeiData(){return o()(this.fullEma).then(t=>t.text()).then(t=>(this.meiData=t,t))}setupVerovio(){this.div.innerHTML="Loading score...";const t={pageWidth:100*this.div.offsetWidth/35,pageHeight:100*this.div.offsetHeight/35,ignoreLayout:1,adjustPageHeight:1,border:10,scale:35};this.vrv.setOptions(t)}renderMei(){if(this.vrv.loadData(this.meiData+"\n",""),0==this.highlightedIds.length){const t=(new window.DOMParser).parseFromString(this.meiData,"text/xml");this.highlightedIds=t.querySelector("annot[type='ema_highlight']").getAttribute("plist").split(" ")}this.startPage=this.vrv.getPageWithElement(this.highlightedIds[0].replace("#","")),this.curPage=this.startPage,this.renderPage()}renderPage(){if(this.meiData){this.vrv.loadData(this.meiData+"\n","");const t=this.vrv.renderPage(this.curPage);this.div.innerHTML=t,this.highlightMusic()}}highlightMusic(){for(const t of this.highlightedIds){const e=this.div.querySelector(t);e&&e.classList.add("cw-highlighted")}}prevPage(){this.curPage>1&&(this.curPage=this.curPage-1,this.renderPage())}nextPage(){this.curPage<this.vrv.getPageCount()&&(this.curPage=this.curPage+1,this.renderPage())}firstHighlightedPage(){this.curPage=this.startPage,this.renderPage()}bindControls(){this.controls.querySelector(".cw-prev").onclick=(()=>{this.prevPage()}),this.controls.querySelector(".cw-next").onclick=(()=>{this.nextPage()}),this.controls.querySelector(".cw-show").onclick=(()=>{this.firstHighlightedPage()})}render(){this.setupVerovio(),this.bindControls(),this.getMeiData().then(()=>{this.renderMei()})}}}]);