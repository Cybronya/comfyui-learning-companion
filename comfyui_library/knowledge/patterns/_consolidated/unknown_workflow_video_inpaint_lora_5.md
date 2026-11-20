---
name: unknown_workflow_video_inpaint_lora_5
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.77275
common_nodes: [CR Text Concatenate, ColorMatch, DWPreprocessor, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, Fast Groups Bypasser (rgthree), Florence2Run, Florence2toCoordinates, GrowMaskWithBlur, INTConstant, ImageResize+, ImageResizeKJ, InpaintPreprocessor, Int, LayerMask: LoadFlorence2Model, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, LayerUtility: Florence2Image2Prompt, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, MaskToImage, Mix Color By Mask, PrimitiveString, RH_Captioner, RH_Translator, Sam2Segmentation, SetNode, ShowText|pysssss, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy cleanGpuUsed, easy imageRemBg, easy showAnything, easy textSwitch]
problems: []
missing: []
members: [视频生成/图生视频/1+1+1_1939353504203063298.json, 视频生成/图生视频/指定人物动作迁移_1939679336746422273.json, 视频生成/图生视频/视频动作迁移1+1+1_1939386799787786241.json, 视频生成/图生视频/视频模动+图视+1+1+1+1留案底防丢_1938785658137665538.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_5

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1+1+1_1939353504203063298.json、视频生成/图生视频/指定人物动作迁移_1939679336746422273.json、视频生成/图生视频/视频动作迁移1+1+1_1939386799787786241.json、视频生成/图生视频/视频模动+图视+1+1+1+1留案底防丢_1938785658137665538.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CR Text Concatenate`
- `ColorMatch`
- `DWPreprocessor`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `Fast Groups Bypasser (rgthree)`
- `Florence2Run`
- `Florence2toCoordinates`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageResize+`
- `ImageResizeKJ`
- `InpaintPreprocessor`
- `Int`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerUtility: Florence2Image2Prompt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `Mix Color By Mask`
- `PrimitiveString`
- `RH_Captioner`
- `RH_Translator`
- `Sam2Segmentation`
- `SetNode`
- `ShowText|pysssss`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy imageRemBg`
- `easy showAnything`
- `easy textSwitch`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 3/4 个有
- `GIMMVFI_interpolate` —— 3/4 个有
- `ImageScaleToMegapixels` —— 3/4 个有
- `ImageSmartSharpen+` —— 3/4 个有
- `LatentSyncNode` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `MathExpression|pysssss` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `VideoLengthAdjuster` —— 3/4 个有
- `WanVideoApplyNAG` —— 3/4 个有
- `WanVideoEnhanceAVideo` —— 3/4 个有
- `WanVideoImageToVideoEncode` —— 3/4 个有
- `WanVideoSLG` —— 3/4 个有
- `WanVideoTextEncodeSingle` —— 3/4 个有
- `KEEP_ModelLoader` —— 2/4 个有
- `KEEP_ProcessImageSequence` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `VHS_VideoInfo` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `StringFunction|pysssss` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
