
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(page_title="Clinton University Dashboard", layout="wide")

# Dashboard title
st.title("🎓 Clinton University Dashboard")
st.markdown("#### Academic Performance | Financial Analytics | Student Trends | 2023 – 2025")
st.markdown("---")

# Load data
@st.cache_data
def load_university_data():
    np.random.seed(42)
    
    # Departments
    departments = [
        "School of Business", "School of Engineering", "School of Computing",
        "School of Law", "School of Medicine", "School of Education",
        "School of Humanities", "School of Nursing"
    ]
    
    # Courses by department
    courses = {
        "School of Business": ["BCOM", "BBM", "MBA", "Accounting", "Finance"],
        "School of Engineering": ["Civil Eng", "Electrical Eng", "Mechanical Eng", "Chemical Eng"],
        "School of Computing": ["CS", "IT", "Data Science", "Cybersecurity", "Software Eng"],
        "School of Law": ["LLB", "Diploma in Law", "Master of Laws"],
        "School of Medicine": ["MBChB", "Clinical Medicine", "Pharmacy", "Dentistry"],
        "School of Education": ["B.Ed", "PGDE", "Early Childhood", "Special Needs"],
        "School of Humanities": ["Psychology", "Sociology", "Literature", "History"],
        "School of Nursing": ["BSN", "KRCHN", "Nursing Leadership"]
    }
    
    years = [2023, 2024, 2025]
    
    # Learning modes
    learning_modes = ["Physical", "Distance", "Virtual"]
    
    data = []
    
    for year in years:
        growth = 1 + (year - 2023) * 0.12  # 12% annual growth
        
        for dept in departments:
            # Student population per department
            if dept in ["School of Business", "School of Computing"]:
                students = int(1200 * growth * np.random.uniform(0.9, 1.1))
            elif dept in ["School of Medicine", "School of Nursing"]:
                students = int(800 * growth * np.random.uniform(0.9, 1.1))
            else:
                students = int(500 * growth * np.random.uniform(0.9, 1.1))
            
            # Completion rate (varies by department and year)
            if dept in ["School of Medicine", "School of Nursing"]:
                completion = np.random.uniform(85, 92) + (year - 2023) * 1.5
            elif dept in ["School of Business", "School of Computing"]:
                completion = np.random.uniform(78, 88) + (year - 2023) * 2
            else:
                completion = np.random.uniform(75, 85) + (year - 2023) * 2
            
            completion = min(completion, 98)  # Cap at 98%
            
            # For each course in department
            for course in courses.get(dept, ["General"]):
                # Graduating students per course
                if year == 2023:
                    graduating = int(students * 0.22 * np.random.uniform(0.8, 1.2))
                elif year == 2024:
                    graduating = int(students * 0.24 * np.random.uniform(0.8, 1.2))
                else:
                    graduating = int(students * 0.26 * np.random.uniform(0.8, 1.2))
                
                data.append({
                    "Year": year,
                    "Department": dept,
                    "Course": course,
                    "Total_Students": students,
                    "Graduating_Students": graduating,
                    "Completion_Rate": round(completion, 1),
                    "Learning_Mode": np.random.choice(learning_modes, p=[0.55, 0.25, 0.20])
                })
    
    return pd.DataFrame(data)

# Financial data
@st.cache_data
def load_financial_data():
    years = [2023, 2024, 2025]
    quarters = ["Q1", "Q2", "Q3", "Q4"]
    
    financial_data = []
    
    for year in years:
        growth = 1 + (year - 2023) * 0.15
        
        for quarter in quarters:
            # Revenue streams (KES Millions)
            tuition_revenue = 450 * growth * np.random.uniform(0.95, 1.05)
            research_grants = 80 * growth * np.random.uniform(0.9, 1.1)
            donations = 25 * growth * np.random.uniform(0.8, 1.2)
            other_income = 15 * growth * np.random.uniform(0.9, 1.1)
            
            total_revenue = tuition_revenue + research_grants + donations + other_income
            
            # Expenses (KES Millions)
            salaries = 250 * growth * np.random.uniform(0.95, 1.05)
            infrastructure = 80 * growth * np.random.uniform(0.9, 1.1)
            research_expenses = 40 * growth * np.random.uniform(0.9, 1.1)
            operational = 60 * growth * np.random.uniform(0.95, 1.05)
            student_services = 30 * growth * np.random.uniform(0.9, 1.1)
            
            total_expenses = salaries + infrastructure + research_expenses + operational + student_services
            profit = total_revenue - total_expenses
            
            financial_data.append({
                "Year": year,
                "Quarter": quarter,
                "Tuition_Revenue": round(tuition_revenue, 1),
                "Research_Grants": round(research_grants, 1),
                "Donations": round(donations, 1),
                "Other_Income": round(other_income, 1),
                "Total_Revenue": round(total_revenue, 1),
                "Salaries": round(salaries, 1),
                "Infrastructure": round(infrastructure, 1),
                "Research_Expenses": round(research_expenses, 1),
                "Operational_Expenses": round(operational, 1),
                "Student_Services": round(student_services, 1),
                "Total_Expenses": round(total_expenses, 1),
                "Net_Profit": round(profit, 1)
            })
    
    return pd.DataFrame(financial_data)

