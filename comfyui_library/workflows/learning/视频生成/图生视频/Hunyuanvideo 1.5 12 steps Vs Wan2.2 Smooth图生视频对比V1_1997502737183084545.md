---
key: 视频生成/图生视频/Hunyuanvideo 1.5 12 steps Vs Wan2.2 Smooth图生视频对比V1_1997502737183084545.json
name: Hunyuanvideo 1.5 12 steps Vs Wan2.2 Smooth图生视频对比V1_1997502737183084545.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1997502737183084545.json
hash: 3beeca04e7ca029b
coverage: 0.794872
learned_at: 2026-10-15 22:33:29
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ImageScaleBy, Pick From Batch (mtb), easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, WanImageToVideo, Note, Note, CLIPLoader, Note, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, LayerUtility: PurgeVRAM, ModelSamplingSD3, easy showAnything, PreviewImage, ColorMatch, VHS_VideoCombine, VAEDecode, KSamplerAdvanced, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, LayerUtility: PurgeVRAM, RH_LLMAPI_NODE, AILab_QwenVL, LoadImage, CR Prompt Text, UNETLoader, JWInteger, CLIPVisionLoader, DualCLIPLoader, CLIPVisionEncode, VAELoader, VAEDecode, EasyCache, Note, MarkdownNote, MarkdownNote, RandomNoise, KSamplerSelect, CLIPTextEncode, HunyuanVideo15ImageToVideo, MarkdownNote, easy showAnything, Reroute, SamplerCustomAdvanced, VAEDecodeTiled, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, Seed (rgthree), LayerUtility: ImageScaleByAspectRatio V2, AddLabel, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: PurgeVRAM, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, UNETLoader, ModelSamplingSD3, BasicScheduler, JWInteger, ImageConcanate, CFGGuider, AddLabel]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Hunyuanvideo 1.5 12 steps Vs Wan2.2 Smooth图生视频对比V1_1997502737183084545.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1997502737183084545.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `Note`
- `Note`
- `ImageScaleBy`
- `Note`
- `ImageResizeKJv2`
- `SaveImage`
- `ImageScaleBy`
- `Pick From Batch (mtb)`
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `Note`
- `CLIPVisionLoader`
- `VAELoader`
- `Note`
- `WanImageToVideo`
- `Note`
- `Note`
- `CLIPLoader`
- `Note`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `ModelSamplingSD3`
- `easy showAnything`
- `PreviewImage`
- `ColorMatch`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LayerUtility: PurgeVRAM`
- `RH_LLMAPI_NODE`
- `AILab_QwenVL`
- `LoadImage`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `JWInteger`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `CLIPVisionEncode`
- `VAELoader`
- `VAEDecode` ★核心
- `EasyCache`
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `HunyuanVideo15ImageToVideo`
- `MarkdownNote`
- `easy showAnything`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `Seed (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AddLabel`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `BasicScheduler`
- `JWInteger`
- `ImageConcanate`
- `CFGGuider`
- `AddLabel`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **79%**（62/78）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`Pick From Batch (mtb)`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`WanImageToVideo`、`CLIPLoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`LayerUtility: PurgeVRAM`、`ColorMatch`、`VHS_VideoCombine`、`VAEDecode`、`UNETLoader`、`PathchSageAttentionKJ`、`RH_LLMAPI_NODE`、`AILab_QwenVL`、`LoadImage`、`CR Prompt Text`、`JWInteger`、`DualCLIPLoader`、`EasyCache`、`RandomNoise`、`KSamplerSelect`、`CLIPTextEncode`、`HunyuanVideo15ImageToVideo`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`Seed (rgthree)`、`LayerUtility: ImageScaleByAspectRatio V2`、`AddLabel`、`BasicScheduler`、`ImageConcanate`、`CFGGuider`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
