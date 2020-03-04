import { TestBed } from '@angular/core/testing';

import { PredictorServiceService } from './predictor-service.service';

describe('PredictorServiceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: PredictorServiceService = TestBed.get(PredictorServiceService);
    expect(service).toBeTruthy();
  });
});
