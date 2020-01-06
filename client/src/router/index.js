import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Books from '@/components/Books';
import Posts from '@/components/Posts';
import Moment from '@/components/Moment';
import OrgTag from '@/components/OrgTag';
import Login from '@/components/Login';
import Home from "@/components/Home";
import QuestionLatestPosts from "@/components/QuestionLatestPosts";
import TopicTree from "@/components/TopicTree";
import PostsStruct from "@/components/PostsStruct";
import Post from '@/components/Post';
import TopicNew from '@/components/TopicNew';
import Boss from  '@/components/Boss';
import Tree from '@/view/tree'
import SlotTree from '@/view/slotTree'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path:'/posts',
      name: 'Posts',
      component:Posts,
    },
    {
      path: '/books',
      name: 'Books',
      component: Books,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/moment',
      name: 'Moment',
      component: Moment,
    },
    {
      path: '/orgtag',
      name: 'OrgTag',
      component: OrgTag
    },
    {
      path:'/login',
      name:"Login",
      component:Login
    },
    {
      path: "/home",
      name: "Home",
      component: Home
    },
    {
      path: '/question_posts/:id',
      name: 'QuestionLatestPosts',
      component: QuestionLatestPosts,
    },
    {
      path: '/',
      name: 'TopicTree',
      component: TopicTree,
    },
    {
      path: '/poststruct/:id',
      name: 'PostsStruct',
      component: PostsStruct,
    },
    {
      path:'/post',
      name: 'Post',
      component:Post,
    },
    {
      path:'/topic/new',
      name: 'TopicNew',
      component:TopicNew,
    },
    {
      path:'/boss',
      name:'Boss',
      component:Boss,
    },{
      path: '/render',
      name: 'RenderTree',
      component: Tree
    },{
      path: '/slot',
      name: 'SlotTree',
      component: SlotTree
    }
  ],
  mode: 'hash',
});
