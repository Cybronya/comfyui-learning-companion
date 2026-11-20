---
key: 平台全量/提取纹理extract_texture 电商印花提取  kontext商业级印花提取工作流_1990989119348252674.json
name: 提取纹理extract_texture 电商印花提取  kontext商业级印花提取工作流_1990989119348252674
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/提取纹理extract_texture 电商印花提取  kontext商业级印花提取工作流_1990989119348252674.json
hash: 8ef93a67f1fc37f3
coverage: 0.96
learned_at: 2026-11-14 02:09:58
nodes: [LayerMask: SegformerB2ClothesUltra, LayerUtility: CropByMask V2, ConditioningZeroOut, FluxGuidance, ReferenceLatent, KSampler, VAEDecode, LayerUtility: PurgeVRAM, FluxKontextImageScale, EmptyLatentImage, PreviewImage, DualCLIPLoader, CLIPTextEncode, UNETLoader, VAELoader, ImpactInt, VAEEncode, UpscaleModelLoader, LoraLoaderModelOnly, CR Latent Batch Size, CR Latent Input Switch, ImageUpscaleWithModel, SaveImage, ImpactInt, LoadImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 2, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 587956245282964, "steps": 25, "width": 768}
---

# 平台全量/提取纹理extract_texture 电商印花提取  kontext商业级印花提取工作流_1990989119348252674.json

> 来源文件 `comfyui_library/workflows/平台全量/提取纹理extract_texture 电商印花提取  kontext商业级印花提取工作流_1990989119348252674.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: CropByMask V2`
- `ConditioningZeroOut`
- `FluxGuidance`
- `ReferenceLatent`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `FluxKontextImageScale`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `ImpactInt`
- `VAEEncode` ★核心
- `UpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `CR Latent Batch Size`
- `CR Latent Input Switch`
- `ImageUpscaleWithModel`
- `SaveImage`
- `ImpactInt`
- `LoadImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `587956245282964`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `2`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`LayerMask: SegformerB2ClothesUltra`、`LayerUtility: CropByMask V2`、`ConditioningZeroOut`、`FluxGuidance`、`ReferenceLatent`、`KSampler`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`FluxKontextImageScale`、`EmptyLatentImage`、`DualCLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`VAELoader`、`ImpactInt`、`VAEEncode`、`UpscaleModelLoader`、`LoraLoaderModelOnly`、`CR Latent Batch Size`、`CR Latent Input Switch`、`ImageUpscaleWithModel`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
