import streamlit as st
import snowflake.connector as sc


def main():
    st.write("#### Dashboard d'ajout dans la table étudiants")

    try:
        con = sc.connect(
            account = 'xcsrvma-te06383',
            user='papayecisse',
            password='Snow1990@'
        )

        cursor = con.cursor()

        nom = st.text_input("Entrez le nom de l'etudiant")
        prenom = st.text_input("Entrez le prenom de l'etudiant")
        age = st.text_input("Entrez l'age de l'etudiant")

        if nom and prenom and age:
            btnAjouter = st.button("Ajouter l'etudiant")
            if btnAjouter:
                st.info("Nous sommes entrain de faire l'ajout ...")
                sql = f"INSERT INTO rcw.persons.etudiants VALUES('{nom}','{prenom}','{age}')"
                cursor.execute(sql)
                st.success("L'etudiant a été ajouté avec succès 😃")
        else:
            st.info("Tout les champs doivent être remplie avant de pouvoir ajouter cet etudiant")


    except:
        st.warning("Une erreur est surveneue")



if __name__ == "__main__":
    main()