---
name: unknown_workflow_video_212
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.803
common_nodes: [APersonMaskGenerator, CR Prompt Text, GrowMask, Image Crop Face, ImageComposite+, ImageConcanate, ImageFromBatch, ImageFromBatch+, ImageResizeKJ, ImageToMask, JWInteger, LayerMask: HumanPartsUltra, LayerMask: MaskPreview, LayerUtility: CropByMask, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LayerUtility: RestoreCropBox, LoadImage, MaskBlur+, MaskComposite, MaskToImage, PreviewImage, RHHiddenNodes, RH_Captioner, Text Concatenate, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything, preview_mask]
problems: []
missing: []
members: [平台全量/【视频面部修复神器】AI 崩坏脸拯救_1943477090249285633.json, 平台全量/自用数字人「v2v模式」_1951185043857285122.json]
source: knowledge_consolidation
---

# unknown_workflow_video_212

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/【视频面部修复神器】AI 崩坏脸拯救_1943477090249285633.json、平台全量/自用数字人「v2v模式」_1951185043857285122.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `APersonMaskGenerator`
- `CR Prompt Text`
- `GrowMask`
- `Image Crop Face`
- `ImageComposite+`
- `ImageConcanate`
- `ImageFromBatch`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `ImageToMask`
- `JWInteger`
- `LayerMask: HumanPartsUltra`
- `LayerMask: MaskPreview`
- `LayerUtility: CropByMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `MaskBlur+`
- `MaskComposite`
- `MaskToImage`
- `PreviewImage`
- `RHHiddenNodes`
- `RH_Captioner`
- `Text Concatenate`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`
- `preview_mask`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `Display Int (rgthree)` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetVideoComponents` —— 1/2 个有
- `InpaintPreprocessor` —— 1/2 个有
- `LoadWanVideoT5TextEncoder` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有
- `RH_HeyGemNode` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `VHS_VideoInfoSource` —— 1/2 个有
- `WanVideoDecode` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有
- `WanVideoSampler` —— 1/2 个有
- `WanVideoTextEncode` —— 1/2 个有
- `WanVideoVACEEncode` —— 1/2 个有
- `WanVideoVAELoader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
