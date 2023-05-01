def android_get_desired_capabilities():
    return {
        "appium:autoGrantPermissions": True,
        "appium:automationName": "uiautomator2",
        "appium:newCommandTimeout": "500",
        "appium:noSign": True,
        "platformName": "Android",
        "appium:platformVersion": "10",
        "appium:resetKeyboard": True,
        "appium:systemPort": "5027",
        "appium:takesScreenshot": True,
        "appium:udid": "emulator-5554",
        "appium:appPackage": "com.ajaxsystems",
        "appium:appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
    }
