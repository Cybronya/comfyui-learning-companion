---
key: 视频生成/图生视频/Wan-Animatev2.2_1971886781874499586.json
name: Wan-Animatev2.2_1971886781874499586.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan-Animatev2.2_1971886781874499586.json
hash: d2af46a014edcb42
coverage: 0.445545
learned_at: 2026-10-15 22:31:58
nodes: [PrimitiveFloat, GetNode, GetNode, SetNode, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPTextEncode, GetNode, GetNode, CLIPVisionLoader, CLIPVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, PlaySound|pysssss, VHS_VideoCombine, DownloadAndLoadGIMMVFIModel, SetNode, GetNode, GetNode, GIMMVFI_interpolate, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, easy showAnything, EmptyImage, TrimVideoLatent, SetNode, SetNode, ModelSamplingSD3, SetNode, Fast Groups Bypasser (rgthree), ImageResizeKJv2, Note, Note, Fast Groups Bypasser (rgthree), Note, GetNode, RemBGSession+, GrowMask, BlockifyMask, GetNode, DrawMaskOnImage, WanAnimateToVideo, Note, GetNode, GetNode, GetNode, ImageBlend, MarkdownNote, PoseAndFaceDetection, GetNode, ImageRemoveBackground+, VAEDecode, ImageConcatMulti, ImageConcatMulti, SetNode, SetNode, DrawViTPose, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, Note, GetNode, Fast Groups Bypasser (rgthree), CLIPTextEncode, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, OnnxDetectionModelLoader, CLIPLoader, wanBlockSwap, LoraLoaderModelOnly, Note, Note, PreviewImage, VAELoader, TorchCompileModelWanVideoV2, LoraLoaderModelOnly, UnetLoaderGGUF, KSampler, VHS_VideoCombine, VHS_LoadVideo, VHS_VideoCombine, INTConstant, INTConstant, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 428643340490152, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan-Animatev2.2_1971886781874499586.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971886781874499586.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（101 个）：
- `PrimitiveFloat`
- `GetNode`
- `GetNode`
- `SetNode`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PlaySound|pysssss`
- `VHS_VideoCombine`
- `DownloadAndLoadGIMMVFIModel`
- `SetNode`
- `GetNode`
- `GetNode`
- `GIMMVFI_interpolate`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `EmptyImage`
- `TrimVideoLatent`
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `Note`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `GetNode`
- `RemBGSession+`
- `GrowMask`
- `BlockifyMask`
- `GetNode`
- `DrawMaskOnImage`
- `WanAnimateToVideo`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageBlend`
- `MarkdownNote`
- `PoseAndFaceDetection`
- `GetNode`
- `ImageRemoveBackground+`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SetNode`
- `SetNode`
- `DrawViTPose`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `OnnxDetectionModelLoader`
- `CLIPLoader`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `PreviewImage`
- `VAELoader`
- `TorchCompileModelWanVideoV2`
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `KSampler` ★核心
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `LoadImage`

## 关键参数

- `seed` = `428643340490152`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **45%**（45/101）

**有卡**：`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`CLIPVisionLoader`、`CLIPVisionEncode`、`PlaySound|pysssss`、`VHS_VideoCombine`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`EmptyImage`、`TrimVideoLatent`、`ModelSamplingSD3`、`ImageResizeKJv2`、`RemBGSession+`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`WanAnimateToVideo`、`ImageBlend`、`PoseAndFaceDetection`、`ImageRemoveBackground+`、`VAEDecode`、`ImageConcatMulti`、`DrawViTPose`、`LoraLoaderModelOnly`、`OnnxDetectionModelLoader`、`CLIPLoader`、`wanBlockSwap`、`VAELoader`、`TorchCompileModelWanVideoV2`、`UnetLoaderGGUF`、`KSampler`、`VHS_LoadVideo`、`INTConstant`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
