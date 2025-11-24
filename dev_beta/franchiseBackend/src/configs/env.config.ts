type ENV = {
  PORT: number;
  CAC: string;
};
export const ENV: ENV = {
  PORT: Number(process.env.PORT),
  CAC: process.env.CAC || '',
};
