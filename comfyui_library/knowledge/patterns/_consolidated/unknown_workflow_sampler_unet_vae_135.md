---
name: unknown_workflow_sampler_unet_vae_135
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.879625
common_nodes: [CLIPLoader, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen image 2.1 文生图_2110328458579632130.json, 图片生成/文生图/qwen-image-2.1_2101675550237614082.json, 图片生成/文生图/qwen-image-2.1多图编辑_2101799458202804226.json, 图片生成/文生图/千问iamge2.1文生图_2102716967022063618.json, 图片生成/文生图/多图编辑工作流_2105329811446124546.json, 数字人/数字人/Qwen Image 2.1 图像编辑 Image Edit_2101822303028989953.json, 数字人/数字人/千问工作流_2102229006685917186.json, 视频生成/图生视频/Qwen_image_2.1图片编辑_2104046916651798529.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_135

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1 文生图_2110328458579632130.json、图片生成/文生图/qwen-image-2.1_2101675550237614082.json、图片生成/文生图/qwen-image-2.1多图编辑_2101799458202804226.json、图片生成/文生图/千问iamge2.1文生图_2102716967022063618.json、图片生成/文生图/多图编辑工作流_2105329811446124546.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 7/8 个有
- `LoadImage` —— 6/8 个有
- `CR Text` —— 5/8 个有
- `EmptyLatentImage` —— 5/8 个有
- `ComfySwitchNode` —— 4/8 个有
- `ResolutionSelector` —— 4/8 个有
- `TextGenerateLTX2Prompt` —— 4/8 个有
- `easy showAnything` —— 4/8 个有
- `BatchImagesNode` —— 2/8 个有
- `SaveImageAdvanced` —— 2/8 个有
- `EmptyImage` —— 1/8 个有
- `EmptySD3LatentImage` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `ImageConcatMulti` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 50 | 8 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 1024 - 1152 | 5 | 95% |
| 高度 | 1024 | 1024 - 1536 | 5 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 50，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1152，5 个样本，取值集中（一致性 95%）
- 高度 中位数 1024，观测区间 1024 - 1536，5 个样本，取值集中（一致性 82%）
