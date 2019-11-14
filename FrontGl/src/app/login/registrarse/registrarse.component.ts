import { Component, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { AuthService } from 'src/app/services/auth.service';

@Component({
    selector: 'app-registrarse',
    templateUrl: './registrarse.component.html',
    styleUrls: ['./registrarse.component.css']
})
export class RegistrarseComponent {
    showErrorMessage = false;
    constructor(
        public dialogRef: MatDialogRef<RegistrarseComponent>,
        @Inject(MAT_DIALOG_DATA) public data,
        private authService: AuthService) {}
    
      // onNoClick(): void {
      //   this.dialogRef.close();
      // }

      registrarse() {
        this.showErrorMessage = false
        // 1. Capturar la info del formulario
          const info = {} 
          // 2. Hacer la petición al backend pasandole la info a través del servicio
          this.authService.register(info).subscribe(respuesta => {
            console.log(respuesta);
            if (respuesta === "todo ok") { //Puede ser un true, un 200, lo que acuerden
              // Redirijo a la pantalla de inicio
            } else {
              // Mostrar mensaje de error
              this.showErrorMessage = true
            }
          })
      }
}