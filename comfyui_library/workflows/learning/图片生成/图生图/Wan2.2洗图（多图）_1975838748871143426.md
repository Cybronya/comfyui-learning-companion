---
key: 图片生成/图生图/Wan2.2洗图（多图）_1975838748871143426.json
name: Wan2.2洗图（多图）_1975838748871143426
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2洗图（多图）_1975838748871143426.json
hash: e175536a23f9bcae
coverage: 0.862069
learned_at: 2026-10-23 11:28:24
nodes: [VAEDecode, VAEDecode, VAEDecode, KSampler, UNETLoader, VAELoader, LayerUtility: LoadJoyCaptionBeta1Model, CLIPLoader, Anything Everywhere3, Reroute, VAEEncode, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, ConstrainImage|pysssss, PathchSageAttentionKJ, ModelSamplingSD3, Anything Everywhere, PreviewImage, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LoadImage, LoraLoaderModelOnly, KSampler, KSampler, SaveImage, SaveImage, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.4000000000000001, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 990488655439851, "steps": 20}
---

# 图片生成/图生图/Wan2.2洗图（多图）_1975838748871143426.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2洗图（多图）_1975838748871143426.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `CLIPLoader`
- `Anything Everywhere3`
- `Reroute`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConstrainImage|pysssss`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Anything Everywhere`
- `PreviewImage`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `990488655439851`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`VAEDecode`、`KSampler`、`UNETLoader`、`VAELoader`、`LayerUtility: LoadJoyCaptionBeta1Model`、`CLIPLoader`、`VAEEncode`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ConstrainImage|pysssss`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
