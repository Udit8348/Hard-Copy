//
// Created by ariel on 11/15/19.
//
#ifndef ROBOT_CODE_CONSTANTS_H
#define ROBOT_CODE_CONSTANTS_H

#include "main.h"
#include "okapi/api.hpp"

using namespace okapi;
namespace robot {
    /* Begin drive motor block */
    const int FRONT_LEFT_DRIVE_MOTOR_PORT = 5;
    const int FRONT_RIGHT_DRIVE_MOTOR_PORT = -6;
    const int BACK_LEFT_DRIVE_MOTOR_PORT = 11;
    const int BACK_RIGHT_DRIVE_MOTOR_PORT = -20;
    /* End drive motor block */


    /* Begin lift block */
    const int LIFT_MOTOR_PORT_LEFT = -2; // TODO: Placeholder value
    const int LIFT_MOTOR_PORT_RIGHT = 9; // TODO: Placeholder value

    const char LIFT_POS_LIMIT_SWITCH_UP = 'A'; // TODO: Placeholder value
    const char LIFT_POS_LIMIT_SWITCH_DOWN = 'H';

    const float LIFT_DOWN_POS = 0;
    const float LIFT_UP_POS_LEFT = 2204;
    const float LIFT_UP_POS_RIGHT = 2224;
    const float LIFT_TOWER_LOW_POS_RIGHT = 1800;
    const float LIFT_TOWER_LOW_POS_LEFT = 1800;
    const float LIFT_TOWER_MID_POS_RIGHT = 2200;
    const float LIFT_TOWER_MID_POS_LEFT = 2200;
    /* End lift block */


    /* Begin claw block */
    const int CLAW_MOTOR_PORT = 13;
    const int CLAW_MOTOR_POS_OPEN = 600; // TODO: Placeholder value
    const int CLAW_MOTOR_POS_CLOSED = 450;
    /* End claw block */

    /* Begin random global pointer block */
    extern std::shared_ptr<okapi::ChassisController> chassis;
    extern std::shared_ptr<okapi::AsyncMotionProfileController> profile_controller;
    /* End random global pointer block */
}

namespace bindings {
    // TODO: when all buttons have been mapped, make a comment describing what each one does
    const auto LIFT_POS_UP = okapi::ControllerDigital::up;
    const auto LIFT_POS_DOWN = okapi::ControllerDigital::down;
    const auto LIFT_POS_TOWER_LOW = okapi::ControllerDigital::Y;
    const auto LIFT_POS_TOWER_MID = okapi::ControllerDigital::B;
    const auto LIFT_MOVE_UP = okapi::ControllerDigital::R1;
    const auto LIFT_MOVE_DOWN = okapi::ControllerDigital::R2;

    const auto CLAW_MANUAL_CLOSE = okapi::ControllerDigital::L1;
    const auto CLAW_MANUAL_OPEN = okapi::ControllerDigital::L2;
    const auto TOGGLE_CLAW = okapi::ControllerDigital::right;

    const auto DRIVE_BRAKE_TOGGLE = okapi::ControllerDigital::X;

    // A is used to debug autonomous, leave that button unbound
}

namespace constants {
    const int MOTOR_MAX_VOLTAGE = 12000;

    const int CLAW_MOVE_VELOCITY = 60;

    const std::int32_t LIFT_UP_VELOCITY = 75;
    const std::int32_t LIFT_DOWN_VELOCITY = 50;

    const auto OKAPI_BRAKE = okapi::AbstractMotor::brakeMode::brake;
    const auto OKAPI_COAST = okapi::AbstractMotor::brakeMode::coast;
}

#endif //ROBOT_CODE_CONSTANTS_H
