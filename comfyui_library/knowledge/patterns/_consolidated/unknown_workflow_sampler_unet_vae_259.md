---
name: unknown_workflow_sampler_unet_vae_259
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.829667
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image 2.1｜5倍加速全能工作流_2102372164333821954.json, 图片生成/图生图/qwen image 2.1多图编辑_2102673789824880642.json, 视频生成/图生视频/Qwen_image_2.1图片编辑_2104046916651798529.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_259

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-Image 2.1｜5倍加速全能工作流_2102372164333821954.json、图片生成/图生图/qwen image 2.1多图编辑_2102673789824880642.json、视频生成/图生视频/Qwen_image_2.1图片编辑_2104046916651798529.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 2/3 个有
- `ComfySwitchNode` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `CR Seed` —— 1/3 个有
- `DrawMaskOnImage` —— 1/3 个有
- `EmptyImage` —— 1/3 个有
- `ImpactConditionalBranch` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `SaveImageAdvanced` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 25 | 8 - 50 | 3 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 8 - 50，3 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
