---
key: 图片生成/文生图/z-image-flux-fill-onereward-无缝拼接图-无缝贴图-材质贴图_2041532484155875329.json
name: z-image-flux-fill-onereward-无缝拼接图-无缝贴图-材质贴图_2041532484155875329
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/z-image-flux-fill-onereward-无缝拼接图-无缝贴图-材质贴图_2041532484155875329.json
hash: ea7d86c6f5839080
coverage: 0.875
learned_at: 2026-10-21 02:57:45
nodes: [CLIPTextEncode, UNETLoader, LayerUtility: ImageBlendAdvance V3, DualCLIPLoader, FluxGuidance, PreviewImage, MaskPreview, LayerUtility: ImageShift, LayerUtility: ColorImage V2, VAEDecode, SamplerCustom, CLIPTextEncode, VAEEncode, SplitSigmas, ImageScaleBy, SamplerCustom, PreviewBridge, DifferentialDiffusion, InpaintModelConditioning, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, Mask Invert, Masks Subtract, LayerMask: MaskGrow, MaskPreview, VAELoader, KSamplerSelect, PreviewBridge, easy showAnything, BasicScheduler, UNETLoader, CLIPLoader, ShowText|pysssss, AILab_QwenVL, CLIPTextEncode, ConditioningZeroOut, KSampler, MaskPreview, ImageUntile+, easy promptConcat, easy positive, DetailDaemonSamplerNode, EmptyLatentImage, VAELoader, Seed (rgthree), Note, PreviewImage, RepeatImageBatch, SaveImage, VAEDecode, easy positive, Image Comparer (rgthree), easy showAnything, easy mathInt, easy int, easy int]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "er_sde", "scheduler": "bong_tangent", "seed": 660623356419517, "steps": 20, "width": 1024}
---

# 图片生成/文生图/z-image-flux-fill-onereward-无缝拼接图-无缝贴图-材质贴图_2041532484155875329.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/z-image-flux-fill-onereward-无缝拼接图-无缝贴图-材质贴图_2041532484155875329.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LayerUtility: ImageBlendAdvance V3`
- `DualCLIPLoader`
- `FluxGuidance`
- `PreviewImage`
- `MaskPreview`
- `LayerUtility: ImageShift`
- `LayerUtility: ColorImage V2`
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `SplitSigmas`
- `ImageScaleBy`
- `SamplerCustom` ★核心
- `PreviewBridge`
- `DifferentialDiffusion`
- `InpaintModelConditioning`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `Mask Invert`
- `Masks Subtract`
- `LayerMask: MaskGrow`
- `MaskPreview`
- `VAELoader`
- `KSamplerSelect` ★核心
- `PreviewBridge`
- `easy showAnything`
- `BasicScheduler`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ShowText|pysssss`
- `AILab_QwenVL`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `MaskPreview`
- `ImageUntile+`
- `easy promptConcat`
- `easy positive`
- `DetailDaemonSamplerNode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `Seed (rgthree)`
- `Note`
- `PreviewImage`
- `RepeatImageBatch`
- `SaveImage`
- `VAEDecode` ★核心
- `easy positive`
- `Image Comparer (rgthree)`
- `easy showAnything`
- `easy mathInt`
- `easy int`
- `easy int`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `660623356419517`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（49/56）

**有卡**：`CLIPTextEncode`、`UNETLoader`、`LayerUtility: ImageBlendAdvance V3`、`DualCLIPLoader`、`FluxGuidance`、`MaskPreview`、`LayerUtility: ImageShift`、`LayerUtility: ColorImage V2`、`VAEDecode`、`SamplerCustom`、`VAEEncode`、`SplitSigmas`、`ImageScaleBy`、`PreviewBridge`、`DifferentialDiffusion`、`InpaintModelConditioning`、`LayerUtility: ImageScaleByAspectRatio V2`、`Mask Invert`、`Masks Subtract`、`LayerMask: MaskGrow`、`VAELoader`、`KSamplerSelect`、`BasicScheduler`、`CLIPLoader`、`AILab_QwenVL`、`ConditioningZeroOut`、`KSampler`、`ImageUntile+`、`easy promptConcat`、`easy positive`、`DetailDaemonSamplerNode`、`EmptyLatentImage`、`Seed (rgthree)`、`RepeatImageBatch`、`SaveImage`、`easy mathInt`、`easy int`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
