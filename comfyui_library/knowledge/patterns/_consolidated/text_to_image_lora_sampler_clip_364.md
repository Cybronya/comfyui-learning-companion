---
name: text_to_image_lora_sampler_clip_364
type: Text To Image
frequency: 5
level: strong
coverage: 0.8478
common_nodes: [AddMask, CLIPLoader, CLIPTextEncode, ColorMatchPro, EmptyLatentImage, GetImageSize, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), GrowMaskWithBlur, Image Paste Crop by Location, ImageCompositeMasked, ImageCropV2, ImageScale, InvertMask, JjkText, KSampler, LayerMask: MaskPreview, LayerUtility: ImageAutoCrop, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveBoundingBox, RH_Nano_Banana2_Gemini31Flash, ResolutionSelector, SAMLoader, SaveImage, SegmentV2, SimpleMath+, StringMergeNode, Text, UNETLoader, VAEDecode, VAELoader, YCMaskDirectionExpand, solarL_SaveImagesToZip, 图像缩放V2_孤海, 孤海图像裁剪按比例, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/自动化换脸方案一 一键面部替换保持原画面质感_2104768665513193473.json, 图片生成/图生图/自动化换脸方案三 批量面部替换高效出片一键搞定_2104677188711829506.json, 图片生成/图生图/自动化换脸第1版｜图生图全自动换脸，省时省力稳定出图_2104527348396806145.json, 图片生成/图生图/自动化换脸第2版｜全自动图生图换脸，新手也能一键上手_2104517875368288258.json, 图片生成/图生图/自动化换脸第3弹｜图生图一键换脸，流程全自动省心出片_2104516167573532674.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_364

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/自动化换脸方案一 一键面部替换保持原画面质感_2104768665513193473.json、图片生成/图生图/自动化换脸方案三 批量面部替换高效出片一键搞定_2104677188711829506.json、图片生成/图生图/自动化换脸第1版｜图生图全自动换脸，省时省力稳定出图_2104527348396806145.json、图片生成/图生图/自动化换脸第2版｜全自动图生图换脸，新手也能一键上手_2104517875368288258.json、图片生成/图生图/自动化换脸第3弹｜图生图一键换脸，流程全自动省心出片_2104516167573532674.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `AddMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatchPro`
- `EmptyLatentImage`
- `GetImageSize`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMaskWithBlur`
- `Image Paste Crop by Location`
- `ImageCompositeMasked`
- `ImageCropV2`
- `ImageScale`
- `InvertMask`
- `JjkText`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageAutoCrop`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveBoundingBox`
- `RH_Nano_Banana2_Gemini31Flash`
- `ResolutionSelector`
- `SAMLoader`
- `SaveImage`
- `SegmentV2`
- `SimpleMath+`
- `StringMergeNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `YCMaskDirectionExpand`
- `solarL_SaveImagesToZip`
- `图像缩放V2_孤海`
- `孤海图像裁剪按比例`
- `孤海注释`

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
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