# New courses data
@st.cache_data
def load_new_courses():
    new_courses = {
        2023: [
            "Data Science & AI", "Cybersecurity", "Renewable Energy Eng",
            "Public Health", "Digital Marketing"
        ],
        2024: [
            "Cloud Computing", "Biomedical Engineering", "Financial Technology",
            "Counseling Psychology", "Supply Chain Management"
        ],
        2025: [
            "Machine Learning", "Telemedicine", "Green Architecture",
            "E-Sports Management", "Artificial Intelligence"
        ]
    }
    
    courses_list = []
    for year, courses in new_courses.items():
        for course in courses:
            # Enrollment for new courses
            enrollment = np.random.randint(45, 150)
            courses_list.append({
                "Year": year,
                "Course": course,
                "Enrollment": enrollment
            })
    
    return pd.DataFrame(courses_list)

# Load all data
df_academic = load_university_data()
df_financial = load_financial_data()
df_new_courses = load_new_courses()

# Calculate summary metrics
total_students_2025 = df_academic[df_academic["Year"] == 2025]["Total_Students"].sum()
total_graduates_2025 = df_academic[df_academic["Year"] == 2025]["Graduating_Students"].sum()
avg_completion = df_academic[df_academic["Year"] == 2025]["Completion_Rate"].mean()
total_revenue_2025 = df_financial[df_financial["Year"] == 2025]["Total_Revenue"].sum()
total_profit_2025 = df_financial[df_financial["Year"] == 2025]["Net_Profit"].sum()

# Sidebar Filters
st.sidebar.header("🔍 Filter Dashboard")

# Year filter
years_selected = st.sidebar.multiselect(
    "Select Year(s)", 
    df_academic["Year"].unique(), 
    default=[2023, 2024, 2025]
)

# Department filter
depts = st.sidebar.multiselect(
    "Select Department(s)", 
    df_academic["Department"].unique(), 
    default=df_academic["Department"].unique()[:4]
)

# Learning mode filter
modes = st.sidebar.multiselect(
    "Select Learning Mode", 
    df_academic["Learning_Mode"].unique(), 
    default=df_academic["Learning_Mode"].unique()
)

# Filter data
filtered_academic = df_academic[
    (df_academic["Year"].isin(years_selected)) & 
    (df_academic["Department"].isin(depts)) &
    (df_academic["Learning_Mode"].isin(modes))
]

filtered_financial = df_financial[df_financial["Year"].isin(years_selected)]

# Key Metrics
st.header("📊 University Overview")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("👨‍🎓 Total Students (2025)", f"{total_students_2025:,}")
with col2:
    st.metric("🎓 Graduates (2025)", f"{total_graduates_2025:,}")
with col3:
    st.metric("📈 Avg Completion Rate", f"{avg_completion:.1f}%", delta="+5.2%")
with col4:
    st.metric("💰 Total Revenue (2025)", f"KES {total_revenue_2025:.0f}M")
with col5:
    profit_color = "normal" if total_profit_2025 > 0 else "inverse"
    st.metric("💵 Net Profit (2025)", f"KES {total_profit_2025:.0f}M", delta_color=profit_color)

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📚 Academic Performance", 
    "🎓 Courses & Graduates", 
    "💰 Financial Performance",
    "👥 Student Population",
    "🆕 New Courses"
])

