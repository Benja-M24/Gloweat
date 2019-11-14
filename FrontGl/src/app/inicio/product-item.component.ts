import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {
  // @Input() subtitle;
  @Input() title;
  @Input() image;
  @Input() description;
  @Input() cost;

  constructor() {
  }

  ngOnInit() {
  }

}
