<template>
    <aside id="left-aside bg-dark">
        <nav id="sidebar">
            <b-navbar-brand class=" pl-3 pt-2">Welcome @{{ loggedInUser }}</b-navbar-brand>
            <ul class="list-unstyled components  mt-1 pt-2">
                 <nuxt-link to="/" class="nav-item" tag="li">
                    <a class="nav-link">DASHBOARD</a>
                 </nuxt-link>
                 <nuxt-link to="/memo" class="nav-item" tag="li">
                    <a class="nav-link">Memorandum</a>
                 </nuxt-link>
                 <nuxt-link to="/notice" class="nav-item" tag="li">
                    <a class="nav-link">Notices</a>
                 </nuxt-link>
                <!-- <li >
                    <a 
                    href="#homeSubmenu" 
                    data-toggle="collapse" 
                    aria-expanded="false" 
                    class="dropdown-toggle"
                    @click.prevent.stop="dropToggle($event)" >Home</a>
                    <ul class="collapse list-unstyled" id="homeSubmenu">
                        <li>
                            <a href="#">Home 1</a>
                        </li>
                        <li>
                            <a href="#">Home 2</a>
                        </li>
                        <li>
                            <a href="#">Home 3</a>
                        </li>
                    </ul>
                </li>
                <b-nav-item href="#">Link 2</b-nav-item> -->
            </ul>
        </nav>
    </aside>
</template>

<style lang="css" scoped>
aside {
    min-height: 100vh;
    position: fixed;
    left: 0;
    top: 0;
}

aside,
#sidebar {
    min-width: 200px;
    max-width: 200px;
    background: #343a40!important;
}

#sidebar.active {
    margin-left: -200px;
}

a[data-toggle="collapse"] {
    position: relative;
}

.dropdown-toggle::after {
    display: block;
    position: absolute;
    top: 50%;
    right: 20px;
    transform: translateY(-50%);
}

@media (max-width: 768px) {
    #sidebar {
        margin-left: -200px;
    }
    #sidebar.active {
        margin-left: 0;
    }
}
a, a:hover, a:focus {
    color: inherit;
    text-decoration: none;
    transition: all 0.3s;
}

#sidebar {
    /* don't forget to add all the previously mentioned styles here too */
    background: #343a40!important;
    color: #fff;
    transition: all 0.3s;
}

#sidebar .sidebar-header {
    padding: 20px;
    background: #343a40!important;
}

#sidebar ul.components {
    padding: 20px 0;
    border-bottom: 1px solid #343a40!important;
}

#sidebar ul p {
    color: #fff;
    padding: 10px;
}

#sidebar ul li a {
    padding: 10px;
    font-size: 1.1em;
    display: block;
}
#sidebar ul li a:hover {
    color: #343a40!important;
    background: #fff;
}

#sidebar ul li.nuxt-link-exact-active.nuxt-link-active > a, 
a[aria-expanded="true"] {
    color: #fff;
    background: #ccc;
}
ul ul a {
    font-size: 0.9em !important;
    padding-left: 30px !important;
    background: #343a40!important;
}
</style>

<script>
import { mapGetters } from 'vuex';
export default {
    computed: {
        ...mapGetters({
            loggedInUser: 'loggedInUser'
        })
    },
    methods: {
        dropToggle(e) {
            var allDropDowns = document.querySelectorAll("ul.collapse.list-unstyled");
            for(var i=0; i<=allDropDowns.length-1; i++) 
            {
                if(allDropDowns[i] !== e.toElement.nextElementSibling)
                {
                    allDropDowns[i].classList.remove('show');
                }
            }
            e.toElement.nextElementSibling.classList.toggle('show')
        }
    }
}
</script>