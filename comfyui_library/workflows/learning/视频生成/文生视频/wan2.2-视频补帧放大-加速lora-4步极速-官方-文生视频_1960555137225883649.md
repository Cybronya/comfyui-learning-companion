---
key: 视频生成/文生视频/wan2.2-视频补帧放大-加速lora-4步极速-官方-文生视频_1960555137225883649.json
name: wan2.2-视频补帧放大-加速lora-4步极速-官方-文生视频_1960555137225883649.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2-视频补帧放大-加速lora-4步极速-官方-文生视频_1960555137225883649.json
hash: c17d66224795ac7f
coverage: 0.818182
learned_at: 2026-10-15 22:43:43
nodes: [CLIPLoader, VAELoader, UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, MarkdownNote, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, KSamplerAdvanced, CLIPTextEncode, MarkdownNote, CR Text Replace, SimpleMath+, Int, TextBox, RH_Prompter, easy cleanGpuUsed, CLIPTextEncode, VHS_VideoCombine, RIFE VFI, VAEDecode, PreviewImage, CR Upscale Image, Int, Int, easy showAnything, easy showAnything, PreviewImage, TextBox, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/wan2.2-视频补帧放大-加速lora-4步极速-官方-文生视频_1960555137225883649.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1960555137225883649.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `MarkdownNote`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `CR Text Replace`
- `SimpleMath+`
- `Int`
- `TextBox`
- `RH_Prompter`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `RIFE VFI`
- `VAEDecode` ★核心
- `PreviewImage`
- `CR Upscale Image`
- `Int`
- `Int`
- `easy showAnything`
- `easy showAnything`
- `PreviewImage`
- `TextBox`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **82%**（27/33）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`、`CR Text Replace`、`SimpleMath+`、`Int`、`TextBox`、`RH_Prompter`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`RIFE VFI`、`VAEDecode`、`CR Upscale Image`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
