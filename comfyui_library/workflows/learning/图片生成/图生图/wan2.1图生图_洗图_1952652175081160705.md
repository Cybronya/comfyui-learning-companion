---
key: 图片生成/图生图/wan2.1图生图_洗图_1952652175081160705.json
name: wan2.1图生图_洗图_1952652175081160705
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.1图生图_洗图_1952652175081160705.json
hash: 48d99b73bff8524a
coverage: 0.666667
learned_at: 2026-10-23 11:45:51
nodes: [VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, Anything Everywhere3, RH_LLMAPI_NODE, JjkText, CR Text Concatenate, easy showAnything, CLIPTextEncode, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, VAEDecode, SaveImage, PreviewImage, JjkText, JjkText, JjkText, JjkText, LoadImage, VAEEncode, Image Comparer (rgthree), CLIPTextEncode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.4300000000000001, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 1094403471156990, "steps": 20}
---

# 图片生成/图生图/wan2.1图生图_洗图_1952652175081160705.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.1图生图_洗图_1952652175081160705.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere3`
- `RH_LLMAPI_NODE`
- `JjkText`
- `CR Text Concatenate`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `LoadImage`
- `VAEEncode` ★核心
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1094403471156990`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.4300000000000001`

## 知识

覆盖率 **67%**（18/27）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`RH_LLMAPI_NODE`、`CR Text Concatenate`、`CLIPTextEncode`、`KSampler`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`VAEDecode`、`SaveImage`、`LoadImage`、`VAEEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
