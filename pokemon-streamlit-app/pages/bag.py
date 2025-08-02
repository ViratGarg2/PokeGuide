import streamlit as st
from utils.database import view_items_in_bag

def run_bag_page():
    st.title("🎒 Bag Management")
    
    st.header("👜 View Items in Bag")
    
    # Item type selection
    item_type = st.selectbox("Select Item Type", ["pokeballs", "berries", "normal items"])
    
    if st.button(f"🔍 View {item_type.title()}", use_container_width=True):
        try:
            items = view_items_in_bag(item_type)
            if items:
                st.subheader(f"📦 {item_type.title()} in Bag")
                
                # Display with proper headers based on item type
                if item_type == "pokeballs":
                    st.write("**Pokéballs Collection:**")
                    # Rename columns for better display
                    headers = ["Ball Type", "Cost", "Quantity", "Catch Rate"]
                elif item_type == "berries":
                    st.write("**Berries Collection:**")
                    headers = ["Berry Name", "Effect", "Found At", "Quantity"]
                else:
                    st.write("**Normal Items Collection:**")
                    headers = ["Item Name", "Effect", "Cost", "Quantity"]
                
                st.dataframe(items, use_container_width=True)
                
                # Show total count
                if items:
                    total_items = sum(item.get('Count', 0) for item in items)
                    st.metric(f"Total {item_type.title()}", total_items)
                    
            else:
                st.info(f"📋 No {item_type} found in your bag")
        except Exception as e:
            st.error(f"❌ Error loading {item_type}: {str(e)}")
    
    # Display all items summary
    if st.button("🔄 Show All Items Summary", use_container_width=True):
        try:
            st.subheader("📊 Complete Bag Summary")
            
            # Get all item types
            for item_type in ["pokeballs", "berries", "normal items"]:
                try:
                    items = view_items_in_bag(item_type)
                    if items:
                        total_count = sum(item.get('Count', 0) for item in items)
                        st.write(f"**{item_type.title()}:** {len(items)} types, {total_count} total items")
                    else:
                        st.write(f"**{item_type.title()}:** No items")
                except:
                    st.write(f"**{item_type.title()}:** Error loading data")
                    
        except Exception as e:
            st.error(f"❌ Error loading bag summary: {str(e)}")

if __name__ == "__main__":
    run_bag_page()