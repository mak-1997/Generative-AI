import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DishesComponent } from './dishes/dishes.component';
import { UserLoginComponent } from './user-login/user-login.component';
import { UserSignupComponent } from './user-signup/user-signup.component';
import { AdminLoginComponent } from './admin-login/admin-login.component';
import { AdminSignupComponent } from './admin-signup/admin-signup.component';
import { AllOrdersComponent } from './all-orders/all-orders.component';
import { MyOrdersComponent } from './my-orders/my-orders.component';

const routes: Routes = [
  { path: '/', component: DishesComponent },
  { path: 'user/login', component: UserLoginComponent },
  { path: 'user/signup', component: UserSignupComponent },
  { path: 'user/orders', component: MyOrdersComponent },
  { path: 'admin/login', component: AdminLoginComponent },
  { path: 'admin/signup', component: AdminSignupComponent },
  { path: 'admin/orders', component: AllOrdersComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
