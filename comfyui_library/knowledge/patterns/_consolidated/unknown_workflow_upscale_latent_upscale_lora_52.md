---
name: unknown_workflow_upscale_latent_upscale_lora_52
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9926
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DisableNoise, DualCLIPLoader, FluxGuidance, InjectLatentNoise+, KSamplerSelect, LatentUpscaleBy, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, SplitSigmasDenoise, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/抖音网红脸cos敖闰_1892232669667745794.json, 图片生成/文生图/抖音美女跳舞图片环节_1867930205196271617.json, 图片生成/文生图/炉鼎之家-文生图_1889684383299788802.json, 图片生成/文生图/颜值网红美女工作流_1896063182081490945.json, 视频生成/图生视频/美女跳舞图片_1932281057691729921.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_52

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/抖音网红脸cos敖闰_1892232669667745794.json、图片生成/文生图/抖音美女跳舞图片环节_1867930205196271617.json、图片生成/文生图/炉鼎之家-文生图_1889684383299788802.json、图片生成/文生图/颜值网红美女工作流_1896063182081490945.json、视频生成/图生视频/美女跳舞图片_1932281057691729921.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DisableNoise`
- `DualCLIPLoader`
- `FluxGuidance`
- `InjectLatentNoise+`
- `KSamplerSelect`
- `LatentUpscaleBy`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SplitSigmasDenoise`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Aspect Ratio` —— 4/5 个有
- `ModelSamplingFlux` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `Anything Everywhere` —— 1/5 个有
- `CheckpointLoaderSimple` —— 1/5 个有
- `EmptyLatentImage` —— 1/5 个有
- `ImageSmartSharpen+` —— 1/5 个有
- `LatentInterpolate` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1600 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
