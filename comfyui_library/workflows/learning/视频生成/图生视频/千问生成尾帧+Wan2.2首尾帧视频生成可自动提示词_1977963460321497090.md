---
key: 视频生成/图生视频/千问生成尾帧+Wan2.2首尾帧视频生成可自动提示词_1977963460321497090.json
name: 千问生成尾帧+Wan2.2首尾帧视频生成可自动提示词_1977963460321497090.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1977963460321497090.json
hash: 5e4e1895bc1d8272
coverage: 0.864407
learned_at: 2026-10-15 22:32:16
nodes: [WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, LoadImage, WanVideoModelLoader, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, easy cleanGpuUsed, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSampler, ModelSamplingAuraFlow, CFGNorm, VAEEncode, KSampler, TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, PrimitiveInt, PrimitiveInt, PrimitiveInt, RH_LLMAPI_NODE, ShowText|pysssss, ShowText|pysssss, SimpleMath+, ImageBatchMultiple+, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, ImageScaleToTotalPixels, VAELoader, CLIPLoader, UNETLoader, CR Text, MarkdownNote, MarkdownNote, ImageResizeKJv2, ImageResizeKJv2, WanVideoClipVisionEncode, GetImageSizeAndCount, LoadImage, TextEncodeQwenImageEditPlus, PreviewImage, WanVideoSetBlockSwap, WanVideoSetLoRAs, CLIPVisionLoader, WanVideoTorchCompileSettings, AILab_MiniCPM_4_V_Advanced, LoraLoaderModelOnly, VAEDecode, CR Text Concatenate, String]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 364791062100152, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/千问生成尾帧+Wan2.2首尾帧视频生成可自动提示词_1977963460321497090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1977963460321497090.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `SimpleMath+`
- `ImageBatchMultiple+`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageScaleToTotalPixels`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CR Text`
- `MarkdownNote`
- `MarkdownNote`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoClipVisionEncode`
- `GetImageSizeAndCount`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `CLIPVisionLoader`
- `WanVideoTorchCompileSettings`
- `AILab_MiniCPM_4_V_Advanced`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `CR Text Concatenate`
- `String`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `364791062100152`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **86%**（51/59）

**有卡**：`WanVideoVAELoader`、`easy cleanGpuUsed`、`LoadImage`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSampler`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAEEncode`、`KSampler`、`TextEncodeQwenImageEditPlus`、`LoraLoaderModelOnly`、`RH_LLMAPI_NODE`、`SimpleMath+`、`ImageBatchMultiple+`、`VHS_VideoCombine`、`ImageScaleToTotalPixels`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`CR Text`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`CLIPVisionLoader`、`WanVideoTorchCompileSettings`、`AILab_MiniCPM_4_V_Advanced`、`VAEDecode`、`CR Text Concatenate`、`String`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
