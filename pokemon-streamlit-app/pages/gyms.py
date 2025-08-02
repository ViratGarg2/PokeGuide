import streamlit as st
from utils.database import view_gyms

def run_gyms_page():
    st.title("🏟️ Pokémon Gyms")
    
    st.header("🏛️ Gym Information")
    
    if st.button("🔄 Load All Gyms", use_container_width=True):
        try:
            gyms = view_gyms()
            if gyms:
                st.dataframe(gyms, use_container_width=True)
                
                # Show gym statistics
                total_gyms = len(gyms)
                badges_won = sum(1 for gym in gyms if gym.get('Badge_Won', False))
                
                st.subheader("📊 Gym Progress")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Total Gyms", total_gyms)
                with col2:
                    st.metric("Badges Won", badges_won)
                with col3:
                    progress = (badges_won / total_gyms) * 100 if total_gyms > 0 else 0
                    st.metric("Progress", f"{progress:.1f}%")
                
                # Progress bar
                st.progress(badges_won / total_gyms if total_gyms > 0 else 0)
                
                # Show gym details
                st.subheader("🏆 Gym Details")
                for gym in gyms:
                    with st.expander(f"🏟️ {gym.get('Location', 'Unknown')} Gym"):
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.write(f"**Gym Leader:** {gym.get('Gym_Leader', 'Unknown')}")
                            st.write(f"**Gym Type:** {gym.get('Gym_Type', 'Unknown')}")
                            st.write(f"**Gym Badge:** {gym.get('Gym_Badge', 'Unknown')}")
                        
                        with col2:
                            badge_status = "🏆 Won" if gym.get('Badge_Won', False) else "❌ Not Won"
                            st.write(f"**Badge Status:** {badge_status}")
                            if gym.get('Previous_Gym'):
                                st.write(f"**Previous Gym:** {gym.get('Previous_Gym')}")
                            if gym.get('Next_Gym'):
                                st.write(f"**Next Gym:** {gym.get('Next_Gym')}")
                
            else:
                st.info("📋 No gym data found in database")
        except Exception as e:
            st.error(f"❌ Error loading gym data: {str(e)}")

if __name__ == "__main__":
    run_gyms_page()