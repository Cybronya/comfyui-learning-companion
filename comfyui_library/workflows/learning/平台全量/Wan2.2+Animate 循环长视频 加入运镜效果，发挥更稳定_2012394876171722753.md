---
key: 平台全量/Wan2.2+Animate 循环长视频 加入运镜效果，发挥更稳定_2012394876171722753.json
name: Wan2.2+Animate 循环长视频 加入运镜效果，发挥更稳定_2012394876171722753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2+Animate 循环长视频 加入运镜效果，发挥更稳定_2012394876171722753.json
hash: 351154297c314426
coverage: 0.536842
learned_at: 2026-11-14 01:05:48
nodes: [GetNode, CLIPVisionLoader, SetNode, WanVideoClipVisionEncode, SetNode, GetNode, PreviewImage, easy compare, GetNode, ImageResizeKJv2, GetNode, GetNode, GetNode, easy mathInt, SetNode, easy compare, ImageFromBatch, ImageBatch, RepeatImageBatch, RepeatImageBatch, easy mathInt, easy mathInt, easy mathInt, easy mathInt, BatchCount+, SetNode, easy mathInt, ImageBatch, easy mathInt, GetNode, LazySwitch1way, SetNode, SetNode, GetNode, GetNode, GetNode, OnnxDetectionModelLoader, SetNode, GetNode, WanVideoDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageFromBatch, PoseAndFaceDetection, VHS_VideoInfo, SetNode, SetNode, SetNode, easy cleanGpuUsed, DrawViTPose, easy cleanGpuUsed, SetNode, LazySwitch1way, easy mathInt, easy mathInt, BatchCount+, Int, SetNode, SetNode, SetNode, Int, Int, SetNode, RHHiddenNodes, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, SetNode, GetNode, easy cleanGpuUsed, WanVideoAnimateEmbeds, GetNode, easy mathInt, easy mathInt, GetNode, easy mathInt, SetNode, SetNode, RHHiddenNodes, WanVideoSampler, GetNode, WanVideoVAELoader, WanVideoTextEncodeCached, Int, LoadImage, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/Wan2.2+Animate 循环长视频 加入运镜效果，发挥更稳定_2012394876171722753.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2+Animate 循环长视频 加入运镜效果，发挥更稳定_2012394876171722753.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（95 个）：
- `GetNode`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `easy compare`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy mathInt`
- `SetNode`
- `easy compare`
- `ImageFromBatch`
- `ImageBatch`
- `RepeatImageBatch`
- `RepeatImageBatch`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `BatchCount+`
- `SetNode`
- `easy mathInt`
- `ImageBatch`
- `easy mathInt`
- `GetNode`
- `LazySwitch1way`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `SetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `PoseAndFaceDetection`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `DrawViTPose`
- `easy cleanGpuUsed`
- `SetNode`
- `LazySwitch1way`
- `easy mathInt`
- `easy mathInt`
- `BatchCount+`
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `Int`
- `SetNode`
- `RHHiddenNodes`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `SetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `easy mathInt`
- `easy mathInt`
- `GetNode`
- `easy mathInt`
- `SetNode`
- `SetNode`
- `RHHiddenNodes`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `Int`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 知识

覆盖率 **54%**（51/95）

**有卡**：`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`easy compare`、`ImageResizeKJv2`、`easy mathInt`、`ImageFromBatch`、`ImageBatch`、`RepeatImageBatch`、`BatchCount+`、`LazySwitch1way`、`OnnxDetectionModelLoader`、`WanVideoDecode`、`PoseAndFaceDetection`、`VHS_VideoInfo`、`easy cleanGpuUsed`、`DrawViTPose`、`Int`、`RHHiddenNodes`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`LoadImage`、`VHS_VideoCombine`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoSetLoRAs、CLIPVisionLoader
