#!/usr/bin/env python3
"""
Test script for enhanced PennyFlow system with synthetic identities
"""

import sys
import os

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from automation_engine.ai.identity_factory import SyntheticIdentityFactory
from automation_engine.core.hardware_spoofer import HardwareSpoofer

def test_identity_generation():
    """Test synthetic identity creation"""
    print("🧪 Testing Synthetic Identity Generation...")
    
    factory = SyntheticIdentityFactory()
    identity = factory.create_advanced_identity(age_group="young_adult", location="US")
    
    print(f"✅ Identity Created: {identity['id']}")
    print(f"📊 Demographics: {identity['demographics']}")
    print(f"🌐 Digital Footprint: {len(identity['digital_footprint']['browsing_history'])} browsing sessions")
    print(f"⚙️ Technical Profile: {identity['technical_profile']['timezone']}")
    
    return identity

def test_hardware_spoofing():
    """Test hardware profile loading"""
    print("\n🧪 Testing Hardware Spoofing...")
    
    spoofer = HardwareSpoofer()
    profile = spoofer.load_hardware_profile("gaming_pc")
    
    print(f"✅ Hardware Profile Loaded: {profile['name']}")
    print(f"🎮 GPU: {profile['gpu']['renderer']}")
    print(f"⚡ CPU: {profile['cpu']['cores']} cores")
    
    return profile

def test_integration():
    """Test full integration"""
    print("\n🧪 Testing Full Integration...")
    
    from automation_engine.core.bot_engine import PhantomBot
    from automation_engine.proxies.proxy_rotator import ProxyRotator
    from automation_engine.utils.user_agent_rotator import get_random_user_agent
    
    # Create identity
    factory = SyntheticIdentityFactory()
    identity = factory.create_advanced_identity()
    
    # Launch bot with identity
    proxy_rotator = ProxyRotator(use_tor=True)
    proxy = proxy_rotator.get_random_proxy()
    user_agent = get_random_user_agent()
    
    bot = PhantomBot(proxy=proxy, user_agent=user_agent, use_advanced_stealth=True)
    bot.identity = identity  # Inject identity
    
    print("🚀 Launching enhanced bot with synthetic identity...")
    
    try:
        driver = bot.launch_browser()
        print("✅ Enhanced system operational!")
        
        # Test basic navigation
        driver.get("https://httpbin.org/ip")
        print(f"📄 Page title: {driver.title}")
        
        bot.quit()
        return True
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        return False

if __name__ == "__main__":
    print("🔥 PENNYFLOW ENHANCED SYSTEM TEST 🔥")
    print("=" * 50)
    
    # Run tests
    test_identity_generation()
    test_hardware_spoofing()
    success = test_integration()
    
    if success:
        print("\n🎉 ALL TESTS PASSED! Enhanced system is ready.")
    else:
        print("\n⚠️ Some tests failed. Check the implementation.")