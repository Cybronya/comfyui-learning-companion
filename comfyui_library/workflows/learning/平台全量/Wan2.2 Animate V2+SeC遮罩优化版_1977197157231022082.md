---
key: 平台全量/Wan2.2 Animate V2+SeC遮罩优化版_1977197157231022082.json
name: Wan2.2 Animate V2+SeC遮罩优化版_1977197157231022082
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate V2+SeC遮罩优化版_1977197157231022082.json
hash: d1cb1cf4eb2562e1
coverage: 0.607843
learned_at: 2026-11-14 01:04:52
nodes: [OnnxDetectionModelLoader, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, CLIPVisionLoader, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoVAELoader, easy showAnything, GetNode, WanVideoSetLoRAs, DrawViTPose, SetNode, VHS_VideoCombine, SetNode, SetNode, PoseAndFaceDetection, VHS_VideoCombine, WanVideoTextEncodeCached, WanVideoSampler, LoadImage, ImageResize+, PreviewImage, WanVideoClipVisionEncode, SetNode, SetNode, GetNode, VHS_LoadVideo, GetNode, WanVideoLoraSelectMulti, MarkdownNote, PointsEditor, Note, WanVideoAnimateEmbeds, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, ImageConcanate, VHS_VideoCombine, SeCModelLoader, GrowMask, VHS_VideoCombine, BlockifyMask, DrawMaskOnImage, SeCVideoSegmentation]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate V2+SeC遮罩优化版_1977197157231022082.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate V2+SeC遮罩优化版_1977197157231022082.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（51 个）：
- `OnnxDetectionModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVAELoader`
- `easy showAnything`
- `GetNode`
- `WanVideoSetLoRAs`
- `DrawViTPose`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `LoadImage`
- `ImageResize+`
- `PreviewImage`
- `WanVideoClipVisionEncode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_LoadVideo`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `MarkdownNote`
- `PointsEditor`
- `Note`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `ImageConcanate`
- `VHS_VideoCombine`
- `SeCModelLoader`
- `GrowMask`
- `VHS_VideoCombine`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SeCVideoSegmentation`

## 知识

覆盖率 **61%**（31/51）

**有卡**：`OnnxDetectionModelLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`DrawViTPose`、`VHS_VideoCombine`、`PoseAndFaceDetection`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`LoadImage`、`ImageResize+`、`WanVideoClipVisionEncode`、`VHS_LoadVideo`、`WanVideoLoraSelectMulti`、`PointsEditor`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`SeCModelLoader`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`SeCVideoSegmentation`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
