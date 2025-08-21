from gpt import receive_data
import json



def prepareDataDescricao(relacao):
    prompt = (f"""
    Você é um especialista do MCTI que avaliará a qualidade de relatórios técnicos de Pesquisa, Desenvolvimento e Inovação segundo o manual de frascati.
              
    Com base no texto a seguir, referente a seção de descrição de um relatório técnico da Lei do Bem, elabore uma análise que avalia se o texto de descrição atende a todos os critérios válidos ao caso descritos abaixo.
    (Considere o Manual de Frascati, Guia da Lei do Bem (ANPEI) e fontes confiáveis como embasamento da análise das informações técnicas do projeto.)
                  
    Os critérios são fornecidos via Orientação de escrita fornecidos pelo próprio MCTI
    
    Critérios a serem avaliados: Descreva de forma clara e objetiva o projeto de Pesquisa, Desenvolvimento e Inovação (PD&I), incluindo:
    •	Classificação da pesquisa: informe se o projeto se enquadra como Pesquisa Básica Dirigida, Pesquisa Aplicada ou Desenvolvimento Experimental, conforme os critérios estabelecidos.
    •	Marcos críticos: identifique os principais desafios e etapas estratégicas do projeto.
    •	Elementos tecnologicamente inovadores: detalhe os avanços tecnológicos ou científicos que diferenciam o projeto em relação ao estado da arte.
    •	Caracterização como P&D: explique como o projeto se qualifica como pesquisa e desenvolvimento, destacando a incerteza tecnológica envolvida, o desenvolvimento de novos conhecimentos ou a criação de soluções inovadoras.
    •	Obstáculos ao desenvolvimento do projeto: identifique os fatores que dificultaram o desenvolvimento do projeto.
    Projetos plurianuais: se o projeto tiver duração superior a um ano, apresente a evolução anual das atividades, evitando repetir a mesma descrição em diferentes anos.
    Projetos em cooperação: se o projeto tiver sido desenvolvido em parceria entre empresas, informe no item 'Informações Complementares' a contribuição específica de cada empresa no ano-base, incluindo razão social e CNPJ das participantes. No formulário, declare apenas os valores gastos pela sua empresa.
    
    Texto da descrição do relatório técnico: {relacao}
    
    Forneça um feedback escrito, sobre o que precisa ser melhorado e o que já atende aos critérios. Além disso, retorne uma categoria entre:0 a 10. Conforme os critérios disponibilizados.
    O seu feedback será um guia de ações plausíveis e claras para que o redator saiba de forma muito objetiva o que melhorar e como, esse é o objetivo principal do prompt. Com isso, aponte de forma material do texto, os pontos de melhoria e principalmente, como deve ser melhorado, usando como base o próprio conteúdo do texto.
    
    O feedback deve ser sempre um texto corrido, não use listas ou qualquer outra formatação.
    
    A resposta deve ser um JSON com:
    {{
        feedback: (o feedback escrito do que precisa ser melhorado)
        avaliacao: (a categoria se atende de 0 a 10)
    }}
            """)
    
    response = receive_data(prompt)
    jsonResponse = json.loads(response)
    return jsonResponse


