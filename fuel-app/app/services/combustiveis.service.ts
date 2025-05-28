import {
    CombustiveisApi,
    CombustivelResponse,
    Configuration,
  } from '../api/client/index';
  
  const configuration = new Configuration({
    basePath:  process.env.NEXT_PUBLIC_API_BASE_URL,
  });
  
  const api = new CombustiveisApi(configuration);
  
  export const CombustiveisService = {
    async listar(): Promise<CombustivelResponse[]> {
      const response = await api.getCombustiveisApiV1CombustiveisGet();
      return response.data;
    },
  };