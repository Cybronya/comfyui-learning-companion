---
name: unknown_workflow_video_inpaint_upscale_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9055
common_nodes: [Anything Everywhere, Anything Everywhere3, ColorMatch, DownloadAndLoadFlorence2Model, DownloadAndLoadGIMMVFIModel, DownloadAndLoadSAM2Model, Fast Groups Bypasser (rgthree), Florence2Run, Florence2toCoordinates, GIMMVFI_interpolate, GrowMaskWithBlur, ImageConcanate, ImageResize+, ImageSmartSharpen+, ImageUpscaleWithModel, InpaintPreprocessor, Int, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, MaskToImage, MathExpression|pysssss, Primitive integer [Crystools], PrimitiveString, RH_Captioner, RH_Translator, Sam2Segmentation, ShowText|pysssss, StringFunction|pysssss, Text Multiline, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/777788888_1914980090441101313.json, 视频生成/图生视频/快速视频模仿动作+图生视频_1934099206166466561.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_upscale_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/777788888_1914980090441101313.json、视频生成/图生视频/快速视频模仿动作+图生视频_1934099206166466561.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `ColorMatch`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadGIMMVFIModel`
- `DownloadAndLoadSAM2Model`
- `Fast Groups Bypasser (rgthree)`
- `Florence2Run`
- `Florence2toCoordinates`
- `GIMMVFI_interpolate`
- `GrowMaskWithBlur`
- `ImageConcanate`
- `ImageResize+`
- `ImageSmartSharpen+`
- `ImageUpscaleWithModel`
- `InpaintPreprocessor`
- `Int`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `PrimitiveString`
- `RH_Captioner`
- `RH_Translator`
- `Sam2Segmentation`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `Text Multiline`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `LoadWanVideoClipTextEncoder` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `WanVideoImageClipEncode` —— 1/2 个有
- `WanVideoTeaCache` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
