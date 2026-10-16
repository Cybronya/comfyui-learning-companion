---
key: 视频生成/图生视频/wan2.2 Remix-高动态电影质感模型 图生视频_1988090119234236418.json
name: wan2.2 Remix-高动态电影质感模型 图生视频_1988090119234236418.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1988090119234236418.json
hash: 408e39fec73e8409
coverage: 0.933333
learned_at: 2026-10-15 22:33:01
nodes: [Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, Mute / Bypass Repeater (rgthree), ModelPatchTorchSettings, Fast Bypasser (rgthree), wanBlockSwap, ModelPatchTorchSettings, PathchSageAttentionKJ, wanBlockSwap, ModelSamplingSD3, ModelSamplingSD3, VHS_VideoCombine, KSamplerAdvanced, easy cleanGpuUsed, VAEDecode, ImageScaleBy, ImageResizeKJv2, CLIPVisionEncode, SimpleMath+, WanImageToVideo, CLIPTextEncode, CLIPTextEncode, UNETLoader, UNETLoader, CLIPLoader, VAELoader, CLIPVisionLoader, VHS_VideoCombine, PurgeVRAM_UTK, easy imageScaleDownToSize, AILab_QwenVL, ImpactInt, ImpactInt, ImpactInt, GetImageSize+, TextCombinerTwo, PrimitiveStringMultiline, RIFE VFI, easy cleanGpuUsed, Fast Groups Bypasser (rgthree), Fast Bypasser (rgthree), KSamplerAdvanced, LoadImage, ttN text, easy showAnything]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2 Remix-高动态电影质感模型 图生视频_1988090119234236418.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988090119234236418.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（45 个）：
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `Mute / Bypass Repeater (rgthree)`
- `ModelPatchTorchSettings`
- `Fast Bypasser (rgthree)`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `SimpleMath+`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `PurgeVRAM_UTK`
- `easy imageScaleDownToSize`
- `AILab_QwenVL`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `GetImageSize+`
- `TextCombinerTwo`
- `PrimitiveStringMultiline`
- `RIFE VFI`
- `easy cleanGpuUsed`
- `Fast Groups Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `ttN text`
- `easy showAnything`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **93%**（42/45）

**有卡**：`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`wanBlockSwap`、`ModelSamplingSD3`、`VHS_VideoCombine`、`KSamplerAdvanced`、`easy cleanGpuUsed`、`VAEDecode`、`ImageScaleBy`、`ImageResizeKJv2`、`CLIPVisionEncode`、`SimpleMath+`、`WanImageToVideo`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`PurgeVRAM_UTK`、`easy imageScaleDownToSize`、`AILab_QwenVL`、`ImpactInt`、`GetImageSize+`、`TextCombinerTwo`、`RIFE VFI`、`LoadImage`、`ttN text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
