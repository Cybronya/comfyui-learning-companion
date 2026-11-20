---
name: text_to_image_lora_sampler_clip_377
type: Text To Image
frequency: 5
level: strong
coverage: 0.8992
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX 3 Klein多功能整合16步蒸馏版，官方提示词增强图生图_2112695455879614465.json, 图片生成/文生图/Flux3_Klein图像编辑工作流，文生图图生图双修_2111904655876911106.json, 图片生成/文生图/Z-Image Turbo极速文生图内置身材调节Lora处理工具_2101769735858905090.json, 图片生成/文生图/Z-image-turbo极速文生图｜内置身材调节Lora免折腾_2101556554981011457.json, 视频生成/图生视频/MOSS-Image一键洗图画质修复增强，老图翻新高清放大直出2K画质_2114412047910916097.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_377

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX 3 Klein多功能整合16步蒸馏版，官方提示词增强图生图_2112695455879614465.json、图片生成/文生图/Flux3_Klein图像编辑工作流，文生图图生图双修_2111904655876911106.json、图片生成/文生图/Z-Image Turbo极速文生图内置身材调节Lora处理工具_2101769735858905090.json、图片生成/文生图/Z-image-turbo极速文生图｜内置身材调节Lora免折腾_2101556554981011457.json、视频生成/图生视频/MOSS-Image一键洗图画质修复增强，老图翻新高清放大直出2K画质_2114412047910916097.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 4/5 个有
- `UpscaleModelLoader` —— 4/5 个有
- `ReferenceMultiLatent` —— 3/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `ImageScaleToMaxDimension` —— 2/5 个有
- `Int` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `RHLLMChatNode` —— 2/5 个有
- `GetImageSize` —— 1/5 个有
- `HAIGC_LoadImagesFromZip` —— 1/5 个有
- `HAIGC_SaveImagesToZip` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `LoadImageHighPrec` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `SkipLayerGuidanceDiTSimple` —— 1/5 个有
- `StringFormat` —— 1/5 个有
- `VAEEncode` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
