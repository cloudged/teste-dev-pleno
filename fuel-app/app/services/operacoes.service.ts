import {
    OperacoesApi,
    OperacaoCreate,
    OperacaoResponse,
    Configuration,
  } from '../api/client/index';

   
  const configuration = new Configuration({
    basePath: process.env.NEXT_PUBLIC_API_BASE_URL,
  });

    const api = new OperacoesApi(configuration);

    export const OperacoesService = {
        async postOperation(payload: OperacaoCreate): Promise<OperacaoResponse> {
          const response = await api.criarOperacaoEndpointApiV1OperacoesPost(payload);
          return response.data;
        },
      };