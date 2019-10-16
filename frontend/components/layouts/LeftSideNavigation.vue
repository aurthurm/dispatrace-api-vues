<template>
    <aside id="left-aside">
        <nav id="sidebar">
            <b-navbar-brand href="#">DISPATRACE</b-navbar-brand>
            <ul class="list-unstyled components">
                 <nuxt-link to="/" class="nav-item" tag="li">
                    <a class="nav-link">DASHBOARD</a>
                 </nuxt-link>
                 <nuxt-link to="/memo" class="nav-item" tag="li">
                    <a class="nav-link">Memorandum</a>
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
                <b-nav-item href="#">Link 1</b-nav-item>
                <li>
                    <a 
                    href="#pageSubmenu" 
                    data-toggle="collapse" 
                    aria-expanded="false" 
                    class="dropdown-toggle" 
                    @click.prevent.stop="dropToggle($event)" 
                    >Pages</a>
                    <ul class="collapse list-unstyled" id="pageSubmenu">
                        <li>
                            <a href="#">Page 1</a>
                        </li>
                        <li>
                            <a href="#">Page 2</a>
                        </li>
                        <li>
                            <a href="#">Page 3</a>
                        </li>
                    </ul>
                </li>
                <b-nav-item href="#">Link 2</b-nav-item>
                <b-nav-item href="#">Link 3</b-nav-item> -->
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
    background: black;
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
    background: black;
    color: #fff;
    transition: all 0.3s;
}

#sidebar .sidebar-header {
    padding: 20px;
    background: black;
}

#sidebar ul.components {
    padding: 20px 0;
    border-bottom: 1px solid black;
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
    color: black;
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
    background: black;
}
</style>

<script>
export default {
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