export default  {
    data() {
        return {
          
        };
    },
    methods: {
       openNewTab (url) {
        let evLink = document.createElement('a');
        evLink.href = url;
        evLink.target = '_blank';
        document.body.appendChild(evLink);
        evLink.click();
        // Now delete it
        evLink.parentNode.removeChild(evLink);
       }

    }

};
