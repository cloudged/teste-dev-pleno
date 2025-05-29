"use client";

import { useState, useEffect } from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Loader2, TrendingUp, TrendingDown, DollarSign } from "lucide-react";
import { toast } from "sonner";
import { BalancoService } from "../app/services/balanco.service";

import { BalancoConsultaResponse } from "../app/api/client/api";

interface ChildProps {
  refreshTrigger: number;
}

export const BalanceCard = ({ refreshTrigger }: ChildProps) => {
  const [balance, setBalance] = useState<BalancoConsultaResponse | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAudit = async () => {
      try {
        const response: BalancoConsultaResponse =
          await BalancoService.getBalancos();
        if (response) {
          setBalance(response);
        } else {
          toast.error("Falha ao carregar dados do balanço");
        }
      } catch (error) {
        console.log(error);
        toast.error("Erro de conexão ao carregar balanço");
      } finally {
        setLoading(false);
      }
    };

    fetchAudit();
  }, [refreshTrigger]);

  const formatCurrency = (value: number) => {
    return new Intl.NumberFormat("pt-BR", {
      style: "currency",
      currency: "BRL",
    }).format(value);
  };

  const getDifferenceBadge = (diferenca: number) => {
    if (diferenca > 0) {
      return {
        icon: TrendingUp,
        color: "text-green-600",
        bgColor: "bg-green-50",
        label: "Lucro",
      };
    } else if (diferenca < 0) {
      return {
        icon: TrendingDown,
        color: "text-red-600",
        bgColor: "bg-red-50",
        label: "Prejuízo",
      };
    } else {
      return {
        icon: DollarSign,
        color: "text-gray-600",
        bgColor: "bg-gray-50",
        label: "Equilibrio",
      };
    }
  };

  if (loading) {
    return (
      <Card>
        <CardHeader>
          <CardTitle>Balanço Anual</CardTitle>
          <CardDescription>Resumo das operações de combustível</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="flex items-center justify-center py-8">
            <div className="flex items-center space-x-2">
              <Loader2 className="h-6 w-6 animate-spin" />
              <span>Carregando balanço...</span>
            </div>
          </div>
        </CardContent>
      </Card>
    );
  }

  if (!balance) {
    return (
      <Card>
        <CardHeader>
          <CardTitle>Balanço Anual</CardTitle>
          <CardDescription>Resumo das operações de combustível</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="text-center py-8 text-gray-500">
            Não foi possível carregar os dados do balanço
          </div>
        </CardContent>
      </Card>
    );
  }

  const differenceBadge = getDifferenceBadge(balance.diferenca);
  const DifferenceIcon = differenceBadge.icon;

  return (
    <Card>
      <CardHeader>
        <CardTitle>Balanço Anual - {balance.ano}</CardTitle>
        <CardDescription>Resumo das operações de combustível</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          
          <div className="bg-blue-50 rounded-lg p-4 border border-blue-200">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-blue-600 mb-1">
                  Total Compras
                </p>
                <p className="text-xl font-bold text-blue-900">
                  {formatCurrency(balance.total_compra)}
                </p>
              </div>
              <div className="bg-blue-100 p-2 rounded-full">
                <TrendingDown className="h-3 w-3 text-blue-600" />
              </div>
            </div>
          </div>

          
          <div className="bg-green-50 rounded-lg p-4 border border-green-200">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-green-600 mb-1">
                  Total Vendas
                </p>
                <p className="text-xl font-bold text-green-900">
                  {formatCurrency(balance.total_venda)}
                </p>
              </div>
              <div className="bg-green-100 p-2 rounded-full">
                <TrendingUp className="h-3 w-3 text-green-600" />
              </div>
            </div>
          </div>

          
          <div
            className={`${
              differenceBadge.bgColor
            } rounded-lg p-4 border ${differenceBadge.bgColor
              .replace("bg-", "border-")
              .replace("-50", "-200")}`}
          >
            <div className="flex items-center justify-between">
              <div>
                <p
                  className={`text-sm font-medium ${differenceBadge.color} mb-1`}
                >
                  {differenceBadge.label}
                </p>
                <p
                  className={`text-2xl font-bold ${differenceBadge.color
                    .replace("text-", "text-")
                    .replace("-600", "-900")}`}
                >
                  {formatCurrency(Math.abs(balance.diferenca))}
                </p>
              </div>
              <div
                className={`${differenceBadge.bgColor.replace(
                  "-50",
                  "-100"
                )} p-2 rounded-full`}
              >
                <DifferenceIcon
                  className={`h-3 w-3 ${differenceBadge.color}`}
                />
              </div>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
