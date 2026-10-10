---
key: comfyui-workflow-templates-json/flux_canny_model_example.json
name: flux_canny_model_example
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/flux_canny_model_example.json
hash: 466bb57fdd4e5a9e
official: true
coverage: 0.857143
learned_at: 2026-10-10 22:47:08
nodes: [DualCLIPLoader, ConditioningZeroOut, UNETLoader, VAELoader, FluxGuidance, Canny, LoadImage, SaveImage, VAEDecode, KSampler, InstructPixToPixConditioning, PreviewImage, CLIPTextEncode, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 1125476660951871, "steps": 20}
---

# comfyui-workflow-templates-json/flux_canny_model_example.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/flux_canny_model_example.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `VAELoader`
- `FluxGuidance`
- `Canny`
- `LoadImage`
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `InstructPixToPixConditioning`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `MarkdownNote`

## 关键参数

- `seed` = `1125476660951871`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`DualCLIPLoader`、`ConditioningZeroOut`、`UNETLoader`、`VAELoader`、`FluxGuidance`、`Canny`、`LoadImage`、`SaveImage`、`VAEDecode`、`KSampler`、`InstructPixToPixConditioning`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、Canny
