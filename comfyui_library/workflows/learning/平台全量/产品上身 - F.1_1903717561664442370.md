---
key: 平台全量/产品上身 - F.1_1903717561664442370.json
name: 产品上身 - F.1_1903717561664442370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/产品上身 - F.1_1903717561664442370.json
hash: e2adcf197c950d91
coverage: 0.916667
learned_at: 2026-11-14 01:34:38
nodes: [CLIPTextEncode, SaveImage, CLIPTextEncode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageRemoveAlpha, LayerUtility: ColorPicker, PreviewImage, Florence2Run, LoadImage, LayerUtility: ColorPicker, GrowMaskWithBlur, easy makeImageForICLora, PreviewImage, MaskPreview+, ReduxAdvanced, FluxGuidance, InpaintModelConditioning, VAELoader, KSampler, VAEDecode, easy cleanGpuUsed, easy imageSplitGrid, easy imagesSplitImage, SaveImage, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, DifferentialDiffusion, ShowText|pysssss, LayerMask: SegmentAnythingUltra V2, LayerMask: SegmentAnythingUltra V2, Florence2ModelLoader, DualCLIPLoader, UNETLoader, StyleModelLoader, CLIPVisionLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 723034701240770, "steps": 30}
---

# 平台全量/产品上身 - F.1_1903717561664442370.json

> 来源文件 `comfyui_library/workflows/平台全量/产品上身 - F.1_1903717561664442370.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `CLIPTextEncode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ColorPicker`
- `PreviewImage`
- `Florence2Run`
- `LoadImage`
- `LayerUtility: ColorPicker`
- `GrowMaskWithBlur`
- `easy makeImageForICLora`
- `PreviewImage`
- `MaskPreview+`
- `ReduxAdvanced`
- `FluxGuidance`
- `InpaintModelConditioning`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy imageSplitGrid`
- `easy imagesSplitImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DifferentialDiffusion`
- `ShowText|pysssss`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerMask: SegmentAnythingUltra V2`
- `Florence2ModelLoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `StyleModelLoader`
- `CLIPVisionLoader`

## 关键参数

- `seed` = `723034701240770`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（33/36）

**有卡**：`CLIPTextEncode`、`SaveImage`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageRemoveAlpha`、`LayerUtility: ColorPicker`、`Florence2Run`、`GrowMaskWithBlur`、`easy makeImageForICLora`、`MaskPreview+`、`ReduxAdvanced`、`FluxGuidance`、`InpaintModelConditioning`、`VAELoader`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`easy imageSplitGrid`、`easy imagesSplitImage`、`LoraLoaderModelOnly`、`DifferentialDiffusion`、`LayerMask: SegmentAnythingUltra V2`、`Florence2ModelLoader`、`DualCLIPLoader`、`UNETLoader`、`StyleModelLoader`、`CLIPVisionLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
