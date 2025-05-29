"use client";

import type React from "react";

import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { toast } from "sonner";
import { Loader2 } from "lucide-react";
import { CombustiveisService } from "./services/combustiveis.service";
import { OperacoesService } from "./services/operacoes.service";
import {
  CombustivelResponse,
  OperacaoCreate,
  OperacaoResponse,
  OperacaoCreateTipoEnum,
} from "./api/client/api";
import { BalanceCard } from "../components/balance-card.component"

export default function FuelOperationsPage() {
  const [fuelTypes, setFuelTypes] = useState<CombustivelResponse[]>([]);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [refreshTrigger, setRefreshTrigger] = useState(0)
  const [formData, setFormData] = useState({
    combustivel_id: "",
    tipo: "",
    data: "",
    litros: "",
  });
  const operationTypes: OperacaoCreateTipoEnum[] = ["compra", "venda"];

  useEffect(() => {
    const fetchFuelTypes = async () => {
      try {
        const response = await CombustiveisService.listar();
        if (response) {
          setFuelTypes(response);
        } else {
          toast.error("Erro ao carregar combustíveis");
        }
      } catch (error) {
        console.log(error);
        toast.error("Erro de conexão ao carregar tipos de combustível");
      } finally {
        setLoading(false);
      }
    };

    fetchFuelTypes();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (
      !formData.combustivel_id ||
      !formData.tipo ||
      !formData.data ||
      !formData.litros
    ) {
      toast("Preencha todos os campos antes de registrar uma nova operação");
      return;
    }

    setSubmitting(true);

    try {
      const payload: OperacaoCreate = {
        combustivel_id: Number.parseInt(formData.combustivel_id),
        tipo: operationTypes[Number.parseInt(formData.tipo)],
        data: formData.data,
        litros: Number.parseFloat(formData.litros),
        selic: 11.5,
      };

      const response: OperacaoResponse = await OperacoesService.postOperation(
        payload
      );

      if (response) {
        toast.success("Operação registrada com sucesso");

        setFormData({
          combustivel_id: "",
          tipo: "",
          data: "",
          litros: "",
        });

        setRefreshTrigger(prev => prev + 1)
      } else {
        toast.error("Falha ao registrar operação");
      }
    } catch (error) {
      console.log(error);
      toast.error("Erro de conexão ao registrar operação");
    } finally {
      setSubmitting(false);
    }
  };

  const handleInputChange = (field: string, value: string) => {
    setFormData((prev) => ({
      ...prev,
      [field]: value,
    }));
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="flex items-center space-x-2">
          <Loader2 className="h-6 w-6 animate-spin" />
          <span>Carregando...</span>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <div className="max-w-2xl mx-auto space-y-6">
        <Card>
          <CardHeader>
            <CardTitle>Controle de Operações de Combustível</CardTitle>
            <CardDescription>
              Registre operações de compra e venda de combustível
            </CardDescription>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label htmlFor="fuel-type">Tipo de Combustível</Label>
                  <Select
                    value={formData.combustivel_id}
                    onValueChange={(value) =>
                      handleInputChange("combustivel_id", value)
                    }
                  >
                    <SelectTrigger id="fuel-type">
                      <SelectValue placeholder="Selecione o combustível" />
                    </SelectTrigger>
                    <SelectContent>
                      {fuelTypes.map((fuel) => (
                        <SelectItem key={fuel.id} value={fuel.id.toString()}>
                          {fuel.nome}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>

                <div className="space-y-2">
                  <Label htmlFor="operation-type">Tipo de Operação</Label>
                  <Select
                    value={formData.tipo}
                    onValueChange={(value) => handleInputChange("tipo", value)}
                  >
                    <SelectTrigger id="operation-type">
                      <SelectValue placeholder="Selecione a operação" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="0">Compra</SelectItem>
                      <SelectItem value="1">Venda</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                <div className="space-y-2">
                  <Label htmlFor="date">Data</Label>
                  <Input
                    id="date"
                    type="date"
                    value={formData.data}
                    onChange={(e) => handleInputChange("data", e.target.value)}
                    required
                  />
                </div>

                <div className="space-y-2">
                  <Label htmlFor="liters">Litros</Label>
                  <Input
                    id="liters"
                    type="number"
                    step="0.01"
                    min="0"
                    placeholder="0.00"
                    value={formData.litros}
                    onChange={(e) =>
                      handleInputChange("litros", e.target.value)
                    }
                    required
                  />
                </div>
              </div>

              <Button type="submit" className="w-full" disabled={submitting}>
                {submitting ? (
                  <>
                    <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                    Registrando...
                  </>
                ) : (
                  "Registrar Operação"
                )}
              </Button>
            </form>
          </CardContent>
        </Card>
        <BalanceCard refreshTrigger={refreshTrigger}/>
      </div>
    </div>
  );
}
