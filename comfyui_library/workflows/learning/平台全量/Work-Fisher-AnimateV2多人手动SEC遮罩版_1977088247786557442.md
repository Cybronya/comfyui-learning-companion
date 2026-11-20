---
key: 平台全量/Work-Fisher-AnimateV2多人手动SEC遮罩版_1977088247786557442.json
name: Work-Fisher-AnimateV2多人手动SEC遮罩版_1977088247786557442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Work-Fisher-AnimateV2多人手动SEC遮罩版_1977088247786557442.json
hash: ee83599bc7e9016b
coverage: 0.454545
learned_at: 2026-11-14 01:07:23
nodes: [PreviewImage, GetNode, GetNode, SetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, TrimVideoLatent, GetNode, GetNode, GetNode, GetNode, PoseAndFaceDetection, VAEDecode, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, ModelPatchTorchSettings, PathchSageAttentionKJ, GetNode, GetNode, wanBlockSwap, TorchCompileModelWanVideoV2, Fast Groups Bypasser (rgthree), SetNode, SetNode, SetNode, ImageResizeKJv2, ModelSamplingSD3, SetNode, SetNode, SetNode, SetNode, easy showAnything, PrimitiveFloat, SetNode, SetNode, SetNode, INTConstant, INTConstant, VHS_LoadVideo, OnnxDetectionModelLoader, SetNode, VHS_VideoCombine, LoadImage, KSampler, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, Note, VHS_VideoCombine, MarkdownNote, Fast Groups Bypasser (rgthree), WanAnimateToVideo, CLIPVisionEncode, LoadImage, Note, VHS_VideoCombine, SetNode, ImageBlend, GrowMask, SetNode, Note, GetNode, DrawMaskOnImage, SetNode, DrawViTPose, SeCVideoSegmentation, SeCModelLoader, easy cleanGpuUsed, CLIPVisionLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, BlockifyMask, PointsEditor, UnetLoaderGGUF, ImageConcatMulti, GetNode, PlaySound|pysssss, GetNode, GetNode, RIFE VFI, VHS_VideoCombine, GetNode, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 214, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Work-Fisher-AnimateV2多人手动SEC遮罩版_1977088247786557442.json

> 来源文件 `comfyui_library/workflows/平台全量/Work-Fisher-AnimateV2多人手动SEC遮罩版_1977088247786557442.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
- `PreviewImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `GetNode`
- `GetNode`
- `wanBlockSwap`
- `TorchCompileModelWanVideoV2`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `VHS_LoadVideo`
- `OnnxDetectionModelLoader`
- `SetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `VHS_VideoCombine`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `WanAnimateToVideo`
- `CLIPVisionEncode`
- `LoadImage`
- `Note`
- `VHS_VideoCombine`
- `SetNode`
- `ImageBlend`
- `GrowMask`
- `SetNode`
- `Note`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `DrawViTPose`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `easy cleanGpuUsed`
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `BlockifyMask`
- `PointsEditor`
- `UnetLoaderGGUF` ★核心
- `ImageConcatMulti`
- `GetNode`
- `PlaySound|pysssss`
- `GetNode`
- `GetNode`
- `RIFE VFI`
- `VHS_VideoCombine`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `214`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **45%**（45/99）

**有卡**：`CLIPTextEncode`、`TrimVideoLatent`、`PoseAndFaceDetection`、`VAEDecode`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`wanBlockSwap`、`TorchCompileModelWanVideoV2`、`ImageResizeKJv2`、`ModelSamplingSD3`、`INTConstant`、`VHS_LoadVideo`、`OnnxDetectionModelLoader`、`VHS_VideoCombine`、`LoadImage`、`KSampler`、`ImageConcatMulti`、`WanAnimateToVideo`、`CLIPVisionEncode`、`ImageBlend`、`GrowMask`、`DrawMaskOnImage`、`DrawViTPose`、`SeCVideoSegmentation`、`SeCModelLoader`、`easy cleanGpuUsed`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`BlockifyMask`、`PointsEditor`、`UnetLoaderGGUF`、`PlaySound|pysssss`、`RIFE VFI`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
