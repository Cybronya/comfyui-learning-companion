---
key: 视频生成/文生视频/超级LTX0.95图生视频&文生视频_1898016984871981058.json
name: 超级LTX0.95图生视频&文生视频_1898016984871981058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1898016984871981058.json
hash: 2757461a65e41559
coverage: 0.933333
learned_at: 2026-10-15 22:43:20
nodes: [CLIPTextEncode, VAEDecode, SaveAnimatedWEBP, LTXVConditioning, LTXVScheduler, SamplerCustom, KSamplerSelect, LTXVImgToVideo, VHS_VideoCombine, GetImageSizeAndCount, CLIPTextEncode, VAEDecode, SaveAnimatedWEBP, LTXVConditioning, EmptyLTXVLatentVideo, LTXVScheduler, SamplerCustom, KSamplerSelect, GetImageSizeAndCount, CLIPLoader, LoadImage, CLIPTextEncode, CheckpointLoaderSimple, VHS_VideoCombine, CheckpointLoaderSimple, CLIPLoader, Fast Groups Bypasser (rgthree), Note, CLIPTextEncode, Note Plus (mtb)]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-video-2b-v0.9.5.safetensors"}
---

# 视频生成/文生视频/超级LTX0.95图生视频&文生视频_1898016984871981058.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1898016984871981058.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveAnimatedWEBP`
- `LTXVConditioning`
- `LTXVScheduler`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `LTXVImgToVideo`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveAnimatedWEBP`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVScheduler`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `GetImageSizeAndCount`
- `CLIPLoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `CLIPTextEncode` ★核心
- `Note Plus (mtb)`

## 关键参数

- `checkpoint` = `ltx-video-2b-v0.9.5.safetensors`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`SaveAnimatedWEBP`、`LTXVConditioning`、`LTXVScheduler`、`SamplerCustom`、`KSamplerSelect`、`LTXVImgToVideo`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`EmptyLTXVLatentVideo`、`CLIPLoader`、`LoadImage`、`CheckpointLoaderSimple`、`Note Plus (mtb)`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustom、EmptyLTXVLatentVideo
