---
key: 视频生成/图生视频/Comfy挑战赛4 Qwen image+Wan2.2 Vace全身姿势控制V1_1965691739010945025.json
name: Comfy挑战赛4 Qwen image+Wan2.2 Vace全身姿势控制V1_1965691739010945025.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Comfy挑战赛4 Qwen image+Wan2.2 Vace全身姿势控制V1_1965691739010945025.json
hash: 47ce36c5b50189db
coverage: 0.84
learned_at: 2026-10-15 22:31:37
nodes: [WanVideoVAELoader, Note, JWInteger, PreviewImage, PreviewImage, WanVideoSLG, Note, WanVideoVACEEncode, ImageRepeat, VHS_VideoCombine, Note, ImageConcatMulti, WanVideoDecode, ImageFromBatch+, VHS_VideoCombine, VHS_MergeImages, JWInteger, WanVideoTextEncode, Note, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoSampler, WanVideoLoraSelect, WanVideoModelLoader, CLIPLoader, VAELoader, UNETLoader, ModelSamplingAuraFlow, SetUnionControlNetType, CFGNorm, ControlNetLoader, SaveLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageFromBatch+, PreviewImage, JWInteger, Note, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, ControlNetApplySD3, EmptySD3LatentImage, CLIPTextEncode, ImageConcanate, KSampler, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, Reroute, VHS_VideoInfo, CLIPTextEncode, easy anythingIndexSwitch, PreviewImage, VAEDecode, PreviewImage, CR Prompt Text, easy cleanGpuUsed, ImageMirror, easy anythingIndexSwitch, easy cleanGpuUsed, VHS_VideoCombine, ImageResizeKJ, ImpactSwitch, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVACEModelSelect]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 1005070452883950, "steps": 15}
---

# 视频生成/图生视频/Comfy挑战赛4 Qwen image+Wan2.2 Vace全身姿势控制V1_1965691739010945025.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1965691739010945025.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `WanVideoVAELoader`
- `Note`
- `JWInteger`
- `PreviewImage`
- `PreviewImage`
- `WanVideoSLG`
- `Note`
- `WanVideoVACEEncode`
- `ImageRepeat`
- `VHS_VideoCombine`
- `Note`
- `ImageConcatMulti`
- `WanVideoDecode`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `VHS_MergeImages`
- `JWInteger`
- `WanVideoTextEncode`
- `Note`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
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
- `ImageConcanate`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `VHS_VideoInfo`
- `CLIPTextEncode` ★核心
- `easy anythingIndexSwitch`
- `PreviewImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `CR Prompt Text`
- `easy cleanGpuUsed`
- `ImageMirror`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `ImpactSwitch`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVACEModelSelect`

## 关键参数

- `controlnet_strength` = `1.0000000000000002`
- `seed` = `1005070452883950`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **84%**（63/75）

**有卡**：`WanVideoVAELoader`、`JWInteger`、`WanVideoSLG`、`WanVideoVACEEncode`、`ImageRepeat`、`VHS_VideoCombine`、`ImageConcatMulti`、`WanVideoDecode`、`ImageFromBatch+`、`VHS_MergeImages`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoSampler`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`SetUnionControlNetType`、`CFGNorm`、`ControlNetLoader`、`SaveLatent`、`LoraLoaderModelOnly`、`VHS_LoadVideo`、`ControlNetApplySD3`、`EmptySD3LatentImage`、`CLIPTextEncode`、`ImageConcanate`、`KSampler`、`LayerUtility: PurgeVRAM`、`VHS_VideoInfo`、`easy anythingIndexSwitch`、`VAEDecode`、`CR Prompt Text`、`easy cleanGpuUsed`、`ImageMirror`、`ImageResizeKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVACEModelSelect`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
