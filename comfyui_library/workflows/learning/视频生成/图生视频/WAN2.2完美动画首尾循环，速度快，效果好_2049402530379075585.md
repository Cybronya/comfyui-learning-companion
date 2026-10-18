---
key: 视频生成/图生视频/WAN2.2完美动画首尾循环，速度快，效果好_2049402530379075585.json
name: WAN2.2完美动画首尾循环，速度快，效果好_2049402530379075585.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2完美动画首尾循环，速度快，效果好_2049402530379075585.json
hash: 6e1d5a0be874f426
coverage: 0.46729
learned_at: 2026-10-15 22:37:14
nodes: [Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Note, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, InversionDemoLazyMixImages, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Groups Bypasser (rgthree), Reroute, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, KSamplerAdvanced, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, PreviewImage, CLIPLoader, GetNode, Reroute, Reroute, wanBlockSwap, wanBlockSwap, SolidColorBatched, SolidColorBatched, SetNode, SolidColorBatched, INTConstant, VAEDecode, ColorMatch, WanSkipEndFrameImages_F2, easy cleanGpuUsed, easy cleanGpuUsed, Joy_caption_two_load, Joy_caption_two_advanced, LayerUtility: DeepSeekAPI, TextInputNode, ShowText|pysssss, Joy_extra_options, Reroute, ImpactSwitch, INTConstant, SaveVideo, SetNode, GetNode, ImageResizeKJv2, GetNode, PreviewImage, Note, ImageResizeKJv2, PreviewImage, WanFirstLastFrameToVideo, RMBG, Reroute, CLIPTextEncode, CreateVideo, CreateVideo, Fast Groups Muter (rgthree), Int, Int, SaveVideo, UNETLoader, CLIPTextEncode, CLIPTextEncode, LoadImage, easy int]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/WAN2.2完美动画首尾循环，速度快，效果好_2049402530379075585.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2049402530379075585.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
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
- `Note`
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
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `Reroute`
- `InversionDemoLazyMixImages`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PreviewImage`
- `CLIPLoader`
- `GetNode`
- `Reroute`
- `Reroute`
- `wanBlockSwap`
- `wanBlockSwap`
- `SolidColorBatched`
- `SolidColorBatched`
- `SetNode`
- `SolidColorBatched`
- `INTConstant`
- `VAEDecode` ★核心
- `ColorMatch`
- `WanSkipEndFrameImages_F2`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `Joy_caption_two_load`
- `Joy_caption_two_advanced`
- `LayerUtility: DeepSeekAPI`
- `TextInputNode`
- `ShowText|pysssss`
- `Joy_extra_options`
- `Reroute`
- `ImpactSwitch`
- `INTConstant`
- `SaveVideo`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `PreviewImage`
- `Note`
- `ImageResizeKJv2`
- `PreviewImage`
- `WanFirstLastFrameToVideo`
- `RMBG`
- `Reroute`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `CreateVideo`
- `Fast Groups Muter (rgthree)`
- `Int`
- `Int`
- `SaveVideo`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `easy int`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **47%**（50/107）

**有卡**：`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`InversionDemoLazyMixImages`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`wanBlockSwap`、`SolidColorBatched`、`INTConstant`、`VAEDecode`、`ColorMatch`、`WanSkipEndFrameImages_F2`、`easy cleanGpuUsed`、`Joy_caption_two_load`、`Joy_caption_two_advanced`、`LayerUtility: DeepSeekAPI`、`TextInputNode`、`Joy_extra_options`、`SaveVideo`、`WanFirstLastFrameToVideo`、`RMBG`、`CLIPTextEncode`、`CreateVideo`、`Int`、`LoadImage`、`easy int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
