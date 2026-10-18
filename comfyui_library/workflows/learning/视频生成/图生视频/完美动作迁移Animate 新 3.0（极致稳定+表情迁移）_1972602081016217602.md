---
key: 视频生成/图生视频/完美动作迁移Animate 新 3.0（极致稳定+表情迁移）_1972602081016217602.json
name: 完美动作迁移Animate 新 3.0（极致稳定+表情迁移）_1972602081016217602.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/完美动作迁移Animate 新 3.0（极致稳定+表情迁移）_1972602081016217602.json
hash: cddecfd895a05efd
coverage: 0.575342
learned_at: 2026-10-15 22:32:00
nodes: [TorchCompileModelWanVideoV2, ImpactSwitch, Primitive integer [Crystools], Primitive integer [Crystools], SetNode, SetNode, ImageResizeKJv2, SetNode, PreviewImage, GetNode, GetNode, ImpactSwitch, CLIPTextEncode, CLIPVisionEncode, SetNode, GetNode, GetNode, PoseAndFaceDetection, DrawViTPose, SetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoInfoSource, WanAnimateToVideo, KSampler, SetNode, SetNode, CLIPTextEncode, GetNode, VAELoader, GetNode, SetNode, Primitive integer [Crystools], Primitive integer [Crystools], VHS_LoadVideo, TrimVideoLatent, VAEDecode, Primitive integer [Crystools], GetNode, Primitive integer [Crystools], ModelSamplingSD3, SetNode, VHS_VideoCombine, SimpleMath+, SimpleMath+, VHS_VideoCombine, SimpleMath+, RHHiddenNodes, JjkText, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, ImageConcatMulti, LoadImage, JjkText, PathchSageAttentionKJ, ModelPatchTorchSettings, JjkText, VHS_VideoCombine, SimpleMath+, SimpleMath+, LoadImage, easy showAnything, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 399, "steps": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/完美动作迁移Animate 新 3.0（极致稳定+表情迁移）_1972602081016217602.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1972602081016217602.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `TorchCompileModelWanVideoV2`
- `ImpactSwitch`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `ImpactSwitch`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoInfoSource`
- `WanAnimateToVideo`
- `KSampler` ★核心
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAELoader`
- `GetNode`
- `SetNode`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `VHS_LoadVideo`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `Primitive integer [Crystools]`
- `GetNode`
- `Primitive integer [Crystools]`
- `ModelSamplingSD3`
- `SetNode`
- `VHS_VideoCombine`
- `SimpleMath+`
- `SimpleMath+`
- `VHS_VideoCombine`
- `SimpleMath+`
- `RHHiddenNodes`
- `JjkText`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `LoadImage`
- `JjkText`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `JjkText`
- `VHS_VideoCombine`
- `SimpleMath+`
- `SimpleMath+`
- `LoadImage`
- `easy showAnything`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`

## 关键参数

- `seed` = `399`
- `steps` = `1`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **58%**（42/73）

**有卡**：`TorchCompileModelWanVideoV2`、`Primitive integer [Crystools]`、`ImageResizeKJv2`、`CLIPTextEncode`、`CLIPVisionEncode`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_VideoInfoSource`、`WanAnimateToVideo`、`KSampler`、`VAELoader`、`VHS_LoadVideo`、`TrimVideoLatent`、`VAEDecode`、`ModelSamplingSD3`、`VHS_VideoCombine`、`SimpleMath+`、`RHHiddenNodes`、`ImageConcatMulti`、`LoadImage`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、CLIPVisionEncode、TrimVideoLatent、ImageResizeKJv2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
