let input = document.getElementById("id_password");
if (input==undefined) input = document.getElementById("id_password1");
             const warnText = document.getElementById("warn");
             input.addEventListener("keyup", function(event) {
                if (event.getModifierState("CapsLock")) {
                warnText.style.display = "block";
                } else { warnText.style.display = "none";}
                });
