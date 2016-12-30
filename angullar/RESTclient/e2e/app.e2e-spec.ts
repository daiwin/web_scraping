import { RESTclientPage } from './app.po';

describe('restclient App', function() {
  let page: RESTclientPage;

  beforeEach(() => {
    page = new RESTclientPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
