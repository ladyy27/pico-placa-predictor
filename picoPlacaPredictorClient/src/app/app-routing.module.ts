import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PredictorComponentComponent } from './predictor-component/predictor-component.component';


const routes: Routes = [
  { path: 'plate-predictor', component: PredictorComponentComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
