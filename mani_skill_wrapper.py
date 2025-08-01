from functools import cached_property

from mani_skill.utils.registration import register_env
from mani_skill.envs.tasks import PushTEnv
import gymnasium as gym
from mani_skill.utils import gym_utils, common


@register_env("PushTNoBatchDim-v1",max_episode_steps=100)
class PushTNoBatch(PushTEnv):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @cached_property
    def single_observation_space(self) -> gym.Space:
        """the unbatched observation space of the environment"""
        return gym_utils.convert_observation_to_space(common.to_numpy(self._init_raw_obs.unsqueeze(0)), unbatched=True)

    @cached_property
    def observation_space(self) -> gym.Space:
        """the batched observation space of the environment"""
        return self.single_observation_space

    # def get_obs(self, info=None, unflattened: bool = False):
    #     obs = super().get_obs(info)
    #     print(obs.shape)
    #     return obs[0]

    def _flatten_raw_obs(self, obs):
        return super()._flatten_raw_obs(obs)[0]
