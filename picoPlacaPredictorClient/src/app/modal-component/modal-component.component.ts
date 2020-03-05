import { Component, ViewEncapsulation, ElementRef, Input, OnInit , OnDestroy} from '@angular/core';
import { PredictorServiceService } from '../service/predictor-service.service';

@Component({
  selector: 'jw-modal',
  templateUrl: './modal-component.component.html',
  styleUrls: ['./modal-component.component.less'],
  encapsulation: ViewEncapsulation.None
})
export class ModalComponentComponent implements OnInit, OnDestroy {
  @Input() id: string;
  private element: any;

  constructor(
    private predictorService: PredictorServiceService,
    private el: ElementRef) {
    this.element = el.nativeElement;
  }

  ngOnInit(): void {
    if (!this.id) {
      console.error('modal needs an ID');
      return;
    }

    document.body.appendChild(this.element);

    this.element.addEventListener('click', el => {
      if (el.target.className === 'jw-modal') {
        this.close();
      }
    });

    this.predictorService.add(this);
  }
  ngOnDestroy(): void {
    this.predictorService.remove(this.id);
    this.element.remove();
  }
  open(): void {
    this.element.style.display = 'block';
    document.body.classList.add('jw-modal-open');
  }
  close(): void {
    this.element.style.display = 'none';
    document.body.classList.remove('jw-modal-open');
  }
}
