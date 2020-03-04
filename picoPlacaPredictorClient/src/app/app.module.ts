import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PredictorComponentComponent } from './predictor-component/predictor-component.component';
import { ModalComponentComponent } from './modal-component/modal-component.component';

@NgModule({
  declarations: [
    AppComponent,
    PredictorComponentComponent,
    ModalComponentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
