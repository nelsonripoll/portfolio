using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace XamarinForms
{
    public partial class QuotesPage : ContentPage
    {
        string[] quotes = {
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "Curabitur placerat, tellus vitae malesuada convallis, nibh dui commodo nulla, sed posuere ante est sit amet felis.",
            "Proin felis enim, suscipit in placerat eu, semper non turpis. Donec interdum iaculis ante, nec mattis ex mollis nec.",
            "Nulla porttitor congue laoreet.",
            "Mauris luctus mauris semper tellus sodales suscipit.",
            "Sed a orci massa.",
            "Etiam scelerisque viverra nulla, sed blandit nibh interdum id.",
            "Sed viverra orci eu ante gravida tincidunt. Pellentesque vestibulum id felis eget facilisis."
        };

        int counter = 0;

        public QuotesPage()
        {
            InitializeComponent();
            // padding is set in the xaml, this is just an example of how to do it in the code-behind
            // UpdatePadding();
            quote.FontSize = font_slider.Value;
            quote.Text = quotes[counter];
        }

        private void UpdatePadding()
        {
            switch (Device.RuntimePlatform)
            {
                case Device.iOS:
                    this.Padding = new Thickness(20, 40, 20, 20);
                    break;
                case Device.Android:
                    this.Padding = new Thickness(20, 30, 20, 20);
                    break;
                default:
                    this.Padding = new Thickness(20);
                    break;
            };
        }

        void NextButtonClicked(System.Object sender, System.EventArgs e)
        {
            if (++counter == quotes.Length) counter = 0;
            quote.Text = quotes[counter];
        }

        void FontValueChanged(System.Object sender, Xamarin.Forms.ValueChangedEventArgs e)
        {
            quote.FontSize = e.NewValue;
        }

    }
}
