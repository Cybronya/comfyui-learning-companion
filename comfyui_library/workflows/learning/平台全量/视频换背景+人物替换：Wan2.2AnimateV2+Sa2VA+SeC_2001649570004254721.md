---
key: 平台全量/视频换背景+人物替换：Wan2.2AnimateV2+Sa2VA+SeC_2001649570004254721.json
name: 视频换背景+人物替换：Wan2.2AnimateV2+Sa2VA+SeC_2001649570004254721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频换背景+人物替换：Wan2.2AnimateV2+Sa2VA+SeC_2001649570004254721.json
hash: 3d85e1e3d2919a7f
coverage: 0.450617
learned_at: 2026-11-14 02:38:35
nodes: [easy convertAnything, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoInfoLoaded, easy showAnything, easy showAnything, Int, Int, SetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, PoseAndFaceDetection, GetNode, GetNode, GetNode, OnnxDetectionModelLoader, VHS_VideoCombine, SetNode, SDPoseOODLoader, YOLOModelLoader, SDPoseOODProcessor, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, DrawMaskOnImage, GetNode, GetNode, SetNode, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, SetNode, WanVideoVAELoader, SetNode, Reroute, CoordinatePlotter, PreviewImage, CoordinatePlotter, Reroute, SetNode, SetNode, GetNode, ImageFromBatch, Int, Label (rgthree), PreviewImage, Reroute, PointsEditor, easy convertAnything, GetNode, GetNode, GetNode, GetNode, VHS_VideoInfoLoaded, easy showAnything, easy showAnything, ImageResizeKJv2, PreviewImage, Int, Int, Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), workflow>Frame Padder-1, Mute / Bypass Repeater (rgthree), workflow>Frame Padder-2, Fast Bypasser (rgthree), Int, SetNode, Float, Int, Int, SetNode, SetNode, SetNode, Note, Note, GrowMaskWithBlur, VHS_VideoCombine, GetNode, SetNode, Note, Label (rgthree), Label (rgthree), Label (rgthree), BlockifyMask, SeCVideoSegmentation, easy cleanGpuUsed, SetNode, WanVideoLoraSelectMulti, GetNode, GetNode, SetNode, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, Note, Note, LoadImage, SeCModelLoader, VHS_LoadVideo, GetNode, PreviewImage, ImageResizeKJv2, Note, VHS_LoadVideo, PreviewImage, AILab_MaskPreview, MaskPreview+, VHS_VideoCombine, SetNode, Text, WanVideoModelLoader, WanVideoBlockSwap, Note, SetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, AdaptiveWanVideoAnimateEmbeds, WanVideoSchedulerv2, WanVideoSamplerv2, WanVideoSamplerExtraArgs, GetNode, GetNode, GetNode, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoContextOptions, GetNode, GetNode, Note, GetNode, Sa2VANodeTpl, ImageFromBatch, Int, Note, Note]
patterns: []
missing: []
---

# 平台全量/视频换背景+人物替换：Wan2.2AnimateV2+Sa2VA+SeC_2001649570004254721.json

> 来源文件 `comfyui_library/workflows/平台全量/视频换背景+人物替换：Wan2.2AnimateV2+Sa2VA+SeC_2001649570004254721.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（162 个）：
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
- `GetNode`
- `OnnxDetectionModelLoader`
- `VHS_VideoCombine`
- `SetNode`
- `SDPoseOODLoader`
- `YOLOModelLoader`
- `SDPoseOODProcessor`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
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
- `VHS_VideoInfoLoaded`
- `easy showAnything`
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
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `Note`
- `GrowMaskWithBlur`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `Note`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `BlockifyMask`
- `SeCVideoSegmentation`
- `easy cleanGpuUsed`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `LoadImage`
- `SeCModelLoader`
- `VHS_LoadVideo`
- `GetNode`
- `PreviewImage`
- `ImageResizeKJv2`
- `Note`
- `VHS_LoadVideo`
- `PreviewImage`
- `AILab_MaskPreview`
- `MaskPreview+`
- `VHS_VideoCombine`
- `SetNode`
- `Text`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `Note`
- `SetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `AdaptiveWanVideoAnimateEmbeds`
- `WanVideoSchedulerv2`
- `WanVideoSamplerv2` ★核心
- `WanVideoSamplerExtraArgs` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `WanVideoContextOptions`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `Sa2VANodeTpl`
- `ImageFromBatch`
- `Int`
- `Note`
- `Note`

## 知识

覆盖率 **45%**（73/162）

**有卡**：`easy convertAnything`、`VHS_VideoInfoLoaded`、`Int`、`ImageResizeKJv2`、`ImageConcatMulti`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`VHS_VideoCombine`、`SDPoseOODLoader`、`YOLOModelLoader`、`SDPoseOODProcessor`、`DrawMaskOnImage`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`CoordinatePlotter`、`ImageFromBatch`、`Label (rgthree)`、`PointsEditor`、`Fast Bypasser (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`workflow>Frame Padder-1`、`workflow>Frame Padder-2`、`Float`、`GrowMaskWithBlur`、`BlockifyMask`、`SeCVideoSegmentation`、`easy cleanGpuUsed`、`WanVideoLoraSelectMulti`、`WanVideoDecode`、`LoadImage`、`SeCModelLoader`、`VHS_LoadVideo`、`AILab_MaskPreview`、`MaskPreview+`、`Text`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`AdaptiveWanVideoAnimateEmbeds`、`WanVideoSchedulerv2`、`WanVideoSamplerv2`、`WanVideoSamplerExtraArgs`、`WanVideoTeaCache`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`Sa2VANodeTpl`

**用到的条目**：LoadImage、WanVideoSamplerExtraArgs、WanVideoSamplerv2、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
