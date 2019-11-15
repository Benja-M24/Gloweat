import { Component, OnInit } from '@angular/core';
import {MatDialog} from '@angular/material/dialog';
import { RegistrarseComponent } from './registrarse/registrarse.component';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(public dialog: MatDialog) { }

  ngOnInit() {
  }

  openRegisterDialog(): void {
    const dialogRef = this.dialog.open(RegistrarseComponent, {
      width: '500px',
      data: {}
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      // this.animal = result;
    });
  }

  openLoginDialog() {
    // Hacer componente IniciarSesionComponent
  }
}
