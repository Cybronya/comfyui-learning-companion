---
key: 数字人/数字人/动作迁移人物替换WanAnimate2.2_1990379558673289217.json
name: 动作迁移人物替换WanAnimate2.2_1990379558673289217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/动作迁移人物替换WanAnimate2.2_1990379558673289217.json
hash: e5e0bf3c079d86fe
coverage: 0.5875
learned_at: 2026-10-26 02:00:42
nodes: [GetNode, GetNode, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, GIMMVFI_interpolate, GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, ImageConcatMulti, GetNode, SetNode, WanVideoClipVisionEncode, BlockifyMask, WanVideoTorchCompileSettings, WanVideoBlockSwap, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoDecode, GetNode, GetNode, GetNode, GrowMask, GetNode, DrawMaskOnImage, DownloadAndLoadSAM2Model, DrawViTPose, SetNode, GetNode, WanVideoVAELoader, WanVideoAnimateEmbeds, WanVideoSampler, GetNode, GetNode, DownloadAndLoadGIMMVFIModel, INTConstant, SetNode, SetNode, SetNode, WanVideoTextEncodeCached, CR Text, Int, MathExpression|pysssss, Int, INTConstant, PreviewImage, PreviewImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, OnnxDetectionModelLoader, PoseAndFaceDetection, Sam2Segmentation, SetNode, GetImageSizeAndCount, VHS_VideoCombine, MarkdownNote, INTConstant, INTConstant, LoadImage, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, PreviewImage, ImageBlend, VHS_VideoCombine, VHS_VideoCombine, SetNode, SetNode, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
---

# 数字人/数字人/动作迁移人物替换WanAnimate2.2_1990379558673289217.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/动作迁移人物替换WanAnimate2.2_1990379558673289217.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（80 个）：
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
- `WanVideoVAELoader`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `DownloadAndLoadGIMMVFIModel`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoTextEncodeCached`
- `CR Text`
- `Int`
- `MathExpression|pysssss`
- `Int`
- `INTConstant`
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
- `MarkdownNote`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `ImageBlend`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 知识

覆盖率 **59%**（47/80）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GIMMVFI_interpolate`、`ImageConcatMulti`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`BlockifyMask`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoDecode`、`GrowMask`、`DrawMaskOnImage`、`DownloadAndLoadSAM2Model`、`DrawViTPose`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`DownloadAndLoadGIMMVFIModel`、`INTConstant`、`WanVideoTextEncodeCached`、`CR Text`、`Int`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`Sam2Segmentation`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`LoadImage`、`LayerUtility: PurgeVRAM V2`、`ImageBlend`、`VHS_LoadVideo`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
