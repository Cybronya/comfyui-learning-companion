---
key: 视频生成/图生视频/首-中-尾三帧视频 Wan2.2反推提示词-Remix图生视频_2065456197679017986.json
name: 首-中-尾三帧视频 Wan2.2反推提示词-Remix图生视频_2065456197679017986.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首-中-尾三帧视频 Wan2.2反推提示词-Remix图生视频_2065456197679017986.json
hash: b0f1beda31967a8f
coverage: 0.833333
learned_at: 2026-10-15 22:39:41
nodes: [wanBlockSwap, wanBlockSwap, ModelPatchTorchSettings, ModelPatchTorchSettings, Fast Muter (rgthree), PathchSageAttentionKJ, PathchSageAttentionKJ, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Fast Muter (rgthree), SetNode, CLIPLoader, VAELoader, SetNode, ImpactInt, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, easy getNode, RIFE VFI, VHS_VideoCombine, easy getNode, VHS_VideoCombine, CLIPVisionLoader, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImpactInt, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionEncode, ImageResizeKJ, easy setNode, GetNode, WanFirstMiddleLastFrameToVideo, MarkdownNote, KSamplerAdvanced, KSamplerAdvanced, ImageResizeKJ, MathExpression|pysssss, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, ModelSamplingSD3, ModelSamplingSD3, SetNode, UNETLoader, UNETLoader, CR Text, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/首-中-尾三帧视频 Wan2.2反推提示词-Remix图生视频_2065456197679017986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2065456197679017986.json`

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
- `ImpactInt`
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
