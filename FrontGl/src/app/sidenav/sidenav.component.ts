import { Component, OnInit, ChangeDetectorRef, ViewChild } from '@angular/core';
import { MatSidenav } from '@angular/material/sidenav';
import { AuthServhice } from '../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-sidenav',
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.css']
})
export class SidenavComponent implements OnInit {

  @ViewChild('sidenav', {static: false}) sidenav: MatSidenav;

  productos = [
    {
    title: 'soy un titulo',
    // subtitle: 'soy un subtitulo',
    descripcion: 'la descripcion',
    cost: 50,
    image: 'https://i.pinimg.com/originals/b7/5b/15/b75b153dcba447d2384f94eeb526308e.jpg'
    }];

  reason = '';

  close(reason: string) {
    this.reason = reason;
    this.sidenav.close();
  }

  shouldRun = true;

  constructor(
    private authService: AuthServhice,
    private router: Router
   ) { }

  ngOnInit() {

    // vericamos que esta logeado
    const result = this.authService.isLoggedIn();
    if (!result) {
      console.log('intentando llevarlo', result);

      // navegacion
      this.router.navigate(['/login']);
    }
  }
}
