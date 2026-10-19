---
key: 图片生成/文生图/真实系文生图+wan2.2重绘_2008250817723244545.json
name: 真实系文生图+wan2.2重绘_2008250817723244545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/真实系文生图+wan2.2重绘_2008250817723244545.json
hash: a3a9b01568f93e2d
coverage: 0.913043
learned_at: 2026-10-19 22:01:41
nodes: [KSampler (Efficient), KSampler (Efficient), PreviewImage, Image Comparer (rgthree), Efficient Loader, PreviewTextNode, LatentUpscaleBy, easy loraStack, CLIPTextEncode, SaveImage, CompressImages, easy cleanGpuUsed, easy clearCacheAll, KSampler (Efficient), CLIPTextEncode, WD14Tagger|pysssss, UNETLoader, VAEEncode, CLIPLoader, VAELoader, LoraLoaderModelOnly, ModelSamplingSD3, GoogleTranslateTextNode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 9999, "steps": 3}
---

# 图片生成/文生图/真实系文生图+wan2.2重绘_2008250817723244545.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/真实系文生图+wan2.2重绘_2008250817723244545.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Process → Output → Other

**节点**（23 个）：
- `KSampler (Efficient)` ★核心
- `KSampler (Efficient)` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Efficient Loader`
- `PreviewTextNode`
- `LatentUpscaleBy`
- `easy loraStack`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `CompressImages`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `KSampler (Efficient)` ★核心
- `CLIPTextEncode` ★核心
- `WD14Tagger|pysssss`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `GoogleTranslateTextNode`

## 关键参数

- `seed` = `9999`
- `steps` = `3`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`KSampler (Efficient)`、`Efficient Loader`、`PreviewTextNode`、`LatentUpscaleBy`、`easy loraStack`、`CLIPTextEncode`、`SaveImage`、`CompressImages`、`easy cleanGpuUsed`、`easy clearCacheAll`、`WD14Tagger|pysssss`、`UNETLoader`、`VAEEncode`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`GoogleTranslateTextNode`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSampler (Efficient)、LatentUpscaleBy、VAEEncode
