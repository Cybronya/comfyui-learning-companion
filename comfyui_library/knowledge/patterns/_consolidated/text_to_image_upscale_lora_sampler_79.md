---
name: text_to_image_upscale_lora_sampler_79
type: Text To Image
frequency: 3
level: strong
coverage: 0.903
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), ImageScaleBy, ImageScaleToTotalPixels, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2图生花型设计｜面料印花图案批量出图省设计费_2112865964051230722.json, 图片生成/图生图/Qwen Edit 2511单图编辑全能手｜电商产品个人写真都能改｜局部重绘精细_2102611970536067073.json, 图片生成/图生图/Qwen Edit 2511电商产品图编辑利器｜个人照片也能精修｜写实风局部重绘_2102615492870631426.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_79

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Krea2图生花型设计｜面料印花图案批量出图省设计费_2112865964051230722.json、图片生成/图生图/Qwen Edit 2511单图编辑全能手｜电商产品个人写真都能改｜局部重绘精细_2102611970536067073.json、图片生成/图生图/Qwen Edit 2511电商产品图编辑利器｜个人照片也能精修｜写实风局部重绘_2102615492870631426.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
