---
key: 平台全量/Production of Non Person IP Dataset_1864962757723639809.json
name: Production of Non Person IP Dataset_1864962757723639809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Production of Non Person IP Dataset_1864962757723639809.json
hash: 4b40077bc3446409
coverage: 1
learned_at: 2026-11-14 00:48:36
nodes: [CLIPVisionEncode, KSampler, VAELoader, FluxGuidance, CLIPTextEncode, StyleModelApply, ImagePadForOutpaint, InpaintModelConditioning, SaveImage, LoadImage, VAEDecode, StyleModelLoader, CLIPVisionLoader, DualCLIPLoader, CLIPTextEncode, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc_bh2", "scheduler": "simple", "seed": 740220150614448, "steps": 30}
---

# 平台全量/Production of Non Person IP Dataset_1864962757723639809.json

> 来源文件 `comfyui_library/workflows/平台全量/Production of Non Person IP Dataset_1864962757723639809.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPVisionEncode`
- `KSampler` ★核心
- `VAELoader`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `StyleModelApply`
- `ImagePadForOutpaint`
- `InpaintModelConditioning`
- `SaveImage`
- `LoadImage`
- `VAEDecode` ★核心
- `StyleModelLoader`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `740220150614448`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `uni_pc_bh2`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`CLIPVisionEncode`、`KSampler`、`VAELoader`、`FluxGuidance`、`CLIPTextEncode`、`StyleModelApply`、`ImagePadForOutpaint`、`InpaintModelConditioning`、`SaveImage`、`LoadImage`、`VAEDecode`、`StyleModelLoader`、`CLIPVisionLoader`、`DualCLIPLoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、CLIPVisionEncode
