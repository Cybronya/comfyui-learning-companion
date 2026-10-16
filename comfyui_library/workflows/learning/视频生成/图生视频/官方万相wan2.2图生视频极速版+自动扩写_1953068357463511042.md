---
key: 视频生成/图生视频/官方万相wan2.2图生视频极速版+自动扩写_1953068357463511042.json
name: 官方万相wan2.2图生视频极速版+自动扩写_1953068357463511042.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1953068357463511042.json
hash: 6a0f0396e4d82b7c
coverage: 0.948718
learned_at: 2026-10-15 22:31:04
nodes: [CLIPLoader, PrimitiveInt, Int, Int, CR Prompt Text, CR Prompt Text, RH_Captioner, TextConcat, JWStringConcat, RH_LLMAPI_NODE, WanImageToVideo, VAEDecode, LayerUtility: PurgeVRAM V2, VAELoader, Wan22PromptSelector, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, CR Prompt Text, CLIPTextEncode, CLIPTextEncode, SimpleMath+, easy showAnything, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGZeroStar, CFGZeroStar, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, LoadImage, RHHiddenNodes, easy anythingIndexSwitch, Int, Int, Int]
patterns: []
missing: []
parameters: {"cfg": 14, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/官方万相wan2.2图生视频极速版+自动扩写_1953068357463511042.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953068357463511042.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（39 个）：
- `CLIPLoader`
- `PrimitiveInt`
- `Int`
- `Int`
- `CR Prompt Text`
- `CR Prompt Text`
- `RH_Captioner`
- `TextConcat`
- `JWStringConcat`
- `RH_LLMAPI_NODE`
- `WanImageToVideo`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAELoader`
- `Wan22PromptSelector`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGZeroStar`
- `CFGZeroStar`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `RHHiddenNodes`
- `easy anythingIndexSwitch`
- `Int`
- `Int`
- `Int`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `14`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（37/39）

**有卡**：`CLIPLoader`、`Int`、`CR Prompt Text`、`RH_Captioner`、`TextConcat`、`JWStringConcat`、`RH_LLMAPI_NODE`、`WanImageToVideo`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`VAELoader`、`Wan22PromptSelector`、`KSamplerAdvanced`、`VHS_VideoCombine`、`CLIPTextEncode`、`SimpleMath+`、`LoraLoaderModelOnly`、`CFGZeroStar`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`UNETLoader`、`LoadImage`、`RHHiddenNodes`、`easy anythingIndexSwitch`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
