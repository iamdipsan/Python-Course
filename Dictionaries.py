monthConversion = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}
#can also use  number for keys like this
#monthConversion = {
#   "Jan" : "January",
#   "Feb" : "February",
#   "Mar" : "March",
#}
print(monthConversion["Jan"])
print(monthConversion["Dec"])
print(monthConversion["Nov"])
print(monthConversion.get("Dec"))
print(monthConversion.get("gg","not a key"))