def prepareDataInovacao(relacao):
    prompt = (f"""
    Você é um especialista do MCTI que avaliará a qualidade de relatórios técnicos de Pesquisa, Desenvolvimento e Inovação segundo o manual de frascati.
    Com base no texto a seguir, referente a seção de elemento tecnologicamente novo ou inovador de um relatório técnico da Lei do Bem, elabore uma análise que avalia se o texto de descrição atende a todos os critérios válidos ao caso descritos abaixo.
    (Considere o Manual de Frascati, Guia da Lei do Bem (ANPEI) e fontes confiáveis como embasamento da análise das informações técnicas do projeto.)
    
    Os critérios são fornecidos via Orientação de escrita fornecidos pelo próprio MCTI
    
    Descreva de forma objetiva os aspectos que demonstram a inovação e o avanço tecnológico proposto no projeto.
    
    Abaixo, seguem orientações para elaborar essa descrição de forma clara e alinhada aos critérios estabelecidos:
    1.	Descreva a Tecnologia Desenvolvida: explique de forma detalhada a tecnologia desenvolvida no projeto; destaque as novas funcionalidades ou características que a tornam diferente das soluções existentes; indique a aplicação prática da tecnologia, ou seja, em qual contexto ou setor ela será utilizada;
    2.	Evidencie as Novidades Tecnológicas: explique por que a tecnologia proposta é nova ou inovadora em relação ao estado da arte atual; descreva os avanços científicos ou tecnológicos que o projeto busca alcançar; destaque se a solução envolve:
    o	a compreensão de novos fenômenos (Pesquisa Básica Dirigida);
    o	o desenvolvimento ou aprimoramento de produtos, processos ou sistemas (Pesquisa Aplicada);
    o	a comprovação da viabilidade técnica ou funcional de algo novo ou significativamente melhorado (Desenvolvimento Experimental).
    3.	Compare com as Soluções Existentes: descreva as soluções atualmente disponíveis no mercado ou na literatura técnica; aponte as limitações dessas soluções que justificaram o desenvolvimento da nova tecnologia; explique como o projeto superou essas limitações.
    4.	Justifique o Desenvolvimento: explique os motivos que levaram à necessidade de desenvolver a nova tecnologia; destaque os benefícios esperados, como aumento de eficiência, redução de custos, melhoria de desempenho ou impacto ambiental positivo; relacione o desenvolvimento com a superação de uma barreira tecnológica ou científica.
    5.	Destaque a Não Obviedade da Solução: explique por que a solução proposta não é óbvia; destaque os aspectos criativos ou inovadores que diferenciam a proposta.
    
    OBS:
    •	i) Utilize linguagem clara e técnica, evitando jargões excessivos;
    •	ii) Inclua dados quantitativos sempre que possível (por exemplo, porcentagens, métricas de desempenho);
    •	iii) Relacione o projeto com os objetivos da Lei do Bem, destacando seu alinhamento com o avanço tecnológico e a inovação.
    
    Texto de elemento tecnologicamente novo ou inovador: {relacao}
    
    Forneça um feedback escrito, sobre o que precisa ser melhorado e o que já atende aos critérios. Além disso, retorne uma categoria entre:0 a 10. Conforme os critérios disponibilizados.
    O seu feedback será um guia de ações plausíveis e claras para que o redator saiba de forma muito objetiva o que melhorar e como, esse é o objetivo principal do prompt. Com isso, aponte de forma material do texto, os pontos de melhoria e principalmente, como deve ser melhorado, usando como base o próprio conteúdo do texto.
    
    O feedback deve ser sempre um texto corrido, não use listas ou qualquer outra formatação.
    
    A resposta deve ser um JSON com:
    {{
        feedback: (o feedback escrito do que precisa ser melhorado)
        avaliacao: (a categoria se atende de 0 a 10)
    }}
            """)
    
    response = receive_data(prompt)
    jsonResponse = json.loads(response)
    return jsonResponse


