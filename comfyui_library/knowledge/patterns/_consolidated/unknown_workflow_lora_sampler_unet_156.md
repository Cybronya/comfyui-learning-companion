---
name: unknown_workflow_lora_sampler_unet_156
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9444
common_nodes: [BasicGuider, BasicScheduler, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/08.flux-lora-快速文生图_1993297535381028865.json, 图片生成/文生图/Create 3D PIXAL CARTOON Youtube ratio _ DINO AI_1957737610612670465.json, 图片生成/文生图/F.1 - 极致逼真文生图（噪声注入）_2007506616567992322.json, 图片生成/文生图/FLUX + LORA 基础工作流_1830939420676771841.json, 图片生成/文生图/FLUX去除AI味道-噪波注入文生图工作流_1942941680951574529.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_156

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/08.flux-lora-快速文生图_1993297535381028865.json、图片生成/文生图/Create 3D PIXAL CARTOON Youtube ratio _ DINO AI_1957737610612670465.json、图片生成/文生图/F.1 - 极致逼真文生图（噪声注入）_2007506616567992322.json、图片生成/文生图/FLUX + LORA 基础工作流_1830939420676771841.json、图片生成/文生图/FLUX去除AI味道-噪波注入文生图工作流_1942941680951574529.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 4/5 个有
- `DualCLIPLoader` —— 4/5 个有
- `FluxGuidance` —— 4/5 个有
- `VAEDecode` —— 4/5 个有
- `CR SDXL Aspect Ratio` —— 3/5 个有
- `DisableNoise` —— 2/5 个有
- `EmptyLatentImage` —— 2/5 个有
- `ImageSmartSharpen+` —— 2/5 个有
- `InjectLatentNoise+` —— 2/5 个有
- `LatentInterpolate` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `SplitSigmasDenoise` —— 2/5 个有
- `CLIPTextEncodeFlux` —— 1/5 个有
- `DualCLIPLoaderGGUF` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageGenResolutionFromLatent` —— 1/5 个有
- `LatentUpscaleBy` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `StringConstantMultiline` —— 1/5 个有
- `VAEDecodeTiled` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 872 | - | 2 | 83% |
| 高度 | 1600 | - | 2 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 872，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 1600，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
