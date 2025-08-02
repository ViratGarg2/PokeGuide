import streamlit as st
from utils.database import (list_rival_trainers, add_rival_trainer, 
                           delete_rival_trainer, delete_rival_trainer_by_number)

def run_rivals_page():
    st.title("👥 Rival Trainers")
    
    # Tabs for different rival operations
    tab1, tab2 = st.tabs(["View Rivals", "Edit Rivals"])
    
    with tab1:
        st.header("📋 List of Rival Trainers")
        
        if st.button("🔄 Load All Rivals", use_container_width=True):
            try:
                rivals = list_rival_trainers()
                if rivals:
                    st.dataframe(rivals, use_container_width=True)
                    st.info(f"📊 Total rivals: {len(rivals)}")
                else:
                    st.info("📋 No rival trainers found in database")
            except Exception as e:
                st.error(f"❌ Error loading rivals: {str(e)}")
    
    with tab2:
        st.header("✏️ Edit Rival Trainers")
        
        # Add or Delete selection
        action = st.selectbox("Choose Action", ["Add Rival Trainer", "Delete Rival Trainer"])
        
        if action == "Add Rival Trainer":
            st.subheader("➕ Add New Rival Trainer")
            
            col1, col2 = st.columns(2)
            with col1:
                trainer_no = st.number_input("Trainer Number", min_value=1, step=1)
            with col2:
                trainer_name = st.text_input("Trainer Name")
            
            if st.button("➕ Add Trainer", use_container_width=True):
                if trainer_no and trainer_name:
                    try:
                        add_rival_trainer(trainer_no, trainer_name)
                        st.success(f"✅ Successfully added Trainer '{trainer_name}' with ID {trainer_no}")
                    except Exception as e:
                        st.error(f"❌ Error adding trainer: {str(e)}")
                else:
                    st.warning("⚠️ Please fill in both trainer number and name")
        
        else:  # Delete Rival Trainer
            st.subheader("🗑️ Delete Rival Trainer")
            
            delete_method = st.selectbox("Delete by", ["Trainer Name", "Trainer Number"])
            
            if delete_method == "Trainer Name":
                # Load current rivals for selection
                try:
                    rivals = list_rival_trainers()
                    if rivals:
                        trainer_names = [rival['Name'] for rival in rivals]
                        selected_trainer = st.selectbox("Select Trainer to Delete", trainer_names)
                        
                        if st.button("🗑️ Delete Trainer", use_container_width=True):
                            try:
                                delete_rival_trainer(selected_trainer)
                                st.success(f"✅ Successfully deleted trainer '{selected_trainer}'")
                            except Exception as e:
                                st.error(f"❌ Error deleting trainer: {str(e)}")
                    else:
                        st.info("📋 No trainers available to delete")
                except Exception as e:
                    st.error(f"❌ Error loading trainers: {str(e)}")
            
            else:  # Delete by Trainer Number
                trainer_no = st.number_input("Enter Trainer Number to Delete", min_value=1, step=1)
                
                if st.button("🗑️ Delete Trainer", use_container_width=True):
                    try:
                        if delete_rival_trainer_by_number(trainer_no):
                            st.success(f"✅ Successfully deleted trainer with ID {trainer_no}")
                        else:
                            st.warning(f"⚠️ No trainer found with ID {trainer_no}")
                    except Exception as e:
                        st.error(f"❌ Error deleting trainer: {str(e)}")

if __name__ == "__main__":
    run_rivals_page()