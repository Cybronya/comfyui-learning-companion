---
key: 视频生成/图生视频/官方Wan2.2 lightx2v 图生视频_1949998290236563458.json
name: 官方Wan2.2 lightx2v 图生视频_1949998290236563458.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/官方Wan2.2 lightx2v 图生视频_1949998290236563458.json
hash: 053403972c99a17f
coverage: 0.59322
learned_at: 2026-10-15 22:30:51
nodes: [UNETLoader, UNETLoader, SetNode, SetNode, SetNode, SetNode, CLIPLoader, VAELoader, SetNode, SetNode, ModelSamplingSD3, SetNode, ModelSamplingSD3, SetNode, SetNode, GetNode, CLIPTextEncode, easy cleanGpuUsed, GetNode, VAEDecode, GetNode, GetNode, GetNode, SetNode, GetNode, Bjornulf_ShowStringText, GetNode, ShowText, SimpleCondition+, SetNode, GetNode, GetNode, GetNode, JWInteger, ImageResizeKJv2, PathchSageAttentionKJ, easy clearCacheAll, easy cleanGpuUsed, easy cleanGpuUsed, GetNode, GetNode, PathchSageAttentionKJ, easy cleanGpuUsed, easy clearCacheAll, JWInteger, JWInteger, LoraLoaderModelOnly, LoraLoaderModelOnly, WanImageToVideo, KSamplerAdvanced, KSamplerAdvanced, GetNode, CLIPVisionEncode, CLIPVisionLoader, VHS_VideoCombine, String, RH_LLMAPI_NODE, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/官方Wan2.2 lightx2v 图生视频_1949998290236563458.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949998290236563458.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（59 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `SetNode`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Bjornulf_ShowStringText`
- `GetNode`
- `ShowText`
- `SimpleCondition+`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `JWInteger`
- `ImageResizeKJv2`
- `PathchSageAttentionKJ`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `JWInteger`
- `JWInteger`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `String`
- `RH_LLMAPI_NODE`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **59%**（35/59）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`easy cleanGpuUsed`、`VAEDecode`、`Bjornulf_ShowStringText`、`ShowText`、`SimpleCondition+`、`JWInteger`、`ImageResizeKJv2`、`PathchSageAttentionKJ`、`easy clearCacheAll`、`LoraLoaderModelOnly`、`WanImageToVideo`、`KSamplerAdvanced`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VHS_VideoCombine`、`String`、`RH_LLMAPI_NODE`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
