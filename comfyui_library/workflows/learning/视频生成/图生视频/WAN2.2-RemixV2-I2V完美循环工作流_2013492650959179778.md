---
key: 视频生成/图生视频/WAN2.2-RemixV2-I2V完美循环工作流_2013492650959179778.json
name: WAN2.2-RemixV2-I2V完美循环工作流_2013492650959179778.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2-RemixV2-I2V完美循环工作流_2013492650959179778.json
hash: 1aea64219efc2902
coverage: 0.462264
learned_at: 2026-10-15 22:34:31
nodes: [Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Note, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, Int, Reroute, Reroute, Reroute, InversionDemoLazyMixImages, Fast Groups Muter (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Groups Bypasser (rgthree), Reroute, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, Reroute, Reroute, WanFirstLastFrameToVideo, KSamplerAdvanced, CLIPTextEncode, SetNode, Int, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageResizeKJv2, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, PreviewImage, UNETLoader, CLIPLoader, GetNode, Reroute, Reroute, GetNode, wanBlockSwap, wanBlockSwap, SolidColorBatched, SolidColorBatched, SetNode, SolidColorBatched, INTConstant, VAEDecode, GetNode, ColorMatch, ImageResizeKJv2, WanSkipEndFrameImages_F2, RMBG, CreateVideo, CreateVideo, SaveVideo, easy cleanGpuUsed, easy cleanGpuUsed, Joy_caption_two_load, Joy_caption_two_advanced, LayerUtility: DeepSeekAPI, TextInputNode, ShowText|pysssss, Joy_extra_options, Reroute, Int, ImpactSwitch, INTConstant, SaveVideo, CLIPTextEncode, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/WAN2.2-RemixV2-I2V完美循环工作流_2013492650959179778.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2013492650959179778.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（106 个）：
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
- `Note`
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
- `PreviewImage`
- `Int`
- `Reroute`
- `Reroute`
- `Reroute`
- `InversionDemoLazyMixImages`
- `Fast Groups Muter (rgthree)`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `Int`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `GetNode`
- `Reroute`
- `Reroute`
- `GetNode`
- `wanBlockSwap`
- `wanBlockSwap`
- `SolidColorBatched`
- `SolidColorBatched`
- `SetNode`
- `SolidColorBatched`
- `INTConstant`
- `VAEDecode` ★核心
- `GetNode`
- `ColorMatch`
- `ImageResizeKJv2`
- `WanSkipEndFrameImages_F2`
- `RMBG`
- `CreateVideo`
- `CreateVideo`
- `SaveVideo`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `Joy_caption_two_load`
- `Joy_caption_two_advanced`
- `LayerUtility: DeepSeekAPI`
- `TextInputNode`
- `ShowText|pysssss`
- `Joy_extra_options`
- `Reroute`
- `Int`
- `ImpactSwitch`
- `INTConstant`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **46%**（49/106）

**有卡**：`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`InversionDemoLazyMixImages`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`WanFirstLastFrameToVideo`、`CLIPTextEncode`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`wanBlockSwap`、`SolidColorBatched`、`INTConstant`、`VAEDecode`、`ColorMatch`、`WanSkipEndFrameImages_F2`、`RMBG`、`CreateVideo`、`SaveVideo`、`easy cleanGpuUsed`、`Joy_caption_two_load`、`Joy_caption_two_advanced`、`LayerUtility: DeepSeekAPI`、`TextInputNode`、`Joy_extra_options`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
