import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders} from '@angular/common/http';  
import { backendUrl } from '../constants/endpoints';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class CompraService {
  httpHeaders = new HttpHeaders({'content-type': 'application/json'})

  constructor(private http: HttpClient) { }

  // agregarProducto(producto) {
  //   console.log(`Vamo a agregar ${producto.title}`)
  //   this.listaProductos.push(producto);
  //   // Falta guardar el producto en el backend
  //   console.log(this.listaProductos);
  // }

  obtenerProductos(): Observable<any>{
    const endpoint = "/prod/prod/"
    return this.http.get(`${backendUrl}${endpoint}`, {headers:  this.httpHeaders})
  }

  // actualizarEstadoProducto(id, nuevoEstado) {

  // }

  // borrarProducto(id) { 
  // }
}
