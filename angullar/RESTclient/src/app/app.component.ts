import { Component } from '@angular/core';
import {MyNewServiceService} from './my-new-service.service';
import {Response} from "@angular/http";

export class element {
  count : string;
  dt : string;
}

export class Film {
  mass: any ;
}




@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [MyNewServiceService]
})




export class AppComponent {

  film: any;
  term ="";

	values = [
	];

  countArray = [];
  dtArray=[];





  public constructor(private dataService: MyNewServiceService){
  }

  // lineChart
  public lineChartData:Array<any> = [
    {data: this.countArray, label: 'количество'}
  ];
  public lineChartLabels:Array<any> = this.dtArray;
  public lineChartOptions:any = {
    animation: false,
    responsive: true
  };
  public lineChartColors:Array<any> = [
    { // grey
      backgroundColor: 'rgba(148,159,177,0.2)',
      borderColor: 'rgba(148,159,177,1)',
      pointBackgroundColor: 'rgba(148,159,177,1)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgba(148,159,177,0.8)'
    }
  ];

  public lineChartType:string = 'line';

  ButtClick(value : string){

      this.term = value;

      this.dataService.getData(this.term).subscribe((data: Response) => {this.film = data.json();

      this.values = JSON.parse(this.film)['mass'];

      this.countArray = [];
      this.dtArray=[];

      for (let entry of this.values) {
        this.dtArray.push(entry.dt);
        this.countArray.push(entry.count);
      }

     // console.log(this.countArray);


      this.lineChartData= [
        {data: this.countArray, label: 'количество'}
      ];
      this.lineChartLabels = this.dtArray;

    });
    //this.values = this.film.mass;



  }





}

