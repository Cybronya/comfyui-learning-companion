---
key: 视频生成/文生视频/Wan 2.2-SVI 2.0 Pro-十秒_2015412503383117826.json
name: Wan 2.2-SVI 2.0 Pro-十秒_2015412503383117826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.2-SVI 2.0 Pro-十秒_2015412503383117826.json
hash: 4d52f65339378ec5
coverage: 0.516129
learned_at: 2026-10-10 23:06:15
nodes: [SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, KSamplerAdvanced, KSamplerAdvanced, SetNode, SetNode, INTConstant, INTConstant, GetNode, GetNode, KSamplerAdvanced, CLIPTextEncode, GetNode, GetNode, GetNode, VAEEncode, SetNode, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, ShowText|pysssss, LoraLoaderModelOnly, GetNode, CLIPLoader, KSamplerAdvanced, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoadImage, VAEDecode, DuckHideNode, SaveImage, PreviewImage, VAEDecode, PreviewImage, easy promptLine, LayerUtility: ImageScaleByAspectRatio V2, Int, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, PreviewImage, easy indexAnything, ttN text, ttN text, ImageBatch, ImageBatchExtendWithOverlap, WanImageToVideoSVIPro, WanImageToVideoSVIPro]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy indexAnything, ttN text, ttN text, easy promptLine]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy indexAnything` 知识库中没有该节点类型的任何知识, 次要节点 `ttN text` 知识库中没有该节点类型的任何知识, 次要节点 `ttN text` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
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

覆盖率 **52%**（32/62）

**有卡**：`CLIPTextEncode`、`LoraLoaderModelOnly`、`VAELoader`、`KSamplerAdvanced`、`INTConstant`、`VAEEncode`、`CLIPLoader`、`VHS_VideoCombine`、`LoadImage`、`VAEDecode`、`DuckHideNode`、`SaveImage`、`Int`、`DiffusionModelLoaderKJ`、`ImageBatch`、`ImageBatchExtendWithOverlap`、`WanImageToVideoSVIPro`

**缺卡**（5）：`LayerUtility: ImageScaleByAspectRatio V2`、`easy indexAnything`、`ttN text`、`ttN text`、`easy promptLine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy indexAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `ttN text` 知识库中没有该节点类型的任何知识
- 次要节点 `ttN text` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
