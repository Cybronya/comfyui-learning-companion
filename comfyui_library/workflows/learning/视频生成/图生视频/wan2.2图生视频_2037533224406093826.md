---
key: 视频生成/图生视频/wan2.2图生视频_2037533224406093826.json
name: wan2.2图生视频_2037533224406093826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2037533224406093826.json
hash: c0231dab5a329b60
coverage: 0.971429
learned_at: 2026-10-15 22:35:58
nodes: [WanVideoSetLoRAs, WanVideoSetLoRAs, easy cleanGpuUsed, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSampler, INTConstant, INTConstant, LoadImage, CreateCFGScheduleFloatList, WanVideoSampler, easy cleanGpuUsed, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, CLIPTextEncode, CLIPLoaderGGUF, CLIPLoader, WanVideoTextEmbedBridge, WanVideoVAELoader, WanVideoDecode, ReActorFaceSwap, WanVideoModelLoader, WanVideoModelLoader, LoadImage, VideoFrameExtractor, GetImageSizeAndCount, PreviewImage, SaveVideo, WanVideoImageToVideoEncode, CLIPTextEncode, CreateVideo, PreViewVideo, ImageResizeKJv2]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2图生视频_2037533224406093826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037533224406093826.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（35 个）：
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `CLIPTextEncode` ★核心
- `CLIPLoaderGGUF`
- `CLIPLoader`
- `WanVideoTextEmbedBridge`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `ReActorFaceSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadImage`
- `VideoFrameExtractor`
- `GetImageSizeAndCount`
- `PreviewImage`
- `SaveVideo`
- `WanVideoImageToVideoEncode`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `PreViewVideo`
- `ImageResizeKJv2`

## 知识

覆盖率 **97%**（34/35）

**有卡**：`WanVideoSetLoRAs`、`easy cleanGpuUsed`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`INTConstant`、`LoadImage`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`CLIPTextEncode`、`CLIPLoaderGGUF`、`CLIPLoader`、`WanVideoTextEmbedBridge`、`WanVideoVAELoader`、`WanVideoDecode`、`ReActorFaceSwap`、`WanVideoModelLoader`、`VideoFrameExtractor`、`GetImageSizeAndCount`、`SaveVideo`、`WanVideoImageToVideoEncode`、`CreateVideo`、`PreViewVideo`、`ImageResizeKJv2`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode
