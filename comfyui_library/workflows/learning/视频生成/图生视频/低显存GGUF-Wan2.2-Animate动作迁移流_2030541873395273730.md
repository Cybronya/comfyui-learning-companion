---
key: 视频生成/图生视频/低显存GGUF-Wan2.2-Animate动作迁移流_2030541873395273730.json
name: 低显存GGUF-Wan2.2-Animate动作迁移流_2030541873395273730.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/低显存GGUF-Wan2.2-Animate动作迁移流_2030541873395273730.json
hash: fb508cdaa804971c
coverage: 1
learned_at: 2026-10-15 22:35:26
nodes: [CLIPTextEncode, CLIPVisionEncode, PixelPerfectResolution, DWPreprocessor, DWPreprocessor, ModelSamplingSD3, VAEDecode, KSampler, CLIPTextEncode, TrimVideoLatent, SimpleMath+, LoraLoaderModelOnly, LoraLoaderModelOnly, UnetLoaderGGUF, CLIPLoader, VAELoader, CLIPVisionLoader, WanAnimateToVideo, VHS_VideoCombine, INTConstant, LoadImage, VHS_LoadVideo, INTConstant, INTConstant]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 888, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/低显存GGUF-Wan2.2-Animate动作迁移流_2030541873395273730.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030541873395273730.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（24 个）：
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `DWPreprocessor`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `TrimVideoLatent`
- `SimpleMath+`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `WanAnimateToVideo`
- `VHS_VideoCombine`
- `INTConstant`
- `LoadImage`
- `VHS_LoadVideo`
- `INTConstant`
- `INTConstant`

## 关键参数

- `seed` = `888`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`CLIPTextEncode`、`CLIPVisionEncode`、`PixelPerfectResolution`、`DWPreprocessor`、`ModelSamplingSD3`、`VAEDecode`、`KSampler`、`TrimVideoLatent`、`SimpleMath+`、`LoraLoaderModelOnly`、`UnetLoaderGGUF`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`WanAnimateToVideo`、`VHS_VideoCombine`、`INTConstant`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
