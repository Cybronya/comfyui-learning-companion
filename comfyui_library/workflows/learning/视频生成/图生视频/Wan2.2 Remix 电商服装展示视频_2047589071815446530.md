---
key: 视频生成/图生视频/Wan2.2 Remix 电商服装展示视频_2047589071815446530.json
name: Wan2.2 Remix 电商服装展示视频_2047589071815446530.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Remix 电商服装展示视频_2047589071815446530.json
hash: 779f4816b08bca39
coverage: 0.763889
learned_at: 2026-10-15 22:37:06
nodes: [llama_cpp_parameters, easy cleanGpuUsed, SimpleMath+, easy clearCacheAll, UNETLoader, UNETLoader, VAELoader, CLIPLoader, SetNode, CLIPVisionLoader, SetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, PreviewAny, CLIPTextEncode, SetNode, GetNode, KSamplerAdvanced, GetNode, Fast Groups Muter (rgthree), easy saveText, CLIPVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, GetNode, easy cleanGpuUsed, KSamplerAdvanced, ImageBatchMulti, GetNode, GetNode, VAEDecode, VHS_VideoCombine, SimpleMath+, ImageScaleBy, CLIPVisionEncode, WanImageToVideo, WanImageToVideo, INTConstant, GetNode, GetNode, KSamplerAdvanced, GetImageRangeFromBatch, INTConstant, GetImageRangeFromBatch, INTConstant, RIFE VFI, KSamplerAdvanced, VAEDecode, ImageScaleBy, RIFE VFI, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, SetNode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, llama_cpp_instruct_adv, LoraLoaderModelOnly, LoadImage, llama_cpp_model_loader, INTConstant, GetImageSizeAndCount, ImageScaleBy, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 Remix 电商服装展示视频_2047589071815446530.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047589071815446530.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `llama_cpp_parameters`
- `easy cleanGpuUsed`
- `SimpleMath+`
- `easy clearCacheAll`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `Fast Groups Muter (rgthree)`
- `easy saveText`
- `CLIPVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SimpleMath+`
- `GetNode`
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `ImageBatchMulti`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `SimpleMath+`
- `ImageScaleBy`
- `CLIPVisionEncode`
- `WanImageToVideo`
- `WanImageToVideo`
- `INTConstant`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetImageRangeFromBatch`
- `INTConstant`
- `GetImageRangeFromBatch`
- `INTConstant`
- `RIFE VFI`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `RIFE VFI`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `llama_cpp_instruct_adv`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `llama_cpp_model_loader`
- `INTConstant`
- `GetImageSizeAndCount`
- `ImageScaleBy`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **76%**（55/72）

**有卡**：`llama_cpp_parameters`、`easy cleanGpuUsed`、`SimpleMath+`、`easy clearCacheAll`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`CLIPVisionLoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`easy saveText`、`CLIPVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageBatchMulti`、`VAEDecode`、`VHS_VideoCombine`、`ImageScaleBy`、`WanImageToVideo`、`INTConstant`、`GetImageRangeFromBatch`、`RIFE VFI`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`llama_cpp_instruct_adv`、`LoadImage`、`llama_cpp_model_loader`、`GetImageSizeAndCount`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
