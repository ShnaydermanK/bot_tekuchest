ssql_query_spisok_roTSS = """
            select 
        me.id as id,concat(me.last_name,' ', me.first_name, ' ',me.middle_name) as "ФИО",me.role as special,concat(me4.last_name,' ', me4.first_name, ' ',me4.middle_name) as "РО", me.remove_date as date_uval, pp.project_title as project,me2.first_working_date as first_date
        from main_employeetree me
        left join projects_projects pp 
        on me.project_id =pp.id
        left join main_employeeinfo me2 
        on me.id=me2.worker_id
        left join main_employeetree me3 
        on me.parent_id = me3.id
        left join main_employeetree me4 
        on me3.parent_id =me4.id
        left join main_employeetree me5 
        on me4.parent_id =me5.id 
        where (me.remove_date is null or me.remove_date >'2023-05-31')
        and me.remove_date is not null and me.remove_date >='2023-08-01'
        """

ssql_query_spisok_ro = """select 
        me.id as id,me.role as special,concat(me4.last_name,' ', me4.first_name, ' ',me4.middle_name) as "РО", me.remove_date as date_uval, pp.project_title as project,me2.first_working_date as first_date
        from main_employeetree me
        left join projects_projects pp 
        on me.project_id =pp.id
        left join main_employeeinfo me2 
        on me.id=me2.worker_id
        left join main_employeetree me3 
        on me.parent_id = me3.id
        left join main_employeetree me4 
        on me3.parent_id =me4.id
        left join main_employeetree me5 
        on me4.parent_id =me5.id 
        where (me.remove_date is null or me.remove_date >'2023-05-31')
        and concat(me4.last_name,' ', me4.first_name, ' ',me4.middle_name) like '%{}%'"""

sql_query_all = """
                select
        me.id as id,me.role as special,concat(me5.last_name,' ', me5.first_name, ' ',me5.middle_name) as "Управление", me.remove_date as date_uval, pp.project_title as project,me2.first_working_date as first_date
        from main_employeetree me
        left join projects_projects pp
        on me.project_id =pp.id
        left join main_employeeinfo me2
        on me.id=me2.worker_id
        left join main_employeetree me3
        on me.parent_id = me3.id
        left join main_employeetree me4
        on me3.parent_id =me4.id
        left join main_employeetree me5
        on me4.parent_id =me5.id
        where (me.remove_date is null or me.remove_date >'2023-05-31')
        and concat(me5.last_name,' ', me5.first_name, ' ',me5.middle_name) like '%{}%'
            """

ssql_query_spisok_op = """select
        me.id as id,concat(me.last_name,' ', me.first_name, ' ',me.middle_name) as "ФИО",me.role as special,concat(me5.last_name,' ', me5.first_name, ' ',me5.middle_name) as "Управление", me.remove_date as date_uval, pp.project_title as project,me2.first_working_date as first_date
        from main_employeetree me
        left join projects_projects pp
        on me.project_id =pp.id
        left join main_employeeinfo me2
        on me.id=me2.worker_id
        left join main_employeetree me3
        on me.parent_id = me3.id
        left join main_employeetree me4
        on me3.parent_id =me4.id
        left join main_employeetree me5
        on me4.parent_id =me5.id
        where (me.remove_date is null or me.remove_date >'2023-05-31')
        and concat(me5.last_name,' ', me5.first_name, ' ',me5.middle_name) like '%{}%'
        and me.remove_date is not null and me.remove_date >='2023-08-01'
            """

ssql_query_all_udal="""select 
        me.id as id,me.role as special,concat(me5.last_name,' ', me5.first_name, ' ',me5.middle_name) as "Управление", me.remove_date as date_uval, pp.project_title as project,me2.first_working_date as first_date
        from main_employeetree me
        left join projects_projects pp 
        on me.project_id =pp.id
        left join main_employeeinfo me2 
        on me.id=me2.worker_id
        left join main_employeetree me3 
        on me.parent_id = me3.id
        left join main_employeetree me4 
        on me3.parent_id =me4.id
        left join main_employeetree me5 
        on me4.parent_id =me5.id 
        where (me.remove_date is null or me.remove_date >'2023-05-31')
        and concat(me5.last_name,' ', me5.first_name, ' ',me5.middle_name) like '%{}%'
        and me2.work_format = 'удаленно'"""

ssql_query_all_office="""select 
        me.id as id,me.role as special,concat(me5.last_name,' ', me5.first_name, ' ',me5.middle_name) as "Управление", me.remove_date as date_uval, pp.project_title as project,me2.first_working_date as first_date
        from main_employeetree me
        left join projects_projects pp 
        on me.project_id =pp.id
        left join main_employeeinfo me2 
        on me.id=me2.worker_id
        left join main_employeetree me3 
        on me.parent_id = me3.id
        left join main_employeetree me4 
        on me3.parent_id =me4.id
        left join main_employeetree me5 
        on me4.parent_id =me5.id 
        where (me.remove_date is null or me.remove_date >'2023-05-31')
        and concat(me5.last_name,' ', me5.first_name, ' ',me5.middle_name) like '%{}%'
        and me2.work_format = 'офис'"""