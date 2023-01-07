using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace PGR1
{
    public partial class Home : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Calendar1_SelectionChanged(object sender, EventArgs e)
        {
            DateTime T1 = Calendar1.SelectedDate;
            if (T1.Day%2==0)
                AdRotator1.AdvertisementFile = "Dell.xml";
            else
                AdRotator1.AdvertisementFile = "Lenovo.xml";
        }
    }
}
