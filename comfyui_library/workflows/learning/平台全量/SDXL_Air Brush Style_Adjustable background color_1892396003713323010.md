---
key: 平台全量/SDXL_Air Brush Style_Adjustable background color_1892396003713323010.json
name: SDXL_Air Brush Style_Adjustable background color_1892396003713323010
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/SDXL_Air Brush Style_Adjustable background color_1892396003713323010.json
hash: 89127ca3a2ce6818
coverage: 0.837838
learned_at: 2026-11-14 00:56:17
nodes: [CLIPTextEncodeSDXL, CLIPTextEncodeSDXLRefiner, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, Zoe-DepthMapPreprocessor, EmptyLatentImage, InvertMask, CLIPTextEncode, ImageCompositeMasked, VAEDecode, CheckpointLoaderSimple, CheckpointLoaderSimple, PreviewImage, PreviewImage, VAEDecode, KSamplerAdvanced, PreviewImage, ImageScale, PreviewImage, CheckpointLoaderSimple, VAEEncode, VAEDecode, KSampler, SaveImage, CLIPTextEncodeSDXLRefiner, EmptyLatentImage, CLIPTextEncodeSDXL, CheckpointLoaderSimple, CLIPTextEncode, VAELoader, PrimitiveNode, CLIPTextEncode, CLIPTextEncode, PrimitiveNode, ImageToMask]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "sd_xl_refiner_1.0_0.9vae_1.0.safetensors", "denoise": 0.5, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 109656542990536, "steps": 5, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/SDXL_Air Brush Style_Adjustable background color_1892396003713323010.json

> 来源文件 `comfyui_library/workflows/平台全量/SDXL_Air Brush Style_Adjustable background color_1892396003713323010.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `CLIPTextEncodeSDXL` ★核心
- `CLIPTextEncodeSDXLRefiner` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `Zoe-DepthMapPreprocessor`
- `EmptyLatentImage` ★核心
- `InvertMask`
- `CLIPTextEncode` ★核心
- `ImageCompositeMasked`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `PreviewImage`
- `ImageScale`
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `CLIPTextEncodeSDXLRefiner` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncodeSDXL` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `PrimitiveNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `ImageToMask`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `109656542990536`
- `steps` = `5`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.5`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `checkpoint` = `sd_xl_refiner_1.0_0.9vae_1.0.safetensors`

## 知识

覆盖率 **84%**（31/37）

**有卡**：`CLIPTextEncodeSDXL`、`CLIPTextEncodeSDXLRefiner`、`KSamplerAdvanced`、`VAEDecode`、`Zoe-DepthMapPreprocessor`、`EmptyLatentImage`、`InvertMask`、`CLIPTextEncode`、`ImageCompositeMasked`、`CheckpointLoaderSimple`、`ImageScale`、`VAEEncode`、`KSampler`、`SaveImage`、`VAELoader`、`ImageToMask`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、Zoe-DepthMapPreprocessor、KSamplerAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
