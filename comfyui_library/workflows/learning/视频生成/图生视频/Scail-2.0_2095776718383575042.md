---
key: 视频生成/图生视频/Scail-2.0_2095776718383575042.json
name: Scail-2.0_2095776718383575042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Scail-2.0_2095776718383575042.json
hash: 2906f9c031609481
coverage: 0.644444
learned_at: 2026-10-17 01:09:49
nodes: [CheckpointLoaderSimple, SetNode, SetNode, GetNode, GetNode, CLIPLoader, LoraLoaderModelOnly, SAM3_VideoTrack, SAM3_VideoTrack, VAELoader, GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, SetNode, KSamplerSelect, SetNode, SetNode, ImageResizeKJv2, GetNode, GetNode, GetNode, VHS_VideoCombine, ModelSamplingSD3, PreviewAny, SetNode, Int, LayerUtility: ImageScaleByAspectRatio V2, Int, Int, DiffusionModelLoaderKJ, LoraLoaderModelOnly, ImageColorMatch+, BasicScheduler, VHS_VideoInfoLoaded, ZML_MergeText, CLIPTextEncode, CLIPTextEncode, VHS_LoadVideo, AILab_QwenVL, Text, SCAIL2SimpleVideo, CLIPTextEncode, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 视频生成/图生视频/Scail-2.0_2095776718383575042.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Scail-2.0_2095776718383575042.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（45 个）：
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SAM3_VideoTrack`
- `SAM3_VideoTrack`
- `VAELoader`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `PreviewAny`
- `SetNode`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `Int`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `ImageColorMatch+`
- `BasicScheduler`
- `VHS_VideoInfoLoaded`
- `ZML_MergeText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `AILab_QwenVL`
- `Text`
- `SCAIL2SimpleVideo`
- `CLIPTextEncode` ★核心
- `LoadImage`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **64%**（29/45）

**有卡**：`CheckpointLoaderSimple`、`CLIPLoader`、`LoraLoaderModelOnly`、`SAM3_VideoTrack`、`VAELoader`、`CLIPVisionLoader`、`KSamplerSelect`、`ImageResizeKJv2`、`VHS_VideoCombine`、`ModelSamplingSD3`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`DiffusionModelLoaderKJ`、`ImageColorMatch+`、`BasicScheduler`、`VHS_VideoInfoLoaded`、`ZML_MergeText`、`CLIPTextEncode`、`VHS_LoadVideo`、`AILab_QwenVL`、`Text`、`SCAIL2SimpleVideo`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、KSamplerSelect
