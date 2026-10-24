---
name: text_to_image_controlnet_upscale_latent_upscale_5
type: Text To Image
frequency: 2
level: weak
coverage: 0.7035
common_nodes: [Any Switch (rgthree), BlockifyMask, CLIPLoader, CLIPTextEncode, ConcatTextOfUtils, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DWPreprocessor, DrawMaskOnImage, EmptyLatentImage, FaceMaskFromPoseKeypoints, Fast Groups Bypasser (rgthree), GH_MaskGrowthBlur, Get Image Size, GetNode, GrowMask, GuHaiMaskDetect, Image Comparer (rgthree), ImageAndMaskPreview, ImpactInt, ImpactMinMax, JjkText, KSampler, LG_Color_Match_V2, LatentUpscaleBy, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerMask: SegformerB2ClothesUltra, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, PreviewImage, PrimitiveBoolean, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, ReferenceLatent, RemoveBackgroundWithMask, SZ_KleinTiledKSampler, SaveImage, SetNode, SetUnionControlNetType, SimpleMath+, TextEncodeQwenImageEditPlusCustom_lrzjason, ToBinaryMask, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy ifElse, easy imageRemBg, solarL_SaveImagesToZip, 图像缩放V2_孤海, 孤海-遮罩混合运算, 孤海注释, 孤海遮罩分析]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/换装换脸神还原｜衣冠焕彩多人证件照登记照图生图_2091781513611403265.json, 图片生成/图生图/衣冠焕彩人物换装换脸｜多人证件照结婚登记照图生图_2091609767365136386.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_latent_upscale_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/换装换脸神还原｜衣冠焕彩多人证件照登记照图生图_2091781513611403265.json、图片生成/图生图/衣冠焕彩人物换装换脸｜多人证件照结婚登记照图生图_2091609767365136386.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConcatTextOfUtils`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `EmptyLatentImage`
- `FaceMaskFromPoseKeypoints`
- `Fast Groups Bypasser (rgthree)`
- `GH_MaskGrowthBlur`
- `Get Image Size`
- `GetNode`
- `GrowMask`
- `GuHaiMaskDetect`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImpactInt`
- `ImpactMinMax`
- `JjkText`
- `KSampler`
- `LG_Color_Match_V2`
- `LatentUpscaleBy`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: SegformerB2ClothesUltra`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `PreviewImage`
- `PrimitiveBoolean`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `ReferenceLatent`
- `RemoveBackgroundWithMask`
- `SZ_KleinTiledKSampler`
- `SaveImage`
- `SetNode`
- `SetUnionControlNetType`
- `SimpleMath+`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `ToBinaryMask`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy ifElse`
- `easy imageRemBg`
- `solarL_SaveImagesToZip`
- `图像缩放V2_孤海`
- `孤海-遮罩混合运算`
- `孤海注释`
- `孤海遮罩分析`

**可变部分**（部分 workflow 才有）：
- `忽略多组孤海` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 2 | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
