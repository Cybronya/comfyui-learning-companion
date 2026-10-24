---
key: 图片生成/图生图/Work Fisher_ Qwen Edit Rapid Face Swap-本地编码_2008457430597902338.json
name: Work Fisher_ Qwen Edit Rapid Face Swap-本地编码_2008457430597902338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Work Fisher_ Qwen Edit Rapid Face Swap-本地编码_2008457430597902338.json
hash: 52b9b5591bce576e
coverage: 0.56
learned_at: 2026-10-23 11:28:31
nodes: [CheckpointLoaderSimple, Reroute, Reroute, PreviewImage, Reroute, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, RebatchLatents, Reroute, LayerMask: MaskGrow, LayerMask: MaskPreview, MaskToSEGS, SegsToCombinedMask, LayerMask: PersonMaskUltra V2, TextEncodeQwenImageEditPlusAdvance_lrzjason, InpaintModelConditioning, LayerMask: MaskGrow, Reroute, RepeatLatentBatch, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LayerMask: MaskPreview, VAEDecode, KSampler, Reroute, Reroute, Reroute, ConditioningZeroOut, Note, Note, Reroute, Reroute, Reroute, Note, Int, Float, Int, LoadImage, DifferentialDiffusion, LoraLoaderModelOnly, LoraLoaderModelOnly, DuckHideNode, SaveImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-SFW-v5.safetensors", "denoise": 0.7200000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 570068844826709, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Work Fisher_ Qwen Edit Rapid Face Swap-本地编码_2008457430597902338.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Work Fisher_ Qwen Edit Rapid Face Swap-本地编码_2008457430597902338.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `Reroute`
- `PreviewImage`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `RebatchLatents`
- `Reroute`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `MaskToSEGS`
- `SegsToCombinedMask`
- `LayerMask: PersonMaskUltra V2`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `InpaintModelConditioning`
- `LayerMask: MaskGrow`
- `Reroute`
- `RepeatLatentBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LayerMask: MaskPreview`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `ConditioningZeroOut`
- `Note`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Int`
- `Float`
- `Int`
- `LoadImage`
- `DifferentialDiffusion`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DuckHideNode`
- `SaveImage`
- `LoadImage`

## 关键参数

- `checkpoint` = `Qwen-Rapid-AIO-SFW-v5.safetensors`
- `seed` = `570068844826709`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.7200000000000002`

## 知识

覆盖率 **56%**（28/50）

**有卡**：`CheckpointLoaderSimple`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`RebatchLatents`、`LayerMask: MaskGrow`、`LayerMask: MaskPreview`、`MaskToSEGS`、`SegsToCombinedMask`、`LayerMask: PersonMaskUltra V2`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`InpaintModelConditioning`、`RepeatLatentBatch`、`VAEDecode`、`KSampler`、`ConditioningZeroOut`、`Int`、`Float`、`LoadImage`、`DifferentialDiffusion`、`DuckHideNode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、RepeatLatentBatch、TextEncodeQwenImageEditPlusAdvance_lrzjason

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
