<%@ Page Title="About" Language="VB" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="About.aspx.vb" Inherits="WEBTEST.About" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title"><%: Title %>.</h2>
        <p>
            <asp:GridView ID="GridView1" runat="server" AutoGenerateColumns="False" DataKeyNames="opilaneID" DataSourceID="SqlDataSource1" EmptyDataText="Нет записей для отображения.">
                <Columns>
                    <asp:BoundField DataField="opilaneID" HeaderText="opilaneID" ReadOnly="True" SortExpression="opilaneID" Visible="False" />
                    <asp:BoundField DataField="opilaneNimi" HeaderText="opilaneNimi" SortExpression="opilaneNimi" />
                    <asp:BoundField DataField="opilanePerenimi" HeaderText="opilanePerenimi" SortExpression="opilanePerenimi" />
                    <asp:BoundField DataField="sunniaeg" HeaderText="sunniaeg" SortExpression="sunniaeg" DataFormatString="{0:d}" />
                    <asp:BoundField DataField="aadres" HeaderText="aadres" SortExpression="aadres" />
                    <asp:BoundField />
                </Columns>
            </asp:GridView>
            <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:opilasedConnectionString1 %>" DeleteCommand="DELETE FROM [opilaneTabel] WHERE [opilaneID] = @opilaneID" InsertCommand="INSERT INTO [opilaneTabel] ([opilaneNimi], [opilanePerenimi], [sunniaeg], [aadres]) VALUES (@opilaneNimi, @opilanePerenimi, @sunniaeg, @aadres)" ProviderName="<%$ ConnectionStrings:opilasedConnectionString1.ProviderName %>" SelectCommand="SELECT [opilaneID], [opilaneNimi], [opilanePerenimi], [sunniaeg], [aadres] FROM [opilaneTabel]" UpdateCommand="UPDATE [opilaneTabel] SET [opilaneNimi] = @opilaneNimi, [opilanePerenimi] = @opilanePerenimi, [sunniaeg] = @sunniaeg, [aadres] = @aadres WHERE [opilaneID] = @opilaneID">
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
