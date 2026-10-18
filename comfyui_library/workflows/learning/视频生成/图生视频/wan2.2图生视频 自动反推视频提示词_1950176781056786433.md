---
key: 视频生成/图生视频/wan2.2图生视频 自动反推视频提示词_1950176781056786433.json
name: wan2.2图生视频 自动反推视频提示词_1950176781056786433.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频 自动反推视频提示词_1950176781056786433.json
hash: 7960907c9a978f5b
coverage: 0.931034
learned_at: 2026-10-15 22:30:53
nodes: [UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, VAELoader, CLIPTextEncode, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, TextCombinerSix, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, easy seed, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, WanImageToVideo, ImageResizeKJv2, Wan22PromptSelector, VHS_VideoCombine, Text, Note, LoadImage, ShowText, RH_LLMAPI_NODE, Note]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2图生视频 自动反推视频提示词_1950176781056786433.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950176781056786433.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `TextCombinerSix`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `easy seed`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `ImageResizeKJv2`
- `Wan22PromptSelector`
- `VHS_VideoCombine`
- `Text`
- `Note`
- `LoadImage`
- `ShowText`
- `RH_LLMAPI_NODE`
- `Note`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`TextCombinerSix`、`LayerUtility: PurgeVRAM`、`easy seed`、`VAEDecode`、`KSamplerAdvanced`、`WanImageToVideo`、`ImageResizeKJv2`、`Wan22PromptSelector`、`VHS_VideoCombine`、`Text`、`LoadImage`、`ShowText`、`RH_LLMAPI_NODE`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
