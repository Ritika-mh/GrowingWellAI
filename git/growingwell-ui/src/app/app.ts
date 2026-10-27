import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { DailyRecordComponent } from '../daily-record/daily-record.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet,DailyRecordComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('growingwell-ui');
}
