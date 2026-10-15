---
key: 视频生成/文生视频/Wan 2.2-SVI 2.0 Pro-十秒_2015412503383117826.json
name: Wan 2.2-SVI 2.0 Pro-十秒_2015412503383117826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.2-SVI 2.0 Pro-十秒_2015412503383117826.json
hash: 4d52f65339378ec5
coverage: 0.596774
learned_at: 2026-10-15 22:47:06
nodes: [SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, KSamplerAdvanced, KSamplerAdvanced, SetNode, SetNode, INTConstant, INTConstant, GetNode, GetNode, KSamplerAdvanced, CLIPTextEncode, GetNode, GetNode, GetNode, VAEEncode, SetNode, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, ShowText|pysssss, LoraLoaderModelOnly, GetNode, CLIPLoader, KSamplerAdvanced, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoadImage, VAEDecode, DuckHideNode, SaveImage, PreviewImage, VAEDecode, PreviewImage, easy promptLine, LayerUtility: ImageScaleByAspectRatio V2, Int, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, PreviewImage, easy indexAnything, ttN text, ttN text, ImageBatch, ImageBatchExtendWithOverlap, WanImageToVideoSVIPro, WanImageToVideoSVIPro]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan 2.2-SVI 2.0 Pro-十秒_2015412503383117826.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan 2.2-SVI 2.0 Pro-十秒_2015412503383117826.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `VAEDecode` ★核心
- `DuckHideNode`
- `SaveImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `easy promptLine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `PreviewImage`
- `easy indexAnything`
- `ttN text`
- `ttN text`
- `ImageBatch`
- `ImageBatchExtendWithOverlap`
- `WanImageToVideoSVIPro`
- `WanImageToVideoSVIPro`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **60%**（37/62）

**有卡**：`CLIPTextEncode`、`LoraLoaderModelOnly`、`VAELoader`、`KSamplerAdvanced`、`INTConstant`、`VAEEncode`、`CLIPLoader`、`VHS_VideoCombine`、`LoadImage`、`VAEDecode`、`DuckHideNode`、`SaveImage`、`easy promptLine`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`DiffusionModelLoaderKJ`、`easy indexAnything`、`ttN text`、`ImageBatch`、`ImageBatchExtendWithOverlap`、`WanImageToVideoSVIPro`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode
