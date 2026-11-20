---
name: text_to_image_controlnet_ipadapter_inpaint
type: Text To Image
frequency: 10
level: strong
coverage: 0.6447
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DetailerForEach, EmptyLatentImage, HD UltimateSDUpscale, Image Comparer (rgthree), ImagePadForOutpaint, ImageResize+, ImpactSwitch, KSampler, LayerColor: ColorAdapter, LayerMask: MaskGrow, LayerUtility: ImageBlendAdvance, LoadImage, MZ_ChatGLM3Loader, MZ_ChatGLM3_V2, MZ_IPAdapterAdvancedKolors, MZ_IPAdapterModelLoaderKolors, MZ_KolorsCLIPVisionLoader, MZ_KolorsControlNetPatch, MZ_KolorsUNETLoaderV2, Mask Invert, MaskPreview+, MaskToImage, MaskToSEGS, PreviewImage, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncodeForInpaint, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kolors-风格迁移-溶图_1950211377292075009.json, 图片生成/图生图/完美融合版产品换背景_1915228531930890242.json, 图片生成/图生图/室内参考家装风格换场景_1927909473518501889.json, 图片生成/图生图/摄影级产品换背景_1913921875733377026.json, 图片生成/文生图/白底图+背景参考图-溶图_1893331823282307073.json, 平台全量/「低显存可用」无损无瑕疵一键换脸_1888202083567599617.json, 平台全量/【一键换背景】产品图摄影_1845758651062743041.json, 平台全量/室内家装换背景_1858464108558626817.json, 平台全量/电商参考图换背景文字100%还原_1915051726834204673.json, 平台全量/白底背景替换工作流_1849051050807377921.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_inpaint

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Kolors-风格迁移-溶图_1950211377292075009.json、图片生成/图生图/完美融合版产品换背景_1915228531930890242.json、图片生成/图生图/室内参考家装风格换场景_1927909473518501889.json、图片生成/图生图/摄影级产品换背景_1913921875733377026.json、图片生成/文生图/白底图+背景参考图-溶图_1893331823282307073.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 10 个 workflow 都包含：
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
- `Display Int (rgthree)` —— 8/10 个有
- `GetImageSize` —— 8/10 个有
- `GetNode` —— 8/10 个有
- `ImpactInt` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `Joy_caption` —— 7/10 个有
- `Joy_caption_load` —— 7/10 个有
- `LayerMask: MaskPreview` —— 7/10 个有
- `LayerMask: SegmentAnythingUltra V2` —— 7/10 个有
- `LayerUtility: LaMa` —— 7/10 个有
- `SUPIR_conditioner` —— 7/10 个有
- `SUPIR_decode` —— 7/10 个有
- `SUPIR_encode` —— 7/10 个有
- `SUPIR_first_stage` —— 7/10 个有
- `SUPIR_model_loader_v2` —— 7/10 个有
- `SUPIR_sample` —— 7/10 个有
- `ShowText|pysssss` —— 7/10 个有
- `TextCombinerTwo` —— 7/10 个有
- `easy cleanGpuUsed` —— 7/10 个有
- `easy promptReplace` —— 7/10 个有
- `easy seed` —— 7/10 个有
- `BiRefNet_Hugo` —— 5/10 个有
- `GetImageSizeAndCount` —— 5/10 个有
- `LayerUtility: ColorImage` —— 5/10 个有
- `LayerUtility: ColorPicker` —— 5/10 个有
- `LayerUtility: ImageBlendAdvance V2` —— 5/10 个有
- `Label (rgthree)` —— 4/10 个有
- `InvertMask` —— 3/10 个有
- `RH_Captioner` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `Int` —— 2/10 个有
- `LayerMask: SegmentAnythingUltra` —— 1/10 个有
- `easy getNode` —— 1/10 个有
- `easy setNode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 10 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 10 | 100% |
| 采样算法 | dpmpp_3m_sde_gpu | - | 10 | 100% |
| 调度器 | exponential | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| ControlNet 权重 | 0.5 | 0.5 - 0.5 | 10 | 100% |
| 宽度 | 768 | 768 - 768 | 10 | 100% |
| 高度 | 1024 | 1024 - 1024 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_3m_sde_gpu，10 个样本，一致性 100%
- 调度器 最常用 exponential，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.5，观测区间 0.5 - 0.5，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 768，10 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，10 个样本，取值集中（一致性 100%）
