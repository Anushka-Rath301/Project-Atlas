/*
 Name:		WinsonLib.cpp
 Created:	2022/6/30 上午 11:41:27
 Author:	RD
 Editor:	http://www.visualmicro.com
*/

#include "WCS1700.h"

#pragma endregion
/*
  WCS1700.cpp
  Lightweight WCS1700 Current Sensor Library
  Adapted from WinsonLib for Arduino UNO Q
*/

#include "WCS1700.h"

// Single Output Constructor
WCS1700::WCS1700(uint8_t analogPin, uint16_t mVperA)
{
    _Mode = SingleOutput;
    _AIpin = analogPin;
    _AIpin2 = 0;
    _sensitivity = mVperA;
    _midPoint = 512;
}

// Differential Output Constructor
WCS1700::WCS1700(uint8_t analogPin, uint8_t analogPin2, uint16_t mVperA)
{
    _Mode = DifferentialOutput;
    _AIpin = analogPin;
    _AIpin2 = analogPin2;
    _sensitivity = mVperA;
    _midPoint = 0;
}

// Reset current sensor (find midpoint)
void WCS1700::Reset()
{
    int32_t dataSum = 0;

    ReadADCBuffer(_dataScaled);

    for (int i = 0; i < 120; i++)
    {
        dataSum += _dataScaled[i];
    }

    _midPoint = dataSum / 120;
}

// Measure DC Current
double WCS1700::A_DC()
{
    int16_t steps;

    if (_Mode == SingleOutput)
    {
        analogRead(_AIpin);
        steps = analogRead(_AIpin) - _midPoint;
    }
    else
    {
        analogRead(_AIpin);
        analogRead(_AIpin2);
        steps = analogRead(_AIpin) - analogRead(_AIpin2) - _midPoint;
    }

    return ((double)steps * 5.0 / 1023.0) /
           ((double)_sensitivity * 0.001);
}

// Measure AC Current (RMS)
double WCS1700::A_AC()
{
    int16_t steps;
    double current;
    double sum = 0.0;

    ReadADCBuffer(_dataScaled);

    for (int i = 0; i < 120; i++)
    {
        steps = _dataScaled[i] - _midPoint;

        current = ((double)steps * 5.0 / 1023.0) /
                  ((double)_sensitivity * 0.001);

        sum += current * current;
    }

    return sqrt(sum / 120.0);
}

// Read ADC Samples
void WCS1700::ReadADCBuffer(int16_t *rawData)
{
    analogRead(_AIpin);

    if (_Mode == DifferentialOutput)
        analogRead(_AIpin2);

    if (_Mode == SingleOutput)
    {
        for (int i = 0; i < 120; i++)
        {
            _start = micros();

            rawData[i] = analogRead(_AIpin);

            while ((micros() - _start) < 829);
        }
    }
    else
    {
        for (int i = 0; i < 120; i++)
        {
            _start = micros();

            rawData[i] = analogRead(_AIpin) -
                         analogRead(_AIpin2);

            while ((micros() - _start) < 829);
        }
    }
}
#pragma endregion
