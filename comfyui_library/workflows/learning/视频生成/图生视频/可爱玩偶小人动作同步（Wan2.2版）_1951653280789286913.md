---
key: 视频生成/图生视频/可爱玩偶小人动作同步（Wan2.2版）_1951653280789286913.json
name: 可爱玩偶小人动作同步（Wan2.2版）_1951653280789286913.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1951653280789286913.json
hash: 9001a630b945a659
coverage: 0.982143
learned_at: 2026-10-15 22:30:59
nodes: [ReferenceLatent, VAEEncode, FluxGuidance, ConditioningZeroOut, VAELoader, DualCLIPLoader, UNETLoader, WanVideoExperimentalArgs, WanVideoSLG, WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoTextEncode, LoadWanVideoT5TextEncoder, SaveImage, VAEDecode, WanVideoBlockSwap, WanVideoModelLoader, WanVideoVAELoader, WanVideoSampler, easy cleanGpuUsed, KSampler, easy cleanGpuUsed, WanVideoDecode, CLIPTextEncode, RMBG, ImageFromBatch+, VHS_VideoCombine, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, KSamplerAdvanced, LoraLoaderModelOnly, UNETLoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, WanVideoVACEEncode, OpenposePreprocessor, LayerUtility: ImageBlendAdvance, CR Prompt Text, easy cleanGpuUsed, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, VAELoader, PrimitiveNode, DF_Get_image_size, WanImageToVideo, VHS_VideoCombine, VAEDecode, VHS_VideoCombine, RH_Translator, LoadImage, RH_Translator, RH_Translator]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/可爱玩偶小人动作同步（Wan2.2版）_1951653280789286913.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1951653280789286913.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `SaveImage`
- `VAEDecode` ★核心
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `CLIPTextEncode` ★核心
- `RMBG`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `WanVideoVACEEncode`
- `OpenposePreprocessor`
- `LayerUtility: ImageBlendAdvance`
- `CR Prompt Text`
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `PrimitiveNode`
- `DF_Get_image_size`
- `WanImageToVideo`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `RH_Translator`
- `LoadImage`
- `RH_Translator`
- `RH_Translator`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（55/56）

**有卡**：`ReferenceLatent`、`VAEEncode`、`FluxGuidance`、`ConditioningZeroOut`、`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`SaveImage`、`VAEDecode`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoSampler`、`easy cleanGpuUsed`、`KSampler`、`WanVideoDecode`、`CLIPTextEncode`、`RMBG`、`ImageFromBatch+`、`VHS_VideoCombine`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`CLIPLoader`、`WanVideoVACEEncode`、`OpenposePreprocessor`、`LayerUtility: ImageBlendAdvance`、`CR Prompt Text`、`DF_Get_image_size`、`WanImageToVideo`、`RH_Translator`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
