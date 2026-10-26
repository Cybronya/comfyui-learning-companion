---
name: text_to_image_sampler_clip_unet_84
type: Text To Image
frequency: 8
level: weak
coverage: 0.894875
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/API - FLux文生图_2066848618040086529.json, 图片生成/文生图/API - FLux文生图_2091105641225080833.json, 图片生成/文生图/CFG Zero出图_1907792965371371522.json, 图片生成/文生图/FLux文生图API工作流｜高质量图像生成_2095581101854121986.json, 图片生成/文生图/Krea2图图工作流｜人像写真高质量质感生成_2095245729957761026.json, 图片生成/文生图/Krea2图图文生图｜高质量图像生成工作流_2095973742240423938.json, 图片生成/文生图/Krea2基础文生图高清出图｜美少女写实风格_2090073140905988098.json, 图片生成/文生图/Krea2特定风格人像大作文生图｜固定风格批量出人像大片_2099133481472315394.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_84

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/API - FLux文生图_2066848618040086529.json、图片生成/文生图/API - FLux文生图_2091105641225080833.json、图片生成/文生图/CFG Zero出图_1907792965371371522.json、图片生成/文生图/FLux文生图API工作流｜高质量图像生成_2095581101854121986.json、图片生成/文生图/Krea2图图工作流｜人像写真高质量质感生成_2095245729957761026.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 5/8 个有
- `JjkText` —— 5/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `solarL_SaveImagesToZip` —— 5/8 个有
- `孤海注释` —— 5/8 个有
- `DualCLIPLoader` —— 4/8 个有
- `FluxGuidance` —— 3/8 个有
- `LoraLoader` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `easy int` —— 3/8 个有
- `PreviewImage` —— 2/8 个有
- `CFGZeroStarAndInit` —— 1/8 个有
- `ResolutionSelector` —— 1/8 个有
- `easy ifElse` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1280 | 8 | 0% |
| 高度 | 80 | 80 - 720 | 8 | 7% |
| 采样步数 | 4 | 4 - 20 | 8 | 26% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 8 | 54% |
| 采样算法 | er_sde | - | 8 | 62% |
| 调度器 | beta | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1280，8 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 720，8 个样本，取值分散，一致性仅 7%
- 采样步数 中位数 4，观测区间 4 - 20，8 个样本，取值分散，一致性仅 26%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，8 个样本
- 采样算法 最常用 er_sde，8 个样本，一致性 62%
- 调度器 最常用 beta，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