# ==============================
# TAB 1: Academic Performance
# ==============================
with tab1:
    st.subheader("Completion Rate by Department")
    
    # Completion rate chart
    completion_data = filtered_academic.groupby(["Year", "Department"])["Completion_Rate"].mean().reset_index()
    
    fig1 = px.bar(
        completion_data,
        x="Department",
        y="Completion_Rate",
        color="Year",
        title="Completion Rate by Department (%)",
        barmode="group",
        text_auto=True,
        color_continuous_scale="Viridis"
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Completion trend by department
        top_depts = completion_data.groupby("Department")["Completion_Rate"].mean().nlargest(5).index
        top_completion = completion_data[completion_data["Department"].isin(top_depts)]
        
        fig2 = px.line(
            top_completion,
            x="Year",
            y="Completion_Rate",
            color="Department",
            title="Top 5 Departments - Completion Rate Trend",
            markers=True
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        # Learning mode impact on completion
        mode_completion = filtered_academic.groupby(["Year", "Learning_Mode"])["Completion_Rate"].mean().reset_index()
        
        fig3 = px.bar(
            mode_completion,
            x="Year",
            y="Completion_Rate",
            color="Learning_Mode",
            title="Completion Rate by Learning Mode",
            barmode="group",
            text_auto=True
        )
        st.plotly_chart(fig3, use_container_width=True)
    
    # Department ranking
    st.subheader("Department Performance Ranking (2025)")
    dept_ranking = filtered_academic[filtered_academic["Year"] == 2025].groupby("Department")["Completion_Rate"].mean().sort_values(ascending=False).reset_index()
    dept_ranking["Rank"] = dept_ranking.index + 1
    
    fig4 = px.bar(
        dept_ranking,
        x="Completion_Rate",
        y="Department",
        orientation="h",
        title="2025 Department Ranking by Completion Rate",
        color="Completion_Rate",
        color_continuous_scale="RdYlGn",
        text="Completion_Rate"
    )
    st.plotly_chart(fig4, use_container_width=True)

# ==============================
# TAB 2: Courses & Graduates
# ==============================
with tab2:
    st.subheader("Courses with Highest Graduating Students")
    
    # Top courses by graduates
    top_courses = filtered_academic.groupby(["Year", "Course"])["Graduating_Students"].sum().reset_index()
    top_courses_2025 = top_courses[top_courses["Year"] == 2025].nlargest(10, "Graduating_Students")
    
    fig5 = px.bar(
        top_courses_2025,
        x="Course",
        y="Graduating_Students",
        title="Top 10 Courses by Graduating Students (2025)",
        color="Graduating_Students",
        color_continuous_scale="Blues",
        text_auto=True
    )
    st.plotly_chart(fig5, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Graduates trend by department
        grad_by_dept = filtered_academic.groupby(["Year", "Department"])["Graduating_Students"].sum().reset_index()
        
        fig6 = px.line(
            grad_by_dept,
            x="Year",
            y="Graduating_Students",
            color="Department",
            title="Graduate Trends by Department",
            markers=True
        )
        st.plotly_chart(fig6, use_container_width=True)
    
    with col2:
        # Graduates vs total students
        summary_by_year = filtered_academic.groupby("Year").agg({
            "Total_Students": "sum",
            "Graduating_Students": "sum"
        }).reset_index()
        
        fig7 = px.bar(
            summary_by_year,
            x="Year",
            y=["Total_Students", "Graduating_Students"],
            title="Total Students vs Graduates",
            barmode="group",
            labels={"value": "Count", "variable": "Category"}
        )
        st.plotly_chart(fig7, use_container_width=True)
    
    # Department graduate distribution
    st.subheader("Graduate Distribution by Department (2025)")
    grad_pie = filtered_academic[filtered_academic["Year"] == 2025].groupby("Department")["Graduating_Students"].sum()
    
    fig8 = px.pie(
        values=grad_pie.values,
        names=grad_pie.index,
        title="Graduate Share by Department (2025)",
        hole=0.3
    )
    st.plotly_chart(fig8, use_container_width=True)

# ==============================
# TAB 3: Financial Performance
# ==============================
with tab3:
    st.subheader("University Financial Performance")
    
    # Revenue and Expenses trend
    financial_trend = filtered_financial.groupby("Year").agg({
        "Total_Revenue": "sum",
        "Total_Expenses": "sum",
        "Net_Profit": "sum"
    }).reset_index()
    
    fig9 = px.line(
        financial_trend,
        x="Year",
        y=["Total_Revenue", "Total_Expenses", "Net_Profit"],
        title="Revenue, Expenses & Profit Trend (KES Millions)",
        markers=True,
        labels={"value": "KES Millions", "variable": "Category"}
    )
    st.plotly_chart(fig9, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Revenue breakdown by source (latest year)
        revenue_2025 = filtered_financial[filtered_financial["Year"] == 2025].agg({
            "Tuition_Revenue": "sum",
            "Research_Grants": "sum",
            "Donations": "sum",
            "Other_Income": "sum"
        }).reset_index()
        revenue_2025.columns = ["Source", "Amount"]
        
        fig10 = px.pie(
            revenue_2025,
            values="Amount",
            names="Source",
            title=f"Revenue Breakdown ({max(years_selected)})",
            hole=0.3
        )
        st.plotly_chart(fig10, use_container_width=True)
    
    with col2:
        # Expense breakdown
        expenses_2025 = filtered_financial[filtered_financial["Year"] == 2025].agg({
            "Salaries": "sum",
            "Infrastructure": "sum",
            "Research_Expenses": "sum",
            "Operational_Expenses": "sum",
            "Student_Services": "sum"
        }).reset_index()
        expenses_2025.columns = ["Expense", "Amount"]
        
        fig11 = px.pie(
            expenses_2025,
            values="Amount",
            names="Expense",
            title=f"Expense Breakdown ({max(years_selected)})",
            hole=0.3
        )
        st.plotly_chart(fig11, use_container_width=True)
    
    # Quarterly performance
    st.subheader("Quarterly Financial Performance")
    quarterly_finance = filtered_financial[filtered_financial["Year"] == max(years_selected)]
    
    fig12 = px.bar(
        quarterly_finance,
        x="Quarter",
        y=["Total_Revenue", "Total_Expenses"],
        title=f"Quarterly Revenue vs Expenses ({max(years_selected)})",
        barmode="group",
        labels={"value": "KES Millions", "variable": "Category"}
    )
    st.plotly_chart(fig12, use_container_width=True)
    
    # Financial health indicators
    st.subheader("Financial Health Indicators")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        profit_margin = (financial_trend["Net_Profit"].iloc[-1] / financial_trend["Total_Revenue"].iloc[-1]) * 100
        st.metric("Profit Margin", f"{profit_margin:.1f}%", delta="+2.3%")
    
    with col2:
        rev_growth = ((financial_trend["Total_Revenue"].iloc[-1] - financial_trend["Total_Revenue"].iloc[0]) / financial_trend["Total_Revenue"].iloc[0]) * 100
        st.metric("Revenue Growth (3yr)", f"{rev_growth:.1f}%", delta="+15.2%")
    
    with col3:
        expense_ratio = (financial_trend["Total_Expenses"].iloc[-1] / financial_trend["Total_Revenue"].iloc[-1]) * 100
        st.metric("Expense Ratio", f"{expense_ratio:.1f}%", delta="-3.1%")

# ==============================
# TAB 4: Student Population
# ==============================
with tab4:
    st.subheader("Student Population Trends (2023-2025)")
    
    # Student population by department
    student_pop = filtered_academic.groupby(["Year", "Department"])["Total_Students"].sum().reset_index()
    
    fig13 = px.bar(
        student_pop,
        x="Year",
        y="Total_Students",
        color="Department",
        title="Student Population by Department",
        barmode="stack",
        labels={"Total_Students": "Number of Students"}
    )
    st.plotly_chart(fig13, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Overall student growth
        total_students = filtered_academic.groupby("Year")["Total_Students"].sum().reset_index()
        
        fig14 = px.line(
            total_students,
            x="Year",
            y="Total_Students",
            title="Total University Student Population",
            markers=True,
            line_shape="spline"
        )
        st.plotly_chart(fig14, use_container_width=True)
    
    with col2:
        # Year over year growth
        total_students["YoY_Growth"] = total_students["Total_Students"].pct_change() * 100
        
        fig15 = px.bar(
            total_students,
            x="Year",
            y="YoY_Growth",
            title="Year-over-Year Student Growth",
            text_auto=True,
            color="YoY_Growth",
            color_continuous_scale="RdYlGn"
        )
        st.plotly_chart(fig15, use_container_width=True)
    
    # Learning mode distribution
    st.subheader("Learning Mode Distribution")
    
    mode_dist = filtered_academic.groupby(["Year", "Learning_Mode"])["Total_Students"].sum().reset_index()
    
    fig16 = px.bar(
        mode_dist,
        x="Year",
        y="Total_Students",
        color="Learning_Mode",
        title="Physical vs Distance vs Virtual Learning",
        barmode="stack",
        labels={"Total_Students": "Number of Students"}
    )
    st.plotly_chart(fig16, use_container_width=True)
    
    # Learning mode trend - percentage
    mode_pivot = mode_dist.pivot(index="Year", columns="Learning_Mode", values="Total_Students").fillna(0)
    mode_pct = mode_pivot.div(mode_pivot.sum(axis=1), axis=0) * 100
    
    fig17 = px.area(
        mode_pct.reset_index().melt(id_vars="Year", var_name="Learning_Mode", value_name="Percentage"),
        x="Year",
        y="Percentage",
        color="Learning_Mode",
        title="Learning Mode Share Over Time (%)",
        labels={"Percentage": "Share of Students (%)"}
    )
    st.plotly_chart(fig17, use_container_width=True)
    
    # Department growth
    st.subheader("Fastest Growing Departments")
    dept_growth = filtered_academic.groupby(["Year", "Department"])["Total_Students"].sum().reset_index()
    dept_growth_2023 = dept_growth[dept_growth["Year"] == 2023].set_index("Department")["Total_Students"]
    dept_growth_2025 = dept_growth[dept_growth["Year"] == 2025].set_index("Department")["Total_Students"]
    
    growth_rate = ((dept_growth_2025 - dept_growth_2023) / dept_growth_2023 * 100).sort_values(ascending=False).head(5).reset_index()
    growth_rate.columns = ["Department", "Growth_Rate"]
    
    fig18 = px.bar(
        growth_rate,
        x="Department",
        y="Growth_Rate",
        title="Top 5 Departments by Student Growth (2023-2025)",
        color="Growth_Rate",
        color_continuous_scale="Greens",
        text_auto=True
    )
    st.plotly_chart(fig18, use_container_width=True)

# ==============================
# TAB 5: New Courses
# ==============================
with tab5:
    st.subheader("New Courses Introduced (2023-2025)")
    
    # Display new courses by year
    for year in [2023, 2024, 2025]:
        st.markdown(f"### {year}")
        year_courses = df_new_courses[df_new_courses["Year"] == year]
        
        col1, col2, col3, col4, col5 = st.columns(5)
        cols = [col1, col2, col3, col4, col5]
        
        for idx, (_, row) in enumerate(year_courses.iterrows()):
            with cols[idx % 5]:
                st.info(f"**{row['Course']}**\n\n📊 Enrollment: {row['Enrollment']} students")
    
    # Enrollment trend for new courses
    st.subheader("New Course Enrollment Trends")
    
    fig19 = px.bar(
        df_new_courses,
        x="Year",
        y="Enrollment",
        color="Course",
        title="Enrollment in Newly Introduced Courses",
        barmode="group"
    )
    st.plotly_chart(fig19, use_container_width=True)
    
    # Total new course enrollment by year
    new_course_stats = df_new_courses.groupby("Year").agg({
        "Course": "count",
        "Enrollment": "sum"
    }).reset_index()
    new_course_stats.columns = ["Year", "New_Courses", "Total_Enrollment"]
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig20 = px.bar(
            new_course_stats,
            x="Year",
            y="New_Courses",
            title="Number of New Courses Introduced",
            text_auto=True,
            color="New_Courses",
            color_continuous_scale="Viridis"
        )
        st.plotly_chart(fig20, use_container_width=True)
    
    with col2:
        fig21 = px.bar(
            new_course_stats,
            x="Year",
            y="Total_Enrollment",
            title="Total Enrollment in New Courses",
            text_auto=True,
            color="Total_Enrollment",
            color_continuous_scale="Blues"
        )
        st.plotly_chart(fig21, use_container_width=True)

# ==============================
# DATA DOWNLOAD
# ==============================
st.markdown("---")
st.subheader("📎 Export Data")

col1, col2, col3 = st.columns(3)

with col1:
    csv_academic = filtered_academic.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Academic Data", csv_academic, "academic_data.csv", "text/csv")

with col2:
    csv_financial = filtered_financial.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Financial Data", csv_financial, "financial_data.csv", "text/csv")

with col3:
    csv_courses = df_new_courses.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download New Courses Data", csv_courses, "new_courses.csv", "text/csv")

# Raw data expander
with st.expander("View Raw Academic Data"):
    st.dataframe(filtered_academic, use_container_width=True)

# Footer
st.markdown("---")
st.caption("📌 Clinton University Dashboard | Data 2023-2025 | Powered by Streamlit")
