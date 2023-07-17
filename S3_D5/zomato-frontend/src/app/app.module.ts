import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DishesComponent } from './dishes/dishes.component';
import { UserLoginComponent } from './user-login/user-login.component';
import { UserSignupComponent } from './user-signup/user-signup.component';
import { AdminSignupComponent } from './admin-signup/admin-signup.component';
import { AdminLoginComponent } from './admin-login/admin-login.component';
import { NavabrComponent } from './navabr/navabr.component';
import { FormsModule } from '@angular/forms';
import { AllOrdersComponent } from './all-orders/all-orders.component';
import { MyOrdersComponent } from './my-orders/my-orders.component';

@NgModule({
  declarations: [
    AppComponent,
    DishesComponent,
    UserLoginComponent,
    UserSignupComponent,
    AdminSignupComponent,
    AdminLoginComponent,
    NavabrComponent,
    AllOrdersComponent,
    MyOrdersComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
