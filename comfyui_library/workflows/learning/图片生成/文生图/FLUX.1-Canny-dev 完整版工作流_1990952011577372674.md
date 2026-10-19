---
key: 图片生成/文生图/FLUX.1-Canny-dev 完整版工作流_1990952011577372674.json
name: FLUX.1-Canny-dev 完整版工作流_1990952011577372674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.1-Canny-dev 完整版工作流_1990952011577372674.json
hash: 3704284bb30cdf08
coverage: 0.857143
learned_at: 2026-10-19 20:34:10
nodes: [DualCLIPLoader, ConditioningZeroOut, UNETLoader, VAELoader, FluxGuidance, Canny, SaveImage, VAEDecode, KSampler, InstructPixToPixConditioning, PreviewImage, CLIPTextEncode, MarkdownNote, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 694520606053705, "steps": 20}
---

# 图片生成/文生图/FLUX.1-Canny-dev 完整版工作流_1990952011577372674.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.1-Canny-dev 完整版工作流_1990952011577372674.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `VAELoader`
- `FluxGuidance`
- `Canny`
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `InstructPixToPixConditioning`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `seed` = `694520606053705`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`DualCLIPLoader`、`ConditioningZeroOut`、`UNETLoader`、`VAELoader`、`FluxGuidance`、`Canny`、`SaveImage`、`VAEDecode`、`KSampler`、`InstructPixToPixConditioning`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、Canny
