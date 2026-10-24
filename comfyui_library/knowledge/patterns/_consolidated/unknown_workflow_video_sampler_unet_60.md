---
name: unknown_workflow_video_sampler_unet_60
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91925
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Prompt Text, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, MathExpression|pysssss, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SoundFlow_GetLength, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3 单人音频驱动数字人（最高15秒）_2085434809618358274.json, 视频生成/图生视频/MiniMax-H3 双人音频驱动数字人（双人最高15秒）_2085462125711024129.json, 视频生成/图生视频/MiniMax-H3_单人音频驱动数字人最高15秒_2099774570529120257.json, 视频生成/图生视频/MiniMax-H3_单人音频驱动数字人最高15秒_2100034040945537025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_60

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3 单人音频驱动数字人（最高15秒）_2085434809618358274.json、视频生成/图生视频/MiniMax-H3 双人音频驱动数字人（双人最高15秒）_2085462125711024129.json、视频生成/图生视频/MiniMax-H3_单人音频驱动数字人最高15秒_2099774570529120257.json、视频生成/图生视频/MiniMax-H3_单人音频驱动数字人最高15秒_2100034040945537025.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `MathExpression|pysssss`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SoundFlow_GetLength`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 3/4 个有
- `MiniMaxChunkFeedForward` —— 2/4 个有
- `MiniMaxLowVRAMAttention` —— 2/4 个有
- `ModelAttentionBackend` —— 2/4 个有
- `ModelPreviewOverrideKJ` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `PixaromaLabel` —— 2/4 个有
- `AudioConcat` —— 1/4 个有
- `EmptyAudio` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
