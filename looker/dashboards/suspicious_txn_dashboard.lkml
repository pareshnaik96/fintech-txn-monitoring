view: suspicious_transactions {
  sql_table_name: project.dataset.transactions ;

  dimension: transaction_id {
    type: string
    sql: ${TABLE}.transaction_id ;
  }

  measure: count {
    type: count
  }

  dimension: suspicious {
    type: yesno
    sql: ${TABLE}.suspicious ;
  }
}

dashboard: suspicious_txn_dashboard {
  title: "Suspicious Transactions"

  element {
    title: "Suspicious Transaction Count"
    type: bar
    query {
      dimensions: [suspicious_transactions.suspicious]
      measures: [suspicious_transactions.count]
    }
  }
}