---
key: 平台全量/wanvideo_WanAnimate_secnode_1978001589359235074.json
name: wanvideo_WanAnimate_secnode_1978001589359235074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wanvideo_WanAnimate_secnode_1978001589359235074.json
hash: 3f0a397eeae13558
coverage: 0.5
learned_at: 2026-11-14 01:20:11
nodes: [SetNode, SetNode, INTConstant, INTConstant, GetNode, GetNode, SetNode, MarkdownNote, SetNode, SetNode, SetNode, VHS_LoadVideo, GetNode, GetNode, GetImageSizeAndCount, VHS_VideoCombine, SetNode, SetNode, VHS_VideoCombine, PrimitiveInt, ImageFromBatch, GetNode, CoordinatePlotter, CoordinatePlotter, PreviewImage, GetNode, SetNode, DrawMaskOnImage, SetNode, VHS_VideoCombine, PreviewImage, WanVideoModelLoader, SetNode, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, MarkdownNote, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, GetNode, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoTextEncodeCached, OnnxDetectionModelLoader, DrawViTPose, PoseAndFaceDetection, PointsEditor, SeCModelLoader, SeCVideoSegmentation, GrowMaskWithBlur, BlockifyMask, ImageResizeKJv2, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoDecode]
patterns: []
missing: []
---

# 平台全量/wanvideo_WanAnimate_secnode_1978001589359235074.json

> 来源文件 `comfyui_library/workflows/平台全量/wanvideo_WanAnimate_secnode_1978001589359235074.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（70 个）：
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `SetNode`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `ImageFromBatch`
- `GetNode`
- `CoordinatePlotter`
- `CoordinatePlotter`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `DrawMaskOnImage`
- `SetNode`
- `VHS_VideoCombine`
- `PreviewImage`
- `WanVideoModelLoader`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSetBlockSwap`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `OnnxDetectionModelLoader`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `PointsEditor`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `GrowMaskWithBlur`
- `BlockifyMask`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoDecode`

## 知识

覆盖率 **50%**（35/70）

**有卡**：`INTConstant`、`VHS_LoadVideo`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`ImageFromBatch`、`CoordinatePlotter`、`DrawMaskOnImage`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`LoadImage`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`OnnxDetectionModelLoader`、`DrawViTPose`、`PoseAndFaceDetection`、`PointsEditor`、`SeCModelLoader`、`SeCVideoSegmentation`、`GrowMaskWithBlur`、`BlockifyMask`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
