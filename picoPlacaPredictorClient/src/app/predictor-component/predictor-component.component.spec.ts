import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PredictorComponentComponent } from './predictor-component.component';

describe('PredictorComponentComponent', () => {
  let component: PredictorComponentComponent;
  let fixture: ComponentFixture<PredictorComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PredictorComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PredictorComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
