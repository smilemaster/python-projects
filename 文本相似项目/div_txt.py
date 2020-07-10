import codecs

data = [['3', '20', '21', '25', '27', '30', '34', '38', '45', '64', '76', '77', '87', '90', '92', '95', '116', '118', '126', '127', '132', '138', '140', '142', '143', '147', '148', '153', '174', '178', '181', '182', '186', '188', '196', '203', '221', '223', '231', '250', '259', '265', '274', '278', '287']
,['33', '40', '135', '162', '167']
,['16', '48', '50', '54', '70', '120', '154', '159', '164', '183', '189', '267', '285', '286']
,['15', '31', '35', '41', '44', '52', '53', '55', '57', '62', '66', '68', '91', '96', '103', '117', '134', '163', '166', '168', '172', '175', '191', '200', '205', '206', '209', '211', '217', '219', '225', '226', '230', '247', '263']
,['18', '71', '72', '94', '97', '122', '124', '128', '150', '165', '201', '204', '215', '254']
,['8', '42', '60', '85', '160', '161', '169', '170', '180', '195', '222', '236', '245']
,['17', '51', '67', '81', '107', '109', '113', '185', '192', '197', '198', '208', '213']
,['9', '12', '23', '89', '93', '130', '258', '280', '281', '282', '283', '284']
,['1', '4', '26', '29', '32', '46', '49', '69', '80', '100', '101', '111', '112', '123', '125', '155', '158', '193', '202', '214', '227', '233', '239', '244', '249', '253', '255', '256', '257', '260', '262', '266', '271', '273', '288', '289', '290']
,['13', '19', '61', '65', '99', '104', '105', '106', '119', '133', '144', '152', '157', '216', '220', '240', '243', '248', '252', '261', '264']
]

for i in range(8):
    content = ""
    for j in data[i]:
        try:
            fp = codecs.open('user_txt/{}.txt'.format(j), "r", encoding='utf8', errors='ignore')
            content = content+fp.read()
        except FileNotFoundError:
            continue

    fp = open('{}.txt'.format(i), 'w', encoding='utf8', errors='ignore')
    fp.write(content)
    fp.close()

