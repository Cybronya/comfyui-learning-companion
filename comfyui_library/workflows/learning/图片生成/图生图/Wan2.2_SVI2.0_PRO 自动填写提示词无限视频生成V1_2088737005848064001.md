---
key: 图片生成/图生图/Wan2.2_SVI2.0_PRO 自动填写提示词无限视频生成V1_2088737005848064001.json
name: Wan2.2_SVI2.0_PRO 自动填写提示词无限视频生成V1_2088737005848064001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2_SVI2.0_PRO 自动填写提示词无限视频生成V1_2088737005848064001.json
hash: f1a81e14a5b41f8a
coverage: 0.675393
learned_at: 2026-10-23 11:28:10
nodes: [Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, CLIPTextEncode, WanImageToVideoSVIPro, CLIPTextEncode, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, CR Seed, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, CR Seed, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, CR Seed, CLIPTextEncode, CR Seed, Reroute, Reroute, Reroute, GetImagesFromBatchIndexed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, CLIPLoader, PreviewImage, CR Seed, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Switch any [Crystools], Switch any [Crystools], Switch any [Crystools], ImageResizeKJv2, VAEEncode, PreviewImage, VAELoader, Fast Groups Bypasser (rgthree), CR Seed, INTConstant, INTConstant, Reroute, Reroute, Reroute, Reroute, WanImageToVideoSVIPro, KSamplerAdvanced, ImageBatchExtendWithOverlap, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, VAEDecode, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, VAEDecode, LayerUtility: PurgeVRAM V2, VAEDecode, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, VAEDecode, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, Switch any [Crystools], KSamplerAdvanced, VAEDecode, VAEDecode, WanImageToVideoSVIPro, WanImageToVideoSVIPro, ImageBatchExtendWithOverlap, PreviewImage, WanImageToVideoSVIPro, ImageBatchExtendWithOverlap, GetImagesFromBatchIndexed, GetImagesFromBatchIndexed, WanImageToVideoSVIPro, Reroute, VHS_VideoCombine, GetImagesFromBatchIndexed, VHS_VideoCombine, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, ImageBatchExtendWithOverlap, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, ImageBatchExtendWithOverlap, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, PreviewImage, VHS_VideoCombine, PreviewImage, LayerUtility: PurgeVRAM V2, GetImagesFromBatchIndexed, LayerUtility: PurgeVRAM V2, PixaromaLabel, Any Switch (rgthree), easy boolean, PixaromaResolution, UNETLoader, LoadImage, LoadImage, MarkdownNote, PixaromaLabel, Switch any [Crystools], Any Switch (rgthree), LoraLoaderModelOnly, LayerUtility: PurgeVRAM V2, PathchSageAttentionKJ, LayerUtility: PurgeVRAM V2, PathchSageAttentionKJ, Reroute, Reroute, LoadImage, VHS_VideoCombine, CR Prompt Text, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), VHS_VideoCombine, GetImagesFromBatchIndexed, LayerUtility: PurgeVRAM V2, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, Reroute, VHS_VideoCombine, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, UNETLoader, UNETLoader, Fast Groups Bypasser (rgthree), PixaromaLabel, PixaromaLabel, CLIPTextEncode, Switch any [Crystools], RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes]
patterns: []
missing: []
parameters: {"cfg": 14, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/图生图/Wan2.2_SVI2.0_PRO 自动填写提示词无限视频生成V1_2088737005848064001.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2_SVI2.0_PRO 自动填写提示词无限视频生成V1_2088737005848064001.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（191 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `CLIPTextEncode` ★核心
- `WanImageToVideoSVIPro`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CR Seed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CR Seed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CR Seed`
- `CLIPTextEncode` ★核心
- `CR Seed`
- `Reroute`
- `Reroute`
- `Reroute`
- `GetImagesFromBatchIndexed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CLIPLoader`
- `PreviewImage`
- `CR Seed`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Switch any [Crystools]`
- `Switch any [Crystools]`
- `Switch any [Crystools]`
- `ImageResizeKJv2`
- `VAEEncode` ★核心
- `PreviewImage`
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`
- `CR Seed`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanImageToVideoSVIPro`
- `KSamplerAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `Switch any [Crystools]`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `WanImageToVideoSVIPro`
- `WanImageToVideoSVIPro`
- `ImageBatchExtendWithOverlap`
- `PreviewImage`
- `WanImageToVideoSVIPro`
- `ImageBatchExtendWithOverlap`
- `GetImagesFromBatchIndexed`
- `GetImagesFromBatchIndexed`
- `WanImageToVideoSVIPro`
- `Reroute`
- `VHS_VideoCombine`
- `GetImagesFromBatchIndexed`
- `VHS_VideoCombine`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ImageBatchExtendWithOverlap`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `PreviewImage`
- `VHS_VideoCombine`
- `PreviewImage`
- `LayerUtility: PurgeVRAM V2`
- `GetImagesFromBatchIndexed`
- `LayerUtility: PurgeVRAM V2`
- `PixaromaLabel`
- `Any Switch (rgthree)`
- `easy boolean`
- `PixaromaResolution`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `PixaromaLabel`
- `Switch any [Crystools]`
- `Any Switch (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM V2`
- `PathchSageAttentionKJ`
- `LayerUtility: PurgeVRAM V2`
- `PathchSageAttentionKJ`
- `Reroute`
- `Reroute`
- `LoadImage`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `GetImagesFromBatchIndexed`
- `LayerUtility: PurgeVRAM V2`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `Reroute`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `PixaromaLabel`
- `PixaromaLabel`
- `CLIPTextEncode` ★核心
- `Switch any [Crystools]`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `14`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **68%**（129/191）

**有卡**：`LayerUtility: PurgeVRAM V2`、`CLIPTextEncode`、`WanImageToVideoSVIPro`、`KSamplerAdvanced`、`CR Seed`、`GetImagesFromBatchIndexed`、`easy cleanGpuUsed`、`CLIPLoader`、`Switch any [Crystools]`、`ImageResizeKJv2`、`VAEEncode`、`VAELoader`、`INTConstant`、`ImageBatchExtendWithOverlap`、`VAEDecode`、`VHS_VideoCombine`、`PixaromaLabel`、`easy boolean`、`PixaromaResolution`、`UNETLoader`、`LoadImage`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CR Prompt Text`、`RHHiddenNodes`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
