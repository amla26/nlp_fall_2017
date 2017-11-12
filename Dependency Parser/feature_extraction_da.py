# config {buffer,stack,label}
def get_features_da(config,sent_dict):
    features = []
    # TODO Add Features

    if len(config[0]) > 0:
        # Top of stack.
        top = config[0][-1]


        # postag
        top_stk_token_feature = 'TOP_STK_POSTAG_'+str(sent_dict['POSTAG'][top].lower())
        features.append(top_stk_token_feature)


    #TOP - 1 OF STACK POSTAG

    if len(config[0]) > 1:
        # Top of stack - 1
        top = config[0][-2]

        # postag
        top_stk_token_feature = 'TOP_STK_2_POSTAG_'+str(sent_dict['POSTAG'][top].lower())
        features.append(top_stk_token_feature)


    #TOP - 2 OF STACK POSTAG

    if len(config[0]) > 2:
        # Top of stack - 1
        top = config[0][-3]

        # postag
        top_stk_token_feature = 'TOP_STK_3_POSTAG_'+str(sent_dict['POSTAG'][top].lower())
        features.append(top_stk_token_feature)
        

   #TOP OF BUFFER POSTAG
    if len(config[1]) > 0:
        # Top of buffer.
        top = config[1][-1]


        # POSTAG
        top_stk_token_feature = 'TOP_BUF_POSTAG_'+str(sent_dict['POSTAG'][top].lower())
        features.append(top_stk_token_feature)

    #TOP - 1 OF BUFFER POSTAG

    if len(config[1]) > 1:
        # Top of buffer - 1
        top = config[1][-2]


        # POSTAG
        top_stk_token_feature = 'TOP_BUF_2_POSTAG_'+str(sent_dict['POSTAG'][top].lower())
        features.append(top_stk_token_feature)

    #TOP - 2 OF BUFFER POSTAG

    if len(config[1]) > 2:
        # Top of buffer - 1
        top = config[1][-3]


        # POSTAG
        top_stk_token_feature = 'TOP_BUF_3_POSTAG_'+str(sent_dict['POSTAG'][top].lower())
        features.append(top_stk_token_feature)

    return features

    
    
