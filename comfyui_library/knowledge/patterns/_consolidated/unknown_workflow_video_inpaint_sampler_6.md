---
name: unknown_workflow_video_inpaint_sampler_6
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.727
common_nodes: [CR Text Concatenate, DWPreprocessor, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, Fast Groups Bypasser (rgthree), Florence2Run, Florence2toCoordinates, GrowMaskWithBlur, ImageResize+, ImageResizeKJ, InpaintPreprocessor, Int, LayerMask: LoadFlorence2Model, LayerUtility: Florence2Image2Prompt, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, MaskToImage, MathExpression|pysssss, PrimitiveString, RH_Translator, Sam2Segmentation, ShowText|pysssss, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader, easy cleanGpuUsed, easy imageRemBg, easy textSwitch]
problems: []
missing: []
members: [视频生成/图生视频/1939680452862976002.json, 视频生成/图生视频/1941245784644075522.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_sampler_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1939680452862976002.json、视频生成/图生视频/1941245784644075522.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text Concatenate`
- `DWPreprocessor`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `Fast Groups Bypasser (rgthree)`
- `Florence2Run`
- `Florence2toCoordinates`
- `GrowMaskWithBlur`
- `ImageResize+`
- `ImageResizeKJ`
- `InpaintPreprocessor`
- `Int`
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: Florence2Image2Prompt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `MathExpression|pysssss`
- `PrimitiveString`
- `RH_Translator`
- `Sam2Segmentation`
- `ShowText|pysssss`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy imageRemBg`
- `easy textSwitch`

**可变部分**（部分 workflow 才有）：
- `DepthAnythingV2Preprocessor` —— 1/2 个有
- `ImageScaleToMegapixels` —— 1/2 个有
- `ImageSmartSharpen+` —— 1/2 个有
- `KEEP_ModelLoader` —— 1/2 个有
- `KEEP_ProcessImageSequence` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
