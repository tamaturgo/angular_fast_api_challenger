import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {

  constructor(
    private http: HttpClient

  ) { }

  url = 'http://127.0.0.1:3009/categories/';
  
  public addCategory(name: string) {
    return this.http.post(this.url, {name});
  }

  getCategories() {
    return this.http.get(this.url);
  }

  getCategory(id: string) {
    return this.http.get(`${this.url}/${id}`);
  }

  updateCategory(id: string, categoryName: string) {
    return this.http.put(`${this.url}/${id}`, {categoryName});
  }

  deleteCategory(id: string) {
    return this.http.delete(`${this.url}/${id}`);
  }

}
