---
key: 平台全量/wan2.2分区放大重绘修复中高频_2062394696227446786.json
name: wan2.2分区放大重绘修复中高频_2062394696227446786
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2分区放大重绘修复中高频_2062394696227446786.json
hash: f7de2224c57b9ef8
coverage: 0.596491
learned_at: 2026-11-14 01:19:42
nodes: [GetNode, GetNode, SetNode, GetNode, Image Comparer (rgthree), SaveImage, Display UI, Display UI, Combine Tiles, Note, SetNode, SaveImage, PreviewImage, Florence2ModelLoader, Image Comparer (rgthree), SetNode, Display UI, SetNode, Reroute, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, SetNode, PathchSageAttentionKJ, Florence2Run, Display UI, easy promptConcat, LoraLoaderModelOnly, wanBlockSwap, ModelPatchTorchSettings, CLIPTextEncode, ModelSamplingSD3, Divide Image and Select Tile, Fast Groups Muter (rgthree), VAEEncode, CLIPTextEncode, VAELoader, CR Prompt Text, Fast Groups Bypasser (rgthree), Divide and Conquer Algorithm, UpscaleModelLoader, Fast Groups Bypasser (rgthree), KSampler, Latent Noise Injection, LoraLoaderModelOnly, UNETLoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_LoadVideoFFmpeg, Note, Image Comparer (rgthree), LoadImage, JWImageResizeByShorterSide]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.25, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 770326568905002, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/wan2.2分区放大重绘修复中高频_2062394696227446786.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2分区放大重绘修复中高频_2062394696227446786.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Display UI`
- `Display UI`
- `Combine Tiles`
- `Note`
- `SetNode`
- `SaveImage`
- `PreviewImage`
- `Florence2ModelLoader`
- `Image Comparer (rgthree)`
- `SetNode`
- `Display UI`
- `SetNode`
- `Reroute`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `Florence2Run`
- `Display UI`
- `easy promptConcat`
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `Divide Image and Select Tile`
- `Fast Groups Muter (rgthree)`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `Divide and Conquer Algorithm`
- `UpscaleModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心
- `Latent Noise Injection`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_LoadVideoFFmpeg`
- `Note`
- `Image Comparer (rgthree)`
- `LoadImage`
- `JWImageResizeByShorterSide`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `770326568905002`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.25`

## 知识

覆盖率 **60%**（34/57）

**有卡**：`SaveImage`、`Display UI`、`Combine Tiles`、`Florence2ModelLoader`、`VAEDecode`、`PathchSageAttentionKJ`、`Florence2Run`、`easy promptConcat`、`LoraLoaderModelOnly`、`wanBlockSwap`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`ModelSamplingSD3`、`Divide Image and Select Tile`、`VAEEncode`、`VAELoader`、`CR Prompt Text`、`Divide and Conquer Algorithm`、`UpscaleModelLoader`、`KSampler`、`Latent Noise Injection`、`UNETLoader`、`CLIPLoader`、`VHS_LoadVideoFFmpeg`、`LoadImage`、`JWImageResizeByShorterSide`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
