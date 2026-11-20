---
key: 平台全量/🈚️Flux.1 USO+redux 风格迁移_画风迁移_转插画_1964951606351511553.json
name: 🈚️Flux.1 USO+redux 风格迁移_画风迁移_转插画_1964951606351511553
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/🈚️Flux.1 USO+redux 风格迁移_画风迁移_转插画_1964951606351511553.json
hash: 2ba10cbe7990040a
coverage: 0.712329
learned_at: 2026-11-14 02:54:22
nodes: [ModelPatchLoader, Anything Everywhere, RebatchLatents, Anything Everywhere, EasyCache, RepeatLatentBatch, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, ReferenceLatent, VAEDecode, CheckpointLoaderSimple, Anything Everywhere3, PreviewImage, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, LoadImage, CLIPVisionLoader, Anything Everywhere, Anything Everywhere, StyleModelLoader, GetNode, USOStyleReference, USOStyleReference, CLIPVisionEncode, CLIPVisionEncode, ConditioningZeroOut, Reroute, AIO_Preprocessor, PreviewImage, SetUnionControlNetType, ControlNetLoader, SetNode, SetNode, GetNode, LayerUtility: TextJoin, GetNode, Florence2Run, Florence2ModelLoader, easy showAnything, FluxKontextMultiReferenceLatentMethod, FluxGuidance, KSampler, ImpactSwitch, LoadImage, LoadImage, Anything Everywhere, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ControlNetApplySD3, ReduxFineTuneAdvanced, ReduxFineTuneAdvanced, LoadImage, easy imageRemBg, easy imageColorMatch, RH_Translator, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, easy imageRemBg, LayerColor: Brightness & Contrast, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "flux1-dev-fp8.safetensors", "controlnet_strength": 0.5000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 502440972537404, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/🈚️Flux.1 USO+redux 风格迁移_画风迁移_转插画_1964951606351511553.json

> 来源文件 `comfyui_library/workflows/平台全量/🈚️Flux.1 USO+redux 风格迁移_画风迁移_转插画_1964951606351511553.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `ModelPatchLoader`
- `Anything Everywhere`
- `RebatchLatents`
- `Anything Everywhere`
- `EasyCache`
- `RepeatLatentBatch`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `Anything Everywhere3`
- `PreviewImage`
- `LoadImage`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `LoadImage`
- `CLIPVisionLoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `StyleModelLoader`
- `GetNode`
- `USOStyleReference`
- `USOStyleReference`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `ConditioningZeroOut`
- `Reroute`
- `AIO_Preprocessor`
- `PreviewImage`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: TextJoin`
- `GetNode`
- `Florence2Run`
- `Florence2ModelLoader`
- `easy showAnything`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxGuidance`
- `KSampler` ★核心
- `ImpactSwitch`
- `LoadImage`
- `LoadImage`
- `Anything Everywhere`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ControlNetApplySD3` ★核心
- `ReduxFineTuneAdvanced`
- `ReduxFineTuneAdvanced`
- `LoadImage`
- `easy imageRemBg`
- `easy imageColorMatch`
- `RH_Translator`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy imageRemBg`
- `LayerColor: Brightness & Contrast`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `flux1-dev-fp8.safetensors`
- `seed` = `502440972537404`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.5000000000000001`

## 知识

覆盖率 **71%**（52/73）

**有卡**：`ModelPatchLoader`、`RebatchLatents`、`EasyCache`、`RepeatLatentBatch`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ReferenceLatent`、`VAEDecode`、`CheckpointLoaderSimple`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`CLIPVisionLoader`、`StyleModelLoader`、`USOStyleReference`、`CLIPVisionEncode`、`ConditioningZeroOut`、`AIO_Preprocessor`、`SetUnionControlNetType`、`ControlNetLoader`、`LayerUtility: TextJoin`、`Florence2Run`、`Florence2ModelLoader`、`FluxKontextMultiReferenceLatentMethod`、`FluxGuidance`、`KSampler`、`ControlNetApplySD3`、`ReduxFineTuneAdvanced`、`easy imageRemBg`、`easy imageColorMatch`、`RH_Translator`、`LayerColor: Brightness & Contrast`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetApplySD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
