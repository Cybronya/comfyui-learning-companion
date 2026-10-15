---
key: 视频生成/文生视频/templates_mjm_looped_restyler+全节点注释_2055474470340571137.json
name: templates_mjm_looped_restyler+全节点注释_2055474470340571137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/templates_mjm_looped_restyler+全节点注释_2055474470340571137.json
hash: 710d35082f432714
coverage: 0.511111
learned_at: 2026-10-15 22:47:32
nodes: [SaveVideo, SplitImageWithAlpha, ImageBatch, GetVideoComponents, CreateVideo, GetVideoComponents, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, WanFirstLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, CLIPTextEncode, CreateVideo, GetImageSizeAndCount, ImageScaleToTotalPixels, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, WanFirstLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, UNETLoader, CreateVideo, RH_LLMAPI_Pro_Node, ImageStitch, RH_LLMAPI_Pro_Node, ImageScaleToTotalPixels, RH_RhartImageG2ImageToImage, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/templates_mjm_looped_restyler+全节点注释_2055474470340571137.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/templates_mjm_looped_restyler+全节点注释_2055474470340571137.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（90 个）：
- `SaveVideo`
- `SplitImageWithAlpha`
- `ImageBatch`
- `GetVideoComponents`
- `CreateVideo`
- `GetVideoComponents`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `GetImageSizeAndCount`
- `ImageScaleToTotalPixels`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CreateVideo`
- `RH_LLMAPI_Pro_Node`
- `ImageStitch`
- `RH_LLMAPI_Pro_Node`
- `ImageScaleToTotalPixels`
- `RH_RhartImageG2ImageToImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **51%**（46/90）

**有卡**：`SaveVideo`、`SplitImageWithAlpha`、`ImageBatch`、`GetVideoComponents`、`CreateVideo`、`CLIPTextEncode`、`ModelSamplingSD3`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`WanFirstLastFrameToVideo`、`KSamplerAdvanced`、`VAEDecode`、`GetImageSizeAndCount`、`ImageScaleToTotalPixels`、`RH_LLMAPI_Pro_Node`、`ImageStitch`、`RH_RhartImageG2ImageToImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
