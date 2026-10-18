---
key: 视频生成/图生视频/连贯动作图生视频——smoothMix_Wan2.2+qwem3提示词_2027044559796047873.json
name: 连贯动作图生视频——smoothMix_Wan2.2+qwem3提示词_2027044559796047873.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/连贯动作图生视频——smoothMix_Wan2.2+qwem3提示词_2027044559796047873.json
hash: 28d08bad6547ff86
coverage: 0.744681
learned_at: 2026-10-15 22:35:16
nodes: [VAELoader, SetNode, CLIPLoader, SetNode, WanImageToVideo, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, VAEDecode, ImageResize+, PathchSageAttentionKJ, UNETLoader, wanBlockSwap, LoraLoaderModelOnly, UNETLoader, wanBlockSwap, CLIPTextEncode, easy showAnything, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, LoraLoaderModelOnly, SetNode, SetNode, KSamplerAdvanced, LoadImage, CR Prompt Text, KSamplerAdvanced, Qwen3_VQA, VHS_VideoCombine, LayerUtility: PurgeVRAM, SetNode, TextConcat, CR Prompt Text, MathExpression|pysssss, SomethingToString, CR Prompt Text, CR Prompt Text, easy showAnything, CR Prompt Text, CR Prompt Text, Int]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "increment"}
---

# 视频生成/图生视频/连贯动作图生视频——smoothMix_Wan2.2+qwem3提示词_2027044559796047873.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2027044559796047873.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（47 个）：
- `VAELoader`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `WanImageToVideo`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ImageResize+`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `CR Prompt Text`
- `KSamplerAdvanced` ★核心
- `Qwen3_VQA`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `TextConcat`
- `CR Prompt Text`
- `MathExpression|pysssss`
- `SomethingToString`
- `CR Prompt Text`
- `CR Prompt Text`
- `easy showAnything`
- `CR Prompt Text`
- `CR Prompt Text`
- `Int`

## 关键参数

- `seed` = `disable`
- `steps` = `increment`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **74%**（35/47）

**有卡**：`VAELoader`、`CLIPLoader`、`WanImageToVideo`、`CLIPTextEncode`、`VAEDecode`、`ImageResize+`、`PathchSageAttentionKJ`、`UNETLoader`、`wanBlockSwap`、`LoraLoaderModelOnly`、`LayerUtility: PurgeVRAM`、`ModelSamplingSD3`、`KSamplerAdvanced`、`LoadImage`、`CR Prompt Text`、`Qwen3_VQA`、`VHS_VideoCombine`、`TextConcat`、`MathExpression|pysssss`、`SomethingToString`、`Int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
