(window.webpackJsonp=window.webpackJsonp||[]).push([[18],{414:function(t,e,n){"use strict";n(11);var r={props:{creator:String,subject:String,brief:String,created:String,status:String,id:Number}},c=n(26),component=Object(c.a)(r,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("nuxt-link",{attrs:{to:"/memo/"+t.id,tag:"a"}},[n("div",{staticClass:"result row"},[n("div",{staticClass:"col-2 font-weight-bold"},[t._v("\n            "+t._s(t.creator)+"\n        ")]),t._v(" "),n("div",{staticClass:"col-10 d-flex justify-content-between"},[n("span",[n("span",{staticClass:"subject font-weight-bold"},[t._v(t._s(t.subject))]),t._v(" - \n                "),n("span",{staticClass:"brief text-muted"},[t._v(t._s(t.brief))])]),t._v(" "),n("span",{staticClass:"justify-content-between"},[n("b-badge",{staticClass:"mr-1",attrs:{variant:"info"}},[t._v(t._s(t.status))]),t._v(" "),n("span",{staticClass:"date"},[t._v(t._s(t.created))])],1)])]),t._v(" "),n("hr",{staticClass:"mt-1"})])}),[],!1,null,null,null);e.a=component.exports},432:function(t,e,n){"use strict";n.r(e);var r=n(414),c={props:{truncate:Function},data:function(){return{results:[]}},mounted:function(){var t=this;this.$axios.$get("/memos/?mstate=archived",{headers:this.$store.getters.authHeader}).then((function(e){t.results=e,t.results.forEach((function(e){e.message=t.truncate(e.message,6)}))})).catch((function(t){console.log(t)}))},components:{SearchResult:r.a}},l=n(26),component=Object(l.a)(c,(function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"container-fluid"},[e("h4",[this._v("ARCHIVED ...")]),this._v(" "),e("hr"),this._v(" "),this._l(this.results,(function(t){return e("search-result",{key:t.created,attrs:{creator:t.sender.get_full_name,subject:t.subject,brief:t.message,created:t.created,id:t.id,status:"Archived"}})}))],2)}),[],!1,null,null,null);e.default=component.exports}}]);