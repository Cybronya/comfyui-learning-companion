---
key: 视频生成/文生视频/Wan 2.1 ComfyUI 首尾帧+故事版驱动工作流_1926598014440251394.json
name: Wan 2.1 ComfyUI 首尾帧+故事版驱动工作流_1926598014440251394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.1 ComfyUI 首尾帧+故事版驱动工作流_1926598014440251394.json
hash: 61e3c34a8caec0a8
coverage: 0.576923
learned_at: 2026-10-10 23:06:06
nodes: [CLIPVisionEncode, VHS_VideoCombine, Reroute, CLIPVisionEncode, LoadImage, LoadImage, Reroute, VAELoader, Anything Everywhere, VAEDecode, ImageResize+, ImageResize+, UNETLoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, Note, Note, Note, WanFirstLastFrameToVideo, ModelSamplingSD3, Note, easy clearCacheAll, CLIPVisionLoader, Load Lora, KSampler]
patterns: []
missing: [easy clearCacheAll, ImageResize+, ImageResize+, Load Lora]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 666670, "steps": 8}
discoveries: [次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `Load Lora` 仅有 LoRA 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
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

覆盖率 **58%**（15/26）

**有卡**：`CLIPVisionEncode`、`VHS_VideoCombine`、`LoadImage`、`VAELoader`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`WanFirstLastFrameToVideo`、`ModelSamplingSD3`、`CLIPVisionLoader`、`KSampler`

**缺卡**（4）：`easy clearCacheAll`、`ImageResize+`、`ImageResize+`、`Load Lora`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `Load Lora` 仅有 LoRA 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
