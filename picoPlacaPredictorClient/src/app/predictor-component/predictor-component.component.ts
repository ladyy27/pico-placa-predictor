import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { formatDate } from '@angular/common';
import { PredictorServiceService } from '../service/predictor-service.service';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-predictor-component',
  templateUrl: './predictor-component.component.html',
  styleUrls: ['./predictor-component.component.css']
})
export class PredictorComponentComponent implements OnInit {

  angForm: FormGroup;
  dateNowISO: Date;
  date: string;
  time: string;
  day: string;
  picoPlacaResponse: object;

  constructor(
    private fb: FormBuilder,
    private predictorService: PredictorServiceService) {
    this.angForm = this.fb.group({
      plateLicense: ['', Validators.required],
      datetime: ['', Validators.required]
    });
  }

  ngOnInit() {
  }

  onSubmit() {
    this.date = formatDate(this.angForm.value.datetime, 'yyyy-dd-MM', 'en-US');
    this.time = formatDate(this.angForm.value.datetime, 'HH:mm:ss', 'en-US');
    this.day = formatDate(this.angForm.value.datetime, 'EEEE', 'en-US');
    this.predictorService.findByPlateAndDatetime(this.angForm.value.plateLicense , this.date, this.time, this.day).subscribe(data => {
      this.picoPlacaResponse = data;
    });
    console.log(this.angForm.value.plateLicense);
    console.log(this.date);
    console.log(this.time);
    console.log(this.day);
  }

  openModal(id: string) {
    this.predictorService.open(id);
  }

  closeModal(id: string) {
    this.predictorService.close(id);
  }

}
