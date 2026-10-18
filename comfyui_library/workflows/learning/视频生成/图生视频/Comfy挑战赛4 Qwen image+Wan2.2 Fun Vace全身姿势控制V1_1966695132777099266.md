---
key: 视频生成/图生视频/Comfy挑战赛4 Qwen image+Wan2.2 Fun Vace全身姿势控制V1_1966695132777099266.json
name: Comfy挑战赛4 Qwen image+Wan2.2 Fun Vace全身姿势控制V1_1966695132777099266.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Comfy挑战赛4 Qwen image+Wan2.2 Fun Vace全身姿势控制V1_1966695132777099266.json
hash: 6d74d50db5a750c0
coverage: 0.919463
learned_at: 2026-10-15 22:31:39
nodes: [WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, ImageConcatMulti, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoTextEncode, WanVideoModelLoader, Float, WanVideoSigmaToStep, INTConstant, WanVideoScheduler, WanVideoScheduler, WanVideoDecode, ColorMatch, VHS_VideoCombine, StringToFloatList, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoSampler, VHS_VideoCombine, WanVideoVACEEncode, CLIPLoader, VAELoader, UNETLoader, ModelSamplingAuraFlow, SetUnionControlNetType, CFGNorm, ControlNetLoader, SaveLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, PreviewImage, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, ControlNetApplySD3, EmptySD3LatentImage, CLIPTextEncode, KSampler, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, CLIPTextEncode, easy anythingIndexSwitch, PreviewImage, JWInteger, Note, ImageFromBatch+, LoraLoaderModelOnly, easy anythingIndexSwitch, VHS_VideoInfo, easy cleanGpuUsed, easy cleanGpuUsed, ImageResizeKJv2, Reroute, ImageConcanate, VAEDecode, StringToFloatList, Note, JWInteger, PreviewImage, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, ImageConcatMulti, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoTextEncode, WanVideoModelLoader, Float, WanVideoSigmaToStep, INTConstant, WanVideoScheduler, WanVideoScheduler, WanVideoDecode, ColorMatch, VHS_VideoCombine, StringToFloatList, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoSampler, VHS_VideoCombine, WanVideoVACEEncode, CLIPLoader, VAELoader, UNETLoader, ModelSamplingAuraFlow, SetUnionControlNetType, CFGNorm, ControlNetLoader, SaveLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, PreviewImage, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, ControlNetApplySD3, EmptySD3LatentImage, CLIPTextEncode, KSampler, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, CLIPTextEncode, easy anythingIndexSwitch, PreviewImage, JWInteger, Note, ImageFromBatch+, LoraLoaderModelOnly, easy anythingIndexSwitch, VHS_VideoInfo, easy cleanGpuUsed, easy cleanGpuUsed, ImageResizeKJv2, Reroute, ImageConcanate, VAEDecode, StringToFloatList, Note, JWInteger, PreviewImage, WanVideoVACEModelSelect, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 921013487911929, "steps": 15}
---

# 视频生成/图生视频/Comfy挑战赛4 Qwen image+Wan2.2 Fun Vace全身姿势控制V1_1966695132777099266.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1966695132777099266.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（149 个）：
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `Float`
- `WanVideoSigmaToStep`
- `INTConstant`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoDecode`
- `ColorMatch`
- `VHS_VideoCombine`
- `StringToFloatList`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoVACEEncode`
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
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `easy anythingIndexSwitch`
- `PreviewImage`
- `JWInteger`
- `Note`
- `ImageFromBatch+`
- `LoraLoaderModelOnly` ★核心
- `easy anythingIndexSwitch`
- `VHS_VideoInfo`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `Reroute`
- `ImageConcanate`
- `VAEDecode` ★核心
- `StringToFloatList`
- `Note`
- `JWInteger`
- `PreviewImage`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `Float`
- `WanVideoSigmaToStep`
- `INTConstant`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoDecode`
- `ColorMatch`
- `VHS_VideoCombine`
- `StringToFloatList`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoVACEEncode`
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
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `easy anythingIndexSwitch`
- `PreviewImage`
- `JWInteger`
- `Note`
- `ImageFromBatch+`
- `LoraLoaderModelOnly` ★核心
- `easy anythingIndexSwitch`
- `VHS_VideoInfo`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `Reroute`
- `ImageConcanate`
- `VAEDecode` ★核心
- `StringToFloatList`
- `Note`
- `JWInteger`
- `PreviewImage`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 关键参数

- `controlnet_strength` = `1.0000000000000002`
- `seed` = `921013487911929`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **92%**（137/149）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`ImageConcatMulti`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`Float`、`WanVideoSigmaToStep`、`INTConstant`、`WanVideoScheduler`、`WanVideoDecode`、`ColorMatch`、`VHS_VideoCombine`、`StringToFloatList`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVACEEncode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`SetUnionControlNetType`、`CFGNorm`、`ControlNetLoader`、`SaveLatent`、`LoraLoaderModelOnly`、`VHS_LoadVideo`、`ControlNetApplySD3`、`EmptySD3LatentImage`、`CLIPTextEncode`、`KSampler`、`LayerUtility: PurgeVRAM`、`easy anythingIndexSwitch`、`JWInteger`、`ImageFromBatch+`、`VHS_VideoInfo`、`easy cleanGpuUsed`、`ImageResizeKJv2`、`ImageConcanate`、`VAEDecode`、`WanVideoVACEModelSelect`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
