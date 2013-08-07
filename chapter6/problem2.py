def flatten_dict(d, result={}, prv_keys=[]):
	for k, v in d.iteritems():
		if isinstance(v, dict):
			flatten_dict(v, result, prv_keys + [k])
		else:
			result['.'.join(prv_keys + [k])] = v
	return result
