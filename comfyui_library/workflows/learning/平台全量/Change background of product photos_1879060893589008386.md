---
key: 平台全量/Change background of product photos_1879060893589008386.json
name: Change background of product photos_1879060893589008386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Change background of product photos_1879060893589008386.json
hash: 550b56aec0401ed1
coverage: 0.74359
learned_at: 2026-11-14 00:22:10
nodes: [Reroute, PrimitiveNode, PrimitiveNode, LoadImage, Note, PreviewImage, TilePreprocessor, ControlNetApply, FreeU_V2, PreviewImage, KSampler, UpscaleModelLoader, VAEDecode, ImageUpscaleWithModel, VAEDecode, KSampler, ControlNetLoader, LeReS-DepthMapPreprocessor, PreviewImage, ControlNetApply, ControlNetLoader, CannyEdgePreprocessor, ControlNetApply, GroundingDinoSAMSegment (segment anything), InvertMask (segment anything), SAMLoader, GroundingDinoModelLoader (segment anything), MaskToImage, PreviewImage, PreviewImage, VAEEncodeForInpaint, CLIPTextEncode, CLIPTextEncode, RandomPrompt, CheckpointLoaderSimple, ControlNetLoader, PreviewImage, ImageScaleBy, SaveImage]
patterns: [controlnet]
missing: []
parameters: {"cfg": 7, "checkpoint": "Deliberate_v5 (SFW).safetensors", "controlnet_strength": 0.1, "denoise": 1, "sampler_name": "heunpp2", "scheduler": "normal", "seed": 313157175795980, "steps": 22}
---

# 平台全量/Change background of product photos_1879060893589008386.json

> 来源文件 `comfyui_library/workflows/平台全量/Change background of product photos_1879060893589008386.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `Reroute`
- `PrimitiveNode`
- `PrimitiveNode`
- `LoadImage`
- `Note`
- `PreviewImage`
- `TilePreprocessor`
- `ControlNetApply` ★核心
- `FreeU_V2`
- `PreviewImage`
- `KSampler` ★核心
- `UpscaleModelLoader`
- `VAEDecode` ★核心
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ControlNetLoader`
- `LeReS-DepthMapPreprocessor`
- `PreviewImage`
- `ControlNetApply` ★核心
- `ControlNetLoader`
- `CannyEdgePreprocessor`
- `ControlNetApply` ★核心
- `GroundingDinoSAMSegment (segment anything)`
- `InvertMask (segment anything)`
- `SAMLoader`
- `GroundingDinoModelLoader (segment anything)`
- `MaskToImage`
- `PreviewImage`
- `PreviewImage`
- `VAEEncodeForInpaint` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RandomPrompt`
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `PreviewImage`
- `ImageScaleBy`
- `SaveImage`

**识别到的模式**：controlnet

## 关键参数

- `controlnet_strength` = `0.1`
- `seed` = `313157175795980`
- `steps` = `22`
- `cfg` = `7`
- `sampler_name` = `heunpp2`
- `scheduler` = `normal`
- `denoise` = `1`
- `checkpoint` = `Deliberate_v5 (SFW).safetensors`

## 知识

覆盖率 **74%**（29/39）

**有卡**：`LoadImage`、`TilePreprocessor`、`ControlNetApply`、`FreeU_V2`、`KSampler`、`UpscaleModelLoader`、`VAEDecode`、`ImageUpscaleWithModel`、`ControlNetLoader`、`LeReS-DepthMapPreprocessor`、`CannyEdgePreprocessor`、`GroundingDinoSAMSegment (segment anything)`、`InvertMask (segment anything)`、`SAMLoader`、`GroundingDinoModelLoader (segment anything)`、`MaskToImage`、`VAEEncodeForInpaint`、`CLIPTextEncode`、`RandomPrompt`、`CheckpointLoaderSimple`、`ImageScaleBy`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CannyEdgePreprocessor、ControlNetApply、ControlNetLoader
