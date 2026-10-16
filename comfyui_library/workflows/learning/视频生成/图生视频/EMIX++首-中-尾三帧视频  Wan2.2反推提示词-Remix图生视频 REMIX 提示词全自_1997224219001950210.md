---
key: 视频生成/图生视频/EMIX++首-中-尾三帧视频  Wan2.2反推提示词-Remix图生视频 REMIX 提示词全自_1997224219001950210.json
name: EMIX++首-中-尾三帧视频  Wan2.2反推提示词-Remix图生视频 REMIX 提示词全自_1997224219001950210.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1997224219001950210.json
hash: 6c623496e0e27a9d
coverage: 0.833333
learned_at: 2026-10-15 22:33:29
nodes: [wanBlockSwap, wanBlockSwap, ModelPatchTorchSettings, ModelPatchTorchSettings, Fast Muter (rgthree), PathchSageAttentionKJ, PathchSageAttentionKJ, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Fast Muter (rgthree), SetNode, CLIPLoader, VAELoader, SetNode, ImpactInt, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, easy getNode, RIFE VFI, VHS_VideoCombine, easy getNode, VHS_VideoCombine, CLIPVisionLoader, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImpactInt, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionEncode, ImageResizeKJ, easy setNode, GetNode, KSamplerAdvanced, ImageResizeKJ, MathExpression|pysssss, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, ModelSamplingSD3, ModelSamplingSD3, SetNode, UNETLoader, UNETLoader, CR Text, KSamplerAdvanced, MarkdownNote, WanFirstMiddleLastFrameToVideo, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/EMIX++首-中-尾三帧视频  Wan2.2反推提示词-Remix图生视频 REMIX 提示词全自_1997224219001950210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1997224219001950210.json`

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
- `KSamplerAdvanced` ★核心
- `MarkdownNote`
- `WanFirstMiddleLastFrameToVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `5`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（45/54）

**有卡**：`wanBlockSwap`、`ModelPatchTorchSettings`、`Fast Muter (rgthree)`、`PathchSageAttentionKJ`、`Mute / Bypass Repeater (rgthree)`、`CLIPLoader`、`VAELoader`、`ImpactInt`、`CLIPTextEncode`、`easy getNode`、`RIFE VFI`、`VHS_VideoCombine`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionEncode`、`ImageResizeKJ`、`easy setNode`、`KSamplerAdvanced`、`MathExpression|pysssss`、`VAEDecode`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`UNETLoader`、`CR Text`、`WanFirstMiddleLastFrameToVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
