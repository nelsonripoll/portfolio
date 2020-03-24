using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace XamarinForms
{
    public partial class AbsoluteLayoutSample1 : ContentPage
    {
        public AbsolutePage()
        {
            InitializeComponent();
        }

        private void UpdateContent()
        {
            Content = AbsolutePageXaml();
        }

        private AbsoluteLayout AbsolutePageXaml()
        {
            var layout = new AbsoluteLayout();

            var boxview1 = new BoxView
            {
                Color = Color.Aqua
            };

            var boxview2 = new BoxView
            {
                Color = Color.White
            };

            var button = new Button
            {
                BackgroundColor = Color.Silver,
                TextColor = Color.White,
                Text = "Get Started"
            };

            layout.Children.Add(boxview1);
            AbsoluteLayout.SetLayoutBounds(boxview1, new Rectangle(0, 0, 1, 1));
            AbsoluteLayout.SetLayoutFlags(boxview1, AbsoluteLayoutFlags.All);

            layout.Children.Add(boxview2);
            AbsoluteLayout.SetLayoutBounds(boxview2, new Rectangle(0.5, 0.1, 100, 100));
            AbsoluteLayout.SetLayoutFlags(boxview2, AbsoluteLayoutFlags.PositionProportional);

            layout.Children.Add(button);
            AbsoluteLayout.SetLayoutBounds(button, new Rectangle(0, 1, 1, 50));
            AbsoluteLayout.SetLayoutFlags(button, AbsoluteLayoutFlags.PositionProportional | AbsoluteLayoutFlags.WidthProportional);

            return layout;
        }
    }
}
