import { shallowMount, createLocalVue } from '@vue/test-utils'
import Vuex from 'vuex'
import News from '@/views/Home.vue'

const localVue = createLocalVue();

localVue.use(Vuex);

describe('gain News Loading Test Suit', () => {
  let actions;
  let store;
  let getters;

  beforeEach(() => {
    // set up mockup related things for each it below
    actions = {
      getNewsList: () => [],
    }
    getters ={
        viewportBreakpoint: () => 314, // small screen
        searchBy: () => 'a',
    }
    store = new Vuex.Store({
      actions,
      getters,
    })

  });

  it('click button, Load More; each time increase 15', () => {
    const wrapper = shallowMount(News, { store, localVue });
    const btn = wrapper.find('.load-more');
    expect(wrapper.vm.page.start).toBe(0);
    btn.trigger('click');
    expect(wrapper.vm.page.start).toBe(15);
    btn.trigger('click');
    expect(wrapper.vm.page.start).toBe(30);
  })

  it('click "Load More" button 3 times the button should be disabled due to the max news # is 45', () => {
    const wrapper = shallowMount(News, { store, localVue });
    const btn = wrapper.find('.load-more');
    btn.trigger('click');
    btn.trigger('click');
    btn.trigger('click');
    expect(wrapper.vm.page.start).toBe(45);
    expect(wrapper.contains('.disable')).toBe(true); // check DOM updated
    expect(wrapper.vm.allLoaded).toBe(true);
  })

  it('inspect the small viewport size at global Vuex store and HTML DOM', () => {
    const wrapper = shallowMount(News, { store, localVue });
    wrapper.setData({ clientWidth: 200 });
    expect(wrapper.contains('.small-content')).toBe(true); // check DOM updated
   
  })

  it('inspect the normal viewport size at global Vuex store', () => {
    const wrapper = shallowMount(News, { store, localVue });
    wrapper.setData({ clientWidth: 1200 });
    expect(wrapper.contains('.top-content')).toBe(true); // check DOM updated
   
  })

 
})