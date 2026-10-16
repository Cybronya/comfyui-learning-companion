---
key: 视频生成/图生视频/官方万相wan2.2 首尾帧 极速版+自动扩词_1953122188666802177.json
name: 官方万相wan2.2 首尾帧 极速版+自动扩词_1953122188666802177.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1953122188666802177.json
hash: 9390ff052e8d998c
coverage: 0.957447
learned_at: 2026-10-15 22:31:04
nodes: [PathchSageAttentionKJ, CLIPLoader, VAELoader, CLIPVisionLoader, PathchSageAttentionKJ, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Wan22PromptSelector, LoadImage, LoadImage, WanVideoNAG, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, CLIPVisionEncode, WanFirstLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, SimpleMath+, VAEDecode, ImageResizeKJv2, ImageResizeKJ, Fast Groups Muter (rgthree), Reroute, PIP_StringConcatenation, RH_Captioner, RH_Captioner, TextConcat, CR Prompt Text, CR Prompt Text, JWStringConcat, RH_LLMAPI_NODE, VHS_VideoCombine, SimpleMath+, ImpactInt, ImpactInt, ImpactInt, ImpactInt, CR Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/官方万相wan2.2 首尾帧 极速版+自动扩词_1953122188666802177.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953122188666802177.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（47 个）：
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Wan22PromptSelector`
- `LoadImage`
- `LoadImage`
- `WanVideoNAG`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SimpleMath+`
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJ`
- `Fast Groups Muter (rgthree)`
- `Reroute`
- `PIP_StringConcatenation`
- `RH_Captioner`
- `RH_Captioner`
- `TextConcat`
- `CR Prompt Text`
- `CR Prompt Text`
- `JWStringConcat`
- `RH_LLMAPI_NODE`
- `VHS_VideoCombine`
- `SimpleMath+`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `CR Text`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（45/47）

**有卡**：`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`Wan22PromptSelector`、`LoadImage`、`WanVideoNAG`、`ModelSamplingSD3`、`CLIPTextEncode`、`CLIPVisionEncode`、`WanFirstLastFrameToVideo`、`KSamplerAdvanced`、`SimpleMath+`、`VAEDecode`、`ImageResizeKJv2`、`ImageResizeKJ`、`PIP_StringConcatenation`、`RH_Captioner`、`TextConcat`、`CR Prompt Text`、`JWStringConcat`、`RH_LLMAPI_NODE`、`VHS_VideoCombine`、`ImpactInt`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
