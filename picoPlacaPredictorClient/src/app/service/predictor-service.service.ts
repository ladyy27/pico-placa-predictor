import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Prediction } from '../model/prediction';

@Injectable({
  providedIn: 'root'
})
export class PredictorServiceService {

  private predictorUrl: string;

  constructor(private http: HttpClient) {
    this.predictorUrl = 'http://127.0.0.1:8000/predictor/';
  }

  private modals: any[] = [];

  /* Modal methods*/
  public add(modal: any) {
    this.modals.push(modal);
  }

  public remove(id: string) {
    this.modals = this.modals.filter(x => x.id !== id);
  }

  public open(id: string) {
    const modal = this.modals.find(x => x.id === id);
    modal.open();
  }

  public close(id: string) {
    const modal = this.modals.find(x => x.id === id);
    modal.close();
  }

  /* Predictor methods*/
  public findByPlateAndDatetime(plateLicense: string, date: string, time: string): Observable<Prediction> {
    return this.http.get<Prediction>(this.predictorUrl + plateLicense + '/' + date + '/' + time);
  }
}
