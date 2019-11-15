import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CompraService {
  listaProductos = []
  constructor() { }

  agregarProducto(producto) {
    console.log(`Vamo a agregar ${producto.title}`)
    this.listaProductos.push(producto);
    // Falta guardar el producto en el backend
    console.log(this.listaProductos);
  }

  obtenerProductos() {
    // Falta obtener lista de productos desde el backend
    return this.listaProductos;
  }

  actualizarEstadoProducto(id, nuevoEstado) {

  }

  borrarProducto(id) {
    
  }
}
