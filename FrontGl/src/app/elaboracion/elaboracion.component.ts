import { Component, OnInit } from '@angular/core';
import { CompraService } from '../services/compra.service';

@Component({
  selector: 'app-elaboracion',
  templateUrl: './elaboracion.component.html',
  styleUrls: ['./elaboracion.component.css']
})
export class ElaboracionComponent implements OnInit {
  
  listaProductos = [];
  constructor(private compraService: CompraService) { }

  ngOnInit() {
    this.listaProductos = this.compraService.obtenerProductos()
    console.log(this.listaProductos)
  }

}
