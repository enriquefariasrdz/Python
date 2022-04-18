chainmap.py
#!/usr/bin/env python

# coding: utf-8

# %%
import builtins
#pylookup = ChainMap(locals(),globals(), vars(builtins))

# %%
baseline = {'music': 'bach', 'art': 'rembrandt'}
# %%
adjustments = {'art': 'van gogh', 'opera':'carmen'}
# %%
list((adjustments, baseline))
# %%
baseline
# %%
adjustments
# %%




# %%


# %%
