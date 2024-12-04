<%@ Page Title="Contact" Language="VB" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Contact.aspx.vb" Inherits="WEBTEST.Contact" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title"><%: Title %></h2>
        <h3>Lisa uus opilane</h3>
        <p>Toolbox-->Data-->DetailsVieww</p>
    <p>
        <asp:DetailsView ID="DetailsView1" runat="server" AutoGenerateRows="False" DataKeyNames="opilaneID" DataSourceID="SqlDataSource1" Height="50px" Width="125px">
            <Fields>
                <asp:BoundField DataField="opilaneID" HeaderText="opilaneID" InsertVisible="False" ReadOnly="True" SortExpression="opilaneID" />
                <asp:BoundField DataField="opilaneNimi" HeaderText="opilaneNimi" SortExpression="opilaneNimi" />
                <asp:BoundField DataField="opilanePerenimi" HeaderText="opilanePerenimi" SortExpression="opilanePerenimi" />
                <asp:BoundField DataField="sunniaeg" HeaderText="sunniaeg" SortExpression="sunniaeg" />
                <asp:BoundField DataField="aadres" HeaderText="aadres" SortExpression="aadres" />
                <asp:CommandField ShowInsertButton="True" />
            </Fields>
        </asp:DetailsView>
        <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:opilasedConnectionString %>" DeleteCommand="DELETE FROM [opilaneTabel] WHERE [opilaneID] = @opilaneID" InsertCommand="INSERT INTO [opilaneTabel] ([opilaneNimi], [opilanePerenimi], [sunniaeg], [aadres]) VALUES (@opilaneNimi, @opilanePerenimi, @sunniaeg, @aadres)" SelectCommand="SELECT * FROM [opilaneTabel]" UpdateCommand="UPDATE [opilaneTabel] SET [opilaneNimi] = @opilaneNimi, [opilanePerenimi] = @opilanePerenimi, [sunniaeg] = @sunniaeg, [aadres] = @aadres WHERE [opilaneID] = @opilaneID">
            <DeleteParameters>
                <asp:Parameter Name="opilaneID" Type="Int32" />
            </DeleteParameters>
            <InsertParameters>
                <asp:Parameter Name="opilaneNimi" Type="String" />
                <asp:Parameter Name="opilanePerenimi" Type="String" />
                <asp:Parameter DbType="Date" Name="sunniaeg" />
                <asp:Parameter Name="aadres" Type="String" />
            </InsertParameters>
            <UpdateParameters>
                <asp:Parameter Name="opilaneNimi" Type="String" />
                <asp:Parameter Name="opilanePerenimi" Type="String" />
                <asp:Parameter DbType="Date" Name="sunniaeg" />
                <asp:Parameter Name="aadres" Type="String" />
                <asp:Parameter Name="opilaneID" Type="Int32" />
            </UpdateParameters>
        </asp:SqlDataSource>
    </p>
    </main>
</asp:Content>
