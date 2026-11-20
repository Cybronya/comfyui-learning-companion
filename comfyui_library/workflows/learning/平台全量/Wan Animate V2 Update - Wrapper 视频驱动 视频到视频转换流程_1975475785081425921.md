---
key: 平台全量/Wan Animate V2 Update - Wrapper 视频驱动 视频到视频转换流程_1975475785081425921.json
name: Wan Animate V2 Update - Wrapper 视频驱动 视频到视频转换流程_1975475785081425921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan Animate V2 Update - Wrapper 视频驱动 视频到视频转换流程_1975475785081425921.json
hash: a641262281ea3821
coverage: 0.532468
learned_at: 2026-11-14 01:03:53
nodes: [WanVideoSampler, WanVideoDecode, WanVideoTorchCompileSettings, GetImageSizeAndCount, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoAnimateEmbeds, ImageResizeKJv2, ImageConcatMulti, WanVideoClipVisionEncode, VHS_VideoCombine, ImageConcatMulti, DrawMaskOnImage, Sam2Segmentation, BlockifyMask, WanVideoContextOptions, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, MarkdownNote, PoseAndFaceDetection, DrawViTPose, MarkdownNote, VHS_VideoCombine, GrowMaskWithBlur, SetNode, INTConstant, INTConstant, SetNode, SetNode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoVAELoader, CLIPVisionLoader, SetNode, LoadImage, Note, OnnxDetectionModelLoader, DownloadAndLoadSAM2Model, VHS_VideoCombine, Note, Label (rgthree), Note, Note, SetNode, WanVideoTextEncodeCached, easy textSwitch, Note, CR Text, ShowText|pysssss, AILab_MiniCPM_4_V_Advanced, GetNode, VHS_LoadVideo, GetImageSizeAndCount, SetNode, VHS_VideoCombine, GetNode, CreateVideo, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Wan Animate V2 Update - Wrapper 视频驱动 视频到视频转换流程_1975475785081425921.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan Animate V2 Update - Wrapper 视频驱动 视频到视频转换流程_1975475785081425921.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（77 个）：
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `GetImageSizeAndCount`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoAnimateEmbeds`
- `ImageResizeKJv2`
- `ImageConcatMulti`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `DrawMaskOnImage`
- `Sam2Segmentation`
- `BlockifyMask`
- `WanVideoContextOptions`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `MarkdownNote`
- `VHS_VideoCombine`
- `GrowMaskWithBlur`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `SetNode`
- `LoadImage`
- `Note`
- `OnnxDetectionModelLoader`
- `DownloadAndLoadSAM2Model`
- `VHS_VideoCombine`
- `Note`
- `Label (rgthree)`
- `Note`
- `Note`
- `SetNode`
- `WanVideoTextEncodeCached`
- `easy textSwitch`
- `Note`
- `CR Text`
- `ShowText|pysssss`
- `AILab_MiniCPM_4_V_Advanced`
- `GetNode`
- `VHS_LoadVideo`
- `GetImageSizeAndCount`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `CreateVideo`
- `VHS_VideoCombine`

## 知识

覆盖率 **53%**（41/77）

**有卡**：`WanVideoSampler`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`GetImageSizeAndCount`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoAnimateEmbeds`、`ImageResizeKJv2`、`ImageConcatMulti`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`DrawMaskOnImage`、`Sam2Segmentation`、`BlockifyMask`、`WanVideoContextOptions`、`PoseAndFaceDetection`、`DrawViTPose`、`GrowMaskWithBlur`、`INTConstant`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`LoadImage`、`OnnxDetectionModelLoader`、`DownloadAndLoadSAM2Model`、`Label (rgthree)`、`WanVideoTextEncodeCached`、`easy textSwitch`、`CR Text`、`AILab_MiniCPM_4_V_Advanced`、`VHS_LoadVideo`、`CreateVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
