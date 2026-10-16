---
key: 视频生成/图生视频/TTM轨迹控制视频Wan2.2 Smooth w. SplineEdit（Trajectory control video）_1991106081629798401.json
name: TTM轨迹控制视频Wan2.2 Smooth w. SplineEdit（Trajectory control video）_1991106081629798401.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1991106081629798401.json
hash: bbe7a8f284a77c0f
coverage: 0.896552
learned_at: 2026-10-15 22:33:12
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, ImageToMask, ImageResizeKJv2, WanVideoSetLoRAs, WanVideoEncode, GetNode, WanVideoSampler, WanVideoVAELoader, WanVideoBlockSwap, ImageResizeKJv2, VAEDecode, WanVideoModelLoader, WanVideoModelLoader, LayerUtility: ImageScaleByAspectRatio V2, RMBG, AILab_ColorInput, GetImageSizeAndCount, Mask To Image (mtb), VAEEncode, VAELoader, TextEncodeQwenImageEditPlus, CLIPLoader, NunchakuQwenImageDiTLoader, WanVideoImageToVideoEncode, VHS_VideoCombine, VHS_VideoCombine, GetImageSizeAndCount, ImageConcatMulti, GetNode, CreateCFGScheduleFloatList, INTConstant, INTConstant, WanVideoDecode, WanVideoDecode, VHS_VideoCombine, Int, WanVideoTextEncodeCached, RunningHub Deepcleaner, Int, CutAndDragOnPath, VHS_VideoCombine, VHS_VideoCombine, LoadImage, CR Text, easy showAnything, MarkdownNote, ModelSamplingAuraFlow, CFGNorm, KSampler, PreviewImage, TextEncodeQwenImageEditPlus, WanVideoAddTTMLatents, WanVideoTorchCompileSettings, SetNode, SplineEditor]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 423556042226779, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/TTM轨迹控制视频Wan2.2 Smooth w. SplineEdit（Trajectory control video）_1991106081629798401.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1991106081629798401.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `ImageToMask`
- `ImageResizeKJv2`
- `WanVideoSetLoRAs`
- `WanVideoEncode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `VAEDecode` ★核心
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RMBG`
- `AILab_ColorInput`
- `GetImageSizeAndCount`
- `Mask To Image (mtb)`
- `VAEEncode` ★核心
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `CLIPLoader`
- `NunchakuQwenImageDiTLoader`
- `WanVideoImageToVideoEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `WanVideoDecode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `Int`
- `WanVideoTextEncodeCached`
- `RunningHub Deepcleaner`
- `Int`
- `CutAndDragOnPath`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `CR Text`
- `easy showAnything`
- `MarkdownNote`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `KSampler` ★核心
- `PreviewImage`
- `TextEncodeQwenImageEditPlus`
- `WanVideoAddTTMLatents`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SplineEditor`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `423556042226779`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（52/58）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`ImageToMask`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`VAEDecode`、`WanVideoModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`RMBG`、`AILab_ColorInput`、`GetImageSizeAndCount`、`Mask To Image (mtb)`、`VAEEncode`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`CLIPLoader`、`NunchakuQwenImageDiTLoader`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`、`ImageConcatMulti`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoDecode`、`Int`、`WanVideoTextEncodeCached`、`RunningHub Deepcleaner`、`CutAndDragOnPath`、`LoadImage`、`CR Text`、`ModelSamplingAuraFlow`、`CFGNorm`、`KSampler`、`WanVideoAddTTMLatents`、`WanVideoTorchCompileSettings`、`SplineEditor`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGNorm、WanVideoSampler

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
