import {Component, OnInit} from '@angular/core';
import { formatDate } from '@angular/common';
import { PredictorServiceService } from './service/predictor-service.service';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title: string;
  angForm: FormGroup;
  date: string;
  time: string;
  picoPlacaResponse: object;

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private predictorService: PredictorServiceService) {
    this.title = 'Pico&Placa Predictor';
    this.angForm = this.fb.group({
      licensePlate: ['', Validators.required],
      datetime: ['', Validators.required]
    });
  }
  ngOnInit() {
  }

  onSubmit() {
    this.date = formatDate(this.angForm.value.datetime, 'yyyy-dd-MM', 'en-US');
    this.time = formatDate(this.angForm.value.datetime, 'HH:mm:ss', 'en-US');
    this.predictorService.findByPlateAndDatetime( this.angForm.value.licensePlate, this.date, this.time).subscribe(data => {
      this.picoPlacaResponse = data;
      this.gotoMain();
    });
  }

  openModal(id: string) {
    this.predictorService.open(id);
  }

  closeModal(id: string) {
    this.predictorService.close(id);
    this.angForm.reset();
  }

  gotoMain() {
    this.router.navigate(['']);
  }
}




