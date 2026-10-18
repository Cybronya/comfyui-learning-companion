---
key: 视频生成/图生视频/首尾帧生视频DasiwaV10+Qwen3.5（动漫优化）_2046075077883600898.json
name: 首尾帧生视频DasiwaV10+Qwen3.5（动漫优化）_2046075077883600898.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧生视频DasiwaV10+Qwen3.5（动漫优化）_2046075077883600898.json
hash: 61cf6889be7a2569
coverage: 0.402597
learned_at: 2026-10-15 22:36:54
nodes: [Float, SetNode, SetNode, SetNode, Int, SetNode, SetNode, SetNode, CLIPVisionLoader, CLIPLoader, VAELoader, GetNode, Int, MathExpression_UTK, easy clearCacheAll, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionEncode, CLIPVisionEncode, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, Note, Note, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, Note, ModelSamplingSD3, ModelSamplingSD3, SetNode, SetNode, GetNode, WanFirstLastFrameToVideo, KSamplerAdvanced, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, llama_cpp_parameters, SetNode, ImageConcatMulti, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, SetNode, UNETLoader, UNETLoader, Text, llama_cpp_model_loader, llama_cpp_instruct_adv, LoadImage, LoadImage, GetNode, GetNode, GetNode, SetNode, VAEDecode, GetNode, KSamplerAdvanced, VHS_VideoCombine, easy showAnything, Text]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧生视频DasiwaV10+Qwen3.5（动漫优化）_2046075077883600898.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046075077883600898.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（77 个）：
- `Float`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `Int`
- `MathExpression_UTK`
- `easy clearCacheAll`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `Note`
- `Note`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `llama_cpp_parameters`
- `SetNode`
- `ImageConcatMulti`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Text`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `easy showAnything`
- `Text`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **40%**（31/77）

**有卡**：`Float`、`Int`、`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`MathExpression_UTK`、`easy clearCacheAll`、`CLIPTextEncode`、`CLIPVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingSD3`、`WanFirstLastFrameToVideo`、`KSamplerAdvanced`、`llama_cpp_parameters`、`ImageConcatMulti`、`UNETLoader`、`Text`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`LoadImage`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
