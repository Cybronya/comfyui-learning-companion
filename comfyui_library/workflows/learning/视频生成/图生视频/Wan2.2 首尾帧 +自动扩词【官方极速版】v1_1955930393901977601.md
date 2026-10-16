---
key: 视频生成/图生视频/Wan2.2 首尾帧 +自动扩词【官方极速版】v1_1955930393901977601.json
name: Wan2.2 首尾帧 +自动扩词【官方极速版】v1_1955930393901977601.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1955930393901977601.json
hash: cfecd5567d9e3590
coverage: 0.959184
learned_at: 2026-10-15 22:31:10
nodes: [PathchSageAttentionKJ, CLIPLoader, VAELoader, CLIPVisionLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, WanVideoNAG, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, CLIPVisionEncode, ImageResizeKJv2, ImageResizeKJ, PIP_StringConcatenation, RH_Captioner, RH_Captioner, TextConcat, CR Prompt Text, CR Prompt Text, JWStringConcat, SimpleMath+, ImpactInt, ImpactInt, ModelSamplingSD3, ImpactInt, SimpleMath+, LoadImage, LoadImage, VHS_VideoCombine, Reroute, CR Text, Fast Groups Muter (rgthree), CreateVideo, PreViewVideo, ImpactInt, KSamplerAdvanced, KSamplerAdvanced, RH_LLMAPI_NODE, UNETLoader, UNETLoader, Wan22PromptSelector, VAEDecode, WanFirstLastFrameToVideo]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 首尾帧 +自动扩词【官方极速版】v1_1955930393901977601.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955930393901977601.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（49 个）：
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanVideoNAG`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `ImageResizeKJv2`
- `ImageResizeKJ`
- `PIP_StringConcatenation`
- `RH_Captioner`
- `RH_Captioner`
- `TextConcat`
- `CR Prompt Text`
- `CR Prompt Text`
- `JWStringConcat`
- `SimpleMath+`
- `ImpactInt`
- `ImpactInt`
- `ModelSamplingSD3`
- `ImpactInt`
- `SimpleMath+`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `Reroute`
- `CR Text`
- `Fast Groups Muter (rgthree)`
- `CreateVideo`
- `PreViewVideo`
- `ImpactInt`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `RH_LLMAPI_NODE`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Wan22PromptSelector`
- `VAEDecode` ★核心
- `WanFirstLastFrameToVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（47/49）

**有卡**：`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`LoraLoaderModelOnly`、`WanVideoNAG`、`ModelSamplingSD3`、`CLIPTextEncode`、`CLIPVisionEncode`、`ImageResizeKJv2`、`ImageResizeKJ`、`PIP_StringConcatenation`、`RH_Captioner`、`TextConcat`、`CR Prompt Text`、`JWStringConcat`、`SimpleMath+`、`ImpactInt`、`LoadImage`、`VHS_VideoCombine`、`CR Text`、`CreateVideo`、`PreViewVideo`、`KSamplerAdvanced`、`RH_LLMAPI_NODE`、`UNETLoader`、`Wan22PromptSelector`、`VAEDecode`、`WanFirstLastFrameToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
