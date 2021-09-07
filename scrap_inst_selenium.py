from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time as tm
import random as rd
import numpy as np
import pandas as pd
from datetime import datetime


#specify the path to chromedriver.exe 
driver = webdriver.Chrome('C:/Users/Felilpe Lima/Documents/chromedriver.exe')

#funcao de espera
def espere(m):
    #m deve levar valor de 1 a 3
    if m == 0:
        tm.sleep(rd.uniform(0,1))
    if m == 1:
        tm.sleep(rd.uniform(1,6))
    elif m == 2:
        tm.sleep(rd.uniform(8, 16))
    elif m == 3:
        tm.sleep(rd.uniform(30,120))
#função de como esperar

def como_esperar(n):
    #fazendo o programa de espera em tempos aleatorios
    if n==0:
        espere(0)
    elif n%22==0:
        espere(3)
    elif n%80==0:
        #espera muito tempo depois de 80 contas
        tm.sleep(rd.uniform(3600,3000))
    elif n%2 == 0:
        espere(2)
    else:
        espere(1)
#função login
def login(account_now):
    
    #open the webpage
    driver.get("https://www.instagram.com/accounts/login/")
    
    #target username
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    
    my_username = ["fionagatos","cami.oliveiro","aurora_gatos"]
    my_password = ["pitocofiona3","1000000nudes","pitocofiona"]

    print('fazendo o login como',my_username[account_now])

    #enter username and password
    username.clear()
    username.send_keys(my_username[account_now])
    password.clear()
    password.send_keys(my_password[account_now])
    
    #target the login button and click it
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    tm.sleep(5)
    alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Agora não")]'))).click()
    alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Agora não")]'))).click()

#encontrar a data por motivo de analise de progresso
date=datetime.now()
StrDate=str(date.day) + '_' + str(date.month) + '_' + str(date.year)


#login
my_account_now=-1
#login(my_account_now)

