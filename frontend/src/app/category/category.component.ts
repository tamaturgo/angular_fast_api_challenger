import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.scss']
})
export class CategoryComponent {
  constructor() { }

  categoryForm = new FormGroup({
    categoryName: new FormControl(''),
  });

  createCategory() {
    console.log(this.categoryForm.value);
  }


}
