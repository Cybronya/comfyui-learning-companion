---
key: 平台全量/Wan2.2 Animate V2视频人物替换+SeC遮罩最新版_2028100957145403393.json
name: Wan2.2 Animate V2视频人物替换+SeC遮罩最新版_2028100957145403393
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate V2视频人物替换+SeC遮罩最新版_2028100957145403393.json
hash: e5d64a36f39b3643
coverage: 0.441176
learned_at: 2026-11-14 01:04:53
nodes: [SetNode, SetNode, GrowMask, VHS_VideoCombine, WanVideoBlockSwap, VHS_LoadVideo, WanVideoAnimateEmbeds, PreviewImage, SetNode, ImageResize+, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, SetNode, SetNode, SetNode, DrawViTPose, VHS_VideoCombine, PoseAndFaceDetection, GetNode, GetNode, SetNode, VHS_VideoCombine, GetNode, OnnxDetectionModelLoader, ImageConcanate, SetNode, GetNode, GetNode, GetNode, GetNode, SeCModelLoader, SeCVideoSegmentation, WanVideoLoraSelectMulti, WanVideoVAELoader, GetNode, WanVideoModelLoader, SetNode, SetNode, BlockifyMask, SetNode, SetNode, DrawMaskOnImage, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, WanVideoTextEncodeCached, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, CLIPVisionLoader, GetNode, GetNode, AdaptiveWanVideoAnimateEmbeds, WanVideoDecode, GetNode, VHS_VideoCombine, GetNode, VHS_VideoCombine, PointsEditor, LoadImage, Note, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate V2视频人物替换+SeC遮罩最新版_2028100957145403393.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate V2视频人物替换+SeC遮罩最新版_2028100957145403393.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（68 个）：
- `SetNode`
- `SetNode`
- `GrowMask`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `WanVideoAnimateEmbeds`
- `PreviewImage`
- `SetNode`
- `ImageResize+`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `DrawViTPose`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `OnnxDetectionModelLoader`
- `ImageConcanate`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `GetNode`
- `WanVideoModelLoader`
- `SetNode`
- `SetNode`
- `BlockifyMask`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `AdaptiveWanVideoAnimateEmbeds`
- `WanVideoDecode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `PointsEditor`
- `LoadImage`
- `Note`
- `MarkdownNote`

## 知识

覆盖率 **44%**（30/68）

**有卡**：`GrowMask`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`WanVideoAnimateEmbeds`、`ImageResize+`、`LayerUtility: ImageScaleByAspectRatio V2`、`DrawViTPose`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`ImageConcanate`、`SeCModelLoader`、`SeCVideoSegmentation`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoModelLoader`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`AdaptiveWanVideoAnimateEmbeds`、`WanVideoDecode`、`PointsEditor`、`LoadImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
