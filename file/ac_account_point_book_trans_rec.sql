select
  a.`id`,
  a.`book_log_id`,
  a.`trade_id`,
  a.`book_id`,
  a.`book_subject_id`,
  a.`account_id`,
  a.`account_type`,
  a.`cust_id`,
  a.`company_id`,
  a.`total_assets`,
  a.`before_frozen_assets`,
  a.`before_available_assets`,
  a.`change_assets`,
  a.`change_type`,
  a.`change_type_name`,
  a.`change_group`,
  a.`change_direction`,
  a.`change_status`,
  a.`change_desc`,
  a.`from_order_pid`,
  a.`from_order_cid`,
  a.`from_mk_id`,
  a.`from_mk_name`,
  a.`from_cm_id`,
  a.`from_cm_name`,
  a.`provide_time`,
  a.`effect_time`,
  a.`invalid_time`,
  a.`used_time`,
  a.`point_state`,
  a.`give_reason`,
  a.`give_desc`,
  a.`department_id`,
  a.`department_name`,
  a.`template_id`,
  a.`budget_id`,
  a.`comp_form_detail_id`,
  a.`instance_id`,
  a.`create_id`,
  a.`creator`,
  a.`create_time`,
  a.`update_id`,
  a.`updater`,
  a.`update_time`,
  a.`delete_yn`,
  a.`operator_id`,
  a.`operator`,
  a.`operate_time`,
  a.`remark`,
  a.`extra`,
  a.`market_id`
from
  ac_account_point_book_trans_rec a
  inner join `ac_account_point` b on a.`book_id` = b.`book_id`
  and b.delete_yn = 0
where
  1 = 1
  and (
    (
      a.`provide_time` >= '2024-12-01 00:00:00'
      and a.`provide_time` < '2024-12-01 06:00:00'
    )
    or (
      a.`effect_time` >= '2024-12-01 00:00:00'
      and a.`effect_time` < '2024-12-01 06:00:00'
    )
    or (
      a.`invalid_time` >= '2024-12-01 00:00:00'
      and a.`invalid_time` < '2024-12-01 06:00:00'
    )
    or (
      a.`used_time` >= '2024-12-01 00:00:00'
      and a.`used_time` < '2024-12-01 06:00:00'
    )
    or (
      a.`create_time` >= '2024-12-01 00:00:00'
      and a.`create_time` < '2024-12-01 06:00:00'
    )
    or (
      a.`update_time` >= '2024-12-01 00:00:00'
      and a.`update_time` < '2024-12-01 06:00:00'
    )
  )