---
key: 视频生成/文生视频/Wan 2.1 ComfyUI 首尾帧+故事版驱动工作流_1926598014440251394.json
name: Wan 2.1 ComfyUI 首尾帧+故事版驱动工作流_1926598014440251394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.1 ComfyUI 首尾帧+故事版驱动工作流_1926598014440251394.json
hash: 61e3c34a8caec0a8
coverage: 0.730769
learned_at: 2026-10-15 22:47:05
nodes: [CLIPVisionEncode, VHS_VideoCombine, Reroute, CLIPVisionEncode, LoadImage, LoadImage, Reroute, VAELoader, Anything Everywhere, VAEDecode, ImageResize+, ImageResize+, UNETLoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, Note, Note, Note, WanFirstLastFrameToVideo, ModelSamplingSD3, Note, easy clearCacheAll, CLIPVisionLoader, Load Lora, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 666670, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan 2.1 ComfyUI 首尾帧+故事版驱动工作流_1926598014440251394.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan 2.1 ComfyUI 首尾帧+故事版驱动工作流_1926598014440251394.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（26 个）：
- `CLIPVisionEncode`
- `VHS_VideoCombine`
- `Reroute`
- `CLIPVisionEncode`
- `LoadImage`
- `LoadImage`
- `Reroute`
- `VAELoader`
- `Anything Everywhere`
- `VAEDecode` ★核心
- `ImageResize+`
- `ImageResize+`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `Note`
- `WanFirstLastFrameToVideo`
- `ModelSamplingSD3`
- `Note`
- `easy clearCacheAll`
- `CLIPVisionLoader`
- `Load Lora`
- `KSampler` ★核心

## 关键参数

- `seed` = `666670`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（19/26）

**有卡**：`CLIPVisionEncode`、`VHS_VideoCombine`、`LoadImage`、`VAELoader`、`VAEDecode`、`ImageResize+`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`WanFirstLastFrameToVideo`、`ModelSamplingSD3`、`easy clearCacheAll`、`CLIPVisionLoader`、`Load Lora`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
