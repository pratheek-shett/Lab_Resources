<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Home.aspx.cs" Inherits="PGR2.Home" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
    <head id="Head1" runat="server">
        <title></title>
        <style type="text/css">
            #form1
            {
                text-align: center;
            }
        </style>
    </head>
    <body>
        <form id="form1" runat="server">
        HOTEL<asp:Panel ID="Panel1" runat="server">
        <asp:RadioButtonList ID="RadioButtonList1" runat="server"
            RepeatDirection="Horizontal">
            <asp:ListItem>Morning</asp:ListItem>
            <asp:ListItem>Afternoon</asp:ListItem>
            <asp:ListItem>Evening</asp:ListItem>
            <asp:ListItem>Night</asp:ListItem>
        </asp:RadioButtonList>
        </asp:Panel>
        <asp:Panel ID="Panel2" runat="server">
        <asp:CheckBoxList ID="CheckBoxList1" runat="server"
        style="text-align: left" Height="28px" Width="176px">
            <asp:ListItem Value="20">Idly</asp:ListItem>
            <asp:ListItem Value="25">Dosa</asp:ListItem>
            <asp:ListItem Value="35">Pulav</asp:ListItem>
            <asp:ListItem Value="40">Puliyogare</asp:ListItem>
            <asp:ListItem Value="50">Biriyani</asp:ListItem>
        </asp:CheckBoxList>
        <br />
        </asp:Panel>
        <asp:CheckBoxList ID="CheckBoxList2" runat="server" style="text-align: left">
            <asp:ListItem Value="40">Veg Thali</asp:ListItem>
            <asp:ListItem Value="50">Non veg thali</asp:ListItem>
            <asp:ListItem Value="35">Paratha</asp:ListItem>
            <asp:ListItem Value="30">Curd Rice</asp:ListItem>
            <asp:ListItem Value="30">Chapathi</asp:ListItem>
        </asp:CheckBoxList>
        <br />
        <asp:CheckBoxList ID="CheckBoxList3" runat="server" style="text-align: left"
        Height="107px" Width="210px">
            <asp:ListItem Value="25">Paani Puri</asp:ListItem>
            <asp:ListItem Value="40">VadaPav</asp:ListItem>
            <asp:ListItem Value="20">Gobi Manchurian</asp:ListItem>
            <asp:ListItem Value="30">Masal Puri</asp:ListItem>
            <asp:ListItem Value="30">Sev Puri</asp:ListItem>
        </asp:CheckBoxList>
        <br />
        <asp:CheckBoxList ID="CheckBoxList4" runat="server" style="text-align: left"
        Height="59px" Width="148px">
            <asp:ListItem Value="50">Biriyani</asp:ListItem>
            <asp:ListItem Value="40">Poori</asp:ListItem>
            <asp:ListItem Value="30">Ice cream</asp:ListItem>
            <asp:ListItem Value="40">Fish fry</asp:ListItem>
            <asp:ListItem Value="60">Chicken </asp:ListItem>
        </asp:CheckBoxList>
        <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="Bill"
        Width="80px" />
        <p>
            <asp:Label ID="Label1" runat="server"></asp:Label>
        </p>
        </form>
    </body>
</html>
