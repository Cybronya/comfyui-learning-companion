---
name: unknown_workflow_sampler_unet_vae_167
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.923667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/15秒段_一采二采_UI格式_魔法少女_2109253533366312961.json, 视频生成/文生视频/MiniMax H3｜20步质量基准｜参考生视频_2098317985948721153.json, 视频生成/文生视频/MiniMax H3｜20步质量基准｜首尾帧视频_2098317999458570241.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_167

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/15秒段_一采二采_UI格式_魔法少女_2109253533366312961.json、视频生成/文生视频/MiniMax H3｜20步质量基准｜参考生视频_2098317985948721153.json、视频生成/文生视频/MiniMax H3｜20步质量基准｜首尾帧视频_2098317999458570241.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3AudioConditioningT8` —— 2/3 个有
- `VAEDecodeAudio` —— 2/3 个有
- `GetVideoComponents` —— 1/3 个有
- `GoohaiMinimaxH3LatentUpscalerGH` —— 1/3 个有
- `GoohaiMinimaxH3TiledSampler` —— 1/3 个有
- `LoadVideo` —— 1/3 个有
- `MiniMaxH3ReferenceToVideo` —— 1/3 个有
- `SplitSigmas` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