#loading accounts
accounts_to_scrap = ['_labeet', 'extsaudecidadania', 'projetosaudeequi', 'usinaescolasolar', 'aextce', 'extensao.ccae', 'capacitandocuidadores', 'prof.joaosamuelmeira', 'treinoadaptado.lm', 'gestacaoesaude.ufpb', 'lapsus.ufpb', 'infoprodutos_autocuidado', 'extmcc', 'extradufpb', 'agregaufpb', 'ucehulw', 'proambiufpb', 'rose_educadorasexual', 'inclusaonaeducacao', 'projeto_folheto', 'ciatox_jp', 'apoiomatricialufpb', 'maressemplastico', 'neuroconexoesufpb', 'probexufpb.sentidonavida', 'plantaofiscal_ufpb', 'laetufpb', 'educacim', 'infofisio.ufpb', 'cgaufpb', 'tessiturasnegras', 'gepaezufpb', 'aplicadaliteratura', 'coraleucuido', 'projetoalfaufpb', 'coletivoempoderi', 'biosseguranca_ccs_ufpb', 'normalizacao.lattes', 'neabi.baobaymyrapyta', 'casbsus', 'grdcufpb', 'caprinova.ufpb', 'acessoaodiutcobre380a', 'saudeauditivaufpb', 'extensaocca', 'extprevavc', 'ovocultura', 'bichopreguica.ufpb', 'austregiselojr', 'nube.ufpb', 'tvufpb', 'andrea.acastro', 'rose.limasantos', 'estatisticalivre', 'movimentear', 'lacfacialufpb', 'suportebasicoufpb', 'edufinanceiraprobex', 'tribunadebate', 'nepflor', 'extensaocear', 'comuufpb', 'ext.feridasufpb', 'trama.assessoriatecnica', 'bibliotecacca_ufpb', 'mulheresemcena_', 'descarta.cim', 'bancodedentesufpb', 'down_geex', 'empautacast', 'probemufpb', 'cicloartescenicas', 'acaojaguaribeufpb', 'mccufpb', 'mirellacahu', 'desconstruaufpb', 'epeufpb', 'extensaopediabeticoufpb', 'inter.psicopedagogia', 'escoladeposturasufpb', 'tramasdaquarentena', 'universidadeemdebate', 'simoesbartollini', 'produtoseresiduosdefrutas', 'envelhesendoufpb', 'licoesdecapoeira', 'extprevencaodequedas', 'pedagogiahospitalar.ufpb', 'geppadi.ufpb', 'coletivoredemoinho', 'tenis_ufpb', 'engaje.ext', 'terapiafloral.ufpb', 'pianolabufpb', 'curadoriaideiasuspb', 'lafabe.dbm', 'lacesse.ufpb', 'treeufpb', 'sexualidadenaufpb', 'falardepolitica.ufpb', 'probexcuia.ufpb', 'cctaufpb', 'historiasdequilombo', 'proexufpb', 'anatomianaescola', 'labempreendedor', 'olhodotempo', 'projextdiversitas', 'protocolosfito', 'terapiacomunitariaufpb', 'efopliufpb', 'ceoufpb', 'projetoescritaacademicaufpb', 'odontologiaprobex', 'cuidadofarmaceuticoufpb', 'hortagastronomiaufpb', 'justimagine_ufpb', 'ciclaoleo_ufpb', 'exdima_ufpb', 'probex2021.suinoculturaufpb', 'grupoconjor', 'pernasebracos_ufpb', 'miga.sua.louca.chega.junta', 'extensaoccen_ufpb', 'projeto_artesvisuaiseinclusao', 'mestrapenhacirandeira', 'laboratoriolean', 'cuidandodasmulheres', 'naprosaufpb', 'lefidef', 'cipyproex', 'diu.ufpb', 'cidadaonocontrole', 'saudenapuericultura', 'projetodias.ufpb', 'compostagem_ufpb', 'cafecommedicinaufpb', 'laolufpb', 'dapbparaomundo', 'lavir.ufba', 'bibliotecacesufcg', 'assessoria.cbiotec', 'extdiagnosticocb', 'circulotabajara', 'educacaoantirracista_ufpb', 'educacaoambientalnaescola_cca', 'extensaotabagismoufpb', 'exerciciofisicoparadiabeticos', 'orientacoesparacolonoscopia', 'direitocomcidadania', 'semabandonosufpb', 'estudos_administracao', 'peep_ufpb', 'projetomedicacao', 'descomplicatcc_ufpb', 'gestaopublica_ufpb', 'coletivoatuador', 'diario.de.micologia', 'imcac.ufpb', 'pedagogiaurbanabr', 'juventude_trabalhadora', 'interfaceslivres', 'contemp_ufpb', 'extensao.domissanitarios_ufpb', 'promama.ufpb', 'professores.e.o.lem', 'lutas.urbanas', 'educa.serpentes', 'tecleite', 'apoioaoforro', 'espacoexperimentalufpb', 'contraceptivos.ufpb', 'juan_marcelo10', 'planeta_cavalos', 'hilcamarianagomes', 'hortamedicinalcca', 'erikaandrade', 'lecopsilab', 'ecitmestresivuca', 'webradioportodocapim', 'cimexufpb', 'projetobemmequeroufpb', 'prof.franciscodireitoanimal', 'dimpecarca', 'nuplarufpb', 'biotecnologianaescola_', 'micologiaclinicaufpb', 'ufpbpelavida', 'aspta_ufpb', 'projeto_passarelacidada', 'projetomaternidadeufpb', 'sameufpb', 'extensaoetippe2021', 'fiosdeestima', 'enlacespb', 'id.afrobraprojeto', 'ecosoldocampopb', 'projetopais_ufpb', 'prodeleufpb', 'gaju_santarita', 'renovaveis.probex', 'glaucomaemevidencia', 'projetomediacaodeconflitos', 'tarjapretaufpb', 'geotb.ufpb', 'nejaufpb', 'assevoxufpb', 'cultivandosaudenaescola_ufpb', 'saudedotrabalhador_covid19', 'contemdancaz', 'coletaseletivaufpb', 'monteiro.jpa', 'observatorioufpb', 'maespancreas_al', 'setoqueparavida', 'saberesemroda_ufpb', 'liafo_ufpb', 'construindo_meioambiente', 'lesoescervicaisnaocariosas', 'escorpiaoeduca', 'assessoriaext_cchla', 'inovaleufpb', 'ext.amor', 'generosexualidadeufpb', 'ecosol.pb', 'tecnologiadealimentos.ufpb', 'sondagempb', 'probex.subprodutosdefrutas', 'nucleohabilidadesufpb', 'npd.ufpb', 'naepsi.ufpb', 'itgirlsrt', 'secretariacopac', 'ufpbaja', 'gilvanedja', 'diunaatencaobasica', 'projetoextensao.recastufpb', 'biotecnologiadealimentos', 'balcaouniversitario', 'escrevivencias_ufpb', 'tedumufpboficial', 'aextensaoccsa', 'projetomelhorart', 'brenameira', 'musicaclassicaparaleigos', 'tecendo_redes', 'info.ccaufpb', 'cacadoresdeparasitos', 'cchla_ufpb', 'quimica.cear', '_reciclajp', 'metodoativas_ufpb', 'inteligencia_financeira_ccae', 'loucosporobstetriciaeneo', 'percepcoesdoparto', 'pespic_ufpb', 'festaruanda', 'dlem.ufpb', 'bt_ufpb', 'musicalmente.ufpb', 'estruturenegocios', 'infancia_verde', 'ext.espiritualidade', 'memoriadireitoufpb', 'cinemedicina', 'extccjufpb', 'probex2021_pgr', 'meiodiacomanatomia', 'donasdobolso', 'pamellakellyaguiar', 'galeria_lavandeira', 'qualidade.de.alimentos', 'projetodoremefazcomer', 'ecoscineambiental', 'agamificacaoeasfuncoes', 'mcmorfologicasufpb', 'probex_uniacao', 'maya.mm28', 'teleodontosb_ufpb', 'ecolanchespb', 'projetonocarcere', 'extensao.picsnocuidado', 'extensaoxoamere', 'midiasproex', 'oficinasdecontacao', 'projnamaste', 'eeproexufpb', 'biossegurancaufpb', 'laboaa_ufpb', 'vamos_conversar_sobre_artigos', 'katiambond', 'tecnologiafarmaceutica.ufpb', 'preparoparaalta', 'saudedotrabalhador_ufpb', 'narrativaspotiguara', 'ext.cappe', 'renata.oliveira.psi', 'nedetufpb', 'boaspraticas.suinos', 'extensaohemovigilancia', 'aerojampaufpb', 'xoparasita', 'contabilidadeconectada', 'curriculo_contexto', 'picsdigital', 'labcozinhaexperimental', 'enfnacomunidade', 'lucianyaparecida', 'espacosparticipativos', 'municipalizacaoambiental.ufpb', 'dormirbemevivermelhor', 'extensao_pastagensnobrejo', 'edufinccae', 'canalufpb', 'aextensaocchsa', 'idefufpb', 'decklivre', 'sosanimaiseplantas', 'cinemacessivel', 'animaiscomunitariosufpb', 'projetogeoescola', 'rachelmelo2', 'descomplica_ensinomedio', 'grupoat_cbhs', 'projetofeiralivre', 'profaingriddantas', 'estimular.hulw', 'periodontia.ufpb', 'seliganolixo', 'pinab.ufpb', 'falandosobreaids', 'cine_trava', 'extensaopcrufpb', 'melyssavet', 'medveterinariabr', 'guiasdaequoufpb', 'ts_calculadora', 'ppgecamufpb', 'alimentandocomafeto', 'letslearnenglish.ufpb', 'mergulhee', 'criaanato', 'oficinadevelas_ufpbcca', 'salaacoes', 'cantodamainha', 'loucidufpb', 'fabianenagabe', 'thiag0_magn0', 'ronaldomagalhaes3', 'mulheresecosol_', 'projetocatraca.ufpb', 'primeirossocorrosufpb', 'extensaoautismo', 'mobilang_ufpb', 'culturaliterarianaescola', 'escrevegabi', 'doacaodecorpos.ufpb', 'biblioteca.ccbs.ufcg', 'insulinaediabetes', 'iniciacaoaflautatransversal21', 'projetofungospb', 'amar.expo', 'acolhergenero', 'nedhes.ufpb', 'obuntu.ufpb', 'epc.extensao', 'extensao_fotoprotecao', 'marubenita', 'medvetplay', 'combatecovid.odonto', 'redesdobem', 'extensao_formacao', 'uso.medicamento', 'estanciaamazonas', 'derivados_cana', 'trama.mutiraonavizinhanca', 'projeto.rede.atencao.ufpbss', 'trama.mobilidadeurbana', 'reduzaplastico', 'gecimp', 'projeto_people_', 'dcmaos_fono', 'preguicinha_esperta_', 'ppgci_ufpb', 'talentocientificojovem_', 'subindoaladeira', 'lapefi.ufpb', 'alimentoseguro.ufpb', 'apoinme_brasil', 'fononcoufpe', 'aspaufpb1', 'rolezinhodoportodocapim', 'iandepotiguara', 'aguapocos_ccaufpb', 'simone_targino', 'memoriasenarrativasdocampo', 'cidadaniaecontaspublicas', 'casadelpanejp', 'filosofia_publica', 'franciscodireitoanimal', 'coletivo_margaridas', 'dciccsaufpb', 'vacinasemmito', 'estatisticacomjogos', 'asmulheresocupamaspracas', 'projetopisciculturando', 'pisciculturaeagricultura.ufpb', 'profeyonara', 'relacoesraciaisccaeufpb', 'luta_antimanicomialap', 'safdaesperanca', 'projetolabmua', 'bibliocentralufpb', 'literaturaedocente', 'nykaferve', 'diversas.ufpb', '3diadecampo', 'dicanucleo', 'mnla_antimanicomial', 'solosnaescola_ufpb', 'drousy', 'literaturaleituraeescrita', 'cadeiaaosdesumanos', 'profa.luhlima', 'alertaesporotricose', 'ifpecampusigarassu', 'cuidadospreepos', 'ideiasusfiocruz', 'hortaseducativas', 'bibliotecaifalmaceio', 'direitodoconsumidornaescola', 'institutoacuna', '2ie.ufpb', 'paecibio', 'lanchess_saudaveis', 'rompendocorrentesufpb', 'projetoabracojp', 'monitora_ufpb', 'ecotropics_uepb', 'podcastjornadas', 'psicofarm.orienta', 'mariomarianoruizcardoso', 'maria.quiteria.pb', 'emocoesemfoco_ufpb', 'crushfloresta_probex2021', 'ouvirrefletireagir', 'ongaipan', 'turismodebasecomunitariapb', 'nepalufpb', 'palavracorpo', 'oficinasdesaberes', 'enfdilyanecabral', 'projetoamamentamamae', 'praticaseducativasgrio', 'progebufpb', 'projetoecofossas', 'nenn.ccae', 'elianepotiguara', 'probex_relacoeshumanas', 'agroagenda', 'indios_do_brasil', 'percepcoesacercadodiu_ufpb', 'descarta_cabedelo', 'dcs.ufpb', 'assessoriabalaionordeste', 'rogerio_aiki']
false_accounts=[]
accounts_scrap_done = []
data=[]
number_reapeted_errors = 0
n=0

