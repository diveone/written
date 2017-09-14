window.onload = function() {
    const vm = new Vue({
        el: '#app',
        data: {
            message: 'Hello Vue!',
            articles: []

        },
        created: function() {
            this.loadArticles();
        },
        methods: {
            loadArticles: function() {
                this.articles = "Loading ...";
                var vm = this;
                axios.defaults.baseURL = 'http://localhost:8000/api';
                axios.get('/blog/articles')
                    .then(function (response) {
                        vm.articles = response.data;
                        console.log(response);
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            }
        }
    })

};

