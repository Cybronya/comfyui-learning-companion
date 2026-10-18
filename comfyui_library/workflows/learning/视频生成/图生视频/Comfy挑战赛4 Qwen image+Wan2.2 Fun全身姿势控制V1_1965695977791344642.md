---
key: 视频生成/图生视频/Comfy挑战赛4 Qwen image+Wan2.2 Fun全身姿势控制V1_1965695977791344642.json
name: Comfy挑战赛4 Qwen image+Wan2.2 Fun全身姿势控制V1_1965695977791344642.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Comfy挑战赛4 Qwen image+Wan2.2 Fun全身姿势控制V1_1965695977791344642.json
hash: 9d1d246014bab5b5
coverage: 0.732673
learned_at: 2026-10-15 22:31:37
nodes: [WanVideoTextEmbedBridge, CLIPTextEncode, CLIPLoader, Note, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, Note, Note, Note, MarkdownNote, Note, WanVideoBlockSwap, CLIPTextEncode, SetNode, GetNode, SetNode, SetNode, GetNode, INTConstant, INTConstant, Reroute, SetNode, VHS_VideoCombine, Reroute, WanVideoEncode, GetNode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoTextEncodeCached, WanVideoAddControlEmbeds, GetImageSizeAndCount, WanVideoEncode, ImageResizeKJv2, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, ImageConcatMulti, ImageConcanate, VHS_VideoCombine, PDIMAGE_LongerSize, Note, Note, CLIPLoader, VAELoader, UNETLoader, ModelSamplingAuraFlow, SetUnionControlNetType, CFGNorm, ControlNetLoader, SaveLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PreviewImage, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, ControlNetApplySD3, EmptySD3LatentImage, CLIPTextEncode, ImageConcanate, KSampler, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, VHS_VideoInfo, CLIPTextEncode, easy anythingIndexSwitch, PreviewImage, PreviewImage, Reroute, Note, JWInteger, JWInteger, CR Prompt Text, GetNode, VHS_VideoCombine, VHS_VideoCombine, Reroute, easy cleanGpuUsed, JWInteger, ImageResizeKJv2, VAEDecode, easy cleanGpuUsed, WanVideoSetLoRAs, WanVideoDecode, WanVideoSampler, PrimitiveNode, easy anythingIndexSwitch, JWInteger, Note, ImageFromBatch+, WanVideoSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 716644440531110, "steps": 15}
---

# 视频生成/图生视频/Comfy挑战赛4 Qwen image+Wan2.2 Fun全身姿势控制V1_1965695977791344642.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1965695977791344642.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（101 个）：
- `WanVideoTextEmbedBridge`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `Note`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `Note`
- `Note`
- `Note`
- `MarkdownNote`
- `Note`
- `WanVideoBlockSwap`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `SetNode`
- `VHS_VideoCombine`
- `Reroute`
- `WanVideoEncode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoTextEncodeCached`
- `WanVideoAddControlEmbeds`
- `GetImageSizeAndCount`
- `WanVideoEncode`
- `ImageResizeKJv2`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `ImageConcatMulti`
- `ImageConcanate`
- `VHS_VideoCombine`
- `PDIMAGE_LongerSize`
- `Note`
- `Note`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `SetUnionControlNetType`
- `CFGNorm`
- `ControlNetLoader`
- `SaveLatent`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `ControlNetApplySD3` ★核心
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `ImageConcanate`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `VHS_VideoInfo`
- `CLIPTextEncode` ★核心
- `easy anythingIndexSwitch`
- `PreviewImage`
- `PreviewImage`
- `Reroute`
- `Note`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Reroute`
- `easy cleanGpuUsed`
- `JWInteger`
- `ImageResizeKJv2`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `easy anythingIndexSwitch`
- `JWInteger`
- `Note`
- `ImageFromBatch+`
- `WanVideoSampler` ★核心

## 关键参数

- `controlnet_strength` = `1.0000000000000002`
- `seed` = `716644440531110`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **73%**（74/101）

**有卡**：`WanVideoTextEmbedBridge`、`CLIPTextEncode`、`CLIPLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`INTConstant`、`VHS_VideoCombine`、`WanVideoEncode`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoTextEncodeCached`、`WanVideoAddControlEmbeds`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`WanVideoLoraSelectMulti`、`ImageConcatMulti`、`ImageConcanate`、`PDIMAGE_LongerSize`、`VAELoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`SetUnionControlNetType`、`CFGNorm`、`ControlNetLoader`、`SaveLatent`、`LoraLoaderModelOnly`、`VHS_LoadVideo`、`ControlNetApplySD3`、`EmptySD3LatentImage`、`KSampler`、`LayerUtility: PurgeVRAM`、`VHS_VideoInfo`、`easy anythingIndexSwitch`、`JWInteger`、`CR Prompt Text`、`easy cleanGpuUsed`、`VAEDecode`、`WanVideoDecode`、`WanVideoSampler`、`ImageFromBatch+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、ControlNetLoader
