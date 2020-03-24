using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace XamarinForms
{
    public partial class StackLayoutSample2 : ContentPage
    {
        public StackLayoutSample2()
        {
            InitializeComponent();
            SetContent();
        }

        private void SetContent()
        {
            var layout = StackLayoutExercise1Xaml();
            Content = layout;
            Content.BackgroundColor = Color.FromHex("#127ac7");
        }

        private StackLayout StackLayoutExercise1Xaml()
        {
            var layout = new StackLayout
            {
                VerticalOptions = LayoutOptions.Center,
                Spacing = 20
            };

            var label1 = new Label
            {
                HorizontalOptions = LayoutOptions.Center,
                FontSize = 30,
                FontAttributes = FontAttributes.Bold,
                TextColor = Color.White,
                Text = "Welcome to Xamarin"
            };

            var label2 = new Label
            {
                HorizontalOptions = LayoutOptions.Center,
                FontSize = 18,
                TextColor = Color.White,
                Text = "Cross-platform apps made easy"
            };

            var button1 = new Button
            {
                BackgroundColor = Color.FromHex("#1dabf0"),
                TextColor = Color.White,
                Text = "Login"
            };

            var button2 = new Button
            {
                BackgroundColor = Color.FromHex("#1dabf0"),
                TextColor = Color.White,
                Text = "Register"
            };

            layout.Children.Add(label1);
            layout.Children.Add(label2);
            layout.Children.Add(button1);
            layout.Children.Add(button2);

            return layout;
        }
    }
}
