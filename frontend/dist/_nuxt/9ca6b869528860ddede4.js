(window.webpackJsonp=window.webpackJsonp||[]).push([[2],{224:function(t,e,o){"use strict";o.r(e);o(21),o(24);var n={data:function(){return{editProfile:!1,account:{user:"",firstname:"",lastname:"",title:"",email:"",department:"",city:"",office:"",level:"",groups:[]},options:{cities:{options:[{value:null,text:"Select a City"}]},departments:{options:[{value:null,text:"Select a Department"}]},offices:{options:[{value:null,text:"Select an Office"}]},levels:{options:[{value:null,text:"Select a level"}]},groups:{options:[{value:null,text:"Select a Group"}]}}}},mounted:function(){var t=this;this.$axios.$get("accounts/"+this.$route.params.id.split("-")[0]+"/").then((function(e){t.account=e,t.account.firstname=t.account.user.first_name,t.account.lastname=t.account.user.last_name,t.account.email=t.account.user.email})).catch((function(t){return console.log(t)}))},methods:{initUpdate:function(){var t=this;this.editProfile=!0,console.log("initialise cities"),this.$axios.$get("accounts/cities/").then((function(e){e.forEach((function(e){t.options.cities.options.push({value:e.id,text:e.name})}))})).catch((function(t){return console.log(t)})),console.log("initialise levels"),this.$axios.$get("accounts/levels/").then((function(e){e.forEach((function(e){t.options.levels.options.push({value:e.id,text:e.level})}))})).catch((function(t){return console.log(t)})),console.log("initialise groups"),this.$axios.$get("accounts/groups/").then((function(e){e.forEach((function(e){t.options.groups.options.push({value:{id:e.id,name:e.name},text:e.name})}))})).catch((function(t){return console.log(t)})),this.options.offices.options.push({value:this.account.office.id,text:this.account.office.name}),this.options.departments.options.push({value:this.account.department.id,text:this.account.department.name})},onCityUpdate:function(){var t=this;this.options.offices.options=[{value:null,text:"Select an Office"}],this.options.departments.options=[{value:null,text:"Select a Department"}],console.log("initialise offices for city",this.account.city),this.$axios.$get("accounts/offices?city="+this.account.city.id).then((function(e){e.forEach((function(e){t.options.offices.options.push({value:e.id,text:e.name})}))})).catch((function(t){return console.log(t)}))},onOfficeUpdate:function(){var t=this;this.options.departments.options=[{value:null,text:"Select a Department"}],console.log("initialise departmnets for office",this.account.office),this.$axios.$get("accounts/departments?office="+this.account.office.id).then((function(e){e.forEach((function(e){t.options.departments.options.push({value:e.id,text:e.name})}))})).catch((function(t){return console.log(t)}))},profileUpdate:function(){console.log(this.account),this.$axios.$put("accounts/"+this.$route.params.id.split("-")[0]+"/",{account_data:this.account}).then((function(t){console.log(t)})).catch((function(t){return console.log(t)}))}},watch:{}},c=o(20),component=Object(c.a)(n,(function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{staticClass:"container"},[o("h4",[t._v("Account Profile Detail")]),t._v(" "),o("hr"),t._v(" "),o("div",{staticClass:"row mb-5"},[o("div",{staticClass:"col-md-4"},[o("div",{staticClass:"card card-outline-dark p-2"},[o("h4",{staticClass:"text-center"},[t._v("\n                    "+t._s(t.account.user.get_full_name)+"\t\t\t\t\t\n                    "),t.editProfile?t._e():o("span",{staticClass:"float-right mr-auto"},[o("a",{staticClass:"text-dark btn btn-outline-info",attrs:{href:"#"},on:{click:function(e){return e.stopPropagation(),e.preventDefault(),t.initUpdate(e)}}},[o("span",[o("font-awesome-icon",{attrs:{icon:"edit"}})],1)])])]),t._v(" "),o("table",{staticClass:"table mt-2"},[o("tbody",[o("tr",[o("td",{staticClass:"text-dark"},[t._v("Username")]),t._v(" "),o("td",{staticClass:"text-dark"},[t._v("@"+t._s(t.account.user.username))])]),t._v(" "),o("tr",[o("td",{staticClass:"text-dark"},[t._v("Email")]),t._v(" "),o("td",{staticClass:"text-dark"},[t._v(t._s(t.account.user.email))])]),t._v(" "),o("tr",[o("td",{staticClass:"text-dark"},[t._v("Permission Groups")]),t._v(" "),o("td",{staticClass:"text-dark"},t._l(t.account.groups,(function(e){return o("span",{key:e.index,staticClass:"mr-1"},[t._v(t._s(e.name)+", ")])})),0)]),t._v(" "),o("tr",[o("td",{staticClass:"text-dark"},[t._v("Title")]),t._v(" "),o("td",{staticClass:"text-dark"},[t._v(t._s(t.account.title))])]),t._v(" "),o("tr",[o("td",{staticClass:"text-dark"},[t._v("Level")]),t._v(" "),o("td",{staticClass:"text-dark"},[t._v(t._s(t.account.level.level))])]),t._v(" "),o("tr",[o("td",{staticClass:"text-dark"},[t._v("Department")]),t._v(" "),o("td",{staticClass:"text-dark"},[t._v(t._s(t.account.department.name))])]),t._v(" "),o("tr",[o("td",{staticClass:"text-dark"},[t._v("Office/Branch")]),t._v(" "),o("td",{staticClass:"text-dark"},[t._v(t._s(t.account.office.name))])]),t._v(" "),o("tr",[o("td",{staticClass:"text-dark"},[t._v("City")]),t._v(" "),o("td",{staticClass:"text-dark"},[t._v(t._s(t.account.city.name))])])])]),t._v(" "),o("button",{staticClass:"btn btn-outline-danger btn-sm",attrs:{"data-toggle":"modal","data-target":"#PasswordChangeModal"}},[t._v("Reset Password")])])]),t._v(" "),t.editProfile?o("div",{staticClass:"col-md-8"},[o("h5",[t._v("\n                Profile Edit                    \t\t\t\t\t\n                "),o("span",{staticClass:" ml-5 text-danger"},[o("a",{staticClass:"text-dark btn btn-outline-info",attrs:{href:"#"},on:{click:function(e){e.stopPropagation(),e.preventDefault(),t.editProfile=!1}}},[o("span",[o("font-awesome-icon",{attrs:{icon:"times"}})],1)])])]),t._v(" "),o("hr"),t._v(" "),o("b-card",{attrs:{"bg-variant":"light"}},[o("b-form",[o("b-row",[o("b-col",[o("b-form-group",{attrs:{id:"fieldset-horizontal","label-size":"sm",label:"firstname:","label-for":"firstaname"}},[o("b-form-input",{attrs:{id:"firstname",size:"sm"},model:{value:t.account.firstname,callback:function(e){t.$set(t.account,"firstname",e)},expression:"account.firstname"}})],1)],1),t._v(" "),o("b-col",[o("b-form-group",{attrs:{id:"fieldset-horizontal","label-size":"sm",label:"lastname:","label-for":"lastname"}},[o("b-form-input",{attrs:{id:"lastname",size:"sm"},model:{value:t.account.lastname,callback:function(e){t.$set(t.account,"lastname",e)},expression:"account.lastname"}})],1)],1)],1),t._v(" "),o("b-row",[o("b-col",[o("b-form-group",{attrs:{id:"fieldset-horizontal","label-size":"sm",label:"email:","label-for":"email"}},[o("b-form-input",{attrs:{id:"email",size:"sm"},model:{value:t.account.email,callback:function(e){t.$set(t.account,"email",e)},expression:"account.email"}})],1)],1),t._v(" "),o("b-col",[o("b-form-group",{attrs:{id:"fieldset-horizontal","label-size":"sm",label:"job title:","label-for":"title"}},[o("b-form-input",{attrs:{id:"title",size:"sm"},model:{value:t.account.title,callback:function(e){t.$set(t.account,"title",e)},expression:"account.title"}})],1)],1),t._v(" "),o("b-col",[o("b-form-group",{attrs:{id:"fieldset-horizontal","label-size":"sm",label:"level:","label-for":"level"}},[o("b-form-select",{attrs:{id:"level",options:t.options.levels.options,size:"sm"},model:{value:t.account.level.id,callback:function(e){t.$set(t.account.level,"id",e)},expression:"account.level.id"}})],1)],1)],1),t._v(" "),o("b-row",[o("b-col",[o("b-form-group",{attrs:{id:"fieldset-horizontal","label-size":"sm",label:"City:","label-for":"city"}},[o("b-form-select",{ref:"city",attrs:{id:"city",options:t.options.cities.options,size:"sm"},on:{change:t.onCityUpdate},model:{value:t.account.city.id,callback:function(e){t.$set(t.account.city,"id",e)},expression:"account.city.id"}})],1)],1),t._v(" "),o("b-col",[o("b-form-group",{attrs:{id:"fieldset-horizontal","label-size":"sm",label:"Office:","label-for":"office"}},[o("b-form-select",{ref:"office",attrs:{id:"office",options:t.options.offices.options,size:"sm"},on:{change:t.onOfficeUpdate},model:{value:t.account.office.id,callback:function(e){t.$set(t.account.office,"id",e)},expression:"account.office.id"}})],1)],1),t._v(" "),null!=t.account.office?o("b-col",[o("b-form-group",{attrs:{id:"fieldset-horizontal","label-size":"sm",label:"department:","label-for":"department"}},[o("b-form-select",{ref:"department",attrs:{id:"department",options:t.options.departments.options,size:"sm"},model:{value:t.account.department.id,callback:function(e){t.$set(t.account.department,"id",e)},expression:"account.department.id"}})],1)],1):t._e()],1),t._v(" "),o("b-row",[o("b-col",[o("b-form-group",{attrs:{id:"fieldset-horizontal","label-cols-sm":"3","label-cols-lg":"2","label-size":"sm",label:"groups:","label-for":"groups"}},[o("b-form-select",{ref:"city",attrs:{id:"city",options:t.options.groups.options,size:"sm",multiple:"","select-size":t.options.groups.options.length},model:{value:t.account.groups,callback:function(e){t.$set(t.account,"groups",e)},expression:"account.groups"}})],1)],1)],1),t._v(" "),o("b-button",{staticClass:"float-left",attrs:{type:"submit",variant:"primary"},on:{click:function(e){return e.stopPropagation(),e.preventDefault(),t.profileUpdate(e)}}},[t._v("Sign In")]),t._v(" "),t._t("default")],2)],1)],1):t._e()])])}),[],!1,null,null,null);e.default=component.exports}}]);