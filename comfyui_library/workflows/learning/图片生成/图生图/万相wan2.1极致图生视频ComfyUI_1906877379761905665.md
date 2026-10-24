---
key: 图片生成/图生图/万相wan2.1极致图生视频ComfyUI_1906877379761905665.json
name: 万相wan2.1极致图生视频ComfyUI_1906877379761905665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/万相wan2.1极致图生视频ComfyUI_1906877379761905665.json
hash: e41dff33ad4863da
coverage: 0.882353
learned_at: 2026-10-23 12:01:15
nodes: [CLIPLoader, CLIPTextEncode, Note, CLIPVisionLoader, VAEDecode, VHS_VideoCombine, Note, ImageResizeKJ, Int, KSampler, CLIPVisionEncode, WanImageToVideo, VAELoader, LoadImage, UNETLoader, CLIPTextEncode, TextInput_]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 913769959031559, "steps": 20}
---

# 图片生成/图生图/万相wan2.1极致图生视频ComfyUI_1906877379761905665.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/万相wan2.1极致图生视频ComfyUI_1906877379761905665.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `Note`
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `Note`
- `ImageResizeKJ`
- `Int`
- `KSampler` ★核心
- `CLIPVisionEncode`
- `WanImageToVideo`
- `VAELoader`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `TextInput_`

## 关键参数

- `seed` = `913769959031559`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`CLIPVisionLoader`、`VAEDecode`、`VHS_VideoCombine`、`ImageResizeKJ`、`Int`、`KSampler`、`CLIPVisionEncode`、`WanImageToVideo`、`VAELoader`、`LoadImage`、`UNETLoader`、`TextInput_`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
