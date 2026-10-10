---
key: comfyui-workflow-templates-json/flux_fill_outpaint_example.json
name: flux_fill_outpaint_example
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/flux_fill_outpaint_example.json
hash: 87f4f940de570cab
official: true
coverage: 0.928571
learned_at: 2026-10-10 22:47:12
nodes: [DualCLIPLoader, UNETLoader, CLIPTextEncode, VAELoader, ConditioningZeroOut, FluxGuidance, DifferentialDiffusion, ImagePadForOutpaint, VAEDecode, InpaintModelConditioning, KSampler, SaveImage, LoadImage, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 164211176398261, "steps": 20}
---

# comfyui-workflow-templates-json/flux_fill_outpaint_example.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/flux_fill_outpaint_example.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `FluxGuidance`
- `DifferentialDiffusion`
- `ImagePadForOutpaint`
- `VAEDecode` ★核心
- `InpaintModelConditioning`
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `MarkdownNote`

## 关键参数

- `seed` = `164211176398261`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`ConditioningZeroOut`、`FluxGuidance`、`DifferentialDiffusion`、`ImagePadForOutpaint`、`VAEDecode`、`InpaintModelConditioning`、`KSampler`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
