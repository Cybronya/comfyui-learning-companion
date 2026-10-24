---
key: 图片生成/图生图/洗图 WAN2.2（最强版）_1960565908315996162.json
name: 洗图 WAN2.2（最强版）_1960565908315996162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/洗图 WAN2.2（最强版）_1960565908315996162.json
hash: a987a3675f02dd67
coverage: 0.71875
learned_at: 2026-10-23 13:11:31
nodes: [Anything Everywhere, ModelSamplingSD3, CLIPTextEncode, PathchSageAttentionKJ, GetNode, GetNode, VAEEncode, Anything Everywhere3, VAELoader, PDIMAGE_LongerSize, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, easy showAnything, SetNode, easy stylesSelector, RH_Captioner, StringFunction|pysssss, SetNode, UpscaleModelLoader, CLIPLoader, CLIPTextEncode, LoadImage, KSampler (Efficient), Image Comparer (rgthree), EsesImageEffectBloom, ImageSharpen, SaveImage, UltimateSDUpscale, Image Comparer (rgthree), SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 679411406397954, "steps": 10}
---

# 图片生成/图生图/洗图 WAN2.2（最强版）_1960565908315996162.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/洗图 WAN2.2（最强版）_1960565908315996162.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Process → Output → Other

**节点**（32 个）：
- `Anything Everywhere`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `Anything Everywhere3`
- `VAELoader`
- `PDIMAGE_LongerSize`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `SetNode`
- `easy stylesSelector`
- `RH_Captioner`
- `StringFunction|pysssss`
- `SetNode`
- `UpscaleModelLoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `KSampler (Efficient)` ★核心
- `Image Comparer (rgthree)`
- `EsesImageEffectBloom`
- `ImageSharpen`
- `SaveImage`
- `UltimateSDUpscale`
- `Image Comparer (rgthree)`
- `SaveImage`

## 关键参数

- `seed` = `679411406397954`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **72%**（23/32）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`VAEEncode`、`VAELoader`、`PDIMAGE_LongerSize`、`UNETLoader`、`LoraLoaderModelOnly`、`easy stylesSelector`、`RH_Captioner`、`StringFunction|pysssss`、`UpscaleModelLoader`、`CLIPLoader`、`LoadImage`、`KSampler (Efficient)`、`EsesImageEffectBloom`、`ImageSharpen`、`SaveImage`、`UltimateSDUpscale`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSampler (Efficient)、VAEEncode
