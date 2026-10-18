---
key: 视频生成/图生视频/wan2.2_smoothmix_首尾帧_中间帧_自动提示词_2021521498401411074.json
name: wan2.2_smoothmix_首尾帧_中间帧_自动提示词_2021521498401411074.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2_smoothmix_首尾帧_中间帧_自动提示词_2021521498401411074.json
hash: 387f3dc5babf6f8f
coverage: 0.945946
learned_at: 2026-10-15 22:35:08
nodes: [ImageLoader, MultiplePathsInput, PathchSageAttentionKJ, CLIPTextEncode, easy int, WanVideoNAG, PathchSageAttentionKJ, KSamplerAdvanced, ImageLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionEncode, CLIPTextEncode, easy int, easy seed, ImageLoader, WanFirstMiddleLastFrameToVideo, Text Multiline, KSamplerAdvanced, easy seed, Text Multiline, CR Text Replace, Note, CLIPVisionLoader, CLIPLoader, UNETLoader, UNETLoader, VAELoader, easy showAnything, LayerUtility: PurgeVRAM, Qwen3_VQA, LayerUtility: PurgeVRAM, VAEDecode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2_smoothmix_首尾帧_中间帧_自动提示词_2021521498401411074.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2021521498401411074.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（37 个）：
- `ImageLoader`
- `MultiplePathsInput`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `easy int`
- `WanVideoNAG`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `ImageLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `easy int`
- `easy seed`
- `ImageLoader`
- `WanFirstMiddleLastFrameToVideo`
- `Text Multiline`
- `KSamplerAdvanced` ★核心
- `easy seed`
- `Text Multiline`
- `CR Text Replace`
- `Note`
- `CLIPVisionLoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `easy showAnything`
- `LayerUtility: PurgeVRAM`
- `Qwen3_VQA`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`ImageLoader`、`MultiplePathsInput`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`easy int`、`WanVideoNAG`、`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionEncode`、`easy seed`、`WanFirstMiddleLastFrameToVideo`、`Text Multiline`、`CR Text Replace`、`CLIPVisionLoader`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LayerUtility: PurgeVRAM`、`Qwen3_VQA`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、easy seed、CLIPVisionEncode
