---
key: 图片生成/图生图/✅SDXL Instant ID+hyperlora 换脸_脸部重绘_面部重绘参考_1925260058052206594.json
name: ✅SDXL Instant ID+hyperlora 换脸_脸部重绘_面部重绘参考_1925260058052206594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/✅SDXL Instant ID+hyperlora 换脸_脸部重绘_面部重绘参考_1925260058052206594.json
hash: 6dff8334c42eefbf
coverage: 0.566265
learned_at: 2026-10-23 11:47:42
nodes: [SetNode, HyperLoRAGenerateIDLoRA, SetNode, HyperLoRAApplyLoRA, GetNode, HyperLoRAFaceAttr, HyperLoRAIDCond, SetNode, SetNode, HyperLoRAConfig, HyperLoRALoader, LoadImage, SetNode, GetNode, LoadImage, LoadImage, ApplyInstantIDAdvanced, ControlNetLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, BNK_CLIPTextEncodeAdvanced, BNK_CLIPTextEncodeAdvanced, VAEDecode, GetNode, InstantIDModelLoader, ApplyFBCacheOnModel, InpaintStitchImproved, GetNode, ImageAndMaskPreview, ImpactSwitch, InvertMask (segment anything), ReActorFaceSwap, GetNode, ImageCompositeMasked, PreviewImage, SetNode, InpaintCropImproved, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, ImageFromBatch+, InpaintCropImproved, LayerMask: PersonMaskUltra V2, PreviewImage, ImageFromBatch+, SetNode, ImpactSwitch, SetNode, SetNode, LoadImage, LoadImage, LoadImage, ImpactMakeImageBatch, LoadImage, SetNode, GetNode, LayerMask: PersonMaskUltra V2, GetNode, GetNode, SetNode, GetNode, Note, RepeatLatentBatch, RebatchLatents, GetNode, GetNode, GetNode, GetNode, InpaintModelConditioning, InstantIDFaceAnalysis, SaveImage, KSampler, GetNode, CheckpointLoaderSimple]
patterns: []
missing: []
parameters: {"cfg": 1.5, "checkpoint": "realvisxlV50_v50Bakedvae.safetensors", "denoise": 0.5000000000000001, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 266215087399433, "steps": 20}
---

# 图片生成/图生图/✅SDXL Instant ID+hyperlora 换脸_脸部重绘_面部重绘参考_1925260058052206594.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/✅SDXL Instant ID+hyperlora 换脸_脸部重绘_面部重绘参考_1925260058052206594.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `SetNode`
- `HyperLoRAGenerateIDLoRA`
- `SetNode`
- `HyperLoRAApplyLoRA`
- `GetNode`
- `HyperLoRAFaceAttr`
- `HyperLoRAIDCond`
- `SetNode`
- `SetNode`
- `HyperLoRAConfig`
- `HyperLoRALoader` ★核心
- `LoadImage`
- `SetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `ApplyInstantIDAdvanced`
- `ControlNetLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `BNK_CLIPTextEncodeAdvanced` ★核心
- `BNK_CLIPTextEncodeAdvanced` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `InstantIDModelLoader`
- `ApplyFBCacheOnModel`
- `InpaintStitchImproved`
- `GetNode`
- `ImageAndMaskPreview`
- `ImpactSwitch`
- `InvertMask (segment anything)`
- `ReActorFaceSwap`
- `GetNode`
- `ImageCompositeMasked`
- `PreviewImage`
- `SetNode`
- `InpaintCropImproved`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch+`
- `InpaintCropImproved`
- `LayerMask: PersonMaskUltra V2`
- `PreviewImage`
- `ImageFromBatch+`
- `SetNode`
- `ImpactSwitch`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImpactMakeImageBatch`
- `LoadImage`
- `SetNode`
- `GetNode`
- `LayerMask: PersonMaskUltra V2`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Note`
- `RepeatLatentBatch`
- `RebatchLatents`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `SaveImage`
- `KSampler` ★核心
- `GetNode`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `266215087399433`
- `steps` = `20`
- `cfg` = `1.5`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.5000000000000001`
- `checkpoint` = `realvisxlV50_v50Bakedvae.safetensors`

## 知识

覆盖率 **57%**（47/83）

**有卡**：`HyperLoRAGenerateIDLoRA`、`HyperLoRAApplyLoRA`、`HyperLoRAFaceAttr`、`HyperLoRAIDCond`、`HyperLoRAConfig`、`HyperLoRALoader`、`LoadImage`、`ApplyInstantIDAdvanced`、`ControlNetLoader`、`BNK_CLIPTextEncodeAdvanced`、`VAEDecode`、`InstantIDModelLoader`、`ApplyFBCacheOnModel`、`InpaintStitchImproved`、`ImageAndMaskPreview`、`InvertMask (segment anything)`、`ReActorFaceSwap`、`ImageCompositeMasked`、`InpaintCropImproved`、`ImageFromBatch+`、`LayerMask: PersonMaskUltra V2`、`ImpactMakeImageBatch`、`RepeatLatentBatch`、`RebatchLatents`、`InpaintModelConditioning`、`InstantIDFaceAnalysis`、`SaveImage`、`KSampler`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、LoadImage、ControlNetLoader、RepeatLatentBatch、RebatchLatents、BNK_CLIPTextEncodeAdvanced
