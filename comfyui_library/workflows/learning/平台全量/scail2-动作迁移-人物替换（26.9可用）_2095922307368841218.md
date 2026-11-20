---
key: 平台全量/scail2-动作迁移-人物替换（26.9可用）_2095922307368841218.json
name: scail2-动作迁移-人物替换（26.9可用）_2095922307368841218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/scail2-动作迁移-人物替换（26.9可用）_2095922307368841218.json
hash: ffadb82f9505c0df
coverage: 0.612245
learned_at: 2026-11-14 01:17:07
nodes: [CLIPTextEncode, BasicScheduler, ModelSamplingSD3, GetNode, GetNode, GetNode, VAELoader, KSamplerSelect, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, ImageResizeKJv2, GetNode, CheckpointLoaderSimple, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, VHS_VideoInfoLoaded, PreviewAny, SAM3_VideoTrack, SAM3_VideoTrack, CLIPTextEncode, CLIPTextEncode, SCAIL2SimpleVideo, SetNode, ImageColorMatch+, easy mathInt, PrimitiveInt, PrimitiveInt, WanChunkFeedForward, MiniMaxLowVRAMAttention, LoraLoaderModelOnly, DiffusionModelLoaderKJ, LoraLoaderModelOnly, PrimitiveInt, CLIPLoader, CLIPVisionLoader, VHS_VideoCombine, VHS_LoadVideo, ComfyNumberConvert, LoraLoaderModelOnly, LoraLoaderModelOnly, SAM3_TrackPreview, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/scail2-动作迁移-人物替换（26.9可用）_2095922307368841218.json

> 来源文件 `comfyui_library/workflows/平台全量/scail2-动作迁移-人物替换（26.9可用）_2095922307368841218.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（49 个）：
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `PreviewAny`
- `SAM3_VideoTrack`
- `SAM3_VideoTrack`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SCAIL2SimpleVideo`
- `SetNode`
- `ImageColorMatch+`
- `easy mathInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `WanChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `CLIPLoader`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `ComfyNumberConvert`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SAM3_TrackPreview`
- `LoadImage`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **61%**（30/49）

**有卡**：`CLIPTextEncode`、`BasicScheduler`、`ModelSamplingSD3`、`VAELoader`、`KSamplerSelect`、`ImageResizeKJv2`、`CheckpointLoaderSimple`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfoLoaded`、`SAM3_VideoTrack`、`SCAIL2SimpleVideo`、`ImageColorMatch+`、`easy mathInt`、`WanChunkFeedForward`、`MiniMaxLowVRAMAttention`、`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`、`CLIPLoader`、`CLIPVisionLoader`、`VHS_VideoCombine`、`VHS_LoadVideo`、`ComfyNumberConvert`、`SAM3_TrackPreview`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、KSamplerSelect
