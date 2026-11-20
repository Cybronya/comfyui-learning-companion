---
key: 平台全量/Wan2.2 洗图 超级修复_1954148423886880769.json
name: Wan2.2 洗图 超级修复_1954148423886880769
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 洗图 超级修复_1954148423886880769.json
hash: 22337c3915587583
coverage: 0.903226
learned_at: 2026-11-14 01:05:46
nodes: [LayerUtility: JoyCaptionBeta1ExtraOptions, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, Anything Everywhere, CLIPLoader, VAELoader, LayerUtility: LoadJoyCaptionBeta1Model, Anything Everywhere3, ConstrainImage|pysssss, VAEDecode, KSampler, KSampler, KSampler, KSampler, CLIPTextEncode, VAEEncode, LayerUtility: JoyCaptionBeta1, SaveImage, SaveImage, SaveImage, SaveImage, VAEDecode, VAEDecode, VAEDecode, CLIPTextEncode, LoadImage, Reroute]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.4200000000000001, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 86148922227549, "steps": 20}
---

# 平台全量/Wan2.2 洗图 超级修复_1954148423886880769.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 洗图 超级修复_1954148423886880769.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Anything Everywhere`
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `Anything Everywhere3`
- `ConstrainImage|pysssss`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LayerUtility: JoyCaptionBeta1`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `Reroute`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `86148922227549`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.4200000000000001`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`LayerUtility: JoyCaptionBeta1ExtraOptions`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`LayerUtility: LoadJoyCaptionBeta1Model`、`ConstrainImage|pysssss`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`VAEEncode`、`LayerUtility: JoyCaptionBeta1`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader
