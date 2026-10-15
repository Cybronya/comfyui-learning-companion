---
key: 图片生成/文生图/Wan2.2+千问剪纸风格视频生成_1976913869014765569.json
name: Wan2.2+千问剪纸风格视频生成_1976913869014765569
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2+千问剪纸风格视频生成_1976913869014765569.json
hash: 772a8b311ea8fb0d
coverage: 0.703704
learned_at: 2026-10-10 20:59:14
nodes: [WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, LoadWanVideoT5TextEncoder, WanVideoDecode, WanVideoSetBlockSwap, CLIPVisionLoader, easy cleanGpuUsed, VHS_VideoCombine, LoadImage, PrimitiveInt, PrimitiveInt, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoImageToVideoEncode, easy cleanGpuUsed, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoClipVisionEncode, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, easy cleanGpuUsed, CLIPTextEncode, ModelSamplingAuraFlow, easy cleanGpuUsed, CLIPTextEncode, KSampler, CR Text, String, CR Text Concatenate, GetImageSizeAndCount, easy cleanGpuUsed, WanVideoSampler, WanVideoSampler, ColorMatch, VHS_VideoCombine, ImageResizeKJv2, PreviewImage, VAEDecode, AILab_MiniCPM_4_V_Advanced, LoraLoaderModelOnly, CLIPLoader, VAELoader, EmptySD3LatentImage, LoraLoaderModelOnly, UNETLoader, MarkdownNote, ShowText|pysssss]
patterns: []
missing: [CR Text, CR Text Concatenate, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 757501154494349, "steps": 8}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Wan2.2+千问剪纸风格视频生成_1976913869014765569.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2+千问剪纸风格视频生成_1976913869014765569.json`

## 结构

**节点**（54 个）：
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoImageToVideoEncode`
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoClipVisionEncode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `easy cleanGpuUsed`
- `CLIPTextEncode`
- `ModelSamplingAuraFlow`
- `easy cleanGpuUsed`
- `CLIPTextEncode`
- `KSampler`
- `CR Text`
- `String`
- `CR Text Concatenate`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `WanVideoSampler`
- `WanVideoSampler`
- `ColorMatch`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `PreviewImage`
- `VAEDecode`
- `AILab_MiniCPM_4_V_Advanced`
- `LoraLoaderModelOnly`
- `CLIPLoader`
- `VAELoader`
- `EmptySD3LatentImage`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `MarkdownNote`
- `ShowText|pysssss`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `seed` = `757501154494349`
- `steps` = `8`

## 知识

覆盖率 **70%**（38/54）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`CLIPVisionLoader`、`VHS_VideoCombine`、`LoadImage`、`PrimitiveInt`、`WanVideoTorchCompileSettings`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`KSampler`、`CR Text`、`String`、`CR Text Concatenate`、`GetImageSizeAndCount`

**缺卡**（11）：`CR Text`、`CR Text Concatenate`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
