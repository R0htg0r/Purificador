import os
import Raney
import colorama

Comparados = set()
ComparadosA = []

ComparadosA_Texto = set()

colorama.init()
def Windows():
    os.system("mode 120, 60")

def Menu():
    Windows()
    print(colorama.Fore.RED + "-" * 120 + colorama.Fore.WHITE)
    print(" " * 4, colorama.Fore.YELLOW + "Brasil", " " * 95, colorama.Fore.YELLOW + "R0htg0r" + colorama.Fore.WHITE)
    print("\n" * 9)
    print(" " * 9, "Bem-Vindo ao Purificador de Endereços IP repetidos.", "\n")
    print(" " * 9, "  1 ) Usar um banco de IPs em arquivo.")
    print(" " * 9, "  2 ) Usar um banco de IPs pelo terminal.")
    print("\n" * 9)
    print(colorama.Fore.RED + "-" * 120 + colorama.Fore.WHITE)
    
    while True:
        try:
            Escolha = input(" Número: ")

            if int(Escolha) == 1:
                try:
                    Enderecos = input(" Nome do Arquivo: ")
                    Encontrado = open(Enderecos, "r")
                    
                    for Arquivo in Encontrado.readlines():
                        ComparadosA.append(Arquivo.strip())
                        Comparados.add(Arquivo.strip())

                    print(colorama.Fore.YELLOW + " [!] Foi removido", len(ComparadosA) - len(Comparados), "e reagrupado", len(Comparados), "de", len(ComparadosA), colorama.Fore.WHITE + "\n")
                    
                    Confirmar = input(" Você deseja salvar(S ou N): ")
                    
                    if Confirmar == "S" or "Y" or "Sim" or "Yes":
                        print(colorama.Fore.YELLOW + " [!] Aguarde, seu arquivo está sendo criado." + colorama.Fore.WHITE)
                        
                        NovoArquivo = open(Enderecos + Raney.criar(0, "C", 5) + "-" + Raney.criar(0, "C", 5), "a")
                        for CriandoArquivo in Comparados:
                            NovoArquivo.write(CriandoArquivo + "\n")
                        NovoArquivo.close()
                        
                        print(colorama.Fore.YELLOW + " [+] Pronto, seu arquivo foi criado com sucesso." + colorama.Fore.WHITE + "\n")
                        break
                    
                    elif Confimar == "N" or "No" or "Nao" or "Não":
                        print(colorama.Fore.YELLOW + " [+] Seu trabalho de purificar o arquivo foi em vão." + colorama.Fore.WHITE + "\n")
                        break

                except:
                    print(colorama.Fore.RED + " [!] Ops, aconteceu um problema inesperado, tente novamente." + colorama.Fore.WHITE)
                    break

            elif int(Escolha) == 2:
                while True:
                    try:
                        Esperando = input(" Endereços: ")
                        
                        if Esperando == "pronto" or "parar" or "finalizar" or "stop" or "done" or "finish":
                            print(colorama.Fore.YELLOW + " [!] Foram purificados", len(ComparadosA_Texto), "endereços da lista." + colorama.Fore.WHITE + "\n")
                            ArquivoTexto = open("Purificado-" + Raney.criar(0, "C", 5) + "-" + Raney.criar(0, "C", 5) + ".txt", "a")
                            
                            for ComparadosB_Texto in ComparadosA_Texto:
                                ArquivoTexto.write(ComparadosB_Texto + "\n")
                            ArquivoTexto.close()
                            break
                            
                        ComparadosA_Texto.add(Esperando)
                    except:
                        break
            else:
                print(" [!] Esse comando não existe, corrija sua ortográfia.")
                break
        except:
            break
Menu()