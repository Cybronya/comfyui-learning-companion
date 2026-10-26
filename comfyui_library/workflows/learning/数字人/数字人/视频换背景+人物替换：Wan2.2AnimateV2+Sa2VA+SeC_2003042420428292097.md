---
key: 数字人/数字人/视频换背景+人物替换：Wan2.2AnimateV2+Sa2VA+SeC_2003042420428292097.json
name: 视频换背景+人物替换：Wan2.2AnimateV2+Sa2VA+SeC_2003042420428292097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/视频换背景+人物替换：Wan2.2AnimateV2+Sa2VA+SeC_2003042420428292097.json
hash: 5129e13bccb6b3f3
coverage: 0.440252
learned_at: 2026-10-26 02:05:15
nodes: [easy convertAnything, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoInfoLoaded, easy showAnything, easy showAnything, Int, Int, SetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, PoseAndFaceDetection, GetNode, GetNode, OnnxDetectionModelLoader, VHS_VideoCombine, SetNode, SDPoseOODLoader, YOLOModelLoader, SDPoseOODProcessor, GetNode, GetNode, SeCModelLoader, GetNode, SetNode, GetNode, ImageFromBatch, PreviewImage, GetNode, GetNode, GetNode, GetNode, GetNode, Int, GetNode, SetNode, DrawMaskOnImage, GetNode, GetNode, SetNode, Sa2VANodeTpl, WanVideoModelLoader, GetNode, GetNode, GetNode, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, SetNode, WanVideoVAELoader, SetNode, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, WanVideoTextEncodeCached, Evaluate Integers, Note, GetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoContextOptions, WanVideoSampler, SetNode, GetNode, Reroute, CoordinatePlotter, PreviewImage, CoordinatePlotter, Reroute, SetNode, SetNode, GetNode, ImageFromBatch, Int, Label (rgthree), PreviewImage, Reroute, PointsEditor, easy convertAnything, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, VHS_VideoInfoLoaded, easy showAnything, ImageResizeKJv2, PreviewImage, Int, Int, Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), workflow>Frame Padder-1, Mute / Bypass Repeater (rgthree), workflow>Frame Padder-2, Fast Bypasser (rgthree), Int, SetNode, Float, Int, SetNode, SetNode, SetNode, SetNode, Text, Note, Note, VHS_VideoCombine, Note, Note, Note, GrowMaskWithBlur, VHS_VideoCombine, GetNode, Note, Label (rgthree), Label (rgthree), Label (rgthree), BlockifyMask, easy cleanGpuUsed, SetNode, WanVideoLoraSelectMulti, GetNode, GetNode, SetNode, WanVideoDecode, Note, VHS_VideoCombine, Note, Note, AILab_MaskPreview, MaskPreview+, SeCVideoSegmentation, SetNode, GetNode, Note, easy showAnything, VHS_LoadVideo, LoadImage, VHS_VideoCombine, VHS_LoadVideo, Int]
patterns: []
missing: []
---

# 数字人/数字人/视频换背景+人物替换：Wan2.2AnimateV2+Sa2VA+SeC_2003042420428292097.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/视频换背景+人物替换：Wan2.2AnimateV2+Sa2VA+SeC_2003042420428292097.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（159 个）：
- `easy convertAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `easy showAnything`
- `Int`
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `VHS_VideoCombine`
- `SetNode`
- `SDPoseOODLoader`
- `YOLOModelLoader`
- `SDPoseOODProcessor`
- `GetNode`
- `GetNode`
- `SeCModelLoader`
- `GetNode`
- `SetNode`
- `GetNode`
- `ImageFromBatch`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `GetNode`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `Sa2VANodeTpl`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `WanVideoTextEncodeCached`
- `Evaluate Integers`
- `Note`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `SetNode`
- `GetNode`
- `Reroute`
- `CoordinatePlotter`
- `PreviewImage`
- `CoordinatePlotter`
- `Reroute`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageFromBatch`
- `Int`
- `Label (rgthree)`
- `PreviewImage`
- `Reroute`
- `PointsEditor`
- `easy convertAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `ImageResizeKJv2`
- `PreviewImage`
- `Int`
- `Int`
- `Fast Bypasser (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `workflow>Frame Padder-1`
- `Mute / Bypass Repeater (rgthree)`
- `workflow>Frame Padder-2`
- `Fast Bypasser (rgthree)`
- `Int`
- `SetNode`
- `Float`
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Text`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `Note`
- `GrowMaskWithBlur`
- `VHS_VideoCombine`
- `GetNode`
- `Note`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `BlockifyMask`
- `easy cleanGpuUsed`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoDecode`
- `Note`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `AILab_MaskPreview`
- `MaskPreview+`
- `SeCVideoSegmentation`
- `SetNode`
- `GetNode`
- `Note`
- `easy showAnything`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `Int`

## 知识

覆盖率 **44%**（70/159）

**有卡**：`easy convertAnything`、`VHS_VideoInfoLoaded`、`Int`、`ImageResizeKJv2`、`ImageConcatMulti`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`VHS_VideoCombine`、`SDPoseOODLoader`、`YOLOModelLoader`、`SDPoseOODProcessor`、`SeCModelLoader`、`ImageFromBatch`、`DrawMaskOnImage`、`Sa2VANodeTpl`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoTextEncodeCached`、`Evaluate Integers`、`CLIPVisionLoader`、`WanVideoContextOptions`、`WanVideoSampler`、`CoordinatePlotter`、`Label (rgthree)`、`PointsEditor`、`Fast Bypasser (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`workflow>Frame Padder-1`、`workflow>Frame Padder-2`、`Float`、`Text`、`GrowMaskWithBlur`、`BlockifyMask`、`easy cleanGpuUsed`、`WanVideoLoraSelectMulti`、`WanVideoDecode`、`AILab_MaskPreview`、`MaskPreview+`、`SeCVideoSegmentation`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
