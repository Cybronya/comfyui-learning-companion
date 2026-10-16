---
key: 视频生成/图生视频/Wan 2.2 REMIX V2  图生视频_2059921253905027073.json
name: Wan 2.2 REMIX V2  图生视频_2059921253905027073.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2059921253905027073.json
hash: 5985899cd52b5790
coverage: 0.816327
learned_at: 2026-10-15 22:38:43
nodes: [ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, PathchSageAttentionKJ, easy getNode, RIFE VFI, easy getNode, ImpactInt, VHS_VideoCombine, VHS_VideoCombine, ImpactInt, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, SetNode, SetNode, CLIPLoader, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, SetNode, SetNode, VAELoader, wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), Fast Muter (rgthree), Mute / Bypass Repeater (rgthree), Fast Muter (rgthree), CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, MathExpression|pysssss, GetNode, VAEDecode, GetNode, GetNode, PainterI2V, easy setNode, WanMoeKSampler, CLIPTextEncode, easy seed, Float, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 视频生成/图生视频/Wan 2.2 REMIX V2  图生视频_2059921253905027073.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2059921253905027073.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（49 个）：
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `easy getNode`
- `RIFE VFI`
- `easy getNode`
- `ImpactInt`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImpactInt`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `VAELoader`
- `wanBlockSwap`
- `wanBlockSwap`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Muter (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Muter (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `PainterI2V`
- `easy setNode`
- `WanMoeKSampler` ★核心
- `CLIPTextEncode` ★核心
- `easy seed`
- `Float`
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **82%**（40/49）

**有卡**：`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`easy getNode`、`RIFE VFI`、`ImpactInt`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`Fast Muter (rgthree)`、`CLIPTextEncode`、`CLIPVisionEncode`、`CLIPVisionLoader`、`MathExpression|pysssss`、`VAEDecode`、`PainterI2V`、`easy setNode`、`WanMoeKSampler`、`easy seed`、`Float`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
