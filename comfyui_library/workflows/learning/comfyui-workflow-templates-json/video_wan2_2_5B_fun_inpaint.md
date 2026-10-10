---
key: comfyui-workflow-templates-json/video_wan2_2_5B_fun_inpaint.json
name: video_wan2_2_5B_fun_inpaint
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_2_5B_fun_inpaint.json
hash: 8efa4d2434745c6f
official: true
coverage: 0.928571
learned_at: 2026-10-10 22:50:43
nodes: [CLIPLoader, VAEDecode, SaveVideo, CLIPTextEncode, VAELoader, UNETLoader, ModelSamplingSD3, WanFunInpaintToVideo, KSampler, CLIPTextEncode, MarkdownNote, LoadImage, LoadImage, CreateVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 115716327295867, "steps": 20}
---

# comfyui-workflow-templates-json/video_wan2_2_5B_fun_inpaint.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_2_5B_fun_inpaint.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `WanFunInpaintToVideo`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `CreateVideo`

## 关键参数

- `seed` = `115716327295867`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CLIPLoader`、`VAEDecode`、`SaveVideo`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`ModelSamplingSD3`、`WanFunInpaintToVideo`、`KSampler`、`LoadImage`、`CreateVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SaveVideo
