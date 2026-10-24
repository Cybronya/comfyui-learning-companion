---
key: 图片生成/图生图/Flux-Cotrolent-InstantX-V2版_1913099380973600770.json
name: Flux-Cotrolent-InstantX-V2版_1913099380973600770
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux-Cotrolent-InstantX-V2版_1913099380973600770.json
hash: 1d0237a13509d0b9
coverage: 0.870968
learned_at: 2026-10-23 10:58:22
nodes: [LayerUtility: PurgeVRAM, ConditioningZeroOut, VAELoader, ControlNetApplySD3, KSampler, DualCLIPLoader, ConstrainImage|pysssss, LoraLoaderModelOnly, Joy_caption_two, Joy_caption_two_load, ShowText|pysssss, EmptyLatentImage, easy imageSize, AIO_Preprocessor, PreviewImage, ControlNetLoader, SetUnionControlNetType, KSampler, VAEDecode, PreviewImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, ControlNetLoader, SetUnionControlNetType, ControlNetApplySD3, SaveImage, UNETLoader, CLIPTextEncode, VAEDecode, PreviewImage, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 1, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "simple", "seed": 1, "steps": 20, "width": 1024}
---

# 图片生成/图生图/Flux-Cotrolent-InstantX-V2版_1913099380973600770.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux-Cotrolent-InstantX-V2版_1913099380973600770.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `LayerUtility: PurgeVRAM`
- `ConditioningZeroOut`
- `VAELoader`
- `ControlNetApplySD3` ★核心
- `KSampler` ★核心
- `DualCLIPLoader`
- `ConstrainImage|pysssss`
- `LoraLoaderModelOnly` ★核心
- `Joy_caption_two`
- `Joy_caption_two_load`
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心
- `easy imageSize`
- `AIO_Preprocessor`
- `PreviewImage`
- `ControlNetLoader`
- `SetUnionControlNetType`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `ControlNetLoader`
- `SetUnionControlNetType`
- `ControlNetApplySD3` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `controlnet_strength` = `1`
- `seed` = `1`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `768`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`LayerUtility: PurgeVRAM`、`ConditioningZeroOut`、`VAELoader`、`ControlNetApplySD3`、`KSampler`、`DualCLIPLoader`、`ConstrainImage|pysssss`、`LoraLoaderModelOnly`、`Joy_caption_two`、`Joy_caption_two_load`、`EmptyLatentImage`、`easy imageSize`、`AIO_Preprocessor`、`ControlNetLoader`、`SetUnionControlNetType`、`VAEDecode`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`SaveImage`、`UNETLoader`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
