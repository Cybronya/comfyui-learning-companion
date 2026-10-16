---
key: 视频生成/图生视频/wan2.2首尾 版官方_1952339456634368002.json
name: wan2.2首尾 版官方_1952339456634368002.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952339456634368002.json
hash: 743dc6c82961ad33
coverage: 0.941176
learned_at: 2026-10-15 22:31:01
nodes: [CLIPLoader, VAELoader, VAEDecode, CreateVideo, CLIPVisionLoader, WanFirstLastFrameToVideo, CLIPVisionEncode, CLIPVisionEncode, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, UNETLoader, KSamplerAdvanced, ImageStitch, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, SaveVideo, KSamplerAdvanced, ModelSamplingSD3, WanVideoNAG, WanVideoNAG, LoadImage, LoadImage, RH_Captioner, easy showAnything, RH_Translator, CLIPTextEncode, CLIPTextEncode, LayerUtility: ImageMaskScaleAs, DF_Integer, SimpleMath+, easy showAnything]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2首尾 版官方_1952339456634368002.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952339456634368002.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `CreateVideo`
- `CLIPVisionLoader`
- `WanFirstLastFrameToVideo`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `ImageStitch`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `WanVideoNAG`
- `WanVideoNAG`
- `LoadImage`
- `LoadImage`
- `RH_Captioner`
- `easy showAnything`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageMaskScaleAs`
- `DF_Integer`
- `SimpleMath+`
- `easy showAnything`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（32/34）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`CreateVideo`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`CLIPVisionEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`ImageStitch`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveVideo`、`WanVideoNAG`、`LoadImage`、`RH_Captioner`、`RH_Translator`、`CLIPTextEncode`、`LayerUtility: ImageMaskScaleAs`、`DF_Integer`、`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
