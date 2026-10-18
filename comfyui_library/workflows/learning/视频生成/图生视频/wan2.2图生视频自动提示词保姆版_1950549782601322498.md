---
key: 视频生成/图生视频/wan2.2图生视频自动提示词保姆版_1950549782601322498.json
name: wan2.2图生视频自动提示词保姆版_1950549782601322498.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频自动提示词保姆版_1950549782601322498.json
hash: 2f51c5c1aafc412b
coverage: 0.916667
learned_at: 2026-10-15 22:30:55
nodes: [RH_LLMAPI_NODE, VAEDecode, CR Text, SaveVideo, LoadImage, ShowText|pysssss, CLIPTextEncode, KSamplerAdvanced, CreateVideo, LayerUtility: ImageScaleByAspectRatio V2, PathchSageAttentionKJ, CFGZeroStar, CLIPTextEncode, ModelSamplingSD3, WanImageToVideo, PreviewImage, KSamplerAdvanced, ModelSamplingSD3, easy cleanGpuUsed, easy cleanGpuUsed, UNETLoader, UNETLoader, CLIPLoader, VAELoader]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2图生视频自动提示词保姆版_1950549782601322498.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950549782601322498.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `RH_LLMAPI_NODE`
- `VAEDecode` ★核心
- `CR Text`
- `SaveVideo`
- `LoadImage`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CreateVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PathchSageAttentionKJ`
- `CFGZeroStar`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `WanImageToVideo`
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`RH_LLMAPI_NODE`、`VAEDecode`、`CR Text`、`SaveVideo`、`LoadImage`、`CLIPTextEncode`、`KSamplerAdvanced`、`CreateVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`PathchSageAttentionKJ`、`CFGZeroStar`、`ModelSamplingSD3`、`WanImageToVideo`、`easy cleanGpuUsed`、`UNETLoader`、`CLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
