
export interface DailyRecord {
  id?: number;
  child_age: number;
  food: string;
  protein_foods: string;
  sleep_hours: number;
  outdoor_minutes: number;
  study_minutes: number;
  screen_minutes: number;
  record_date: string;
  ai_response?:string;
}

export interface DailyRecordResponse {
  message: string;
  record: DailyRecord;
  ai_summary: string;
}
