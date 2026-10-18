---
key: 视频生成/图生视频/双图参考-Wan2.1-VACE-Native_1924845161095098369.json
name: 双图参考-Wan2.1-VACE-Native_1924845161095098369.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/双图参考-Wan2.1-VACE-Native_1924845161095098369.json
hash: e8f2a4bec60fadb5
coverage: 0.897436
learned_at: 2026-10-15 22:29:51
nodes: [VAEDecode, TrimVideoLatent, CLIPLoader, CLIPTextEncode, VAELoader, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, CFGZeroStarAndInit, WanVideoEnhanceAVideoKJ, TorchCompileModelWanVideo, PatchModelPatcherOrder, VHS_VideoCombine, KSampler, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, LayerMask: ObjectDetectorFL2, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, LayerMask: ObjectDetectorFL2, GetImageSize, Image Blank, ImageCompositeMasked, PreviewImage, PreviewImage, GetImageSize, Image Blank, ImageCompositeMasked, PreviewImage, easy showAnything, ImageConcanate, WanVaceToVideo, LoadImage, LoadImage, INTConstant, RH_Captioner, CLIPTextEncode, ImageResizeKJ, INTConstant]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 393989715004638, "steps": 20}
---

# 视频生成/图生视频/双图参考-Wan2.1-VACE-Native_1924845161095098369.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1924845161095098369.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `WanVideoEnhanceAVideoKJ`
- `TorchCompileModelWanVideo`
- `PatchModelPatcherOrder`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `LayerMask: ObjectDetectorFL2`
- `GetImageSize`
- `Image Blank`
- `ImageCompositeMasked`
- `PreviewImage`
- `PreviewImage`
- `GetImageSize`
- `Image Blank`
- `ImageCompositeMasked`
- `PreviewImage`
- `easy showAnything`
- `ImageConcanate`
- `WanVaceToVideo`
- `LoadImage`
- `LoadImage`
- `INTConstant`
- `RH_Captioner`
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `INTConstant`

## 关键参数

- `seed` = `393989715004638`
- `steps` = `20`
- `cfg` = `4`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（35/39）

**有卡**：`VAEDecode`、`TrimVideoLatent`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`CFGZeroStarAndInit`、`WanVideoEnhanceAVideoKJ`、`TorchCompileModelWanVideo`、`PatchModelPatcherOrder`、`VHS_VideoCombine`、`KSampler`、`LayerMask: LoadFlorence2Model`、`LayerMask: SAM2Ultra`、`LayerMask: ObjectDetectorFL2`、`GetImageSize`、`Image Blank`、`ImageCompositeMasked`、`ImageConcanate`、`WanVaceToVideo`、`LoadImage`、`INTConstant`、`RH_Captioner`、`ImageResizeKJ`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
