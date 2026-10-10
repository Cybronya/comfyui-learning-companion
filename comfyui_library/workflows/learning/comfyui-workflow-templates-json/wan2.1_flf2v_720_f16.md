---
key: comfyui-workflow-templates-json/wan2.1_flf2v_720_f16.json
name: wan2.1_flf2v_720_f16
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/wan2.1_flf2v_720_f16.json
hash: 01f100c0ed6a8bc5
official: true
coverage: 0.941176
learned_at: 2026-10-10 22:50:54
nodes: [VAELoader, CLIPVisionEncode, CLIPVisionLoader, CLIPVisionEncode, ModelSamplingSD3, WanFirstLastFrameToVideo, KSampler, CLIPTextEncode, LoadImage, UNETLoader, CLIPLoader, CLIPTextEncode, VAEDecode, CreateVideo, SaveVideo, LoadImage, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1012535162155917, "steps": 20}
---

# comfyui-workflow-templates-json/wan2.1_flf2v_720_f16.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/wan2.1_flf2v_720_f16.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `VAELoader`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `WanFirstLastFrameToVideo`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `LoadImage`
- `MarkdownNote`

## 关键参数

- `seed` = `1012535162155917`
- `steps` = `20`
- `cfg` = `3`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`VAELoader`、`CLIPVisionEncode`、`CLIPVisionLoader`、`ModelSamplingSD3`、`WanFirstLastFrameToVideo`、`KSampler`、`CLIPTextEncode`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`CreateVideo`、`SaveVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
