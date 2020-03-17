using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace XamarinForms
{
    public partial class GridPage : ContentPage
    {
        public GridPage()
        {
            InitializeComponent();
        }

        // SetContent recreates the xaml page in code-behind
        private void SetContent()
        {
            Content = GridPageXaml();
        }

        private Grid GridPageXaml()
        {
            var grid = new Grid
            {
                RowSpacing = 20,
                ColumnSpacing = 40,
                BackgroundColor = Color.Yellow
            };

            SetGridRowDefinitions(grid);
            SetGridColumnDefinitions(grid);
            SetGridLabels(grid);
            
            return grid;
        }

        private void SetGridRowDefinitions(Grid grid)
        {
            var rowDef1 = new RowDefinition
            {
                Height = new GridLength(100, GridUnitType.Absolute)
            };

            var rowDef2 = new RowDefinition
            {
                Height = new GridLength(2, GridUnitType.Star)
            };

            var rowDef3 = new RowDefinition
            {
                Height = new GridLength(1, GridUnitType.Star)
            };

            grid.RowDefinitions.Add(rowDef1);
            grid.RowDefinitions.Add(rowDef2);
            grid.RowDefinitions.Add(rowDef3);
        }

        private void SetGridColumnDefinitions(Grid grid)
        {
            var colDef1 = new ColumnDefinition
            {
                Width = new GridLength(1, GridUnitType.Auto)
            };

            var colDef2 = new ColumnDefinition
            {
                Width = new GridLength(2, GridUnitType.Star)
            };

            var colDef3 = new ColumnDefinition
            {
                Width = new GridLength(1, GridUnitType.Star)
            };


            grid.ColumnDefinitions.Add(colDef1);
            grid.ColumnDefinitions.Add(colDef2);
            grid.ColumnDefinitions.Add(colDef3);
        }

        private void SetGridLabels(Grid grid)
        {
            var label1 = new Label
            {
                BackgroundColor = Color.Silver,
                Text = "Label 1"
            };

            var label2 = new Label
            {
                BackgroundColor = Color.Silver,
                Text = "Label 2"
            };

            var label3 = new Label
            {
                BackgroundColor = Color.Silver,
                Text = "Label 3"
            };

            var label4 = new Label
            {
                BackgroundColor = Color.Silver,
                Text = "Label 4"
            };

            var label5 = new Label
            {
                BackgroundColor = Color.Red,
                Text = "Label 5"
            };

            var label6 = new Label
            {
                BackgroundColor = Color.Blue,
                Text = "Label 6"
            };

            grid.Children.Add(label1, 0, 0);
            grid.Children.Add(label2, 1, 0);
            grid.Children.Add(label3, 0, 1);
            grid.Children.Add(label4, 1, 1);
            grid.Children.Add(label5, 0, 2);
            Grid.SetColumnSpan(label5, 3);
            grid.Children.Add(label6, 2, 0);
            Grid.SetRowSpan(label6, 3);
        }
    }
}
