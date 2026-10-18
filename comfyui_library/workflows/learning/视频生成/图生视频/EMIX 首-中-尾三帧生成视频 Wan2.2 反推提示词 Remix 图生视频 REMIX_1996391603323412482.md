---
key: 视频生成/图生视频/EMIX 首-中-尾三帧生成视频 Wan2.2 反推提示词 Remix 图生视频 REMIX_1996391603323412482.json
name: EMIX 首-中-尾三帧生成视频 Wan2.2 反推提示词 Remix 图生视频 REMIX_1996391603323412482.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/EMIX 首-中-尾三帧生成视频 Wan2.2 反推提示词 Remix 图生视频 REMIX_1996391603323412482.json
hash: 3697a1610f70d1cf
coverage: 0.833333
learned_at: 2026-10-15 22:33:26
nodes: [wanBlockSwap, wanBlockSwap, ModelPatchTorchSettings, ModelPatchTorchSettings, Fast Muter (rgthree), PathchSageAttentionKJ, PathchSageAttentionKJ, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Fast Muter (rgthree), SetNode, CLIPLoader, VAELoader, SetNode, ImpactInt, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, easy getNode, RIFE VFI, VHS_VideoCombine, easy getNode, VHS_VideoCombine, CLIPVisionLoader, GetNode, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionEncode, ImageResizeKJ, easy setNode, GetNode, WanFirstMiddleLastFrameToVideo, MarkdownNote, KSamplerAdvanced, KSamplerAdvanced, ImageResizeKJ, MathExpression|pysssss, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, ModelSamplingSD3, ModelSamplingSD3, SetNode, UNETLoader, UNETLoader, CR Text, LoadImage, LoadImage, LoadImage, ImpactInt]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/EMIX 首-中-尾三帧生成视频 Wan2.2 反推提示词 Remix 图生视频 REMIX_1996391603323412482.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1996391603323412482.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（54 个）：
- `wanBlockSwap`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Fast Muter (rgthree)`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Muter (rgthree)`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `ImpactInt`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `easy getNode`
- `RIFE VFI`
- `VHS_VideoCombine`
- `easy getNode`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `ImageResizeKJ`
- `easy setNode`
- `GetNode`
- `WanFirstMiddleLastFrameToVideo`
- `MarkdownNote`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageResizeKJ`
- `MathExpression|pysssss`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CR Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImpactInt`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `5`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（45/54）

**有卡**：`wanBlockSwap`、`ModelPatchTorchSettings`、`Fast Muter (rgthree)`、`PathchSageAttentionKJ`、`Mute / Bypass Repeater (rgthree)`、`CLIPLoader`、`VAELoader`、`ImpactInt`、`CLIPTextEncode`、`easy getNode`、`RIFE VFI`、`VHS_VideoCombine`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionEncode`、`ImageResizeKJ`、`easy setNode`、`WanFirstMiddleLastFrameToVideo`、`KSamplerAdvanced`、`MathExpression|pysssss`、`VAEDecode`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`UNETLoader`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
