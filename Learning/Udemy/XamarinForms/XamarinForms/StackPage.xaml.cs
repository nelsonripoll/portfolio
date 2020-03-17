using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace XamarinForms
{
    public partial class StackPage : ContentPage
    {
        public StackPage()
        {
            InitializeComponent();
        }

        // SetContent recreates the xaml page in code-behind
        private void SetContent()
        {
            Content = StackPageXaml();
        }

        private StackLayout StackPageXaml()
        {
            var layout = new StackLayout
            {
                Spacing = 40,
                Padding = new Thickness(20),
                Orientation = StackOrientation.Horizontal,
                VerticalOptions = LayoutOptions.Center,
                HorizontalOptions = LayoutOptions.Center,
                BackgroundColor = Color.Black
            };

            var image1 = new Image
            {
                Source = "http://placehold.it/100x100"
            };

            var label1 = new Label
            {
                Text = "Label 1",
                BackgroundColor = Color.Red
            };

            var innerLayout = new StackLayout { };

            innerLayout.Children.Add(image1);
            innerLayout.Children.Add(label1);

            var label2 = new Label
            {
                Text = "Label 2",
                BackgroundColor = Color.White
            };

            var label3 = new Label
            {
                Text = "Label 3",
                BackgroundColor = Color.Blue
            };

            layout.Children.Add(innerLayout);
            layout.Children.Add(label2);
            layout.Children.Add(label3);

            return layout;
        }
    }
}
