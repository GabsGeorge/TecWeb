var salgadinho_frito,
	salgadinho_assado,
	minissanduiche,
	minipizza,
	cachorro_quente,
	minalmoco,
    batata_frita,
	pipoca,
	docinhos,
	chocolate,
	cupcake,
	biscoito_decorado,
	bolo,
	saladinha,
	sorvete,
    refrigerante,
	agua,
	suco,
	cerveja, 
	tubete, 
	latinha, 
	lembrancinha,
	adulto,
	crianca;

var botao;
botao = false


//var teste = document.getElementById('exemplo').innerText;



//Salgados 
// Unidades <
salgadinho_frito = 4
salgadinho_assado = 4
minissanduiche = 4
minipizza = 4
cachorro_quente = 4
minalmoco = 2
//>

// Saquinho <
batata_frita = 2
pipoca = 2
// >

// Doces

// Unidade<
docinhos = 6
chocolate = 4
// >
// Decorativos <
cupcake = 20
biscoito_decorado = 15
// >
// Fatia<
bolo = 2
//>
// Pote<
saladinha = 4
sorvete = 2
// >

// Bebidas
// Em L<
refrigerante = 0.5
agua = 1
suco = 0.5
cerveja = 0.7
// >

//Brindes
//Unidade<
tubete = 8
latinha = 8
lembrancinha = 8

function PegaValor(){
	adulto = document.getElementById('adultos').value
	var adultos,
	adultos = Number(adulto);
	alert(adulto)
	crianca = document.getElementById('criancas').value
	var criancas;
	criancas = Number(crianca/2)
	alert(criancas)
	total = Number(criancas + adultos)
	alert(total)
	Calculo(adultos, criancas)
}

function Calculo(adultos,criancas){
	document.getElementById('caixa_salgadinho_frito').value = salgadinho_frito * (adultos + criancas)
	document.getElementById('caixa_salgadinho_assado').value = salgadinho_assado * (adultos + criancas)
	document.getElementById('caixa_minissanduiche').value = minissanduiche * (adultos + criancas)
	document.getElementById('caixa_minipizza').value = minipizza * (adultos + criancas)
	document.getElementById('caixa_cachorro_quente').value = cachorro_quente * (adultos + criancas)
	document.getElementById('caixa_minialmoco').value = minalmoco * (adultos + criancas)
	document.getElementById('caixa_batata_frita').value = batata_frita * (adultos + criancas)
	document.getElementById('caixa_pipoca').value = pipoca * (adultos + criancas)
	document.getElementById('caixa_docinhos').value = docinhos * (adultos + criancas)
	document.getElementById('caixa_chocolate').value = chocolate * (adultos + criancas)
	document.getElementById('caixa_cupcake').value = cupcakes
	document.getElementById('caixa_biscoito_decorado').value = biscoito_decorado
	document.getElementById('caixa_bolo').value = bolo * (adultos + criancas)
	document.getElementById('caixa_saladinha').value = saladinha * (adultos + criancas)
	document.getElementById('caixa_sorvete').value = sorvete * (adultos + criancas)
	document.getElementById('caixa_refrigerante').value = refrigerante * (adultos + criancas) + "L"
	document.getElementById('caixa_agua').value = agua * (adultos + criancas) + "L"
	document.getElementById('caixa_suco').value = suco  * (adultos + criancas)+ "L"
	document.getElementById('caixa_cerveja').value = cerveja * adultos + "L"
	document.getElementById('caixa_tubete').value = tubete * (adultos + criancas)
	document.getElementById('caixa_latinha').value = latinha * (adultos + criancas)
	document.getElementById('caixa_lembrancinha').value = lembrancinha * (adultos + criancas)



}

function Valores(){
	document.getElementById('caixa_salgadinho_frito').value = salgadinho_frito
	document.getElementById('caixa_salgadinho_assado').value = salgadinho_assado
	document.getElementById('caixa_minissanduiche').value = minissanduiche
	document.getElementById('caixa_minipizza').value = minipizza
	document.getElementById('caixa_cachorro_quente').value = cachorro_quente
	document.getElementById('caixa_minialmoco').value = minalmoco
	document.getElementById('caixa_batata_frita').value = batata_frita
	document.getElementById('caixa_pipoca').value = pipoca
	document.getElementById('caixa_docinhos').value = docinhos
	document.getElementById('caixa_chocolate').value = chocolate
	document.getElementById('caixa_cupcake').value = cupcake
	document.getElementById('caixa_biscoito_decorado').value = biscoito_decorado
	document.getElementById('caixa_bolo').value = bolo
	document.getElementById('caixa_saladinha').value = saladinha
	document.getElementById('caixa_sorvete').value = sorvete
	document.getElementById('caixa_refrigerante').value = refrigerante + "L"
	document.getElementById('caixa_agua').value = agua + "L"
	document.getElementById('caixa_suco').value = suco + "L"
	document.getElementById('caixa_cerveja').value = cerveja + "L"
	document.getElementById('caixa_tubete').value = tubete
	document.getElementById('caixa_latinha').value = latinha
	document.getElementById('caixa_lembrancinha').value = lembrancinha
	}

Valores()
	// document.getElementById('caixa_salgadinho_frito').value = salgadinho_frito
	// document.getElementById('caixa_salgadinho_assado').value = salgadinho_assado
	// document.getElementById('caixa_minissanduiche').value = minissanduiche
	// document.getElementById('caixa_minipizza').value = minipizza
	// document.getElementById('caixa_cachorro_quente').value = cachorro_quente
	// document.getElementById('caixa_minialmoco').value = minalmoco
	// document.getElementById('caixa_batata_frita').value = batata_frita
	// document.getElementById('caixa_pipoca').value = pipoca
	// document.getElementById('caixa_docinhos').value = docinhos
	// document.getElementById('caixa_chocolate').value = chocolate
	// document.getElementById('caixa_cupcake').value = cupcake
	// document.getElementById('caixa_biscoito_decorado').value = biscoito_decorado
	// document.getElementById('caixa_bolo').value = bolo
	// document.getElementById('caixa_saladinha').value = saladinha
	// document.getElementById('caixa_sorvete').value = sorvete
	// document.getElementById('caixa_refrigerante').value = refrigerante
	// document.getElementById('caixa_agua').value = agua
	// document.getElementById('caixa_suco').value = suco
	// document.getElementById('caixa_cerveja').value = cerveja
	// document.getElementById('caixa_tubete').value = tubete
	// document.getElementById('caixa_latinha').value = latinha
	// document.getElementById('caixa_lembrancinha').value = lembrancinha
