---
key: 视频生成/图生视频/Wan2.2-RemixV2_首-中-尾图生视频（补帧版）_2044949937833648130.json
name: Wan2.2-RemixV2_首-中-尾图生视频（补帧版）_2044949937833648130.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2044949937833648130.json
hash: 9cd16a6d0e9a9ba6
coverage: 0.833333
learned_at: 2026-10-15 22:36:42
nodes: [wanBlockSwap, wanBlockSwap, ModelPatchTorchSettings, ModelPatchTorchSettings, Fast Muter (rgthree), PathchSageAttentionKJ, PathchSageAttentionKJ, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Fast Muter (rgthree), SetNode, CLIPLoader, VAELoader, SetNode, ImpactInt, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, easy getNode, RIFE VFI, VHS_VideoCombine, CLIPVisionLoader, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImpactInt, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionEncode, ImageResizeKJ, GetNode, WanFirstMiddleLastFrameToVideo, MarkdownNote, KSamplerAdvanced, ImageResizeKJ, MathExpression|pysssss, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, ModelSamplingSD3, ModelSamplingSD3, SetNode, UNETLoader, UNETLoader, KSamplerAdvanced, VAEDecode, easy setNode, easy getNode, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2-RemixV2_首-中-尾图生视频（补帧版）_2044949937833648130.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044949937833648130.json`

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
- `CLIPVisionLoader`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactInt`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `ImageResizeKJ`
- `GetNode`
- `WanFirstMiddleLastFrameToVideo`
- `MarkdownNote`
- `KSamplerAdvanced` ★核心
- `ImageResizeKJ`
- `MathExpression|pysssss`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `easy setNode`
- `easy getNode`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `5`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（45/54）

**有卡**：`wanBlockSwap`、`ModelPatchTorchSettings`、`Fast Muter (rgthree)`、`PathchSageAttentionKJ`、`Mute / Bypass Repeater (rgthree)`、`CLIPLoader`、`VAELoader`、`ImpactInt`、`CLIPTextEncode`、`easy getNode`、`RIFE VFI`、`VHS_VideoCombine`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionEncode`、`ImageResizeKJ`、`WanFirstMiddleLastFrameToVideo`、`KSamplerAdvanced`、`MathExpression|pysssss`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`UNETLoader`、`VAEDecode`、`easy setNode`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
