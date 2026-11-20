---
name: text_to_image_controlnet_ipadapter_inpaint_2
type: Text To Image
frequency: 4
level: strong
coverage: 0.66575
common_nodes: [AV_VAELoader, ApplyInstantID, ApplyPulid, BNK_CLIPTextEncodeAdvanced, BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, BboxDetectorSEGS, CLIPTextEncode, CR Model Input Switch, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, Crop Face, DF_Image_scale_to_side, DWPreprocessor, DepthAnything_V2, Display Int (rgthree), DownloadAndLoadDepthAnythingV2Model, EmptyLatentImage, GetNode, GrowMask, IPAdapterMS, IPAdapterUnifiedLoader, Image Comparer (rgthree), Image Overlay, ImageComposite+, ImageCrop+, ImageResize+, ImageResizeKJ, ImageUpscaleWithModel, ImpactInt, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, InvertMask, Joy_caption, Joy_caption_load, KSampler, LayerColor: ColorAdapter, Load RetinaFace, LoadImage, Mask Crop Region, MaskBlur+, MaskToImage, PrepImageForClipVision, PreviewImage, PulidEvaClipLoader, PulidModelLoader, SAMDetectorCombined, SAMLoader, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, Seed (rgthree), SetNode, StringFunction|pysssss, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/【风格迁移换装 换脸】人像摄影- 邻家AI大女孩_2043945436586713090.json, 平台全量/【风格迁移换装 换脸】人像摄影_1833762927504683010.json, 平台全量/【风格迁移换装 换脸】人像摄影_1834429338405027842.json, 平台全量/最强参考姿势换脸换服装_1915276851621593089.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_inpaint_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【风格迁移换装 换脸】人像摄影- 邻家AI大女孩_2043945436586713090.json、平台全量/【风格迁移换装 换脸】人像摄影_1833762927504683010.json、平台全量/【风格迁移换装 换脸】人像摄影_1834429338405027842.json、平台全量/最强参考姿势换脸换服装_1915276851621593089.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
- `AV_VAELoader`
- `ApplyInstantID`
- `ApplyPulid`
- `BNK_CLIPTextEncodeAdvanced`
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `BboxDetectorSEGS`
- `CLIPTextEncode`
- `CR Model Input Switch`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `Crop Face`
- `DF_Image_scale_to_side`
- `DWPreprocessor`
- `DepthAnything_V2`
- `Display Int (rgthree)`
- `DownloadAndLoadDepthAnythingV2Model`
- `EmptyLatentImage`
- `GetNode`
- `GrowMask`
- `IPAdapterMS`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `Image Overlay`
- `ImageComposite+`
- `ImageCrop+`
- `ImageResize+`
- `ImageResizeKJ`
- `ImageUpscaleWithModel`
- `ImpactInt`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `InvertMask`
- `Joy_caption`
- `Joy_caption_load`
- `KSampler`
- `LayerColor: ColorAdapter`
- `Load RetinaFace`
- `LoadImage`
- `Mask Crop Region`
- `MaskBlur+`
- `MaskToImage`
- `PrepImageForClipVision`
- `PreviewImage`
- `PulidEvaClipLoader`
- `PulidModelLoader`
- `SAMDetectorCombined`
- `SAMLoader`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `StringFunction|pysssss`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.85 | 0.85 - 0.85 | 4 | 100% |
| 宽度 | 768 | 768 - 768 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 7 | 6.64 - 7 | 4 | 98% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 0.49 | 0.49 - 1 | 4 | 64% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.85，观测区间 0.85 - 0.85，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 768，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 6.64 - 7，4 个样本，取值集中（一致性 98%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 0.49，观测区间 0.49 - 1，4 个样本
