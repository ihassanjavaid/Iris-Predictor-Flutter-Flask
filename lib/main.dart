import 'package:flutter/material.dart';
import 'package:iris_predictor/prediction_screen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Iris-Predictor',
      debugShowCheckedModeBanner: false,
      home: Predictor(),
    );
  }
}


