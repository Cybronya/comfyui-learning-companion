---
key: 视频生成/图生视频/【LHX】Wan2.2图生视频_2067148001327542273.json
name: 【LHX】Wan2.2图生视频_2067148001327542273.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067148001327542273.json
hash: b9a49819d1e018fb
coverage: 0.84375
learned_at: 2026-10-15 22:39:57
nodes: [CLIPLoader, CR Text, PreviewAny, RH_LLMAPI_Pro_Node, UNETLoader, Note, Int, Note, Note, Note, CLIPTextEncode, CLIPTextEncode, Int, Int, Int, VAELoader, VAEDecode, easy cleanGpuUsed, UNETLoader, FL_RIFE, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, CR Text, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, WanImageToVideo, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/【LHX】Wan2.2图生视频_2067148001327542273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067148001327542273.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（32 个）：
- `CLIPLoader`
- `CR Text`
- `PreviewAny`
- `RH_LLMAPI_Pro_Node`
- `UNETLoader` ★核心
- `Note`
- `Int`
- `Note`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Int`
- `Int`
- `Int`
- `VAELoader`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `FL_RIFE`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `CR Text`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanImageToVideo`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（27/32）

**有卡**：`CLIPLoader`、`CR Text`、`RH_LLMAPI_Pro_Node`、`UNETLoader`、`Int`、`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`easy cleanGpuUsed`、`FL_RIFE`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanImageToVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
