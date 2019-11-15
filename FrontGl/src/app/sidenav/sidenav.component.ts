import { Component, OnInit, ChangeDetectorRef, ViewChild } from '@angular/core';
import { MatSidenav } from '@angular/material/sidenav';
import { AuthService } from '../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-sidenav',
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.css']
})
export class SidenavComponent implements OnInit {

  @ViewChild('sidenav', { static: false }) sidenav: MatSidenav;

  productos = [
    {
      id: 0,
      title: 'soy una hamburguesa',
      // subtitle: 'soy un subtitulo',
      descripcion: 'la descripcion',
      cost: 50,
      image: 'https://i.pinimg.com/originals/b7/5b/15/b75b153dcba447d2384f94eeb526308e.jpg'
    },
    {
      id: 1,
      title: 'soy una hamburguesa más cara',
      // subtitle: 'soy un subtitulo',
      descripcion: 'la descripcion mas beia',
      cost: 250,
      image: 'https://i.pinimg.com/originals/b7/5b/15/b75b153dcba447d2384f94eeb526308e.jpg'
    },
    {
      id: 2,
      title: 'soy una hamburguesa con onda (más cara)',
      // subtitle: 'soy un subtitulo',
      descripcion: 'la descripcion mucho muy beia',
      cost: 350,
      image: 'https://i.pinimg.com/originals/b7/5b/15/b75b153dcba447d2384f94eeb526308e.jpg'
    }];

  reason = '';


  shouldRun = true;

  constructor(
    private authService: AuthService,
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
  
  close(reason: string) {
    this.reason = reason;
    this.sidenav.close();
  }

}
