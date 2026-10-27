import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DailyRecordComponent } from './daily-record.component';

describe('DailyRecordComponent', () => {
  let component: DailyRecordComponent;
  let fixture: ComponentFixture<DailyRecordComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DailyRecordComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DailyRecordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
