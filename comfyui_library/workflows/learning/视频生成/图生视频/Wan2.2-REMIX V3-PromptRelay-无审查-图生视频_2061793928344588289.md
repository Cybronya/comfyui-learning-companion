---
key: 视频生成/图生视频/Wan2.2-REMIX V3-PromptRelay-无审查-图生视频_2061793928344588289.json
name: Wan2.2-REMIX V3-PromptRelay-无审查-图生视频_2061793928344588289.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-REMIX V3-PromptRelay-无审查-图生视频_2061793928344588289.json
hash: 152db95844c6dfbc
coverage: 0.8
learned_at: 2026-10-15 22:38:56
nodes: [UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, DapaoSmartMemoryOptimizerNode, DapaoSmartMemoryOptimizerNode, PathchSageAttentionKJ, PathchSageAttentionKJ, Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), CLIPLoader, VAELoader, SetNode, SetNode, SetNode, SetNode, ModelPatchTorchSettings, ModelPatchTorchSettings, PrimitiveInt, VHS_VideoCombine, RIFE VFI, VHS_VideoCombine, PrimitiveInt, Mute / Bypass Repeater (rgthree), ImageConcanate, CustomAddLabel, Mute / Bypass Repeater (rgthree), FlashVSRNode, Fast Bypasser (rgthree), Fast Bypasser (rgthree), VHS_VideoCombine, GetNode, GetNode, PromptRelayEncodeTimeline, GetNode, LoadImage, CLIPVisionLoader, CLIPVisionEncode, CLIPTextEncode, GetNode, PainterI2V, MarkdownNote, WanMoeKSampler, VAEDecode, easy setNode, EmptyLTXVLatentVideo, MathExpression|pysssss, VHS_VideoCombine, ImpactInt, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, PromptRelayEncodeTimeline]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2-REMIX V3-PromptRelay-无审查-图生视频_2061793928344588289.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061793928344588289.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（55 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `DapaoSmartMemoryOptimizerNode`
- `DapaoSmartMemoryOptimizerNode`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `RIFE VFI`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `Mute / Bypass Repeater (rgthree)`
- `ImageConcanate`
- `CustomAddLabel`
- `Mute / Bypass Repeater (rgthree)`
- `FlashVSRNode`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `PromptRelayEncodeTimeline`
- `GetNode`
- `LoadImage`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `PainterI2V`
- `MarkdownNote`
- `WanMoeKSampler` ★核心
- `VAEDecode` ★核心
- `easy setNode`
- `EmptyLTXVLatentVideo`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `ImpactInt`
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PromptRelayEncodeTimeline`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **80%**（44/55）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`DapaoSmartMemoryOptimizerNode`、`PathchSageAttentionKJ`、`Mute / Bypass Repeater (rgthree)`、`Fast Bypasser (rgthree)`、`CLIPLoader`、`VAELoader`、`ModelPatchTorchSettings`、`VHS_VideoCombine`、`RIFE VFI`、`ImageConcanate`、`CustomAddLabel`、`FlashVSRNode`、`PromptRelayEncodeTimeline`、`LoadImage`、`CLIPVisionLoader`、`CLIPVisionEncode`、`CLIPTextEncode`、`PainterI2V`、`WanMoeKSampler`、`VAEDecode`、`easy setNode`、`EmptyLTXVLatentVideo`、`MathExpression|pysssss`、`ImpactInt`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
