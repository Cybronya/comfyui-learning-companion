---
name: text_to_image_sampler_clip_unet_120
type: Text To Image
frequency: 6
level: weak
coverage: 0.894167
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/API - FLux文生图_2066848618040086529.json, 图片生成/文生图/API - FLux文生图_2091105641225080833.json, 图片生成/文生图/CFG Zero出图_1907792965371371522.json, 图片生成/文生图/FLux文生图API工作流｜高质量图像生成_2095581101854121986.json, 图片生成/文生图/Qwen Image 2.1文生图加4步加速，高质量文本到图像生成工作流_2103932568507863042.json, 图片生成/文生图/Qwen_Image_2.1文生图工作流｜零门槛直出创意画面_2110761065725382658.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_120

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/API - FLux文生图_2066848618040086529.json、图片生成/文生图/API - FLux文生图_2091105641225080833.json、图片生成/文生图/CFG Zero出图_1907792965371371522.json、图片生成/文生图/FLux文生图API工作流｜高质量图像生成_2095581101854121986.json、图片生成/文生图/Qwen Image 2.1文生图加4步加速，高质量文本到图像生成工作流_2103932568507863042.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `DualCLIPLoader` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `CLIPLoader` —— 3/6 个有
- `FluxGuidance` —— 3/6 个有
- `JjkText` —— 3/6 个有
- `LoraLoader` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `easy int` —— 3/6 个有
- `solarL_SaveImagesToZip` —— 3/6 个有
- `孤海注释` —— 3/6 个有
- `ModelAttentionBackend` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `SaveImageAdvanced` —— 2/6 个有
- `CFGZeroStarAndInit` —— 1/6 个有
- `ResolutionSelector` —— 1/6 个有
- `TextEncodeQwenImage21` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 296 | 80 - 1280 | 6 | 0% |
| 高度 | 296 | 80 - 720 | 6 | 21% |
| 采样步数 | 6 | 4 - 20 | 6 | 29% |
| Prompt 约束强度(CFG) | 3 | 1 - 4.5 | 6 | 45% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 296，观测区间 80 - 1280，6 个样本，取值分散，一致性仅 0%
- 高度 中位数 296，观测区间 80 - 720，6 个样本，取值分散，一致性仅 21%
- 采样步数 中位数 6，观测区间 4 - 20，6 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4.5，6 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
