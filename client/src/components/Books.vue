<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Books</h1>
        <hr><br><br>
        <alert :message="message" v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>Add Book</button>
        <br><br>
        <table class="table table-hover">
          <thead class="w-100">
          <tr>
            <th scope="col">Title</th>
            <th scope="col">Author</th>
            <th scope="col">Read</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(book,index) in books" :key="index">
            <td>{{ book.title }}</td>
            <td>{{ book.author }}</td>
            <td>
              <span v-if="book.read">Yes</span>
              <span v-else>No</span>
            </td>
            <td>
              <button type="button" class="btn btn-warning btn-sm" v-b-modal.book-update-modal @click="editBook(book)">
                Update</button>
              <button type="button" class="btn btn-danger btn-sm" @click="deleteBook(book)">Delete</button>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addBookModal"
             id="book-modal"
             title="add a new book"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-title-group"
                      label="Title"
                      label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addBookForm.title"
                        required
                        plcaeholder="Enter title">
          </b-form-input>
        </b-form-group>
            <b-form-group id="form-author-group"
                  label="Author:"
                  label-for="form-author-input">
        <b-form-input id="form-author-input"
                      type="text"
                      v-model="addBookForm.author"
                      required
                      placeholder="Enter author">
        </b-form-input>
      </b-form-group>
<b-form-group id="form-read-group">
      <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
        <b-form-checkbox value="true">Read?</b-form-checkbox>
      </b-form-checkbox-group>
    </b-form-group>
    <b-button type="submit" variant="primary">Submit</b-button>
    <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>



        <b-modal ref="updateBookModal"
             id="book-update-modal"
             title="update a new book"
             hide-footer>
      <b-form @submit="onEditSubmit" @reset="onEditReset" class="w-100">
        <b-form-group id="form-title-group"
                      label="Title"
                      label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="editBookForm.title"
                        required
                        plcaeholder="Enter title">
          </b-form-input>
        </b-form-group>
            <b-form-group id="form-author-group"
                  label="Author:"
                  label-for="form-author-input">
        <b-form-input id="form-author-input"
                      type="text"
                      v-model="editBookForm.author"
                      required
                      placeholder="Enter author">
        </b-form-input>
      </b-form-group>
<b-form-group id="form-read-group">
      <b-form-checkbox-group v-model="editBookForm.read" id="form-checks">
        <b-form-checkbox value="true">Read?</b-form-checkbox>
      </b-form-checkbox-group>
    </b-form-group>
    <b-button type="submit" variant="primary">Submit</b-button>
    <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </div>
</template>


<script>
  import axios from 'axios';
  import Alert from './Alert';

  export default {
   data(){
     return {
       books: [],
       addBookForm:{
         id:'',
         title: '',
         author: '',
         read: [],
       },
       editBookForm:{
         id:'',
         title: '',
         author: '',
         read: [],
       },
       message:'',
       showMessage: false,
     }
   },
    components:{
     alert: Alert,
    },
    methods:{
     getBooks(){
       const path = 'http://localhost:5000/books';
       axios.get(path)
         .then((res) => {
           this.books = res.data.books;
           })
         .catch((error) => {
           // eslint-disable-next-line
           console.log(error);
           })
     },
      addBook(payload){
        const path = 'http://localhost:5000/books';
        axios.post(path,payload)
          .then(() => {
            this.getBooks();
            this.message="Book Added!";
            this.showMessage=true;
          })
          .catch((error) => {
            console.log(error);
            this.getBooks();
            this.message="Book Added Failed";
            this.showMessage=false;
          })
      },
      initForm(){
       this.addBookForm.title = '';
       this.addBookForm.author = '';
       this.addBookForm.read = [];
      },
      onSubmit(evt){
       evt.preventDefault();
       this.$refs.addBookModal.hide();
       let read = false;
       if(this.addBookForm.read[0]) read = true;
       const payload = {
         title: this.addBookForm.title,
         author: this.addBookForm.author,
         read,
       };
       this.addBook(payload);
       this.initForm();
      },
      onReset(evt){
       evt.preventDefault();
       this.$refs.addBookModal.hide();
       this.initForm();
      },
      initEditForm(){
        this.editBookForm.title = '';
        this.editBookForm.author = '';
        this.editBookForm.read = [];
      },
      updateBook(payload,bookId){
       // alert(bookId)
       const path = `http://localhost:5000/books/${bookId}`
        // alert(path)
        axios.put(path,payload).then((res)=>{
          this.getBooks();
          this.message='update success';
          this.showMessage=true;
        }).catch((error)=>{
          console.log(error);
        })
      },
      editBook(book){
       this.editBookForm.id = book.id;
       this.editBookForm.title = book.title;
       this.editBookForm.author = book.author;
       this.editBookForm.read = book.read;
      },
      onEditSubmit(evt){
       evt.preventDefault();
       this.$refs.updateBookModal.hide();
       let read = false;
       if(this.editBookForm.read[0]) read = true;
       const payload = {
         title: this.editBookForm.title,
         author: this.editBookForm.author,
         read
       };
       this.updateBook(payload,this.editBookForm.id);
       this.initEditForm();
       // this.getBooks();
      },
      onEditReset(evt){
       evt.preventDefault();
       this.$refs.updateBookModal.hide();
       this.initEditForm();
      },
      deleteBook(book){
       let bookId = book.id;
       const path = `http://localhost:5000/books/${bookId}`;
       axios.delete(path).then(()=>{
         this.getBooks();
         this.message = 'delete success';
         this.showMessage = true;
       }).catch((error) => {
         console.log(error);
       })
      }
    },
    created(){
     this.getBooks();
    }
  }
</script>
