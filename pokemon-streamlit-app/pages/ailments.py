import streamlit as st
from utils.database import read_ailments, check_cures_for_ailments

def run_ailments_page():
    st.title("🩹 Ailments & Cures")
    
    # Tabs for different ailment operations
    tab1, tab2 = st.tabs(["View All Ailments", "Find Cures"])
    
    with tab1:
        st.header("📋 All Ailments and Their Cures")
        
        if st.button("🔄 Load All Ailments", use_container_width=True):
            try:
                ailments = read_ailments()
                if ailments:
                    st.dataframe(ailments, use_container_width=True)
                    st.info(f"📊 Total ailments found: {len(ailments)}")
                else:
                    st.info("📋 No ailments found in database")
            except Exception as e:
                st.error(f"❌ Error loading ailments: {str(e)}")
    
    with tab2:
        st.header("🔍 Find Cures for Specific Ailments")
        
        ailment_name = st.text_input("Enter ailment name (e.g., poison, burn, paralysis):")
        
        if st.button("🔍 Find Cures", use_container_width=True):
            if ailment_name:
                try:
                    cures = check_cures_for_ailments(ailment_name)
                    if cures:
                        st.subheader(f"💊 Cures for {ailment_name.title()}")
                        st.dataframe(cures, use_container_width=True)
                        
                        # Show summary
                        berries = [cure for cure in cures if cure.get('Location')]
                        items = [cure for cure in cures if cure.get('Cost') is not None]
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Berry Cures", len(berries))
                        with col2:
                            st.metric("Item Cures", len(items))
                            
                    else:
                        st.info(f"📋 No cures found for ailment: {ailment_name}")
                except Exception as e:
                    st.error(f"❌ Error searching cures: {str(e)}")
            else:
                st.warning("⚠️ Please enter an ailment name")
        
        # Common ailments quick buttons
        st.subheader("🚀 Quick Search - Common Ailments")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔥 Burn", use_container_width=True):
                st.session_state.ailment_search = "burn"
        with col2:
            if st.button("⚡ Paralysis", use_container_width=True):
                st.session_state.ailment_search = "paralysis"
        with col3:
            if st.button("🟢 Poison", use_container_width=True):
                st.session_state.ailment_search = "poison"
        
        # Handle quick search
        if hasattr(st.session_state, 'ailment_search'):
            try:
                cures = check_cures_for_ailments(st.session_state.ailment_search)
                if cures:
                    st.subheader(f"💊 Cures for {st.session_state.ailment_search.title()}")
                    st.dataframe(cures, use_container_width=True)
                else:
                    st.info(f"📋 No cures found for: {st.session_state.ailment_search}")
                # Clear the search after displaying
                del st.session_state.ailment_search
            except Exception as e:
                st.error(f"❌ Error in quick search: {str(e)}")

if __name__ == "__main__":
    run_ailments_page()