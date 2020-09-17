<template>
    <b-container fluid>
        <h4 class="h4 my-2 text-uppercase">settings</h4>
        <hr>
        <b-row>
            <b-col md="3" sm="4">
                <h5 class="h5 my-2 text-uppercase">General</h5>
                <b-list-group>
                    <nuxt-link to="/admin/settings" tag="a" class="list-group-item">Preferences</nuxt-link>
                </b-list-group>
                <h5 class="h5 my-2 text-uppercase">Account</h5>
                <b-list-group>
                    <nuxt-link to="/admin/settings/country" tag="a" class="list-group-item">Country</nuxt-link>
                    <nuxt-link to="/admin/settings/cities" tag="a" class="list-group-item">Cities</nuxt-link>
                    <nuxt-link to="/admin/settings/offices" tag="a" class="list-group-item">Offices/Branches</nuxt-link>
                    <nuxt-link to="/admin/settings/departments" tag="a" class="list-group-item">Departments</nuxt-link>
                    <nuxt-link to="/admin/settings/levels" tag="a" class="list-group-item">User Levels</nuxt-link>
                </b-list-group>
            </b-col>
            <b-col md="9" sm="8">
                <nuxt-child />
            </b-col>
        </b-row>
    </b-container>
</template>