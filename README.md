# mbafan

You might have had issues with Linux installation on your Macbook Air that it is getting hot and that the fans are not kicking in.
Well, this provides a sort of solution to that problem by checking the core temp and varying the fan speeds accordingly.

No guarantee, but it should probably work. It won't probably blow up your system at least.

** If the system still gets hot, please report an issue I'll see if I can help. **

Do keep in mind:
* Its written in python, should have done it C
* Not foolproof
* Temp check may not be the best

My system: `x86_64 Linux 4.10.8-1-ARCH` `Macbook Air7,2`

## Installation instructions

```sh
git clone https://github.com/meain/mbafan.git && cd mbafan && chmod +x install && sudo ./install && cd ..
```

If you get an error saying 'Error, probably restarting it will fix it.'. Restart your computer then do
```sh
cat /sys/devices/platform/applesmc.768/fan1_manual
```
and if the output is is 1 you are good to go


## Useful links

* [Simple MacBook Pro Fan Daemon](http://allanmcrae.com/2010/05/simple-macbook-pro-fan-daemon/)
* [Interpreting sensor names](https://superuser.com/a/967056/328228)
