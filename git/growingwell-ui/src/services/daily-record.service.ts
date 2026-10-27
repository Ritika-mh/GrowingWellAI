
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { DailyRecord, DailyRecordResponse } from '../models/daily-record.model';


@Injectable({
  providedIn: 'root'
})
export class DailyRecordService {

  private apiUrl = 'http://127.0.0.1:8000/api/daily-records/';

  constructor(private http: HttpClient) {}

  createRecord(data: DailyRecord): Observable<DailyRecordResponse> {
    return this.http.post<DailyRecordResponse>(
      `${this.apiUrl}create/`,
      data
    );
  }

  getRecords(): Observable<DailyRecord[]> {
    return this.http.post<DailyRecord[]>(
      this.apiUrl,
      {}
    );
  }

  
updateRecord(
  recordId: number,
  data: Partial<DailyRecord>
): Observable<DailyRecordResponse> {
  return this.http.post<DailyRecordResponse>(
    `${this.apiUrl}update/`,
    { ...data, record_id: recordId }
  );
}


  
getRecord(recordId: number): Observable<DailyRecord> {
  return this.http.post<DailyRecord>(
    `${this.apiUrl}retrieve/`,
    { record_id: recordId }
  );
}

deleteRecord(recordId: number): Observable<{ message: string }> {
  return this.http.post<{ message: string }>(
    `${this.apiUrl}delete/`,
    { record_id: recordId }
  );
}

}
