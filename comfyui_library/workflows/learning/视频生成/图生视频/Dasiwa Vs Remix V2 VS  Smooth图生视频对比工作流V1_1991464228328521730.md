---
key: 视频生成/图生视频/Dasiwa Vs Remix V2 VS  Smooth图生视频对比工作流V1_1991464228328521730.json
name: Dasiwa Vs Remix V2 VS  Smooth图生视频对比工作流V1_1991464228328521730.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1991464228328521730.json
hash: 4011da9fe8d33957
coverage: 0.764368
learned_at: 2026-10-15 22:33:13
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ImageScaleBy, Pick From Batch (mtb), easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, Note, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, LayerUtility: PurgeVRAM, CLIPTextEncode, ModelSamplingSD3, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, VHS_VideoCombine, Pick From Batch (mtb), easy showAnything, VAEDecode, LayerUtility: PurgeVRAM, PreviewImage, ColorMatch, VHS_VideoCombine, VAEDecode, JWInteger, PainterI2V, JWInteger, KSamplerAdvanced, UNETLoader, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, PathchSageAttentionKJ, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ImageScaleBy, Pick From Batch (mtb), easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, WanImageToVideo, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, CLIPTextEncode, CLIPTextEncode, Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, PreviewImage, Pick From Batch (mtb), LayerUtility: PurgeVRAM, easy showAnything, ColorMatch, VHS_VideoCombine, ImageConcanate, CLIPTextEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, PathchSageAttentionKJ, PathchSageAttentionKJ, PreviewImage, LayerUtility: PurgeVRAM, AddLabel, Reroute, VAEDecode, Reroute, LayerUtility: PurgeVRAM, ImageConcanate, PDIMAGE_LongerSize, CR Prompt Text, Reroute, AILab_QwenVL, CLIPTextEncode, VHS_VideoCombine, PainterI2V, Note, UNETLoader, UNETLoader, PathchSageAttentionKJ, AddLabel, Note, AddLabel, PainterI2V, AddLabel, WanImageToVideo, RH_LLMAPI_NODE, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, VHS_VideoCombine, LayerUtility: PurgeVRAM, VAEDecode, ImageConcanate, RunningHub Deepcleaner, PDIMAGE_LongerSize, PDIMAGE_LongerSize, RunningHub Deepcleaner, RunningHub Deepcleaner, UNETLoader, UNETLoader, LoadImage, CLIPTextEncode, KSamplerAdvanced, Seed (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Dasiwa Vs Remix V2 VS  Smooth图生视频对比工作流V1_1991464228328521730.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1991464228328521730.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（174 个）：
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
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `Note`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `Note`
- `ImageScaleBy`
- `Note`
- `ImageResizeKJv2`
- `SaveImage`
- `ColorMatch`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `Note`
- `CLIPVisionLoader`
- `VAELoader`
- `Note`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `Note`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `Pick From Batch (mtb)`
- `easy showAnything`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `ColorMatch`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `JWInteger`
- `PainterI2V`
- `JWInteger`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `ImageScaleBy`
- `Note`
- `ImageResizeKJv2`
- `SaveImage`
- `ColorMatch`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `Note`
- `CLIPVisionLoader`
- `VAELoader`
- `Note`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `Pick From Batch (mtb)`
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `ColorMatch`
- `VHS_VideoCombine`
- `ImageConcanate`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `AddLabel`
- `Reroute`
- `VAEDecode` ★核心
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `ImageConcanate`
- `PDIMAGE_LongerSize`
- `CR Prompt Text`
- `Reroute`
- `AILab_QwenVL`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `PainterI2V`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `AddLabel`
- `Note`
- `AddLabel`
- `PainterI2V`
- `AddLabel`
- `WanImageToVideo`
- `RH_LLMAPI_NODE`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `ImageConcanate`
- `RunningHub Deepcleaner`
- `PDIMAGE_LongerSize`
- `PDIMAGE_LongerSize`
- `RunningHub Deepcleaner`
- `RunningHub Deepcleaner`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `Seed (rgthree)`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **76%**（133/174）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`Pick From Batch (mtb)`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`LayerUtility: PurgeVRAM`、`CLIPTextEncode`、`ColorMatch`、`VHS_VideoCombine`、`VAEDecode`、`JWInteger`、`PainterI2V`、`UNETLoader`、`PathchSageAttentionKJ`、`WanImageToVideo`、`ImageConcanate`、`AddLabel`、`PDIMAGE_LongerSize`、`CR Prompt Text`、`AILab_QwenVL`、`RH_LLMAPI_NODE`、`RunningHub Deepcleaner`、`LoadImage`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
