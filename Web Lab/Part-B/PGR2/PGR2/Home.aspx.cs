using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace PGR2 
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        int bill = 0;
        CheckBoxList ch = new CheckBoxList();
        protected void Page_Load(object sender, EventArgs e)
        {
            int d = DateTime.Now.Hour;
            Panel1.Enabled = false;
            Panel2.Visible = true;
            CheckBoxList1.Visible = false;
            CheckBoxList2.Visible = false;
            CheckBoxList3.Visible = false;
            CheckBoxList4.Visible = false;
            if (d>=6&&d<11)
            {
                RadioButtonList1.Items[0].Selected = true;
                CheckBoxList1.Visible = true;
                ch = CheckBoxList1;
            }
            if (d >= 11 && d < 15)
            {
                RadioButtonList1.Items[1].Selected = true;
                CheckBoxList2.Visible = true;
                ch = CheckBoxList2;
            }
            if (d >= 15 && d < 19)
            {
                RadioButtonList1.Items[2].Selected = true;
                CheckBoxList3.Visible = true;
                ch = CheckBoxList3;
            }
            if (d >= 19 && d < 22)
            {
                RadioButtonList1.Items[3].Selected = true;
                CheckBoxList4.Visible = true;
                ch = CheckBoxList4;
            }
        }
    
        protected void RadioButtonList1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            for(int j=0;j<ch.Items.Count;j++)
            if(ch.Items[j].Selected)
            {
                bill+= int.Parse(ch.Items[j].Value);
            }
            Label1.Text = bill.ToString();
        }
    }
}