import { Component, OnInit } from '@angular/core';
import { CompraService } from '../services/compra.service';

@Component({
  selector: 'app-productos',
  templateUrl: './productos.component.html',
  styleUrls: ['./productos.component.css']
})
export class ProductosComponent implements OnInit {
  listaProductos = [];
  constructor(private compraService: CompraService) { }

  ngOnInit() {
    this.listaProductos = this.compraService.obtenerProductos()
    console.log(this.listaProductos)
  }

}
