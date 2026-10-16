---
key: 视频生成/图生视频/Comfy挑战赛4 Qwen image+Wan2.2 UNI3C全身姿势控制V1_1965693287438929921.json
name: Comfy挑战赛4 Qwen image+Wan2.2 UNI3C全身姿势控制V1_1965693287438929921.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1965693287438929921.json
hash: 414463a22bb1baee
coverage: 0.903226
learned_at: 2026-10-15 22:31:37
nodes: [WanVideoDecode, LoadWanVideoT5TextEncoder, ImageResizeKJ, PreviewImage, WanVideoImageToVideoEncode, ImageConcanate, WanVideoEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoTextEncode, WanVideoVAELoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoSampler, WanVideoModelLoader, ImageResizeKJ, VHS_VideoCombine, CLIPLoader, VAELoader, UNETLoader, ModelSamplingAuraFlow, SetUnionControlNetType, CFGNorm, ControlNetLoader, SaveLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageFromBatch+, PreviewImage, JWInteger, Note, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, ControlNetApplySD3, EmptySD3LatentImage, CLIPTextEncode, KSampler, LoraLoaderModelOnly, VHS_VideoInfo, CLIPTextEncode, easy anythingIndexSwitch, PreviewImage, PreviewImage, easy anythingIndexSwitch, LoraLoaderModelOnly, ImageConcanate, VAEDecode, CR Prompt Text, LayerUtility: PurgeVRAM, Reroute, VHS_LoadVideo, JWInteger, JWInteger, VHS_VideoCombine, easy cleanGpuUsed, easy cleanGpuUsed]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 438497175679193, "steps": 15}
---

# 视频生成/图生视频/Comfy挑战赛4 Qwen image+Wan2.2 UNI3C全身姿势控制V1_1965693287438929921.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1965693287438929921.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `ImageResizeKJ`
- `PreviewImage`
- `WanVideoImageToVideoEncode`
- `ImageConcanate`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `ImageResizeKJ`
- `VHS_VideoCombine`
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
- `ImageFromBatch+`
- `PreviewImage`
- `JWInteger`
- `Note`
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
- `VHS_VideoInfo`
- `CLIPTextEncode` ★核心
- `easy anythingIndexSwitch`
- `PreviewImage`
- `PreviewImage`
- `easy anythingIndexSwitch`
- `LoraLoaderModelOnly` ★核心
- `ImageConcanate`
- `VAEDecode` ★核心
- `CR Prompt Text`
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`

## 关键参数

- `controlnet_strength` = `1.0000000000000002`
- `seed` = `438497175679193`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **90%**（56/62）

**有卡**：`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`ImageResizeKJ`、`WanVideoImageToVideoEncode`、`ImageConcanate`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`WanVideoTextEncode`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoModelLoader`、`VHS_VideoCombine`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`SetUnionControlNetType`、`CFGNorm`、`ControlNetLoader`、`SaveLatent`、`LoraLoaderModelOnly`、`ImageFromBatch+`、`JWInteger`、`VHS_LoadVideo`、`ControlNetApplySD3`、`EmptySD3LatentImage`、`CLIPTextEncode`、`KSampler`、`VHS_VideoInfo`、`easy anythingIndexSwitch`、`VAEDecode`、`CR Prompt Text`、`LayerUtility: PurgeVRAM`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、ControlNetLoader
