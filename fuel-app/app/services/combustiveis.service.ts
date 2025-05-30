import {
    FuelApi,
    FuelResponse,
    Configuration,
  } from '../api/client/index';
  
  const configuration = new Configuration({
    basePath:  process.env.NEXT_PUBLIC_API_BASE_URL,
  });
  
  const api = new FuelApi(configuration);
  
  export const CombustiveisService = {
    async listar(): Promise<FuelResponse[]> {
      const response = await api.getFuelsApiV1FuelGet();
      return response.data;
    },
  };