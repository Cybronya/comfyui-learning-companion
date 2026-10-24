---
key: 图片生成/图生图/完美人物替换Animate 新3.2（真人替换）_1972999507698913281.json
name: 完美人物替换Animate 新3.2（真人替换）_1972999507698913281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/完美人物替换Animate 新3.2（真人替换）_1972999507698913281.json
hash: 79ddb5221f328e5f
coverage: 0.6
learned_at: 2026-10-23 12:47:46
nodes: [TorchCompileModelWanVideoV2, ImpactSwitch, Primitive integer [Crystools], Primitive integer [Crystools], SetNode, SetNode, SetNode, PreviewImage, GetNode, GetNode, ImpactSwitch, CLIPVisionEncode, SetNode, GetNode, GetNode, PoseAndFaceDetection, DrawViTPose, VHS_VideoInfoSource, KSampler, SetNode, SetNode, CLIPTextEncode, GetNode, VAELoader, GetNode, SetNode, Primitive integer [Crystools], Primitive integer [Crystools], VHS_LoadVideo, TrimVideoLatent, VAEDecode, Primitive integer [Crystools], GetNode, Primitive integer [Crystools], ModelSamplingSD3, SetNode, VHS_VideoCombine, SimpleMath+, SimpleMath+, VHS_VideoCombine, SimpleMath+, JjkText, easy showAnything, GetNode, GetNode, GetNode, ImageConcatMulti, ImageConcatMulti, LoadImage, JjkText, PathchSageAttentionKJ, ModelPatchTorchSettings, WanVideoBlockSwap, JjkText, VHS_VideoCombine, SimpleMath+, ImageResizeKJv2, GetNode, SimpleMath+, SetNode, GetNode, Sam2Segmentation, LoadImage, BlockifyMask, DrawMaskOnImage, SetNode, SetNode, GetNode, GetNode, ImageBlend, VHS_VideoCombine, SetNode, GetNode, WanVideoClipVisionEncode, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, WanAnimateToVideo, CLIPTextEncode, RHHiddenNodes, RHHiddenNodes]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 399, "steps": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/完美人物替换Animate 新3.2（真人替换）_1972999507698913281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/完美人物替换Animate 新3.2（真人替换）_1972999507698913281.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
- `TorchCompileModelWanVideoV2`
- `ImpactSwitch`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `ImpactSwitch`
- `CLIPVisionEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `VHS_VideoInfoSource`
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
- `JjkText`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `LoadImage`
- `JjkText`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `WanVideoBlockSwap`
- `JjkText`
- `VHS_VideoCombine`
- `SimpleMath+`
- `ImageResizeKJv2`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `GetNode`
- `Sam2Segmentation`
- `LoadImage`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageBlend`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `WanAnimateToVideo`
- `CLIPTextEncode` ★核心
- `RHHiddenNodes`
- `RHHiddenNodes`

## 关键参数

- `seed` = `399`
- `steps` = `1`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **60%**（51/85）

**有卡**：`TorchCompileModelWanVideoV2`、`Primitive integer [Crystools]`、`CLIPVisionEncode`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_VideoInfoSource`、`KSampler`、`CLIPTextEncode`、`VAELoader`、`VHS_LoadVideo`、`TrimVideoLatent`、`VAEDecode`、`ModelSamplingSD3`、`VHS_VideoCombine`、`SimpleMath+`、`ImageConcatMulti`、`LoadImage`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`Sam2Segmentation`、`BlockifyMask`、`DrawMaskOnImage`、`ImageBlend`、`WanVideoClipVisionEncode`、`RHHiddenNodes`、`WanAnimateToVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、CLIPVisionEncode、TrimVideoLatent、WanVideoClipVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
