---
key: 图片生成/图生图/扩图效果超好的flux-OneReward2.0（加速版）_1986455556615532546.json
name: 扩图效果超好的flux-OneReward2.0（加速版）_1986455556615532546
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/扩图效果超好的flux-OneReward2.0（加速版）_1986455556615532546.json
hash: 5b22e5c78976f14d
coverage: 0.875
learned_at: 2026-10-23 12:54:02
nodes: [CLIPTextEncode, FluxGuidance, easy ifElse, DifferentialDiffusion, InpaintModelConditioning, ConditioningZeroOut, LayerMask: MaskGrow, KSampler, UNETLoader, DualCLIPLoader, VAELoader, ImpactInt, PrimitiveNode, Image Comparer (rgthree), VAEDecode, LoadImage, ImagePadForOutpaintMasked, CR Text, SaveImage, SaveImage, ImageComposite+, GrowMaskWithBlur, LayerUtility: ImageScaleByAspectRatio V2, ImageConcanate]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "simple", "seed": 942213995580841, "steps": 25}
---

# 图片生成/图生图/扩图效果超好的flux-OneReward2.0（加速版）_1986455556615532546.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/扩图效果超好的flux-OneReward2.0（加速版）_1986455556615532546.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `easy ifElse`
- `DifferentialDiffusion`
- `InpaintModelConditioning`
- `ConditioningZeroOut`
- `LayerMask: MaskGrow`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `ImpactInt`
- `PrimitiveNode`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `LoadImage`
- `ImagePadForOutpaintMasked`
- `CR Text`
- `SaveImage`
- `SaveImage`
- `ImageComposite+`
- `GrowMaskWithBlur`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcanate`

## 关键参数

- `seed` = `942213995580841`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`DifferentialDiffusion`、`InpaintModelConditioning`、`ConditioningZeroOut`、`LayerMask: MaskGrow`、`KSampler`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`ImpactInt`、`VAEDecode`、`LoadImage`、`ImagePadForOutpaintMasked`、`CR Text`、`SaveImage`、`ImageComposite+`、`GrowMaskWithBlur`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
