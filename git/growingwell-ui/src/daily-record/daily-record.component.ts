
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';


import { DailyRecordService } from '../services/daily-record.service';
import { DailyRecord, DailyRecordResponse } from '../models/daily-record.model';

@Component({
  selector: 'app-daily-record',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './daily-record.component.html',
  styleUrl: './daily-record.component.css'
})
export class DailyRecordComponent {

  record: DailyRecord = {
    child_age: 4.5,
    food: '',
    protein_foods: '',
    sleep_hours: 0,
    outdoor_minutes: 0,
    study_minutes: 0,
    screen_minutes: 0,
    record_date: new Date().toISOString().slice(0, 10),
    ai_response:''
  };

  aiSummary = '';
  message = '';
  loading = false;

  constructor(private dailyRecordService: DailyRecordService) {
    this.loadRecords()
  }

  
records: DailyRecord[] = [];
isEditMode = false;
editingRecordId: number | null = null;
loadRecords(): void {
  this.dailyRecordService.getRecords().subscribe({
    next: (response: DailyRecord[]) => {
      this.records = response;
    },
    error: (error) => {
      console.error('Error loading records:', error);
    }
  });
}

  // saveRecord(): void {
  //   this.loading = true;
  //   this.message = '';
  //   this.aiSummary = '';

  //   this.dailyRecordService.createRecord(this.record).subscribe({
  //     next: (response: DailyRecordResponse) => {
  //       this.message = response.message;
  //       this.aiSummary = response.ai_summary;
  //       this.loadRecords();
  //       this.loading = false;
  //     },
  //     error: (error) => {
  //       this.message =
  //         error.error?.error ||
  //         'Unable to save the daily record. Please try again.';
  //       this.loading = false;
  //     }
  //   });
  // }


saveRecord(): void {
  this.loading = true;
  this.message = '';
  this.aiSummary = '';

  // EDIT MODE: call Update API
  if (this.isEditMode && this.editingRecordId !== null) {
    this.dailyRecordService
      .updateRecord(this.editingRecordId, this.record)
      .subscribe({
        next: () => {
          this.message = 'Daily record updated successfully!';
          this.isEditMode = false;
          this.editingRecordId = null;
          this.loadRecords();
          this.loading = false;
        },
        error: (error) => {
          this.message =
            error.error?.error || 'Unable to update the record.';
          this.loading = false;
        }
      });

    return;
  }

  // CREATE MODE: call Create API
  this.dailyRecordService.createRecord(this.record).subscribe({
    next: (response: DailyRecordResponse) => {
      this.message = response.message;
      this.aiSummary = response.ai_summary;
      this.loadRecords();
      this.loading = false;
    },
    error: (error) => {
      this.message =
        error.error?.error ||
        'Unable to save the daily record. Please try again.';
      this.loading = false;
    }
  });
}

  
selectedRecord: DailyRecord | null = null;
viewLoading = false;

viewRecord(recordId: number): void {
  this.viewLoading = true;
  this.message = '';

  this.dailyRecordService.getRecord(recordId).subscribe({
    next: (response: DailyRecord) => {
      this.selectedRecord = response;
      this.viewLoading = false;
    },
    error: (error) => {
      this.message =
        error.error?.error || 'Unable to retrieve this record.';
      this.viewLoading = false;
    }
  });
}

deleteRecord(recordId: number): void {
  const confirmed = window.confirm(
    'Are you sure you want to delete this daily record?'
  );

  if (!confirmed) {
    return;
  }

  this.dailyRecordService.deleteRecord(recordId).subscribe({
    next: (response) => {
      this.message = response.message;
      this.selectedRecord = null;
      this.loadRecords();
    },
    error: (error) => {
      this.message =
        error.error?.error || 'Unable to delete this record.';
    }
  });
}


editRecord(item: DailyRecord): void {
  if (item.id === undefined) {
    return;
  }

  this.record = {
    child_age: item.child_age,
    food: item.food,
    protein_foods: item.protein_foods || '',
    sleep_hours: item.sleep_hours,
    outdoor_minutes: item.outdoor_minutes,
    study_minutes: item.study_minutes,
    screen_minutes: item.screen_minutes,
    record_date: item.record_date
  };

  this.editingRecordId = item.id;
  this.isEditMode = true;
  this.aiSummary = item.ai_response || '';
  this.message = '';

  window.scrollTo({ top: 0, behavior: 'smooth' });
}


clearForm(): void {
  this.record = {
    child_age: 4.5,
    food: '',
    protein_foods: '',
    sleep_hours: 0,
    outdoor_minutes: 0,
    study_minutes: 0,
    screen_minutes: 0,
    record_date: new Date().toISOString().slice(0, 10)
  };

  this.isEditMode = false;
  this.editingRecordId = null;
  this.aiSummary = '';
  this.message = '';
}



}
