import streamlit as st
from app_home import run_home
from app_eda import run_eda

def main():
    st.title('리뷰 긍정 부정 예측 앱')
    menu = ['Home','EDA','ML']
    choice =st.sidebar.selectbox('메뉴 선택', menu)
    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[3] :
        pass





if __name__ == '__main__' :
    main()

    ## 파이썬 가상환경을 확인한다.
    ## 이 앱은 구글 코랩에서 만든 아보카도 가격 예측 환경과 동일하게 하기위해서
    ## 파이썬 가상환경을 streamlit3.7로 바꿔준다.
    ## vs code 맨 오른쪽아래 있는 base를 streamlit 3.7로 바꿔준다.
    