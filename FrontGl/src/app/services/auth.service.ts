import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { backendUrl } from '../constants/endpoints';

@Injectable({
  providedIn: 'root',
})
export class AuthService {

  private isLogedIn = true;

  constructor(private httpClient: HttpClient) {
  }

  isLoggedIn() {
    return this.isLogedIn;
  }

  setStatus(status: boolean) {
    this.isLogedIn = status;
  }

  register(info) {
    const endpoint = "/login"
    // Este metodo debería recibir la info de los campos cuando el usuario hace click en "registrarse"
    // Hacer la petición al backend y en caso de éxito, devolver un "true"
    return this.httpClient.post(`${backendUrl}${endpoint}`, info)
  }

}
