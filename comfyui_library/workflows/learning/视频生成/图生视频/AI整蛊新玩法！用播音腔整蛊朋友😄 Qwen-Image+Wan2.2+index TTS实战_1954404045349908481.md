---
key: 视频生成/图生视频/AI整蛊新玩法！用播音腔整蛊朋友😄 Qwen-Image+Wan2.2+index TTS实战_1954404045349908481.json
name: AI整蛊新玩法！用播音腔整蛊朋友😄 Qwen-Image+Wan2.2+index TTS实战_1954404045349908481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AI整蛊新玩法！用播音腔整蛊朋友😄 Qwen-Image+Wan2.2+index TTS实战_1954404045349908481.json
hash: 235a881b43b7ecda
coverage: 0.833333
learned_at: 2026-10-15 22:42:35
nodes: [VAELoader, UNETLoader, EmptySD3LatentImage, MarkdownNote, MarkdownNote, Note, ModelSamplingAuraFlow, Note, CLIPTextEncode, TextConcatenator, SetNode, Note, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoLoraSelect, ShowText, WanVideoVAELoader, WanVideoModelLoader, WanVideoTextEncode, ImageResizeKJv2, WanVideoImageToVideoEncode, GetNode, PreviewAudio, WanVideoSampler, WanVideoSampler, INTConstant, INTConstant, PreviewImage, IndexTTSNode, WanVideoModelLoader, CLIPLoader, CLIPTextEncode, KSampler, LoadAudio, Text, WanVideoLoraSelect, CreateCFGScheduleFloatList, VHS_VideoCombine, VAEDecode, Text, Label (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 432263983758413, "steps": 20}
---

# 视频生成/图生视频/AI整蛊新玩法！用播音腔整蛊朋友😄 Qwen-Image+Wan2.2+index TTS实战_1954404045349908481.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/AI整蛊新玩法！用播音腔整蛊朋友😄 Qwen-Image+Wan2.2+index TTS实战_1954404045349908481.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `EmptySD3LatentImage`
- `MarkdownNote`
- `MarkdownNote`
- `Note`
- `ModelSamplingAuraFlow`
- `Note`
- `CLIPTextEncode` ★核心
- `TextConcatenator`
- `SetNode`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `ShowText`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `PreviewAudio`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `PreviewImage`
- `IndexTTSNode`
- `WanVideoModelLoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoadAudio`
- `Text`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `Text`
- `Label (rgthree)`

## 关键参数

- `seed` = `432263983758413`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（40/48）

**有卡**：`VAELoader`、`UNETLoader`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`TextConcatenator`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`GetImageSizeAndCount`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`ShowText`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoTextEncode`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`PreviewAudio`、`WanVideoSampler`、`INTConstant`、`IndexTTSNode`、`CLIPLoader`、`KSampler`、`LoadAudio`、`Text`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`、`VAEDecode`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、WanVideoSampler、CreateCFGScheduleFloatList
