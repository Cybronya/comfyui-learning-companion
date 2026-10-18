---
key: 视频生成/图生视频/Wan2.2-Remix-V2最好用的图生视频_2044778241440878594.json
name: Wan2.2-Remix-V2最好用的图生视频_2044778241440878594.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Remix-V2最好用的图生视频_2044778241440878594.json
hash: 81cdc04be7b50ea8
coverage: 0.804348
learned_at: 2026-10-15 22:36:41
nodes: [ModelSamplingSD3, ModelSamplingSD3, wanBlockSwap, wanBlockSwap, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, UNETLoader, PathchSageAttentionKJ, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Fast Muter (rgthree), SetNode, SetNode, SetNode, CLIPLoader, VAELoader, SetNode, WanMoeKSampler, easy getNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, MarkdownNote, easy setNode, GetNode, GetNode, VAEDecode, CLIPVisionLoader, MathExpression|pysssss, CLIPVisionEncode, CLIPTextEncode, PainterI2V, GetNode, GetNode, ImageResizeKJv2, LoadImage, Fast Muter (rgthree), easy getNode, ImpactInt, CR Text, TTResolutionSelector, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2-Remix-V2最好用的图生视频_2044778241440878594.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044778241440878594.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（46 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `wanBlockSwap`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Muter (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `WanMoeKSampler` ★核心
- `easy getNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `easy setNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `CLIPVisionLoader`
- `MathExpression|pysssss`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `PainterI2V`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `Fast Muter (rgthree)`
- `easy getNode`
- `ImpactInt`
- `CR Text`
- `TTResolutionSelector`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **80%**（37/46）

**有卡**：`ModelSamplingSD3`、`wanBlockSwap`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`UNETLoader`、`Mute / Bypass Repeater (rgthree)`、`Fast Muter (rgthree)`、`CLIPLoader`、`VAELoader`、`WanMoeKSampler`、`easy getNode`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`easy setNode`、`VAEDecode`、`CLIPVisionLoader`、`MathExpression|pysssss`、`CLIPVisionEncode`、`PainterI2V`、`ImageResizeKJv2`、`LoadImage`、`ImpactInt`、`CR Text`、`TTResolutionSelector`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
