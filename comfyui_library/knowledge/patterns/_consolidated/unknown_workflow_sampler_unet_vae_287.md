---
name: unknown_workflow_sampler_unet_vae_287
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.713
common_nodes: [Anything Everywhere3, CLIPLoader, CR Prompt Text, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, KSampler, QwenImage21Cache, ResolutionSelector, SaveImage, Seed (rgthree), SetNode, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy setNode, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Qwen Image 2.1 Character Reference Sheet (Four Views)_2102316050699345921.json, 图片生成/文生图/Qwen Image 2.1 Short Drama Asset Series – Environm_2102362481237782530.json, 图片生成/文生图/【Qwen Image 2.1】图生图_2113732060803330050.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_287

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 Character Reference Sheet (Four Views)_2102316050699345921.json、图片生成/文生图/Qwen Image 2.1 Short Drama Asset Series – Environm_2102362481237782530.json、图片生成/文生图/【Qwen Image 2.1】图生图_2113732060803330050.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CR Prompt Text`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSampler`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy setNode`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LayerUtility: TextJoin` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SeedVR2LoadDiTModel` —— 2/3 个有
- `SeedVR2LoadVAEModel` —— 2/3 个有
- `SeedVR2VideoUpscaler` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 40 | 40 - 40 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 40 - 40，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
