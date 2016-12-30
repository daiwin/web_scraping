import { Injectable } from '@angular/core';
import {Http} from '@angular/http';

@Injectable()
export class MyNewServiceService {

  constructor(private http: Http){ }

  getData(word:string){
    return this.http.get('http://localhost:5000/'+word);
  }
}
