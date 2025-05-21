const eliminarFila=(url, nombreTabla)=> {
    iziToast.question({
    timeout: 20000,
    close: false,
    overlay: true,
    displayMode: 'once',
    id: 'question',
    zindex: 999,
    title: "CONFIRMACION!!",
    message: `¿Estas seguro de eliminar el registro ${nombreTabla}`,
    position: 'center',
    buttons: [
        ['<button><b><h6>SI</64></b></button>', function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button');
            window.location.href=url;
 
        }, true],
        ['<button><h6>NO</h6></button>', function (instance, toast) {
 
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button');

 
        }],
    ],
    onClosing: function(instance, toast, closedBy){
        console.info('Closing | closedBy: ' + closedBy);
    },
    onClosed: function(instance, toast, closedBy){
        console.info('Closed | closedBy: ' + closedBy);
    }
});
}