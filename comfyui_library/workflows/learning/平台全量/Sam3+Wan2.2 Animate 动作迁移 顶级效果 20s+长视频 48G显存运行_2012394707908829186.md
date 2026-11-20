---
key: 平台全量/Sam3+Wan2.2 Animate 动作迁移 顶级效果 20s+长视频 48G显存运行_2012394707908829186.json
name: Sam3+Wan2.2 Animate 动作迁移 顶级效果 20s+长视频 48G显存运行_2012394707908829186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Sam3+Wan2.2 Animate 动作迁移 顶级效果 20s+长视频 48G显存运行_2012394707908829186.json
hash: e71e2c62bd21b5e5
coverage: 0.965517
learned_at: 2026-11-14 00:56:49
nodes: [WanVideoBlockSwap, WanVideoLoraSelectMulti, CLIPVisionLoader, ImageResizeKJv2, PreviewImage, INTConstant, INTConstant, VHS_VideoInfo, WanVideoTextEncodeSingle, WanVideoSampler, WanVideoContextOptions, WanVideoDecode, VHS_VideoCombine, LoadWanVideoT5TextEncoder, PoseAndFaceDetection, DrawViTPose, ColorToMask, SDPoseOODProcessor, SDPoseOODLoader, WanVideoModelLoader, WanVideoVAELoader, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, OnnxDetectionModelLoader, ImageFromBatch, VHS_LoadVideo, LayerUtility: ImageBlend V2, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Sam3+Wan2.2 Animate 动作迁移 顶级效果 20s+长视频 48G显存运行_2012394707908829186.json

> 来源文件 `comfyui_library/workflows/平台全量/Sam3+Wan2.2 Animate 动作迁移 顶级效果 20s+长视频 48G显存运行_2012394707908829186.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（29 个）：
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `VHS_VideoInfo`
- `WanVideoTextEncodeSingle`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `ColorToMask`
- `SDPoseOODProcessor`
- `SDPoseOODLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `OnnxDetectionModelLoader`
- `ImageFromBatch`
- `VHS_LoadVideo`
- `LayerUtility: ImageBlend V2`
- `LoadImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`ImageResizeKJv2`、`INTConstant`、`VHS_VideoInfo`、`WanVideoTextEncodeSingle`、`WanVideoSampler`、`WanVideoContextOptions`、`WanVideoDecode`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`PoseAndFaceDetection`、`DrawViTPose`、`ColorToMask`、`SDPoseOODProcessor`、`SDPoseOODLoader`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`OnnxDetectionModelLoader`、`ImageFromBatch`、`VHS_LoadVideo`、`LayerUtility: ImageBlend V2`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeSingle、WanVideoVAELoader、WanVideoLoraSelectMulti
