from prova_utfpr import PACKAGE_NAME


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if prova_utfpr is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that IProvaUtfprLayer is registered."""
        from prova_utfpr.interfaces import IProvaUtfprLayer

        assert IProvaUtfprLayer in browser_layers

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "20240331001"
