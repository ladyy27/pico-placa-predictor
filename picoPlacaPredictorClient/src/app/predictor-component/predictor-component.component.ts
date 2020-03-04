import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
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
    this.dateNowISO = this.angForm.value.datetime.toISOString();
    /*this.predictorService.findByPlateAndDatetime(this.angForm.value.plateLicense , this.dateNowISO).subscribe(data => {
      this.picoPlacaResponse = data;
    });*/
    this.predictorService.findByPlate(this.angForm.value.plateLicense).subscribe(data => {
      this.picoPlacaResponse = data;
    });
    console.log(this.angForm.value.plateLicense);
    console.log(this.dateNowISO);
  }

  openModal(id: string) {
    this.predictorService.open(id);
  }

  closeModal(id: string) {
    this.predictorService.close(id);
  }

}
