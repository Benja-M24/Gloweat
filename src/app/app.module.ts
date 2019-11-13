//Componentes

import { BrowserModule } from '@angular/platform-browser';
import { NgModule, Component } from '@angular/core';
import { InicioComponent } from './inicio/inicio.component';
import { AppComponent } from './app.component';
import { SidenavComponent } from './sidenav/sidenav.component';
import { LoginComponent } from './login/login.component';


//Modulos Material

import { AppRoutingModule } from './app-routing.module';
import {MatCardModule} from '@angular/material/card';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatListModule} from '@angular/material/list';
import {LayoutModule} from '@angular/cdk/layout';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatInputModule} from '@angular/material/input';
import {MatButtonModule} from '@angular/material/button';
import {MatTableModule} from '@angular/material/table';

import {RouterModule, Routes} from '@angular/router';
import { ProductosComponent } from './productos/productos.component';
import { ElaboracionComponent } from './elaboracion/elaboracion.component';

const routes: Routes = [
  // {path: '', component: SidenavComponent},
  // {path: '/login', component: LoginComponent}
];

@NgModule({
  declarations: [
    AppComponent,
    InicioComponent,
    SidenavComponent,
    LoginComponent,
    ProductosComponent,
    ElaboracionComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatCardModule,
    BrowserAnimationsModule,
    MatSidenavModule,
    MatListModule,
    LayoutModule,
    MatToolbarModule,
    MatInputModule,
    MatButtonModule,
    MatTableModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
