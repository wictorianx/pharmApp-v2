
let druggrid = document.querySelector('#mydrugs');

function hoverAdd(x){
  x.style.backgroundColor = 'rgb(0,255,255,0.6';
}
function hoverOutAdd(x){
  x.style.backgroundColor = 'rgb(0,0,255,0.6';
}
function clickAdd(x){
  x.style.backgroundColor = 'rgb(0,255,0,0.6';
}
document.getElementById("uploadfile").onchange = function() {
  document.getElementById("form").submit();
};

function getDate(){
  let d = new Date()
  return(`${d.getDate()}-${d.getMonth()}-${d.getFullYear()}`)
}
class drug {
    constructor(elements) {
      this.drug_id = elements[0];
      this.spoil_date = elements[1].replaceAll(".","-").split("-").reverse().join("-");
      this.drug_amount = elements[2];
      this.user_id = elements[3];
      this.record_id = elements[4];
      this.initial_difference = new Date(this.spoil_date).getTime()-new Date(getDate()).getTime();
    }
    place(){
      this.box = document.createElement('div');
      this.box.style.height="200px";
      this.box.style.width="200px";
      this.box.classList.add('drug');
      this.box.innerHTML=`${this.drug_amount} Adet <br/> SKT: ${this.spoil_date}`
      druggrid.appendChild(this.box);
    }
    date(){
      let curdate = new Date(getDate()).getTime();
      let spoil_date = new Date(this.spoil_date).getTime();
      let timeleft = spoil_date - curdate;
      let ratio = parseInt((timeleft / this.initial_difference)*512)-512
      
      if (ratio >255){
        this.green=0
        this.red = ratio-256
      }
      else{
        this.red=0
        this.green = 255-ratio
      }

      this.box.style.backgroundColor=`rgb(${this.red},${this.green},0)`
      this.box.style.opacity="0.6";
      this.box.style.borderRadius="25px";

    }
  }



new drug(1,"11.06.2023",5,1,2)
// x.place()
// x.date()
//renk önce full yeşil, kırmızı artçak sonra 255 olunca yeşil azalcak
