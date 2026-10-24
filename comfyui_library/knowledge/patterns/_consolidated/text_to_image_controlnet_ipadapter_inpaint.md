---
name: text_to_image_controlnet_ipadapter_inpaint
type: Text To Image
frequency: 5
level: strong
coverage: 0.6094
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DetailerForEach, EmptyLatentImage, HD UltimateSDUpscale, Image Comparer (rgthree), ImagePadForOutpaint, ImageResize+, ImpactSwitch, KSampler, LayerColor: ColorAdapter, LayerMask: MaskGrow, LayerUtility: ImageBlendAdvance, LoadImage, MZ_ChatGLM3Loader, MZ_ChatGLM3_V2, MZ_IPAdapterAdvancedKolors, MZ_IPAdapterModelLoaderKolors, MZ_KolorsCLIPVisionLoader, MZ_KolorsControlNetPatch, MZ_KolorsUNETLoaderV2, Mask Invert, MaskPreview+, MaskToImage, MaskToSEGS, PreviewImage, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncodeForInpaint, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kolors-风格迁移-溶图_1950211377292075009.json, 图片生成/图生图/完美融合版产品换背景_1915228531930890242.json, 图片生成/图生图/室内参考家装风格换场景_1927909473518501889.json, 图片生成/图生图/摄影级产品换背景_1913921875733377026.json, 图片生成/文生图/白底图+背景参考图-溶图_1893331823282307073.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_inpaint

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Kolors-风格迁移-溶图_1950211377292075009.json、图片生成/图生图/完美融合版产品换背景_1915228531930890242.json、图片生成/图生图/室内参考家装风格换场景_1927909473518501889.json、图片生成/图生图/摄影级产品换背景_1913921875733377026.json、图片生成/文生图/白底图+背景参考图-溶图_1893331823282307073.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DetailerForEach`
- `EmptyLatentImage`
- `HD UltimateSDUpscale`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `ImageResize+`
- `ImpactSwitch`
- `KSampler`
- `LayerColor: ColorAdapter`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageBlendAdvance`
- `LoadImage`
- `MZ_ChatGLM3Loader`
- `MZ_ChatGLM3_V2`
- `MZ_IPAdapterAdvancedKolors`
- `MZ_IPAdapterModelLoaderKolors`
- `MZ_KolorsCLIPVisionLoader`
- `MZ_KolorsControlNetPatch`
- `MZ_KolorsUNETLoaderV2`
- `Mask Invert`
- `MaskPreview+`
- `MaskToImage`
- `MaskToSEGS`
- `PreviewImage`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncodeForInpaint`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BiRefNet_Hugo` —— 4/5 个有
- `Display Int (rgthree)` —— 3/5 个有
- `GetImageSize` —— 3/5 个有
- `GetNode` —— 3/5 个有
- `ImpactInt` —— 3/5 个有
- `Joy_caption` —— 3/5 个有
- `Joy_caption_load` —— 3/5 个有
- `LayerMask: MaskPreview` —— 3/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/5 个有
- `LayerUtility: LaMa` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `TextCombinerTwo` —— 3/5 个有
- `easy promptReplace` —— 3/5 个有
- `Int` —— 2/5 个有
- `InvertMask` —— 2/5 个有
- `RH_Captioner` —— 2/5 个有
- `SUPIR_conditioner` —— 2/5 个有
- `SUPIR_decode` —— 2/5 个有
- `SUPIR_encode` —— 2/5 个有
- `SUPIR_first_stage` —— 2/5 个有
- `SUPIR_model_loader_v2` —— 2/5 个有
- `SUPIR_sample` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `easy seed` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GetImageSizeAndCount` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LayerMask: SegmentAnythingUltra` —— 1/5 个有
- `LayerUtility: ColorImage` —— 1/5 个有
- `LayerUtility: ColorPicker` —— 1/5 个有
- `LayerUtility: ImageBlendAdvance V2` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 5 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 5 | 100% |
| 采样算法 | dpmpp_3m_sde_gpu | - | 5 | 100% |
| 调度器 | exponential | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| ControlNet 权重 | 0.5 | 0.5 - 0.5 | 5 | 100% |
| 宽度 | 768 | 768 - 768 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_3m_sde_gpu，5 个样本，一致性 100%
- 调度器 最常用 exponential，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.5，观测区间 0.5 - 0.5，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 768，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
