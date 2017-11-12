# config {stack,buffer,label}
def get_features(config,sent_dict):
    features = []

    # TODO Improve Features

    #TOP OF STACK FORM, LEMMA, POSTAG
    if len(config[0]) > 0:
        # Top of stack.
        top = config[0][-1]
        
        # Token form
        top_stk_token_feature = 'TOP_STK_FORM_'+str(sent_dict['FORM'][top].lower())
        features.append(top_stk_token_feature)

        # Lemma
        top_stk_token_feature = 'TOP_STK_LEMMA_'+str(sent_dict['LEMMA'][top].lower())
        features.append(top_stk_token_feature)

        # postag
        top_stk_token_feature = 'TOP_STK_POSTAG_'+str(sent_dict['POSTAG'][top].lower())
        features.append(top_stk_token_feature)


    #TOP - 1 OF STACK FORM, LEMMA, POSTAG

    if len(config[0]) > 1:
        # Top of stack - 1
        top = config[0][-2]
        
        # Token form
        top_stk_token_feature = 'TOP_STK_2_FORM_'+str(sent_dict['FORM'][top].lower())
        features.append(top_stk_token_feature)

        # Lemma
        top_stk_token_feature = 'TOP_STK_2_LEMMA_'+str(sent_dict['LEMMA'][top].lower())
        features.append(top_stk_token_feature)

        # POSTAG
        top_stk_token_feature = 'TOP_STK_2_POSTAG_'+str(sent_dict['POSTAG'][top].lower())
        features.append(top_stk_token_feature)


    #TOP - 2 OF STACK FORM, LEMMA, POSTAG

    if len(config[0]) > 2:
        # Top of stack - 2
        top = config[0][-3]
        
        # Token form
        top_stk_token_feature = 'TOP_STK_3_FORM_'+str(sent_dict['FORM'][top].lower())
        features.append(top_stk_token_feature)

        # Lemma
        top_stk_token_feature = 'TOP_STK_3_LEMMA_'+str(sent_dict['LEMMA'][top].lower())
        features.append(top_stk_token_feature)

        # POSTAG
        top_stk_token_feature = 'TOP_STK_3_POSTAG_'+str(sent_dict['POSTAG'][top].lower())
        features.append(top_stk_token_feature)

        



    #TOP OF BUFFER FORM, LEMMA, POSTAG
    if len(config[1]) > 0:
        # Top of buffer.
        top = config[1][-1]
        
        # Token form
        top_stk_token_feature = 'TOP_BUF_FORM_'+str(sent_dict['FORM'][top].lower())
        features.append(top_stk_token_feature)

        # Lemma
        top_stk_token_feature = 'TOP_BUF_LEMMA_'+str(sent_dict['LEMMA'][top].lower())
        features.append(top_stk_token_feature)

        # POSTAG
        top_stk_token_feature = 'TOP_BUF_POSTAG_'+str(sent_dict['POSTAG'][top].lower())
        features.append(top_stk_token_feature)


    #TOP - 1 OF BUFFER FORM, LEMMA, POSTAG

    if len(config[1]) > 1:
        # Top of buffer - 1
        top = config[1][-2]
        
        # Token form
        top_stk_token_feature = 'TOP_BUF_2_FORM_'+str(sent_dict['FORM'][top].lower())
        features.append(top_stk_token_feature)

        # Lemma
        top_stk_token_feature = 'TOP_BUF_2_LEMMA_'+str(sent_dict['LEMMA'][top].lower())
        features.append(top_stk_token_feature)

        # POSTAG
        top_stk_token_feature = 'TOP_BUF_2_POSTAG_'+str(sent_dict['POSTAG'][top].lower())
        features.append(top_stk_token_feature)


       #TOP - 2 OF BUFFER FORM, LEMMA, POSTAG

    if len(config[1]) > 2:
        # Top of buffer - 2
        top = config[1][-3]
        
        # Token form
        top_stk_token_feature = 'TOP_BUF_3_FORM_'+str(sent_dict['FORM'][top].lower())
        features.append(top_stk_token_feature)

        # Lemma
        top_stk_token_feature = 'TOP_BUF_3_LEMMA_'+str(sent_dict['LEMMA'][top].lower())
        features.append(top_stk_token_feature)

        # POSTAG
        top_stk_token_feature = 'TOP_BUF_3_POSTAG_'+str(sent_dict['POSTAG'][top].lower())
        features.append(top_stk_token_feature)



       
    return features
