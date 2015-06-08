/* radare - LGPL - Copyright 2007-2015 - ret2libc */

#include <r_util.h>

R_API RQueue *r_queue_new (int n) {
	RQueue *q = R_NEW0 (RQueue);
	q->elems = calloc (n, sizeof(void *));
	if (!q->elems)
		return NULL;

	q->front = 0;
	q->rear = -1;
	q->size = 0;
	q->capacity = n;
	return q;
}

R_API void r_queue_free (RQueue *q) {
	free (q->elems);
	free (q);
}

static int is_full (RQueue *q) {
	 return q->size == q->capacity;
}

static int increase_capacity (RQueue *q) {
	unsigned int new_capacity = q->capacity * 2;
	void **newelems;
	int i, tmp_front;

	newelems = calloc (new_capacity, sizeof(void *));
	if (!newelems)
		return R_FALSE;

	i = -1;
	tmp_front = q->front;
	while (i + 1 < q->size) {
		i++;
		newelems[i] = q->elems[tmp_front];
		tmp_front = (tmp_front + 1) % q->capacity;
	}

	free (q->elems);
	q->elems = newelems;
	q->front = 0;
	q->rear = i;
	q->capacity = new_capacity;
	return R_TRUE;
}

R_API int r_queue_enqueue (RQueue *q, void *el) {
	if (is_full(q)) {
		int res = increase_capacity (q);
		if (!res)
			return R_FALSE;
	}

	q->rear = (q->rear + 1) % q->capacity;
	q->elems[q->rear] = el;
	q->size++;
	return R_TRUE;
}

R_API void *r_queue_dequeue (RQueue *q) {
	void *res;

	if (r_queue_is_empty (q))
		return NULL;

	res = q->elems[q->front];
	q->front = (q->front + 1) % q->capacity;
	q->size--;
	return res;
}

R_API int r_queue_is_empty (RQueue *q) {
	return q->size == 0;
}
