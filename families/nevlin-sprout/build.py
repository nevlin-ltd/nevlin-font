"""Compatibility entry point; authoritative generator is in sources/."""
import runpy
if __name__ == "__main__":
    runpy.run_module("sources.build_font", run_name="__main__")
