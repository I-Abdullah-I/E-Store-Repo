import { makeAutoObservable } from 'mobx';

export default class UiStore {
  constructor() {
    makeAutoObservable(this);
  }

  activePath = '/';
  notificationData = {};

  setActivePage = (path: string) => {
    this.activePath = path;
  };

  showNotification = (message: string , status: string) => {
    this.notificationData = {
      message,
      status,
    };
  };

  hideNotification = () => {
    this.notificationData = {};
  };
}
