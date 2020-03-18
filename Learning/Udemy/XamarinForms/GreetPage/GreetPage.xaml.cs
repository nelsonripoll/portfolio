using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace XamarinForms
{
    public partial class GreetPage : ContentPage
    {
        public GreetPage()
        {
            InitializeComponent();
            UpdateContent();
        }

        // UpdateContent recreates the xaml page in code-behind
        private void UpdateContent()
        {
            Content = new Label
            {
                HorizontalOptions = LayoutOptions.Center,
                VerticalOptions = LayoutOptions.Center,
                Text = "Hello, world!"
            };
        }
    }
}