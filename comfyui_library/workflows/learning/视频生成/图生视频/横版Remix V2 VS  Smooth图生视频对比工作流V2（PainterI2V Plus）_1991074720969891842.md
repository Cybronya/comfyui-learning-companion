---
key: 视频生成/图生视频/横版Remix V2 VS  Smooth图生视频对比工作流V2（PainterI2V Plus）_1991074720969891842.json
name: 横版Remix V2 VS  Smooth图生视频对比工作流V2（PainterI2V Plus）_1991074720969891842.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/横版Remix V2 VS  Smooth图生视频对比工作流V2（PainterI2V Plus）_1991074720969891842.json
hash: 03f041ba688fd58a
coverage: 0.771429
learned_at: 2026-10-15 22:33:12
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ImageScaleBy, Pick From Batch (mtb), easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, WanImageToVideo, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, Note, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, LayerUtility: PurgeVRAM, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, Pick From Batch (mtb), easy showAnything, VAEDecode, LayerUtility: PurgeVRAM, PreviewImage, ColorMatch, VHS_VideoCombine, VAEDecode, JWInteger, PainterI2V, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, PathchSageAttentionKJ, PathchSageAttentionKJ, Note, ImageScaleBy, Note, SaveImage, ImageScaleBy, Pick From Batch (mtb), easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, Note, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, LayerUtility: PurgeVRAM, CLIPTextEncode, ModelSamplingSD3, Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, VHS_VideoCombine, Pick From Batch (mtb), LayerUtility: PurgeVRAM, easy showAnything, VAEDecode, LayerUtility: PurgeVRAM, ColorMatch, VHS_VideoCombine, PainterI2V, KSamplerAdvanced, CLIPTextEncode, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, PathchSageAttentionKJ, PreviewImage, LayerUtility: PurgeVRAM, Reroute, VAEDecode, Reroute, LayerUtility: PurgeVRAM, PDIMAGE_LongerSize, PDIMAGE_LongerSize, PDIMAGE_LongerSize, RunningHub Deepcleaner, UNETLoader, CR Prompt Text, Reroute, RH_LLMAPI_NODE, AILab_QwenVL, CLIPTextEncode, VHS_VideoCombine, UNETLoader, UNETLoader, Note, PainterI2V, VHS_VideoCombine, AddLabel, AddLabel, AddLabel, KSamplerAdvanced, Seed (rgthree), ImageConcanate, ImageConcanate, ImageConcanate, LoadImage, CLIPTextEncode, PathchSageAttentionKJ, AddLabel, LoraLoaderModelOnly, UNETLoader, UNETLoader, PainterI2V, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/横版Remix V2 VS  Smooth图生视频对比工作流V2（PainterI2V Plus）_1991074720969891842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1991074720969891842.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（175 个）：
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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `Note`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
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
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ModelSamplingSD3`
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
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Note`
- `ImageScaleBy`
- `Note`
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
- `CLIPLoader`
- `Note`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `Pick From Batch (mtb)`
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `ColorMatch`
- `VHS_VideoCombine`
- `PainterI2V`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `VAEDecode` ★核心
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `PDIMAGE_LongerSize`
- `PDIMAGE_LongerSize`
- `PDIMAGE_LongerSize`
- `RunningHub Deepcleaner`
- `UNETLoader` ★核心
- `CR Prompt Text`
- `Reroute`
- `RH_LLMAPI_NODE`
- `AILab_QwenVL`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Note`
- `PainterI2V`
- `VHS_VideoCombine`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `KSamplerAdvanced` ★核心
- `Seed (rgthree)`
- `ImageConcanate`
- `ImageConcanate`
- `ImageConcanate`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `AddLabel`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PainterI2V`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `JWInteger`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **77%**（135/175）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`Pick From Batch (mtb)`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`WanImageToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`LayerUtility: PurgeVRAM`、`CLIPTextEncode`、`ColorMatch`、`VAEDecode`、`VHS_VideoCombine`、`JWInteger`、`PainterI2V`、`UNETLoader`、`PathchSageAttentionKJ`、`PDIMAGE_LongerSize`、`RunningHub Deepcleaner`、`CR Prompt Text`、`RH_LLMAPI_NODE`、`AILab_QwenVL`、`AddLabel`、`Seed (rgthree)`、`ImageConcanate`、`LoadImage`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
