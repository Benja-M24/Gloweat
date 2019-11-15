import { Component, OnInit, Input } from '@angular/core';
import { CompraService } from '../services/compra.service';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {
  // @Input() subtitle;
  @Input() id;
  @Input() title;
  @Input() image;
  @Input() description;
  @Input() cost;

  constructor(private compraService: CompraService) {
  }

  ngOnInit() {
  }

  comprarProducto() {
    const producto = {
      id: this.id,
      title: this.title,
      image: this.image,
      description: this.description,
      cost: this.cost,
    }
    this.compraService.agregarProducto(producto);
  }
}
