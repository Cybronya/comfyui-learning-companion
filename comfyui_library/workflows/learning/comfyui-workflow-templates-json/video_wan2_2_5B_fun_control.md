---
key: comfyui-workflow-templates-json/video_wan2_2_5B_fun_control.json
name: video_wan2_2_5B_fun_control
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_2_5B_fun_control.json
hash: 9e671aa9cf9013ee
official: true
coverage: 0.833333
learned_at: 2026-10-07 21:37:17
nodes: [CLIPLoader, ModelSamplingSD3, VAELoader, UNETLoader, Canny, GetVideoComponents, PreviewImage, KSampler, CreateVideo, VAEDecode, SaveVideo, Wan22FunControlToVideo, LoadVideo, CLIPTextEncode, LoadImage, CLIPTextEncode, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 436961904444694, "steps": 20}
---

# comfyui-workflow-templates-json/video_wan2_2_5B_fun_control.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_2_5B_fun_control.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `ModelSamplingSD3`
- `VAELoader`
- `UNETLoader` ★核心
- `Canny`
- `GetVideoComponents`
- `PreviewImage`
- `KSampler` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `SaveVideo`
- `Wan22FunControlToVideo`
- `LoadVideo`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `seed` = `436961904444694`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CLIPLoader`、`ModelSamplingSD3`、`VAELoader`、`UNETLoader`、`Canny`、`GetVideoComponents`、`KSampler`、`CreateVideo`、`VAEDecode`、`SaveVideo`、`Wan22FunControlToVideo`、`LoadVideo`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Canny
