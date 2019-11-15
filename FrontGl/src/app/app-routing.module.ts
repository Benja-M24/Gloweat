import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SidenavComponent } from './sidenav/sidenav.component';
import { LoginComponent } from './login/login.component';
import { ProductosComponent } from './productos/productos.component';
import { ElaboracionComponent } from './elaboracion/elaboracion.component';

const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'index',      component: SidenavComponent},
  { path: 'productos', component: ProductosComponent },
  { path: 'elaboracion', component: ElaboracionComponent },
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
