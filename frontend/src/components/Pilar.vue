<template>
  <div class="container-fluid" id="pilar">
    <div class="row">
      <div class="col-lg-12 mx-auto">
        <h1>Coba Saja Dulu</h1>
        <div class="card mt-4">
          <div class="card-body">
           <button @click="Tambah" class="btn btn-primary mb-3">Tambah Data</button>
            <table class=" table table-bordered table-striped table-hover">
              <thead class="alert-primary">
                  <tr>
                    <th>Id</th>
                    <th>Pilar</th>
                    <th>Deskripsi</th>
                    <th>Aksi</th>
                  </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1</td>
                  <td >Misal Nya Ini Data DAri DB</td>
                  <td>Dan ini juga sama data dari DB</td>
                  <td width="175px">
                    <button @click="Edit(pilar)" class="btn btn-primary">Edit</button>
                    <button @click="Hapus()" class="btn btn-danger">Hapus</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <div class="modal fade" id="ModalTambah" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 v-show="!EditMode" class="modal-title" id="exampleModalLabel">Tambah Data</h5>
            <h5 v-show="EditMode" class="modal-title" id="exampleModalLabel">Perbarui Data</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
         <form @submit.prevent="EditMode ? PerbaruiData() : TambahData()" >
          <div class="modal-body">
            <div class="form-group">
              <label for="pilar">Pilar</label>
              <input v-model="pilar" placeholder="Masukan Pilar" type="text" class="form-control" id="pilar">
            </div>
            <div class="form-group">
              <label for="deskripsi">Deskripsi</label>
              <textarea v-model="deskripsi" placeholder="Masukan Deskripsi" type="text" class="form-control" id="deskripsi">
              </textarea>
            </div>
           </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Tutup</button>
            <button v-show="!EditMode" type="submit" class="btn btn-success">Tambah</button>
            <button v-show="EditMode" type="submit" class="btn btn-warning">Perbarui</button>
          </div>
        </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data(){
    return {
      pilar:[],
      id:'',
      pilar:'',
      deskripsi:'',
      EditMode: false
    }
  },
  mounted() {
    console.log('Terload');
  },
  methods:{
    PerbaruiData(){
      $('#ModalTambah').modal('hide');
       this.$swal(
        'Berhasil ',
        'Datamu sudah berhasil Diperbarui.',
        'success'
      )
    },
    TambahData(){
      $('#ModalTambah').modal('hide');
       this.$swal(
        'Berhasil ',
        'Datamu sudah berhasil Dibuat.',
        'success'
      )
    },
    Tambah(){
      this.EditMode = false;
      $('#ModalTambah').modal('show');
    },
    Edit(pilar){
      this.EditMode = true;
      $('#ModalTambah').modal('show');
    },
    Hapus(){
            this.$swal({
              title: 'Apa Anda Yakin?',
              text: "Kamu tidak dapat mengembalikan nya",
              icon: 'warning',
              showCancelButton: true,
              confirmButtonColor: '#3085d6',
              cancelButtonColor: '#d33',
              cancelButtonText: 'Batalkan',
              confirmButtonText: 'Ya, Hapus Saja!',
            }).then((result) => {
              if (result.value) {
                this.$swal(
                  'Terhapus!',
                  'Datamu sudah berhasil Terhapus.',
                  'success'
                )
              }else if (
                    /* Read more about handling dismissals below */
                    result.dismiss === swal.DismissReason.cancel
                  ) {
                    this.$swal(
                      'Dibatalkan!',
                      'Datamu masih Aman.',
                      'warning'
                    )
                  }
            });
      }
    }
}

</script>