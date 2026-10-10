---
key: Flux-Cotrolent-InstantX-V2版_1912664033240252418.json
name: Flux-Cotrolent-InstantX-V2版_1912664033240252418
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux-Cotrolent-InstantX-V2版_1912664033240252418.json
hash: c02bb6b9418d70b6
coverage: 0.6875
learned_at: 2026-10-10 20:58:35
nodes: [LayerUtility: PurgeVRAM, ConditioningZeroOut, VAELoader, ControlNetApplySD3, KSampler, DualCLIPLoader, CR Text, ConstrainImage|pysssss, LoraLoaderModelOnly, Joy_caption_two, Joy_caption_two_load, ShowText|pysssss, EmptyLatentImage, easy imageSize, AIO_Preprocessor, PreviewImage, ControlNetLoader, SetUnionControlNetType, KSampler, VAEDecode, PreviewImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, ControlNetLoader, SetUnionControlNetType, ControlNetApplySD3, SaveImage, LoadImage, UNETLoader, CLIPTextEncode, VAEDecode, PreviewImage]
patterns: [text_to_image]
missing: [CR Text, ConstrainImage|pysssss, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM, easy imageSize]
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 1, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "simple", "seed": 1, "steps": 20, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ConstrainImage|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# Flux-Cotrolent-InstantX-V2版_1912664033240252418.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux-Cotrolent-InstantX-V2版_1912664033240252418.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `LayerUtility: PurgeVRAM`
- `ConditioningZeroOut`
- `VAELoader`
- `ControlNetApplySD3` ★核心
- `KSampler` ★核心
- `DualCLIPLoader`
- `CR Text`
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
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`

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

覆盖率 **69%**（22/32）

**有卡**：`ConditioningZeroOut`、`VAELoader`、`ControlNetApplySD3`、`KSampler`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`Joy_caption_two`、`Joy_caption_two_load`、`EmptyLatentImage`、`AIO_Preprocessor`、`ControlNetLoader`、`SetUnionControlNetType`、`VAEDecode`、`SaveImage`、`LoadImage`、`UNETLoader`、`CLIPTextEncode`

**缺卡**（6）：`CR Text`、`ConstrainImage|pysssss`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`LayerUtility: PurgeVRAM`、`easy imageSize`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ConstrainImage|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
