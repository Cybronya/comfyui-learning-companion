---
key: 视频生成/文生视频/wan2.1图生视频（自动提示词）+视频高清放大_1922961501655920642.json
name: wan2.1图生视频（自动提示词）+视频高清放大_1922961501655920642.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1922961501655920642.json
hash: 2ca0b7c33ae97347
coverage: 0.893617
learned_at: 2026-10-15 22:43:24
nodes: [CLIPTextEncode, CLIPTextEncode, VAELoader, KSampler, EmptyHunyuanLatentVideo, ModelSamplingSD3, CLIPTextEncode, LayerMask: LoadFlorence2Model, LayerUtility: Florence2Image2Prompt, LoadImage, easy cleanGpuUsed, ShowText|pysssss, LayerMask: LoadFlorence2Model, CLIPTextEncode, LayerUtility: Florence2Image2Prompt, ShowText|pysssss, ShowText, CLIPVisionLoader, CLIPLoader, WanVideoTeaCacheKJ, VAELoader, KSampler, ModelSamplingSD3, CLIPVisionEncode, easy imageSize, LoadImage, VHS_VideoCombine, ImageResizeKJ, VAEDecode, WanImageToVideo, CLIPLoader, WanVideoTeaCacheKJ, LayerUtility: PurgeVRAM, VHS_VideoCombine, UpscaleModelLoader, ImageScale, ImageUpscaleWithModel, LayerUtility: PurgeVRAM, VAEDecode, UNETLoader, LoraLoaderModelOnly, ttN text3BOX_3WAYconcat, Note, Note, UNETLoader, VHS_VideoCombine, Note]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 473710667018299, "steps": 20}
---

# 视频生成/文生视频/wan2.1图生视频（自动提示词）+视频高清放大_1922961501655920642.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1922961501655920642.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（47 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: Florence2Image2Prompt`
- `LoadImage`
- `easy cleanGpuUsed`
- `ShowText|pysssss`
- `LayerMask: LoadFlorence2Model`
- `CLIPTextEncode` ★核心
- `LayerUtility: Florence2Image2Prompt`
- `ShowText|pysssss`
- `ShowText`
- `CLIPVisionLoader`
- `CLIPLoader`
- `WanVideoTeaCacheKJ`
- `VAELoader`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `CLIPVisionEncode`
- `easy imageSize`
- `LoadImage`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `VAEDecode` ★核心
- `WanImageToVideo`
- `CLIPLoader`
- `WanVideoTeaCacheKJ`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `UpscaleModelLoader`
- `ImageScale`
- `ImageUpscaleWithModel`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ttN text3BOX_3WAYconcat`
- `Note`
- `Note`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `Note`

## 关键参数

- `seed` = `473710667018299`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（42/47）

**有卡**：`CLIPTextEncode`、`VAELoader`、`KSampler`、`EmptyHunyuanLatentVideo`、`ModelSamplingSD3`、`LayerMask: LoadFlorence2Model`、`LayerUtility: Florence2Image2Prompt`、`LoadImage`、`easy cleanGpuUsed`、`ShowText`、`CLIPVisionLoader`、`CLIPLoader`、`WanVideoTeaCacheKJ`、`CLIPVisionEncode`、`easy imageSize`、`VHS_VideoCombine`、`ImageResizeKJ`、`VAEDecode`、`WanImageToVideo`、`LayerUtility: PurgeVRAM`、`UpscaleModelLoader`、`ImageScale`、`ImageUpscaleWithModel`、`UNETLoader`、`LoraLoaderModelOnly`、`ttN text3BOX_3WAYconcat`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
