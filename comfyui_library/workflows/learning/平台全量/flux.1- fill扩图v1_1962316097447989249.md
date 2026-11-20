---
key: 平台全量/flux.1- fill扩图v1_1962316097447989249.json
name: flux.1- fill扩图v1_1962316097447989249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/flux.1- fill扩图v1_1962316097447989249.json
hash: af4f2ae4b8de1beb
coverage: 0.954545
learned_at: 2026-11-14 01:10:58
nodes: [NunchakuFluxDiTLoader, INPAINT_MaskedFill, INPAINT_MaskedBlur, ConditioningZeroOut, LayerMask: MaskGrow, LoadAndResizeImage, ImagePadKJ, PrimitiveInt, CLIPTextEncodeFlux, LayerUtility: ImageBlend V2, InpaintModelConditioning, KSampler (Efficient), LayerColor: ColorAdapter, KSampler (Efficient), InpaintModelConditioning, LayerUtility: PurgeVRAM V2, CLIPTextEncodeFlux, LayerUtility: PurgeVRAM V2, NunchakuTextEncoderLoaderV2, VAELoader, SaveImage, NunchakuFluxDiTLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.6000000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 393509448879755, "steps": 28}
---

# 平台全量/flux.1- fill扩图v1_1962316097447989249.json

> 来源文件 `comfyui_library/workflows/平台全量/flux.1- fill扩图v1_1962316097447989249.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（22 个）：
- `NunchakuFluxDiTLoader`
- `INPAINT_MaskedFill`
- `INPAINT_MaskedBlur`
- `ConditioningZeroOut`
- `LayerMask: MaskGrow`
- `LoadAndResizeImage`
- `ImagePadKJ`
- `PrimitiveInt`
- `CLIPTextEncodeFlux` ★核心
- `LayerUtility: ImageBlend V2`
- `InpaintModelConditioning`
- `KSampler (Efficient)` ★核心
- `LayerColor: ColorAdapter`
- `KSampler (Efficient)` ★核心
- `InpaintModelConditioning`
- `LayerUtility: PurgeVRAM V2`
- `CLIPTextEncodeFlux` ★核心
- `LayerUtility: PurgeVRAM V2`
- `NunchakuTextEncoderLoaderV2`
- `VAELoader`
- `SaveImage`
- `NunchakuFluxDiTLoader`

## 关键参数

- `seed` = `393509448879755`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.6000000000000001`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`NunchakuFluxDiTLoader`、`INPAINT_MaskedFill`、`INPAINT_MaskedBlur`、`ConditioningZeroOut`、`LayerMask: MaskGrow`、`LoadAndResizeImage`、`ImagePadKJ`、`CLIPTextEncodeFlux`、`LayerUtility: ImageBlend V2`、`InpaintModelConditioning`、`KSampler (Efficient)`、`LayerColor: ColorAdapter`、`LayerUtility: PurgeVRAM V2`、`NunchakuTextEncoderLoaderV2`、`VAELoader`、`SaveImage`

**用到的条目**：VAELoader、ConditioningZeroOut、KSampler (Efficient)、CLIPTextEncodeFlux、NunchakuTextEncoderLoaderV2、LayerColor: ColorAdapter、NunchakuFluxDiTLoader、InpaintModelConditioning
