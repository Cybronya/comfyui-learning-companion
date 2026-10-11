---
key: 视频生成/文生视频/Remix 3.0+Z-Image Turbo文到视频_2036368662243844097.json
name: Remix 3.0+Z-Image Turbo文到视频_2036368662243844097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Remix 3.0+Z-Image Turbo文到视频_2036368662243844097.json
hash: de48d9219a09f6c6
coverage: 0.875
learned_at: 2026-10-11 03:48:37
nodes: [CLIPTextEncode, llama_cpp_instruct_adv, LayerUtility: PurgeVRAM V2, ShowText|pysssss, image_scale_pixel_v2, PainterVRAM, VAELoader, UNETLoader, UNETLoader, llama_cpp_model_loader, llama_cpp_model_loader, easy cleanGpuUsed, CLIPTextEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, WanVideoNAG, WanVideoNAG, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, CLIPTextEncode, KSampler, CLIPTextEncode, VAELoader, LayerUtility: PurgeVRAM V2, VAEDecodeTiled, ModelSamplingAuraFlow, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, EmptySD3LatentImage, PrimitiveStringMultiline, CLIPLoader, LoadImage, llama_cpp_model_loader, TextInput_, TextInput_, Label (rgthree), VAEDecode, UnetLoaderGGUF, ClipLoaderGGUF, PainterI2VAdvanced, CLIPLoader, SaveImage, VHS_VideoCombine]
patterns: []
missing: [Label (rgthree), LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 389497974075174, "steps": 9}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Remix 3.0+Z-Image Turbo文到视频_2036368662243844097.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Remix 3.0+Z-Image Turbo文到视频_2036368662243844097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `CLIPTextEncode` ★核心
- `llama_cpp_instruct_adv`
- `LayerUtility: PurgeVRAM V2`
- `ShowText|pysssss`
- `image_scale_pixel_v2`
- `PainterVRAM`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `llama_cpp_model_loader`
- `llama_cpp_model_loader`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `WanVideoNAG`
- `WanVideoNAG`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecodeTiled` ★核心
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptySD3LatentImage`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `LoadImage`
- `llama_cpp_model_loader`
- `TextInput_`
- `TextInput_`
- `Label (rgthree)`
- `VAEDecode` ★核心
- `UnetLoaderGGUF` ★核心
- `ClipLoaderGGUF`
- `PainterI2VAdvanced`
- `CLIPLoader`
- `SaveImage`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `389497974075174`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（42/48）

**有卡**：`CLIPTextEncode`、`llama_cpp_instruct_adv`、`image_scale_pixel_v2`、`PainterVRAM`、`VAELoader`、`UNETLoader`、`llama_cpp_model_loader`、`PathchSageAttentionKJ`、`WanVideoNAG`、`ModelSamplingSD3`、`KSamplerAdvanced`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`KSampler`、`VAEDecodeTiled`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`EmptySD3LatentImage`、`CLIPLoader`、`LoadImage`、`TextInput_`、`VAEDecode`、`UnetLoaderGGUF`、`ClipLoaderGGUF`、`PainterI2VAdvanced`、`SaveImage`、`VHS_VideoCombine`

**缺卡**（4）：`Label (rgthree)`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
