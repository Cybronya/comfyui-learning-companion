---
key: 平台全量/老照片修复_Stage_1.大面积区域修复_1891128683543826434.json
name: 老照片修复_Stage_1.大面积区域修复_1891128683543826434
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/老照片修复_Stage_1.大面积区域修复_1891128683543826434.json
hash: aa35e032be425430
coverage: 0.684211
learned_at: 2026-11-14 02:30:15
nodes: [GetNode, GetNode, GetNode, GetNode, SelfAttentionGuidance, DifferentialDiffusion, GetNode, SetNode, GetNode, PreviewImage, SetLatentNoiseMask, AIO_Preprocessor, VAEEncode, LayerUtility: LaMa, SetNode, LayerUtility: ImageBlend, SaveImage, VAEDecode, WD14Tagger|pysssss, CLIPSetLastLayer, Anything Everywhere3, Prompts Everywhere, CLIPTextEncode, VAEEncodeForInpaint, ControlNetApplyAdvanced, GrowMaskWithBlur, GrowMaskWithBlur, CLIPTextEncode, CheckpointLoaderSimple, VAELoader, StringFunction|pysssss, INPAINT_LoadFooocusInpaint, ControlNetLoader, GetNode, VAEDecode, PreviewImage, KSampler, KSampler, GoogleTranslateTextNode, LayerMask: MaskPreview, PreviewImage, SetNode, LoadImage, LayerMask: MaskPreview, ImageResizeKJ, ImageResizeKJ, PreviewImage, ImageToMask, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, GetNode, PowerPaint, PowerPaintCLIPLoader, BrushNetLoader, INPAINT_ApplyFooocusInpaint, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1.8, "checkpoint": "majicmixRealistic_v7.safetensors", "controlnet_strength": 1, "denoise": 0.6, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 19673983308028, "steps": 10}
---

# 平台全量/老照片修复_Stage_1.大面积区域修复_1891128683543826434.json

> 来源文件 `comfyui_library/workflows/平台全量/老照片修复_Stage_1.大面积区域修复_1891128683543826434.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SelfAttentionGuidance`
- `DifferentialDiffusion`
- `GetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `SetLatentNoiseMask`
- `AIO_Preprocessor`
- `VAEEncode` ★核心
- `LayerUtility: LaMa`
- `SetNode`
- `LayerUtility: ImageBlend`
- `SaveImage`
- `VAEDecode` ★核心
- `WD14Tagger|pysssss`
- `CLIPSetLastLayer`
- `Anything Everywhere3`
- `Prompts Everywhere`
- `CLIPTextEncode` ★核心
- `VAEEncodeForInpaint` ★核心
- `ControlNetApplyAdvanced` ★核心
- `GrowMaskWithBlur`
- `GrowMaskWithBlur`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `VAELoader`
- `StringFunction|pysssss`
- `INPAINT_LoadFooocusInpaint`
- `ControlNetLoader`
- `GetNode`
- `VAEDecode` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `KSampler` ★核心
- `GoogleTranslateTextNode`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `SetNode`
- `LoadImage`
- `LayerMask: MaskPreview`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `PreviewImage`
- `ImageToMask`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `GetNode`
- `PowerPaint`
- `PowerPaintCLIPLoader`
- `BrushNetLoader`
- `INPAINT_ApplyFooocusInpaint`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `1`
- `checkpoint` = `majicmixRealistic_v7.safetensors`
- `seed` = `19673983308028`
- `steps` = `10`
- `cfg` = `1.8`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `0.6`

## 知识

覆盖率 **68%**（39/57）

**有卡**：`SelfAttentionGuidance`、`DifferentialDiffusion`、`SetLatentNoiseMask`、`AIO_Preprocessor`、`VAEEncode`、`LayerUtility: LaMa`、`LayerUtility: ImageBlend`、`SaveImage`、`VAEDecode`、`WD14Tagger|pysssss`、`CLIPSetLastLayer`、`Prompts Everywhere`、`CLIPTextEncode`、`VAEEncodeForInpaint`、`ControlNetApplyAdvanced`、`GrowMaskWithBlur`、`CheckpointLoaderSimple`、`VAELoader`、`StringFunction|pysssss`、`INPAINT_LoadFooocusInpaint`、`ControlNetLoader`、`KSampler`、`GoogleTranslateTextNode`、`LayerMask: MaskPreview`、`LoadImage`、`ImageResizeKJ`、`ImageToMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`PowerPaint`、`PowerPaintCLIPLoader`、`BrushNetLoader`、`INPAINT_ApplyFooocusInpaint`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、ControlNetApplyAdvanced