def prepareDataBarreira(relacao):
    prompt = (f"""
    Você é um especialista do MCTI que avaliará a qualidade de relatórios técnicos de Pesquisa, Desenvolvimento e Inovação segundo o manual de frascati.
    Com base no texto a seguir, referente a seção de Descrição da barreira ou desafio tecnológico superável de um relatório técnico da Lei do Bem, elabore uma análise que avalia se o texto de descrição atende a todos os critérios válidos ao caso descritos abaixo.
    (Considere o Manual de Frascati, Guia da Lei do Bem (ANPEI) e fontes confiáveis como embasamento da análise das informações técnicas do projeto.)
    
    Os critérios são fornecidos via Orientação de escrita fornecidos pelo próprio MCTI
    
    Critérios a serem avaliados: Descreva de forma clara e detalhada os obstáculos tecnológicos enfrentados durante o projeto de PD&I, bem como as estratégias adotadas para superá-los.
    Abaixo, seguem orientações para elaborar essa descrição de maneira alinhada aos critérios estabelecidos:
    1.	Identifique o Problema Tecnológico (descreva o problema ou dificuldade tecnológica específica que o projeto buscou resolver; explique os impactos que essa barreira gerou no desenvolvimento do projeto, como atrasos, custos adicionais ou limitações técnicas.)
    2.	Descreva a Abordagem para Superação (detalhe as atividades, estudos, análises e testes realizados para resolver o problema)
    3.	Indique o Status de Superação (informe se a barreira tecnológica já foi superada ou se o projeto ainda está em desenvolvimento. Caso a barreira tenha sido superada, descreva os resultados alcançados e como eles impactam positivamente o projeto. Caso a barreira ainda não tenha sido superada, detalhe as hipóteses sendo testadas e as etapas futuras para resolver o problema. Caso a barreira ainda não tenha sido superada, descreva as etapas futuras e o cronograma previsto para a resolução do problema, assim como indique os recursos necessários (humanos, financeiros, tecnológicos) para concluir a superação.)
    4.	Destaque a Relevância do Desafio (explique por que a superação dessa barreira é importante para o sucesso do projeto; relacione a superação do desafio com os objetivos gerais do projeto e os benefícios esperados).
    5.	Inclua Dados e Evidências (utilize dados concretos para embasar a descrição, como métricas de desempenho, resultados de testes ou comparações com soluções existentes; inclua evidências científicas ou técnicas que comprovem a eficácia da abordagem adotada).
    OBS:
    •	i) Seja específico e evite generalidades;
    •	ii) Utilize linguagem técnica, mas clara e acessível;
    •	iii) Inclua dados quantitativos sempre que possível (por exemplo, porcentagens, métricas de desempenho);
    •	iv) Relacione o projeto com os objetivos da Lei do Bem, destacando seu alinhamento com o avanço tecnológico e a inovação.
    
    Texto Descrição da barreira ou desafio tecnológico superável: {relacao}
    
    Forneça um feedback escrito, sobre o que precisa ser melhorado e o que já atende aos critérios. Além disso, retorne uma categoria entre:0 a 10. Conforme os critérios disponibilizados.
    O seu feedback será um guia de ações plausíveis e claras para que o redator saiba de forma muito objetiva o que melhorar e como, esse é o objetivo principal do prompt. Com isso, aponte de forma material do texto, os pontos de melhoria e principalmente, como deve ser melhorado, usando como base o próprio conteúdo do texto.
    
    O feedback deve ser sempre um texto corrido, não use listas ou qualquer outra formatação.
    
    A resposta deve ser um JSON com:
    {{
        feedback: (o feedback escrito do que precisa ser melhorado)
        avaliacao: (a categoria se atende de 0 a 10)
    }}
            """)
    
    response = receive_data(prompt)
    jsonResponse = json.loads(response)
    return jsonResponse

def prepareDataMetodologia(relacao):
    prompt = (f"""
    Você é um especialista do MCTI que avaliará a qualidade de relatórios técnicos de Pesquisa, Desenvolvimento e Inovação segundo o manual de frascati.
    Avalie o texto da seção metodologia e métodos utilizados no desenvolvimento do projeto de um relatório técnico e atribua uma nota de 0 a 10 conforme o atendimento dos critérios abaixo. Responda somente com a nota numérica.

    Critérios de avaliação: 
    Descrever de forma detalhada as técnicas, métodos e procedimentos utilizados para superar o desafio tecnológico e alcançar os objetivos do projeto de PD&I.
    Abaixo, seguem orientações para elaborar essa descrição:
    1.	Descreva as Atividades Realizadas (detalhe as atividades específicas realizadas durante o projeto, como estudos bibliográficos, experimentos em laboratório, testes em bancada, desenvolvimento de protótipos, etc. Explique como essas atividades contribuíram para a superação do desafio tecnológico).
    2.	Explique os Métodos e Técnicas Utilizados (descreva os métodos científicos e técnicos aplicados no projeto, como análises estatísticas, modelagem computacional, ensaios físicos, etc.; destaque a cientificidade dos métodos, ou seja, como eles garantem a confiabilidade e a validade dos resultados)
    3.	Detalhe os Processos de Desenvolvimento Experimental (explique como foi conduzido o desenvolvimento experimental, desde a concepção da ideia até a validação da solução; inclua informações sobre os recursos e equipamentos utilizados, bem como as etapas de teste e validação).
    4.	Demonstre as Competências Exigidas (descreva as competências técnicas e científicas necessárias para implementar o projeto; mencione a qualificação da equipe e a colaboração com instituições de pesquisa, se aplicável).
    5.	Explique como a Barreira/Desafio foi Superado (descreva como os métodos e processos adotados contribuíram para a superação do desafio tecnológico; destaque os resultados alcançados e como eles representam uma melhoria em relação às soluções existentes.)
    6.	Inclua Dados e Evidências (utilize dados concretos para embasar a descrição, como métricas de desempenho, resultados de testes ou comparações com soluções existentes; inclua evidências científicas ou técnicas que comprovem a eficácia da abordagem adotada.)
    OBS:
    •	i) Caso o projeto ainda esteja em andamento, descreva as etapas futuras e os métodos que serão utilizados para concluir o desenvolvimento;
    •	ii) Mencione os recursos necessários (humanos, financeiros, tecnológicos) para finalizar o projeto;
    •	iii) Utilize uma linguagem técnica, mas clara e acessível;
    •	iv) Evite generalidades e seja específico ao descrever métodos e processos;
    •	v) Relacione a descrição com os objetivos da Lei do Bem, destacando a inovação e o avanço tecnológico.


    Texto da metodologia e métodos utilizados no desenvolvimento do projeto:{relacao}
    Forneça um feedback escrito, sobre o que precisa ser melhorado e o que já atende aos critérios. Além disso, retorne uma categoria entre:0 a 10. Conforme os critérios disponibilizados.
    O seu feedback será um guia de ações plausíveis e claras para que o redator saiba de forma muito objetiva o que melhorar e como, esse é o objetivo principal do prompt. Com isso, aponte de forma material do texto, os pontos de melhoria e principalmente, como deve ser melhorado, usando como base o próprio conteúdo do texto.
    
    O feedback deve ser sempre um texto corrido, não use listas ou qualquer outra formatação.
    
    A resposta deve ser um JSON com:
    {{
        feedback: (o feedback escrito do que precisa ser melhorado)
        avaliacao: (a categoria se atende de 0 a 10)
    }}
            """)
    
    response = receive_data(prompt)
    jsonResponse = json.loads(response)
    return jsonResponse


