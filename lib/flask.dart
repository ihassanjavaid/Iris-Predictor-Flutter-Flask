import 'package:http/http.dart';

Future getData(url) async {
  Response response = await get(url);
  return response.body;
}