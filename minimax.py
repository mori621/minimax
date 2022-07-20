from game import State, random_action

max_search_level = 4

def evaluate(state):
    legal_actions = state.legal_actions()
    if legal_actions == [64]:
        num_action = 0
    else:
        num_action = len(legal_actions)

    reverse_state = State(state.enemy_pieces, state.pieces)
    enemy_legal_actions = reverse_state.legal_actions()
    if enemy_legal_actions == [64]:
        enemy_num_action = 0
    else:
        enemy_num_action = len(enemy_legal_actions)

    # return num_action / 64
    return num_action - enemy_num_action

# アルファベータ法で状態価値計算
def alpha_beta(state, alpha, beta, search_level):
    # # 負けは状態価値-1
    # if state.is_lose():
    #     return -1
    
    # # 引き分けは状態価値0
    # if state.is_draw():
    #     return  0

    if search_level == max_search_level:
        return evaluate(state)
    next_search_level = search_level+1
    # 合法手の状態価値の計算    
    for action in state.legal_actions():
        
        score = -alpha_beta(state.next(action), -beta, -alpha, next_search_level)
        if score > alpha:
            alpha = score

        # 現ノードのベストスコアが親ノードを超えたら探索終了
        if alpha >= beta:
            return alpha

    # 合法手の状態価値の最大値を返す        
    return alpha

# アルファベータ法で行動選択
def alpha_beta_action(state):
    # 合法手の状態価値の計算
    best_action = 0
    alpha = -float('inf')
    for action in state.legal_actions():
        score = -alpha_beta(state.next(action), -float('inf'), -alpha, 0)
        if score > alpha:
            best_action = action
            alpha = score

    # 合法手の状態価値の最大値を持つ行動を返す
    return best_action

if __name__ == '__main__':
    # 状態の生成
    state = State()

    print(state)

    # ゲーム終了までのループ
    while True:
        # ゲーム終了時
        if state.is_done():
            break

        if state.is_first_player():
            action = alpha_beta_action(state)
        else:
            action = random_action(state)

        # 次の状態の取得
        state = state.next(action)

        # 文字列表示
        print(state)
        print()