---
key: 视频生成/图生视频/wan2.2急速 图生视频，高度准确，可本地运行_2048963923868651521.json
name: wan2.2急速 图生视频，高度准确，可本地运行_2048963923868651521.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2急速 图生视频，高度准确，可本地运行_2048963923868651521.json
hash: 44838263d493bb80
coverage: 0.8125
learned_at: 2026-10-15 22:37:12
nodes: [ModelSamplingSD3, ModelSamplingSD3, wanBlockSwap, wanBlockSwap, ModelPatchTorchSettings, ModelPatchTorchSettings, Fast Muter (rgthree), PathchSageAttentionKJ, PathchSageAttentionKJ, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Fast Muter (rgthree), SetNode, SetNode, SetNode, VAELoader, ImpactInt, ImpactInt, WanMoeKSampler, easy getNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, MarkdownNote, easy setNode, GetNode, GetNode, VAEDecode, CLIPVisionLoader, MathExpression|pysssss, CLIPVisionEncode, CLIPTextEncode, PainterI2V, GetNode, GetNode, RIFE VFI, easy getNode, VHS_VideoCombine, VHS_VideoCombine, SetNode, CLIPLoader, UNETLoader, UNETLoader, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, CR Text, CR Text]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2急速 图生视频，高度准确，可本地运行_2048963923868651521.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2048963923868651521.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（48 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
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
- `SetNode`
- `SetNode`
- `VAELoader`
- `ImpactInt`
- `ImpactInt`
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
- `RIFE VFI`
- `easy getNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `CR Text`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **81%**（39/48）

**有卡**：`ModelSamplingSD3`、`wanBlockSwap`、`ModelPatchTorchSettings`、`Fast Muter (rgthree)`、`PathchSageAttentionKJ`、`Mute / Bypass Repeater (rgthree)`、`VAELoader`、`ImpactInt`、`WanMoeKSampler`、`easy getNode`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`easy setNode`、`VAEDecode`、`CLIPVisionLoader`、`MathExpression|pysssss`、`CLIPVisionEncode`、`PainterI2V`、`RIFE VFI`、`VHS_VideoCombine`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
