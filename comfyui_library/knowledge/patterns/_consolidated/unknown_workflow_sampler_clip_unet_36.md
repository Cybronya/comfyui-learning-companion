---
name: unknown_workflow_sampler_clip_unet_36
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.962143
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [InjectLatentNoise+, Upscale Model Loader]
members: [图片生成/文生图/1916028810548936705.json, 图片生成/文生图/人猫合影_1891781898589384705.json, 图片生成/文生图/抖音美女跳舞图片环节_1867930205196271617.json, 图片生成/文生图/炉鼎之家-文生图_1889684383299788802.json, 图片生成/文生图/颜值网红美女工作流_1896063182081490945.json, 视频生成/图生视频/1932281057691729921.json, 视频生成/文生视频/1930226449242865665.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_36

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1916028810548936705.json、图片生成/文生图/人猫合影_1891781898589384705.json、图片生成/文生图/抖音美女跳舞图片环节_1867930205196271617.json、图片生成/文生图/炉鼎之家-文生图_1889684383299788802.json、图片生成/文生图/颜值网红美女工作流_1896063182081490945.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DisableNoise` —— 6/7 个有
- `InjectLatentNoise+` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `SplitSigmasDenoise` —— 6/7 个有
- `CR Aspect Ratio` —— 4/7 个有
- `LatentUpscaleBy` —— 4/7 个有
- `EmptySD3LatentImage` —— 3/7 个有
- `LoadImage` —— 2/7 个有
- `LoraLoader` —— 2/7 个有
- `UltimateSDUpscale` —— 2/7 个有
- `Upscale Model Loader` —— 2/7 个有
- `BetterFilmGrain` —— 1/7 个有
- `CheckpointLoaderSimple` —— 1/7 个有
- `ExpressionEditor` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `Simple String` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.9 | - | 2 | 100% |
| LoRA 文本强度 | 0.9 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：InjectLatentNoise+、Upscale Model Loader
