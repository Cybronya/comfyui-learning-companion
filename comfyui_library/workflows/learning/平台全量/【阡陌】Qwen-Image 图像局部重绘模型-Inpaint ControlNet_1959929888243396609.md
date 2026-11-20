---
key: 平台全量/【阡陌】Qwen-Image 图像局部重绘模型-Inpaint ControlNet_1959929888243396609.json
name: 【阡陌】Qwen-Image 图像局部重绘模型-Inpaint ControlNet_1959929888243396609
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/【阡陌】Qwen-Image 图像局部重绘模型-Inpaint ControlNet_1959929888243396609.json
hash: 15a5af241049872a
coverage: 0.952381
learned_at: 2026-11-14 01:26:09
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, LoadImage, LoraLoaderModelOnly, KSampler, ModelSamplingAuraFlow, QwenImageDiffsynthControlnet, LoadImage, ModelPatchLoader, EmptyLatentImage, VAEDecode, LayerMask: MaskGrow, LayerUtility: ImageScaleByAspectRatio V2, Image Compare (mtb), ImageCompositeMasked, SaveImage, SaveImage, PreviewImage, CLIPTextEncode, UNETLoader]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 878462878597544, "steps": 4, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/【阡陌】Qwen-Image 图像局部重绘模型-Inpaint ControlNet_1959929888243396609.json

> 来源文件 `comfyui_library/workflows/平台全量/【阡陌】Qwen-Image 图像局部重绘模型-Inpaint ControlNet_1959929888243396609.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `QwenImageDiffsynthControlnet`
- `LoadImage`
- `ModelPatchLoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `LayerMask: MaskGrow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Compare (mtb)`
- `ImageCompositeMasked`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `878462878597544`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`LoadImage`、`LoraLoaderModelOnly`、`KSampler`、`ModelSamplingAuraFlow`、`QwenImageDiffsynthControlnet`、`ModelPatchLoader`、`EmptyLatentImage`、`VAEDecode`、`LayerMask: MaskGrow`、`LayerUtility: ImageScaleByAspectRatio V2`、`Image Compare (mtb)`、`ImageCompositeMasked`、`SaveImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
