---
key: 平台全量/动作模仿动作迁移人物替换WanAnimate2.2_1971104745878392833.json
name: 动作模仿动作迁移人物替换WanAnimate2.2_1971104745878392833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/动作模仿动作迁移人物替换WanAnimate2.2_1971104745878392833.json
hash: d17923eb1228ac19
coverage: 0.580247
learned_at: 2026-11-14 01:44:26
nodes: [GetNode, GetNode, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, GIMMVFI_interpolate, GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, ImageConcatMulti, GetNode, SetNode, WanVideoClipVisionEncode, BlockifyMask, WanVideoTorchCompileSettings, WanVideoBlockSwap, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoDecode, ImageBlend, GetNode, GetNode, GetNode, GrowMask, GetNode, DrawMaskOnImage, DownloadAndLoadSAM2Model, DrawViTPose, SetNode, GetNode, MarkdownNote, WanVideoVAELoader, WanVideoAnimateEmbeds, WanVideoSampler, GetNode, GetNode, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, DownloadAndLoadGIMMVFIModel, SetNode, SetNode, INTConstant, INTConstant, VHS_LoadVideo, INTConstant, SetNode, SetNode, SetNode, WanVideoTextEncodeCached, CR Text, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, Int, MathExpression|pysssss, Int, INTConstant, Note, LoadImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, OnnxDetectionModelLoader, PoseAndFaceDetection, Sam2Segmentation, SetNode, GetImageSizeAndCount, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/动作模仿动作迁移人物替换WanAnimate2.2_1971104745878392833.json

> 来源文件 `comfyui_library/workflows/平台全量/动作模仿动作迁移人物替换WanAnimate2.2_1971104745878392833.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（81 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetNode`
- `GIMMVFI_interpolate`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `BlockifyMask`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `ImageBlend`
- `GetNode`
- `GetNode`
- `GetNode`
- `GrowMask`
- `GetNode`
- `DrawMaskOnImage`
- `DownloadAndLoadSAM2Model`
- `DrawViTPose`
- `SetNode`
- `GetNode`
- `MarkdownNote`
- `WanVideoVAELoader`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `DownloadAndLoadGIMMVFIModel`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `VHS_LoadVideo`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoTextEncodeCached`
- `CR Text`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `Int`
- `MathExpression|pysssss`
- `Int`
- `INTConstant`
- `Note`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `Sam2Segmentation`
- `SetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`

## 知识

覆盖率 **58%**（47/81）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GIMMVFI_interpolate`、`ImageConcatMulti`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`BlockifyMask`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoDecode`、`ImageBlend`、`GrowMask`、`DrawMaskOnImage`、`DownloadAndLoadSAM2Model`、`DrawViTPose`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`DownloadAndLoadGIMMVFIModel`、`INTConstant`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`、`CR Text`、`Int`、`MathExpression|pysssss`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`Sam2Segmentation`、`GetImageSizeAndCount`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
