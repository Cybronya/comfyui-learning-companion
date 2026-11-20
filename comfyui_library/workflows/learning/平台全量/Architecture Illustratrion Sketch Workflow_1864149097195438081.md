---
key: 平台全量/Architecture Illustratrion Sketch Workflow_1864149097195438081.json
name: Architecture Illustratrion Sketch Workflow_1864149097195438081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Architecture Illustratrion Sketch Workflow_1864149097195438081.json
hash: 39ea7d988abda969
coverage: 0.935484
learned_at: 2026-11-14 00:19:24
nodes: [CLIPTextEncode, Zoe-DepthMapPreprocessor, AIO_Preprocessor, ConstrainImage|pysssss, VAEDecode, CR Aspect Ratio, Get Image Size, ColorMatch, UpscaleModelLoader, TilePreprocessor, CR Multi-ControlNet Stack, CheckpointLoaderSimple, VAELoader, CR Apply LoRA Stack, IPAdapterUnifiedLoader, WD14Tagger|pysssss, IPAdapter, CR Apply Multi-ControlNet, ToBasicPipe, PreviewImage, ImageUpscaleWithModel, SaveImage, PreviewImage, CR Simple Image Compare, SaveImage, CR Text, CR Text Concatenate, CLIPTextEncode, CR LoRA Stack, ImpactKSamplerBasicPipe, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 7, "checkpoint": "diffusionBrushEverythingSFWNSFWAll_v10.safetensors", "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 592174064200929, "steps": 30}
---

# 平台全量/Architecture Illustratrion Sketch Workflow_1864149097195438081.json

> 来源文件 `comfyui_library/workflows/平台全量/Architecture Illustratrion Sketch Workflow_1864149097195438081.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `CLIPTextEncode` ★核心
- `Zoe-DepthMapPreprocessor`
- `AIO_Preprocessor`
- `ConstrainImage|pysssss`
- `VAEDecode` ★核心
- `CR Aspect Ratio`
- `Get Image Size`
- `ColorMatch`
- `UpscaleModelLoader`
- `TilePreprocessor`
- `CR Multi-ControlNet Stack`
- `CheckpointLoaderSimple` ★核心
- `VAELoader`
- `CR Apply LoRA Stack`
- `IPAdapterUnifiedLoader`
- `WD14Tagger|pysssss`
- `IPAdapter`
- `CR Apply Multi-ControlNet`
- `ToBasicPipe`
- `PreviewImage`
- `ImageUpscaleWithModel`
- `SaveImage`
- `PreviewImage`
- `CR Simple Image Compare`
- `SaveImage`
- `CR Text`
- `CR Text Concatenate`
- `CLIPTextEncode` ★核心
- `CR LoRA Stack`
- `ImpactKSamplerBasicPipe` ★核心
- `LoadImage`

## 关键参数

- `checkpoint` = `diffusionBrushEverythingSFWNSFWAll_v10.safetensors`
- `seed` = `592174064200929`
- `steps` = `30`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`CLIPTextEncode`、`Zoe-DepthMapPreprocessor`、`AIO_Preprocessor`、`ConstrainImage|pysssss`、`VAEDecode`、`CR Aspect Ratio`、`Get Image Size`、`ColorMatch`、`UpscaleModelLoader`、`TilePreprocessor`、`CR Multi-ControlNet Stack`、`CheckpointLoaderSimple`、`VAELoader`、`CR Apply LoRA Stack`、`IPAdapterUnifiedLoader`、`WD14Tagger|pysssss`、`IPAdapter`、`CR Apply Multi-ControlNet`、`ToBasicPipe`、`ImageUpscaleWithModel`、`SaveImage`、`CR Simple Image Compare`、`CR Text`、`CR Text Concatenate`、`CR LoRA Stack`、`ImpactKSamplerBasicPipe`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CR Apply Multi-ControlNet、CR Multi-ControlNet Stack、Zoe-DepthMapPreprocessor
