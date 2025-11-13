🧠 Atividade Prática 06 – Programação com APIs e Módulo Random
Este repositório contém a implementação dos exercícios propostos na Aula 10 da disciplina, conforme descrito no formulário da Atividade Prática 06.

📋 **Descrição dos Exercícios**
**1. Gerador de Senha Aleatória**
Cria uma senha segura com:

Módulo random

Caracteres especiais

Entrada do usuário para definir o número de caracteres

✅ *O que esse código faz:*
Solicita ao usuário o tamanho da senha.

Garante que a senha tenha pelo menos um caractere de cada tipo (letra, número, símbolo).

Embaralha os caracteres para aumentar a segurança.

Exibe a senha gerada.

**2. Gerador de Perfil Aleatório**
Utiliza a API Random User Generator para:

Gerar um perfil fictício

Exibir nome, email e país do usuário

✅ *O que esse código faz:*
Faz uma requisição à API https://randomuser.me/api/

Extrai nome, email e país do usuário gerado

Exibe essas informações no terminal

**3. Consulta de Endereço via CEP**
Utiliza a API ViaCEP para:

Consultar dados de endereço a partir de um CEP informado

Exibir logradouro, bairro, cidade e estado

✅ *O que esse código faz:*
Solicita ao usuário um CEP válido (8 dígitos).

Faz uma requisição à API ViaCEP.

Exibe os dados de endereço: logradouro, bairro, cidade e estado.

Valida se o CEP existe ou se foi digitado incorretamente.
**4. Cotação de Moeda Estrangeira**
Utiliza a API AwesomeAPI para:

Consultar a cotação de uma moeda estrangeira em relação ao BRL

Exibir valor atual, máximo, mínimo, data e hora da última atualização

✅ *O que esse código faz:*
Solicita ao usuário o código da moeda estrangeira (ex: USD, EUR, ARS).

Consulta a cotação em relação ao real (BRL) usando a AwesomeAPI.

Exibe o valor atual, máximo, mínimo e a data da última atualização.