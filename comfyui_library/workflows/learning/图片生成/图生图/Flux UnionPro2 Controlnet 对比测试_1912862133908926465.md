---
key: 图片生成/图生图/Flux UnionPro2 Controlnet 对比测试_1912862133908926465.json
name: Flux UnionPro2 Controlnet 对比测试_1912862133908926465
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux UnionPro2 Controlnet 对比测试_1912862133908926465.json
hash: e949ddb5a2011b78
coverage: 0.875
learned_at: 2026-10-23 10:58:05
nodes: [Anything Everywhere3, VAEDecode, EmptyLatentImage, Anything Everywhere3, AddLabel, VAEDecode, AddLabel, AddLabel, KSampler, KSampler, VAELoader, FluxGuidance, FluxGuidance, DualCLIPLoader, ControlNetLoader, ControlNetLoader, LayerUtility: ImageScaleByAspectRatio V2, SetShakkerLabsUnionControlNetType, SetShakkerLabsUnionControlNetType, CLIPTextEncode, LayerUtility: Florence2Image2Prompt, LayerMask: LoadFlorence2Model, ConditioningZeroOut, AIO_Preprocessor, ControlNetApplyAdvanced, ControlNetApplyAdvanced, LoadImage, CheckpointLoaderSimple, Note, Note, SaveImage, ImageConcatMulti]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "copaxTimeless_xplus4_fp8.safetensors", "controlnet_strength": 0.7000000000000002, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 60804103819595, "steps": 20, "width": 1024}
---

# 图片生成/图生图/Flux UnionPro2 Controlnet 对比测试_1912862133908926465.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux UnionPro2 Controlnet 对比测试_1912862133908926465.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `Anything Everywhere3`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `Anything Everywhere3`
- `AddLabel`
- `VAEDecode` ★核心
- `AddLabel`
- `AddLabel`
- `KSampler` ★核心
- `KSampler` ★核心
- `VAELoader`
- `FluxGuidance`
- `FluxGuidance`
- `DualCLIPLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetShakkerLabsUnionControlNetType`
- `SetShakkerLabsUnionControlNetType`
- `CLIPTextEncode` ★核心
- `LayerUtility: Florence2Image2Prompt`
- `LayerMask: LoadFlorence2Model`
- `ConditioningZeroOut`
- `AIO_Preprocessor`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `Note`
- `SaveImage`
- `ImageConcatMulti`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `60804103819595`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.7000000000000002`
- `checkpoint` = `copaxTimeless_xplus4_fp8.safetensors`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`VAEDecode`、`EmptyLatentImage`、`AddLabel`、`KSampler`、`VAELoader`、`FluxGuidance`、`DualCLIPLoader`、`ControlNetLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`SetShakkerLabsUnionControlNetType`、`CLIPTextEncode`、`LayerUtility: Florence2Image2Prompt`、`LayerMask: LoadFlorence2Model`、`ConditioningZeroOut`、`AIO_Preprocessor`、`ControlNetApplyAdvanced`、`LoadImage`、`CheckpointLoaderSimple`、`SaveImage`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
