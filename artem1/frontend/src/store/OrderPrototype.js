export default class Order {
  constructor (
    id,
    number,
    brand,
    articul,
    term,
    term_wanted,
    amount_wanted,
    amount_actual,
    cost,
    status,
    description
  ) {
    this.id = id;
    this.number = number;
    this.brand = brand;
    this.articul = articul;
    this.term = term;
    this.term_wanted = term_wanted;
    this.amount_wanted = amount_wanted;
    this.amount_actual = amount_actual;
    this.cost = cost;
    this.status = status;
    this.description = description;
  }
}
