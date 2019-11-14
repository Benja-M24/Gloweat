import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class AuthServhice {

  private isLogedIn = true;

  constructor() {
  }

  isLoggedIn() {
    return this.isLogedIn;
  }

  setStatus(status: boolean) {
    this.isLogedIn = status;
  }

}
