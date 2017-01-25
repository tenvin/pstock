# -*- coding: utf-8 -*-

import tushare as ts
ts.set_token('4a9ddb49be2e12af5be42c1162504dc5a6c84cfe33b232313772256b7cf23dc6')

fd = ts.Subject()
df = fd.ThemesPeriod(isLatest=1)
print df

