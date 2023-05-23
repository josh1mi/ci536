# dropshadow.tcl

proc ::tk::DropShadow {w off col op} {
    if {![winfo exists $w]} return

    # Add a drop shadow to the window
    catch {destroy $w.shadow}
    toplevel $w.shadow
    wm overrideredirect $w.shadow 1
    wm geometry $w.shadow [format "+%d+%d" [winfo x $w]+off [winfo y $w]+off]
    wm attributes $w.shadow -alpha $op
    frame $w.shadow.frame -background $col
    pack $w.shadow.frame -fill both -expand 1

    # Copy the content of the window onto the shadow
    set img [image create photo -format window -window $w]
    label $w.shadow.frame.lbl -image $img
    pack $w.shadow.frame.lbl -fill both -expand 1

    # Handle window destruction
    bind $w <Destroy> [list destroy $w.shadow]

    return $w.shadow
}
