---
key: 视频生成/图生视频/Wan2.2_Remin_V3 + Qwen3.5 图生视频_自动润色提示词_2035997613283086338.json
name: Wan2.2_Remin_V3 + Qwen3.5 图生视频_自动润色提示词_2035997613283086338.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2035997613283086338.json
hash: 1f2aa00ab3fdd0e8
coverage: 0.684211
learned_at: 2026-10-15 22:35:50
nodes: [VAELoader, SetNode, SetNode, GetNode, GetNode, VAEDecode, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, SetNode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, UNETLoader, UNETLoader, GetNode, CLIPTextEncode, GetNode, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, ImageResize+, GetNode, ttN concat, MathExpression|pysssss, SomethingToString, GetNode, SetNode, SetNode, VHS_VideoCombine, llama_cpp_instruct_adv, CLIPTextEncode, CR Text, easy showAnything, llama_cpp_parameters, llama_cpp_model_loader, Int, LoadImage, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "increment"}
---

# 视频生成/图生视频/Wan2.2_Remin_V3 + Qwen3.5 图生视频_自动润色提示词_2035997613283086338.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2035997613283086338.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `ImageResize+`
- `GetNode`
- `ttN concat`
- `MathExpression|pysssss`
- `SomethingToString`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `CLIPTextEncode` ★核心
- `CR Text`
- `easy showAnything`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `Int`
- `LoadImage`
- `CR Prompt Text`

## 关键参数

- `seed` = `disable`
- `steps` = `increment`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **68%**（26/38）

**有卡**：`VAELoader`、`VAEDecode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`PathchSageAttentionKJ`、`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`ImageResize+`、`ttN concat`、`MathExpression|pysssss`、`SomethingToString`、`VHS_VideoCombine`、`llama_cpp_instruct_adv`、`CR Text`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`Int`、`LoadImage`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1
