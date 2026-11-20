---
name: image_to_image_sampler_unet_vae_41
type: Image To Image
frequency: 7
level: moderate
coverage: 0.888286
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问edit万物溶图_1970142488826703873.json, 图片生成/图生图/千问图像编辑_1958444118198349826.json, 图片生成/图生图/自己用：Edit重新打光_1965220576757432321.json, 图片生成/图生图/身材管理美化工作流_1970137807157161985.json, 图片生成/文生图/Qwen-Image-Edit—飞翔荷兰人_1971152467314515969.json, 平台全量/千问编辑Plus去水印_1971830729342644226.json, 平台全量/鞋子融图-千问edit_1972125513907171330.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_41

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/千问edit万物溶图_1970142488826703873.json、图片生成/图生图/千问图像编辑_1958444118198349826.json、图片生成/图生图/自己用：Edit重新打光_1965220576757432321.json、图片生成/图生图/身材管理美化工作流_1970137807157161985.json、图片生成/文生图/Qwen-Image-Edit—飞翔荷兰人_1971152467314515969.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/7 个有
- `Image Comparer (rgthree)` —— 6/7 个有
- `ImageScaleToTotalPixels` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `TextEncodeQwenImageEdit` —— 6/7 个有
- `ImageScale` —— 4/7 个有
- `GetImageSize` —— 3/7 个有
- `LayerUtility: AnyRerouter` —— 2/7 个有
- `LayerUtility: HLFrequencyDetailRestore` —— 2/7 个有
- `LayerUtility: ImageMaskScaleAs` —— 2/7 个有
- `FastCanvas` —— 1/7 个有
- `FastCanvasTool` —— 1/7 个有
- `LayerMask: BiRefNetUltraV2` —— 1/7 个有
- `LayerMask: LoadBiRefNetModel` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `Note _O` —— 1/7 个有
- `RMBG` —— 1/7 个有
- `TextEncodeQwenImageEditPlus` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 7 | 77% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 7 | 77% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
