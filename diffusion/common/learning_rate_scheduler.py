import optax


def get_learning_rate_scheduler(cfg, step_size):
    """Creates learning rate schedule."""
    if cfg['warmup'] == 'linear':
        warmup_fn = optax.linear_schedule(
            init_value=0., end_value=step_size,
            transition_steps=cfg['warmup_iters'])
        """Creates learning rate schedule."""
    elif cfg['warmup'] == 'const':
        warmup_fn = optax.constant_schedule(step_size)
    else:
        raise ValueError(f"No warmup scheme called {cfg['warmup']}")

    cosine_epochs = max(cfg['iters'] - cfg['warmup_iters'], 1)
    cosine_fn = optax.cosine_decay_schedule(
        init_value=step_size,
        decay_steps=cosine_epochs)

    schedule_fn = optax.join_schedules(
        schedules=[warmup_fn, cosine_fn],
        boundaries=[cfg['warmup_iters']])
    return schedule_fn
