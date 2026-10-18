---
key: 视频生成/图生视频/Wan2.2 SMOOTH MIX-单人物参考+自动运镜+长镜头生成（30秒）_1981343312810598402.json
name: Wan2.2 SMOOTH MIX-单人物参考+自动运镜+长镜头生成（30秒）_1981343312810598402.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 SMOOTH MIX-单人物参考+自动运镜+长镜头生成（30秒）_1981343312810598402.json
hash: 71be2defa144362f
coverage: 0.956522
learned_at: 2026-10-15 22:32:37
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, CLIPVisionLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, Mute / Bypass Repeater (rgthree), ModelPatchTorchSettings, ModelPatchTorchSettings, Seed (rgthree), UNETLoader, ImpactInt, UNETLoader, RIFE VFI, String Literal, Fast Bypasser (rgthree), Fast Bypasser (rgthree), WanMoeKSampler, easy cleanGpuUsed, SimpleMath+, CLIPVisionEncode, VAEDecode, easy cleanGpuUsed, easy forLoopStart, GetImageSizeAndCount, MathExpression|pysssss, easy batchAnything, easy forLoopEnd, ImageFromBatch, ImpactInt, ImpactInt, Text Load Line From File, PrimitiveStringMultiline, CLIPTextEncode, CLIPTextEncode, WanImageToVideo, ImageResizeKJv2, RH_LLMAPI_NODE, easy showAnything, VHS_VideoCombine, LoadImage, ImpactInt]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 1, "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 SMOOTH MIX-单人物参考+自动运镜+长镜头生成（30秒）_1981343312810598402.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981343312810598402.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（46 个）：
- `wanBlockSwap`
- `wanBlockSwap`
- `Mute / Bypass Repeater (rgthree)`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Mute / Bypass Repeater (rgthree)`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `ImpactInt`
- `UNETLoader` ★核心
- `RIFE VFI`
- `String Literal`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `WanMoeKSampler` ★核心
- `easy cleanGpuUsed`
- `SimpleMath+`
- `CLIPVisionEncode`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy forLoopStart`
- `GetImageSizeAndCount`
- `MathExpression|pysssss`
- `easy batchAnything`
- `easy forLoopEnd`
- `ImageFromBatch`
- `ImpactInt`
- `ImpactInt`
- `Text Load Line From File`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `ImageResizeKJv2`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `VHS_VideoCombine`
- `LoadImage`
- `ImpactInt`

## 关键参数

- `seed` = `1`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **96%**（44/46）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Seed (rgthree)`、`UNETLoader`、`ImpactInt`、`RIFE VFI`、`String Literal`、`Fast Bypasser (rgthree)`、`WanMoeKSampler`、`easy cleanGpuUsed`、`SimpleMath+`、`CLIPVisionEncode`、`VAEDecode`、`easy forLoopStart`、`GetImageSizeAndCount`、`MathExpression|pysssss`、`easy batchAnything`、`easy forLoopEnd`、`ImageFromBatch`、`Text Load Line From File`、`CLIPTextEncode`、`WanImageToVideo`、`ImageResizeKJv2`、`RH_LLMAPI_NODE`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、Seed (rgthree)
