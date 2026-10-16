---
key: 视频生成/图生视频/ai女装带货视频_wan2.2 animate人物动作迁移v2_2054814579808587777.json
name: ai女装带货视频_wan2.2 animate人物动作迁移v2_2054814579808587777.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2054814579808587777.json
hash: 3852c2fa159366eb
coverage: 0.448598
learned_at: 2026-10-15 22:37:52
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, PoseAndFaceDetection, GetNode, UNETLoader, GetNode, GetNode, ImageConcatMulti, ImageConcatMulti, GetNode, SDPoseKeypointExtractor, GetNode, GetNode, ImageResizeKJv2, SetNode, LoadImage, GetNode, ImageResizeKJv2, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, SetNode, SetNode, SetNode, CLIPTextEncode, WanVideoTextEmbedBridge, SetNode, CLIPLoader, RTDETR_detect, GetNode, SetNode, GetImageSizeAndCount, SetNode, WanVideoDecode, GetNode, MarkdownNote, VHS_VideoCombine, GetNode, GetNode, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, WanVideoSamplerv2, easy cleanGpuUsed, easy cleanGpuUsed, GetNode, GetNode, GetNode, GetNode, WanVideoSamplerExtraArgs, GetNode, WanVideoSchedulerv2, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, SetNode, PrimitiveInt, SetNode, SimpleMath+, WanVideoAnimateEmbeds, SetNode, VHS_VideoCombine, SDPoseDrawKeypoints, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, SetNode, WanVideoContextOptions, GetNode, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, SetNode, CLIPVisionLoader, SetNode, PrimitiveNode, WanVideoBlockSwap, GetNode, CheckpointLoaderSimple, WanVideoLoraSelectMulti, PrimitiveInt, PrimitiveInt, PrimitiveInt, FloatConstant, Float to Int, VHS_LoadVideo, WanVideoModelLoader, CLIPTextEncode, OnnxDetectionModelLoader, Fast Groups Muter (rgthree)]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/ai女装带货视频_wan2.2 animate人物动作迁移v2_2054814579808587777.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054814579808587777.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（107 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `GetNode`
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetNode`
- `SDPoseKeypointExtractor`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `LoadImage`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `WanVideoTextEmbedBridge`
- `SetNode`
- `CLIPLoader`
- `RTDETR_detect`
- `GetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `WanVideoDecode`
- `GetNode`
- `MarkdownNote`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `WanVideoSamplerv2` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSamplerExtraArgs` ★核心
- `GetNode`
- `WanVideoSchedulerv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveInt`
- `SetNode`
- `SimpleMath+`
- `WanVideoAnimateEmbeds`
- `SetNode`
- `VHS_VideoCombine`
- `SDPoseDrawKeypoints`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `WanVideoContextOptions`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `PrimitiveNode`
- `WanVideoBlockSwap`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `WanVideoLoraSelectMulti`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `FloatConstant`
- `Float to Int`
- `VHS_LoadVideo`
- `WanVideoModelLoader`
- `CLIPTextEncode` ★核心
- `OnnxDetectionModelLoader`
- `Fast Groups Muter (rgthree)`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **45%**（48/107）

**有卡**：`PoseAndFaceDetection`、`UNETLoader`、`ImageConcatMulti`、`SDPoseKeypointExtractor`、`ImageResizeKJv2`、`LoadImage`、`VHS_VideoCombine`、`CLIPTextEncode`、`WanVideoTextEmbedBridge`、`CLIPLoader`、`RTDETR_detect`、`GetImageSizeAndCount`、`WanVideoDecode`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`WanVideoSamplerv2`、`easy cleanGpuUsed`、`WanVideoSamplerExtraArgs`、`WanVideoSchedulerv2`、`WanVideoClipVisionEncode`、`SimpleMath+`、`WanVideoAnimateEmbeds`、`SDPoseDrawKeypoints`、`LayerUtility: PurgeVRAM V2`、`WanVideoContextOptions`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`CheckpointLoaderSimple`、`WanVideoLoraSelectMulti`、`FloatConstant`、`Float to Int`、`VHS_LoadVideo`、`WanVideoModelLoader`、`OnnxDetectionModelLoader`

**用到的条目**：CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler
