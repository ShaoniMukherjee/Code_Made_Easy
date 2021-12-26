{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19aec69b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def reduce_memory(df):\n",
    "    \n",
    "    \"\"\"\n",
    "    This function reduce the dataframe memory usage by converting it's type for easier handling.\n",
    "    \n",
    "    Parameters: Dataframe\n",
    "    Return: Dataframe\n",
    "    \"\"\"\n",
    "    \n",
    "    start_mem_usg = df.memory_usage().sum() / 1024**2 \n",
    "    print(\"Memory usage of properties dataframe is :\",start_mem_usg,\" MB\")\n",
    "    \n",
    "    for col in df.columns:\n",
    "        if df[col].dtypes in [\"int64\", \"int32\", \"int16\"]:\n",
    "            \n",
    "            cmin = df[col].min()\n",
    "            cmax = df[col].max()\n",
    "            \n",
    "            if cmin > np.iinfo(np.int8).min and cmax < np.iinfo(np.int8).max:\n",
    "                df[col] = df[col].astype(np.int8)\n",
    "            \n",
    "            elif cmin > np.iinfo(np.int16).min and cmax < np.iinfo(np.int16).max:\n",
    "                df[col] = df[col].astype(np.int16)\n",
    "            \n",
    "            elif cmin > np.iinfo(np.int32).min and cmax < np.iinfo(np.int32).max:\n",
    "                df[col] = df[col].astype(np.int32)\n",
    "        \n",
    "        if df[col].dtypes in [\"float64\", \"float32\"]:\n",
    "            \n",
    "            cmin = df[col].min()\n",
    "            cmax = df[col].max()\n",
    "            \n",
    "            if cmin > np.finfo(np.float16).min and cmax < np.finfo(np.float16).max:\n",
    "                df[col] = df[col].astype(np.float16)\n",
    "            \n",
    "            elif cmin > np.finfo(np.float32).min and cmax < np.finfo(np.float32).max:\n",
    "                df[col] = df[col].astype(np.float32)\n",
    "    \n",
    "    print(\"\")\n",
    "    print(\"___MEMORY USAGE AFTER COMPLETION:___\")\n",
    "    mem_usg = df.memory_usage().sum() / 1024**2 \n",
    "    print(\"Memory usage is: \",mem_usg,\" MB\")\n",
    "    print(\"This is \",100*mem_usg/start_mem_usg,\"% of the initial size\")\n",
    "    \n",
    "    return df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
