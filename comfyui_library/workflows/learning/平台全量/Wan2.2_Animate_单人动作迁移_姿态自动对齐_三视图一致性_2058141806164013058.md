---
key: 平台全量/Wan2.2_Animate_单人动作迁移_姿态自动对齐_三视图一致性_2058141806164013058.json
name: Wan2.2_Animate_单人动作迁移_姿态自动对齐_三视图一致性_2058141806164013058
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2_Animate_单人动作迁移_姿态自动对齐_三视图一致性_2058141806164013058.json
hash: 17eccde7e20d5adf
coverage: 0.540816
learned_at: 2026-11-14 01:06:15
nodes: [SetNode, SetNode, GetNode, WanVideoClipVisionEncode, GetNode, SetNode, WanVideoSetBlockSwap, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, WanVideoAnimateEmbeds, GetNode, GetNode, SetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, GetNode, GetNode, WanVideoSamplerSettings, INTConstant, SDPoseKeypointExtractor, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, WanVideoEncode, PrimitiveFloat, PoseAndFaceDetection, WanVideoUni3C_embeds, PrimitiveFloat, PrimitiveFloat, PrimitiveBoolean, PrimitiveFloat, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Note, Note, Note, ComfySwitchNode, Seed (rgthree), PrimitiveFloat, LoadImage, LoadImage, WanVideoVAELoader, SetNode, CLIPVisionLoader, CheckpointLoaderSimple, OnnxDetectionModelLoader, WanVideoUni3C_ControlnetLoader, WanVideoSetLoRAs, SDPoseKeypointExtractor, Label (rgthree), WanVideoDecode, WanVideoSamplerFromSettings, GetNode, ImageResizeKJv2, VHS_VideoInfoLoaded, SetNode, VHS_LoadVideo, INTConstant, INTConstant, WanVideoModelLoader, BodyRatioMapperSDPoseRender, VHS_VideoCombine, VHS_VideoCombine, BodyRatioMapperSDPoseRender, BodyRatioMapperProportionTransfer, LayerUtility: PurgeVRAM V2, WanVideoContextOptions, WanVideoBlockSwap, WanVideoTextEncodeCached, PrimitiveFloat]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/Wan2.2_Animate_单人动作迁移_姿态自动对齐_三视图一致性_2058141806164013058.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2_Animate_单人动作迁移_姿态自动对齐_三视图一致性_2058141806164013058.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（98 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoTorchCompileSettings`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `WanVideoSamplerSettings` ★核心
- `INTConstant`
- `SDPoseKeypointExtractor`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `PrimitiveFloat`
- `PoseAndFaceDetection`
- `WanVideoUni3C_embeds`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Note`
- `Note`
- `Note`
- `ComfySwitchNode`
- `Seed (rgthree)`
- `PrimitiveFloat`
- `LoadImage`
- `LoadImage`
- `WanVideoVAELoader`
- `SetNode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple` ★核心
- `OnnxDetectionModelLoader`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoSetLoRAs`
- `SDPoseKeypointExtractor`
- `Label (rgthree)`
- `WanVideoDecode`
- `WanVideoSamplerFromSettings` ★核心
- `GetNode`
- `ImageResizeKJv2`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `VHS_LoadVideo`
- `INTConstant`
- `INTConstant`
- `WanVideoModelLoader`
- `BodyRatioMapperSDPoseRender`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `BodyRatioMapperSDPoseRender`
- `BodyRatioMapperProportionTransfer`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `PrimitiveFloat`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **54%**（53/98）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoAnimateEmbeds`、`ImageResizeKJv2`、`WanVideoSamplerSettings`、`INTConstant`、`SDPoseKeypointExtractor`、`VHS_VideoCombine`、`WanVideoEncode`、`PoseAndFaceDetection`、`WanVideoUni3C_embeds`、`PrimitiveBoolean`、`Label (rgthree)`、`Seed (rgthree)`、`LoadImage`、`WanVideoVAELoader`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`OnnxDetectionModelLoader`、`WanVideoUni3C_ControlnetLoader`、`WanVideoSetLoRAs`、`WanVideoDecode`、`WanVideoSamplerFromSettings`、`VHS_VideoInfoLoaded`、`VHS_LoadVideo`、`WanVideoModelLoader`、`BodyRatioMapperSDPoseRender`、`BodyRatioMapperProportionTransfer`、`LayerUtility: PurgeVRAM V2`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`

**用到的条目**：CheckpointLoaderSimple、LoadImage、WanVideoUni3C_ControlnetLoader、Seed (rgthree)、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoClipVisionEncode、WanVideoDecode
