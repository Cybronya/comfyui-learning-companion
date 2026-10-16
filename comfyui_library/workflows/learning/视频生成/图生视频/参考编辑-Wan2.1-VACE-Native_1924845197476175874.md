---
key: 视频生成/图生视频/参考编辑-Wan2.1-VACE-Native_1924845197476175874.json
name: 参考编辑-Wan2.1-VACE-Native_1924845197476175874.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1924845197476175874.json
hash: 64db98c14b7d6842
coverage: 0.966667
learned_at: 2026-10-15 22:29:51
nodes: [VAEDecode, TrimVideoLatent, CLIPLoader, CLIPTextEncode, VAELoader, UNETLoader, ModelSamplingSD3, CFGZeroStarAndInit, WanVideoEnhanceAVideoKJ, TorchCompileModelWanVideo, PatchModelPatcherOrder, LayerMask: ObjectDetectorFL2, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, InpaintPreprocessor, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, GrowMaskWithBlur, WanVaceToVideo, VHS_LoadVideo, INTConstant, KSampler, LoadImage, INTConstant, CLIPTextEncode, LoraLoaderModelOnly, ImageResizeKJ, PreviewImage, ImageResizeKJ, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 610944523454634, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/参考编辑-Wan2.1-VACE-Native_1924845197476175874.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1924845197476175874.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `WanVideoEnhanceAVideoKJ`
- `TorchCompileModelWanVideo`
- `PatchModelPatcherOrder`
- `LayerMask: ObjectDetectorFL2`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `InpaintPreprocessor`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `GrowMaskWithBlur`
- `WanVaceToVideo`
- `VHS_LoadVideo`
- `INTConstant`
- `KSampler` ★核心
- `LoadImage`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJ`
- `PreviewImage`
- `ImageResizeKJ`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `610944523454634`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`VAEDecode`、`TrimVideoLatent`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`ModelSamplingSD3`、`CFGZeroStarAndInit`、`WanVideoEnhanceAVideoKJ`、`TorchCompileModelWanVideo`、`PatchModelPatcherOrder`、`LayerMask: ObjectDetectorFL2`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`InpaintPreprocessor`、`LayerMask: LoadFlorence2Model`、`LayerMask: SAM2Ultra`、`GrowMaskWithBlur`、`WanVaceToVideo`、`VHS_LoadVideo`、`INTConstant`、`KSampler`、`LoadImage`、`LoraLoaderModelOnly`、`ImageResizeKJ`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
