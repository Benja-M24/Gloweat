import { Component, OnInit, ChangeDetectorRef, ViewChild } from '@angular/core';
import { MatSidenav } from '@angular/material/sidenav';

@Component({
  selector: 'app-sidenav',
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.css']
})
export class SidenavComponent implements OnInit {

  @ViewChild('sidenav', {static: false}) sidenav: MatSidenav;

  prductos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];

  reason = '';

  close(reason: string) {
    this.reason = reason;
    this.sidenav.close();
  }

  shouldRun = true;

  ngOnInit() {
  }

}
