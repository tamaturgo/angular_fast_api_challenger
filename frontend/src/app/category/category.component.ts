import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { CategoryService } from './category.service';
@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.scss'],
  providers: [CategoryService]
})
export class CategoryComponent {
  
  constructor (private categoryService: CategoryService) {}

  categoryForm = new FormGroup({
    categoryName: new FormControl('', Validators.required)
  });

  name: string | null | undefined = '';
  getValues() {
    this.name = this.categoryForm.value.categoryName;
  }

  createCategory() {
    this.name = this.categoryForm.value.categoryName;
    this.categoryService.addCategory(
      this.name as string
    ).subscribe(
      (res) => {
        console.log(res);
      },
      (err) => {
        console.log(err);
      }
    );
  }


}
