---
key: 视频生成/图生视频/（官方版）Wan2.2+Remix+V2+Qwen3.5扩写图生视频V1 (1)_2042534334439100418.json
name: （官方版）Wan2.2+Remix+V2+Qwen3.5扩写图生视频V1 (1)_2042534334439100418.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2042534334439100418.json
hash: 46f7e619c5771bc3
coverage: 0.806452
learned_at: 2026-10-15 22:36:28
nodes: [Note, ImageResizeKJv2, SaveImage, ImageScaleBy, CLIPVisionEncode, Seed (rgthree), WanImageToVideo, Note, Note, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, Note, CLIPTextEncode, Note, JWInteger, VHS_VideoCombine, VHS_VideoCombine, ModelSamplingSD3, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, Pick From Batch (mtb), VHS_VideoCombine, LayerUtility: PurgeVRAM, Note, PathchSageAttentionKJ, wanBlockSwap, LoraLoaderModelOnly, ModelSamplingSD3, ColorMatch, VHS_VideoCombine, UNETLoader, UNETLoader, easy cleanGpuUsed, CLIPVisionLoader, VAELoader, CLIPLoader, ShellAgentPluginOutputText, LayerUtility: ImageScaleByAspectRatio V2, Note, JWInteger, Note, CR Prompt Text, Text Concatenate, Note, LoraLoaderModelOnly, wanBlockSwap, PathchSageAttentionKJ, Note, ImageScaleBy, PreviewImage, LoadImage, MemoryCleaner, llama_cpp_instruct_adv, easy showAnything, llama_cpp_model_loader, CR Text, llama_cpp_parameters, CR Prompt Text, VHS_VideoCombine, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/（官方版）Wan2.2+Remix+V2+Qwen3.5扩写图生视频V1 (1)_2042534334439100418.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042534334439100418.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `Note`
- `ImageResizeKJv2`
- `SaveImage`
- `ImageScaleBy`
- `CLIPVisionEncode`
- `Seed (rgthree)`
- `WanImageToVideo`
- `Note`
- `Note`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `Note`
- `JWInteger`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Pick From Batch (mtb)`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `Note`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ColorMatch`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPLoader`
- `ShellAgentPluginOutputText`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `JWInteger`
- `Note`
- `CR Prompt Text`
- `Text Concatenate`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `Note`
- `ImageScaleBy`
- `PreviewImage`
- `LoadImage`
- `MemoryCleaner`
- `llama_cpp_instruct_adv`
- `easy showAnything`
- `llama_cpp_model_loader`
- `CR Text`
- `llama_cpp_parameters`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **81%**（50/62）

**有卡**：`ImageResizeKJv2`、`SaveImage`、`ImageScaleBy`、`CLIPVisionEncode`、`Seed (rgthree)`、`WanImageToVideo`、`KSamplerAdvanced`、`CLIPTextEncode`、`JWInteger`、`VHS_VideoCombine`、`ModelSamplingSD3`、`Pick From Batch (mtb)`、`LayerUtility: PurgeVRAM`、`PathchSageAttentionKJ`、`wanBlockSwap`、`LoraLoaderModelOnly`、`ColorMatch`、`UNETLoader`、`easy cleanGpuUsed`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`ShellAgentPluginOutputText`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`、`Text Concatenate`、`LoadImage`、`MemoryCleaner`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`CR Text`、`llama_cpp_parameters`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、UNETLoader