espere(2)

while n < len(accounts_to_scrap):

    account = accounts_to_scrap[n]

    #guardando contas já feitas
    accounts_scrap_done.append(account)

    link = 'http://www.instagram.com/' + account
    espere(1)

    #open the webpages
    driver.get(link)

    #espere
    como_esperar(n)

    #data = pub + seguidores + seguidos
    #procurando os elementos na pagina
    new_data=driver.find_elements_by_class_name("g47SY")

    #salvando o len dos dados antes da adicao de novos dados para anular erros
    qt1= len(data)

    #substituindo os elementos no destino
    for y in new_data:
        data.append(y.text)
    
    #salvando o len dos dados depois da adicao de novos dados para anular erros
    qt2= len(data)

    #comparando os lens antes e depois, caso o len seja o mesmo, novos dados não foram adicionados, então ele deve salvar todas as contas que funcionaram e as que não
    if qt1==qt2:
        false_accounts.append(account)

        #contando as contas que tiveram erro, pois caso aconteca muitas vezes, o instagram bloqueou a pesquisa
        number_reapeted_errors+=1

        #printando contas com erro
        print('contas  que nao deram certo:', false_accounts)

        #acrescentando ODE nas contas que deram erro
        i=0
        while i<3:
            data.append('ODE')
            i+=1
        
        

        #se ocorrerem 3 erros seguidos, outra conta deve fazer login
        if number_reapeted_errors==3:
            driver.close()

            driver = webdriver.Chrome('C:/Users/Felilpe Lima/Documents/chromedriver.exe')

            #faz novo login
            my_account_now+=1
            login(my_account_now)

            #Indica as contas que faltam fazer o scrap
            n-=3

            #remove os erros da lista de contas analisadas
            p=0
            while p<3:
                accounts_scrap_done.pop(-1)
                false_accounts.pop(-1)
                p+=1

            #remove dos dados os erros das contas
            q=0
            while q <9:
                data.pop(-1)
                q+=1


    else:
        number_reapeted_errors=0

    #fazendo tabela de seguidores e seguidos
    columns = ['Pubs  ','seguidores  ','seguindo']

    data_for_table = np.array(data).reshape(len(accounts_scrap_done), 3 )

    pd.set_option("display.max_rows",999)
    main_table = pd.DataFrame(data=data_for_table, index=accounts_scrap_done,columns=columns)

    print('\n\n', main_table)
        
    
    print('\n', data, '\n', n)
    


    n+=1

#exportando os dados até o excell
with pd.ExcelWriter("C:/Users/Felilpe Lima/Documents/Data Ode.xlsx", mode="a", engine="openpyxl") as writer:
    main_table.to_excel(writer, sheet_name=StrDate)


driver.close()
