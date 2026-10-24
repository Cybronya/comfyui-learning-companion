---
key: 图片生成/图生图/😯Flux.1 depth_canny 深度_线稿模型+Redux参考_1914029719334125570.json
name: 😯Flux.1 depth_canny 深度_线稿模型+Redux参考_1914029719334125570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/😯Flux.1 depth_canny 深度_线稿模型+Redux参考_1914029719334125570.json
hash: 4d2e98ed124ccb85
coverage: 0.57377
learned_at: 2026-10-23 13:39:55
nodes: [FluxGuidance, SetNode, GetNode, SetNode, SetNode, SetNode, LoadImage, KSampler, LoadImage, RepeatLatentBatch, LoraLoaderModelOnly, UNETLoader, UNETLoader, AIO_Preprocessor, AIO_Preprocessor, GetNode, RH_Translator, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, SetNode, RH_LLMAPI_NODE, RH_LLMAPI_NODE, ShowText|pysssss, easy imageRemBg, easy cleanGpuUsed, easy seed, LoadImage, CR Text Concatenate, ImpactSwitch, DualCLIPLoader, Anything Everywhere, VAELoader, Anything Everywhere, VAEDecode, SetNode, GetNode, GetNode, InstructPixToPixConditioning, LayerUtility: ImageScaleByAspectRatio V2, StyleModelLoader, ReduxAdvanced, CLIPVisionLoader, PreviewImage, ConditioningZeroOut, CLIPTextEncode, CLIPTextEncode, ImpactSwitch, SetNode, LoraLoaderModelOnly, GetNode, GetNode, RebatchLatents, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, SetNode, ImpactSwitch, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "deis", "scheduler": "beta", "seed": 461090718920044, "steps": 20}
---

# 图片生成/图生图/😯Flux.1 depth_canny 深度_线稿模型+Redux参考_1914029719334125570.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/😯Flux.1 depth_canny 深度_线稿模型+Redux参考_1914029719334125570.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `FluxGuidance`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `KSampler` ★核心
- `LoadImage`
- `RepeatLatentBatch`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `GetNode`
- `RH_Translator`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `SetNode`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `easy imageRemBg`
- `easy cleanGpuUsed`
- `easy seed`
- `LoadImage`
- `CR Text Concatenate`
- `ImpactSwitch`
- `DualCLIPLoader`
- `Anything Everywhere`
- `VAELoader`
- `Anything Everywhere`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `InstructPixToPixConditioning`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `StyleModelLoader`
- `ReduxAdvanced`
- `CLIPVisionLoader`
- `PreviewImage`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImpactSwitch`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `RebatchLatents`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImpactSwitch`
- `SaveImage`

## 关键参数

- `seed` = `461090718920044`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **57%**（35/61）

**有卡**：`FluxGuidance`、`LoadImage`、`KSampler`、`RepeatLatentBatch`、`LoraLoaderModelOnly`、`UNETLoader`、`AIO_Preprocessor`、`RH_Translator`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_LLMAPI_NODE`、`easy imageRemBg`、`easy cleanGpuUsed`、`easy seed`、`CR Text Concatenate`、`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`InstructPixToPixConditioning`、`StyleModelLoader`、`ReduxAdvanced`、`CLIPVisionLoader`、`ConditioningZeroOut`、`CLIPTextEncode`、`RebatchLatents`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
