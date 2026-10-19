---
name: unknown_workflow_sampler_unet_vae_33
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.843143
common_nodes: [CLIPLoader, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/2102217964954152961.json, 图片生成/图生图/2102232455502716929.json, 图片生成/图生图/2102236996667265025.json, 图片生成/图生图/2102319407006572545.json, 图片生成/图生图/2102322312635834369.json, 图片生成/图生图/2102343043620888578.json, 图片生成/图生图/2102572577544818689.json, 图片生成/图生图/2102593163918667778.json, 图片生成/图生图/2102599002511462402.json, 图片生成/文生图/OWEN IMAGE 2.1 文生图_2103073574478245890.json, 图片生成/文生图/Qwen_Image_文生图_2102957010739351554.json, 图片生成/文生图/qwen_image_2_1_图像编辑-换背景和姿态_2102217040533745665.json, 视频生成/图生视频/Qwen_image_2.1图片编辑_2104046916651798529.json, 视频生成/图生视频/换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2102960653840510977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_33

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/2102217964954152961.json、图片生成/图生图/2102232455502716929.json、图片生成/图生图/2102236996667265025.json、图片生成/图生图/2102319407006572545.json、图片生成/图生图/2102322312635834369.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 12/14 个有
- `QwenImage21Cache` —— 11/14 个有
- `EmptyLatentImage` —— 10/14 个有
- `ResolutionSelector` —— 9/14 个有
- `ComfySwitchNode` —— 8/14 个有
- `SaveImageAdvanced` —— 6/14 个有
- `PreviewImage` —— 5/14 个有
- `EmptyImage` —— 4/14 个有
- `PrimitiveStringMultiline` —— 4/14 个有
- `BatchImagesNode` —— 2/14 个有
- `TextGenerateLTX2Prompt` —— 2/14 个有
- `YK_LoadImageFromURL` —— 2/14 个有
- `AIO_Preprocessor` —— 1/14 个有
- `ImageConcatMulti` —— 1/14 个有
- `JjkText` —— 1/14 个有
- `easy showAnything` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 50 | 14 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 10 | 100% |
| 高度 | 1024 | 1024 - 1536 | 10 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 50，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，10 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，10 个样本，取值集中（一致性 86%）