def prepareDataComplementar(relacao):
    prompt = (f"""
    Você é um especialista do MCTI que avaliará a qualidade de relatórios técnicos de Pesquisa, Desenvolvimento e Inovação segundo o manual de frascati.
    Avalie o texto da seção Complementar e métodos utilizados no desenvolvimento do projeto de um relatório técnico e atribua uma nota de 0 a 10 conforme o atendimento dos critérios abaixo. Responda somente com a nota numérica.

    Critérios de avaliação: 
    Descrever de forma detalhada as técnicas, métodos e procedimentos utilizados para superar o desafio tecnológico e alcançar os objetivos do projeto de PD&I.
    Abaixo, seguem orientações para elaborar essa descrição:
              
    Objetivo do campo é fornecer detalhes adicionais (se necessários) que não foram contemplados nos campos anteriores. Você pode incluir esclarecimentos sobre aspectos técnicos do projeto, justificativas para escolhas metodológicas, desafios enfrentados, alterações no escopo ou quaisquer informações relevantes para a avaliação do projeto. 
    
    OBS:
    •	i) Caso o projeto ainda esteja em andamento, descreva as etapas futuras e os métodos que serão utilizados para concluir o desenvolvimento;
    •	ii) Mencione os recursos necessários (humanos, financeiros, tecnológicos) para finalizar o projeto;
    •	iii) Utilize uma linguagem técnica, mas clara e acessível;
    •	iv) Evite generalidades e seja específico ao descrever métodos e processos;
    •	v) Relacione a descrição com os objetivos da Lei do Bem, destacando a inovação e o avanço tecnológico.


    Texto complementar e métodos utilizados no desenvolvimento do projeto:{relacao}
    Forneça um feedback escrito, sobre o que precisa ser melhorado e o que já atende aos critérios. Além disso, retorne uma categoria entre:0 a 10. Conforme os critérios disponibilizados.
    O seu feedback será um guia de ações plausíveis e claras para que o redator saiba de forma muito objetiva o que melhorar e como, esse é o objetivo principal do prompt. Com isso, aponte de forma material do texto, os pontos de melhoria e principalmente, como deve ser melhorado, usando como base o próprio conteúdo do texto.
    
    O feedback deve ser sempre um texto corrido, não use listas ou qualquer outra formatação.
    
    A resposta deve ser um JSON com:
    {{
        feedback: (o feedback escrito do que precisa ser melhorado)
        avaliacao: (a categoria se atende de 0 a 10)
    }}
            """)
    
    response = receive_data(prompt) 
    jsonResponse = json.loads(response)
    return jsonResponse


"""
  Forneça um feedback escrito, sobre o que precisa ser melhorado e o que já atende aos critérios. Além disso, retorne uma categoria entre: Não atende, Atende Pouco, Atende Razoavelmente, Atende Totalmente. Conforme os critérios disponibilizados.
    O seu feedback será um guia de ações plausíveis e claras para que o redator saiba de forma muito objetiva o que melhorar e como, esse é o objetivo principal do prompt. Com isso, aponte de forma material do texto, os pontos de melhoria e principalmente, como deve ser melhorado, usando como base o próprio conteúdo do texto.
    
    O feedback deve ser sempre um texto corrido, não use listas ou qualquer outra formatação.

"""