---
key: comfyui-workflow-templates-json/video_wan2_2_5B_ti2v.json
name: video_wan2_2_5B_ti2v
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_2_5B_ti2v.json
hash: 23c93b88adecbdf5
official: true
coverage: 0.923077
learned_at: 2026-10-07 21:37:18
nodes: [UNETLoader, CLIPLoader, VAELoader, VAEDecode, CreateVideo, SaveVideo, Wan22ImageToVideoLatent, LoadImage, CLIPTextEncode, CLIPTextEncode, KSampler, ModelSamplingSD3, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 898471028164125, "steps": 20}
---

# comfyui-workflow-templates-json/video_wan2_2_5B_ti2v.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_2_5B_ti2v.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `Wan22ImageToVideoLatent`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `MarkdownNote`

## 关键参数

- `seed` = `898471028164125`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`Wan22ImageToVideoLatent`、`LoadImage`、`CLIPTextEncode`、`KSampler`、`ModelSamplingSD3`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Wan22ImageToVideoLatent
