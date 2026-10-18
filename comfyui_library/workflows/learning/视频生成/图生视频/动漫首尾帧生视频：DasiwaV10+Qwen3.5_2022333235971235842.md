---
key: 视频生成/图生视频/动漫首尾帧生视频：DasiwaV10+Qwen3.5_2022333235971235842.json
name: 动漫首尾帧生视频：DasiwaV10+Qwen3.5_2022333235971235842.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动漫首尾帧生视频：DasiwaV10+Qwen3.5_2022333235971235842.json
hash: dc922587be2187a8
coverage: 0.402597
learned_at: 2026-10-15 22:35:10
nodes: [Float, SetNode, SetNode, SetNode, Int, SetNode, SetNode, SetNode, GetNode, CLIPVisionLoader, CLIPLoader, GetNode, GetNode, VHS_VideoCombine, VAELoader, GetNode, Int, MathExpression_UTK, easy clearCacheAll, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, SetNode, GetNode, CLIPVisionEncode, CLIPVisionEncode, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, Note, Note, SetNode, SetNode, llama_cpp_model_loader, GetNode, GetNode, SetNode, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, Text, Note, UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, SetNode, SetNode, GetNode, WanFirstLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, llama_cpp_instruct_adv, GetNode, llama_cpp_parameters, SetNode, ImageConcatMulti, Note, Note, LoadImage, LoadImage, Text]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/动漫首尾帧生视频：DasiwaV10+Qwen3.5_2022333235971235842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2022333235971235842.json`

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
- `GetNode`
- `CLIPVisionLoader`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
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
- `VAEDecode` ★核心
- `SetNode`
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
- `SetNode`
- `llama_cpp_model_loader`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `Text`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `llama_cpp_instruct_adv`
- `GetNode`
- `llama_cpp_parameters`
- `SetNode`
- `ImageConcatMulti`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
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

**有卡**：`Float`、`Int`、`CLIPVisionLoader`、`CLIPLoader`、`VHS_VideoCombine`、`VAELoader`、`MathExpression_UTK`、`easy clearCacheAll`、`CLIPTextEncode`、`VAEDecode`、`CLIPVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`llama_cpp_model_loader`、`Text`、`UNETLoader`、`ModelSamplingSD3`、`WanFirstLastFrameToVideo`、`KSamplerAdvanced`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`ImageConcatMulti`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
