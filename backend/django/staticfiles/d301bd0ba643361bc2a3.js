(window.webpackJsonp=window.webpackJsonp||[]).push([[5],{446:function(t,e,o){"use strict";o.r(e);o(29);var n={data:function(){return{fields:[{key:"name",label:"City"},"abbreviation",{key:"offices",label:"Branches"},"action"],items:[],new:!0,form:{country:{},city:"",id:null,offices:[],abbreviation:""},options:{countries:{options:[{value:null,text:"Select a Country"}]},offices:{options:[{value:null,text:"Select some Office(s)"}]}}}},methods:{showCModal:function(t,data){var e=this;this.new=data.new,this.form.offices=[],data.new?(this.form.country="",this.form.city="",this.form.abbreviation=""):(this.form.country=data.item.country,this.form.city=data.item.name,this.form.abbreviation=data.item.abbreviation,this.form.id=data.item.id,data.item.offices.forEach((function(t){e.form.offices.push(t.id)}))),console.log(this.form.offices),this.$refs.cityModal.show()},handleOk:function(){this.handleSubmit()},handleSubmit:function(){var t=this;(this.new?this.$axios.$post:this.$axios.$put)("accounts/city-settings/",this.form,{headers:this.$store.getters.authHeader}).then((function(e){t.items=e,console.log(e)})).catch((function(t){return console.log(t)}))},deleteCity:function(t,data){var e=this;this.$axios.delete("accounts/city-settings/"+data.item.id+"/",{headers:this.$store.getters.authHeader}).then((function(t){e.items=t.data})).catch((function(t){return console.log(t)}))}},mounted:function(){var t=this;this.$axios.get("accounts/city-settings/",{headers:this.$store.getters.authHeader}).then((function(e){t.items=e.data})).catch((function(t){return console.log(t)})),this.options.countries.options=[{value:null,text:"Select a Country"}],this.$axios.get("accounts/country-settings/",{headers:this.$store.getters.authHeader}).then((function(e){e.data.forEach((function(e){t.options.countries.options.push({value:e.id,text:e.name})}))})).catch((function(t){return console.log(t)})),this.options.offices.options=[{value:null,text:"Select some Office(s)"}],this.$axios.get("accounts/office-settings/",{headers:this.$store.getters.authHeader}).then((function(e){e.data.forEach((function(e){t.options.offices.options.push({value:e.id,text:e.name})}))})).catch((function(t){return console.log(t)}))}},r=o(28),component=Object(r.a)(n,(function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",[o("h4",[t._v("Cities "),o("b-button",{staticClass:"ml-5",attrs:{variant:"info",size:"sm"},on:{click:function(e){return e.stopPropagation(),e.preventDefault(),t.showCModal(e,{new:!0})}}},[t._v("+ City")])],1),t._v(" "),o("hr"),t._v(" "),o("b-table",{attrs:{striped:"",hover:"",items:t.items,fields:t.fields},scopedSlots:t._u([{key:"cell(offices)",fn:function(data){return t._l(data.item.offices,(function(e){return o("span",{key:e.id},[t._v(" "+t._s(e.name)+",")])}))}},{key:"cell(action)",fn:function(data){return[o("a",{attrs:{href:"#"},on:{click:function(e){return e.stopPropagation(),e.preventDefault(),t.showCModal(e,{new:!1,item:data.item})}}},[o("font-awesome-icon",{attrs:{icon:"edit"}})],1),t._v(" | \n            "),o("a",{attrs:{href:"#"},on:{click:function(e){return e.stopPropagation(),e.preventDefault(),t.deleteCity(e,{item:data.item})}}},[o("font-awesome-icon",{attrs:{icon:"times"}})],1)]}}])}),t._v(" "),o("b-modal",{ref:"cityModal",attrs:{title:"City",size:"lg",centered:""},on:{ok:t.handleOk}},[o("b-form",{on:{submit:function(e){return e.stopPropagation(),e.preventDefault(),t.handleSubmit(e)}}},[o("b-row",[o("b-col",[o("b-form-group",{attrs:{id:"fieldset-horizontal","label-cols-sm":"3","label-cols-lg":"2","label-size":"sm",description:"Country Name",label:"Country","label-for":"country","invalid-feedback":"title is required"}},[o("b-form-select",{ref:"category",attrs:{id:"categories",options:t.options.countries.options,size:"sm"},model:{value:t.form.country,callback:function(e){t.$set(t.form,"country",e)},expression:"form.country"}})],1)],1),t._v(" "),o("b-col")],1),t._v(" "),o("b-row",[o("b-col",[o("b-form-group",{attrs:{id:"fieldset-horizontal","label-cols-sm":"3","label-cols-lg":"2","label-size":"sm",description:"City Name",label:"City","label-for":"city","invalid-feedback":"title is required"}},[o("b-form-input",{attrs:{type:"text",id:"city",required:""},model:{value:t.form.city,callback:function(e){t.$set(t.form,"city",e)},expression:"form.city"}})],1)],1),t._v(" "),o("b-col",[o("b-form-group",{attrs:{id:"fieldset-horizontal","label-cols-sm":"3","label-cols-lg":"2","label-size":"sm",description:"City Abbreviation",label:"Abbr","label-for":"abbreviation","invalid-feedback":"title is required"}},[o("b-form-input",{attrs:{type:"text",id:"abbreviation",required:""},model:{value:t.form.abbreviation,callback:function(e){t.$set(t.form,"abbreviation",e)},expression:"form.abbreviation"}})],1)],1)],1),t._v(" "),o("b-row",[o("b-col",[o("b-form-group",{attrs:{id:"fieldset-horizontal","label-cols-sm":"3","label-cols-lg":"2","label-size":"sm",description:"Branches/Offices",label:"Branches","label-for":"office","invalid-feedback":"title is required"}},[o("b-form-select",{ref:"office",attrs:{id:"office",options:t.options.offices.options,size:"sm",multiple:"","select-size":t.options.offices.options.length},model:{value:t.form.offices,callback:function(e){t.$set(t.form,"offices",e)},expression:"form.offices"}})],1)],1)],1),t._v(" "),t._t("default")],2)],1)],1)}),[],!1,null,null,null);e.default=component.exports}}]);