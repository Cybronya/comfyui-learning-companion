---
key: 图片生成/文生图/Qwen千问文生图+Wan2.2图生视频，强强联合_1953107742094520321.json
name: Qwen千问文生图+Wan2.2图生视频，强强联合_1953107742094520321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen千问文生图+Wan2.2图生视频，强强联合_1953107742094520321.json
hash: 840fa0ca48eb6268
coverage: 0.956522
learned_at: 2026-10-15 22:27:28
nodes: [WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoTextEncode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoModelLoader, ImageResizeKJv2, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoDecode, GetImageSizeAndCount, WanVideoImageToVideoEncode, CLIPVisionLoader, UNETLoader, VAELoader, CLIPLoader, EmptySD3LatentImage, RH_LLMAPI_NODE, PreviewImage, WanVideoTorchCompileSettings, VAEDecode, ModelSamplingAuraFlow, KSampler, CR Text, CLIPTextEncode, CLIPTextEncode, easy cleanGpuUsed, easy cleanGpuUsed, easy showAnything, LoadImage, LoadImage, WanVideoClipVisionEncode, WanVideoSampler, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 984153404233391, "steps": 20}
---

# 图片生成/文生图/Qwen千问文生图+Wan2.2图生视频，强强联合_1953107742094520321.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen千问文生图+Wan2.2图生视频，强强联合_1953107742094520321.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoImageToVideoEncode`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `RH_LLMAPI_NODE`
- `PreviewImage`
- `WanVideoTorchCompileSettings`
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `CR Text`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `984153404233391`
- `steps` = `20`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（44/46）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoTextEncode`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`ImageResizeKJv2`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoImageToVideoEncode`、`CLIPVisionLoader`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`EmptySD3LatentImage`、`RH_LLMAPI_NODE`、`WanVideoTorchCompileSettings`、`VAEDecode`、`ModelSamplingAuraFlow`、`KSampler`、`CR Text`、`CLIPTextEncode`、`LoadImage`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanVideoSampler
