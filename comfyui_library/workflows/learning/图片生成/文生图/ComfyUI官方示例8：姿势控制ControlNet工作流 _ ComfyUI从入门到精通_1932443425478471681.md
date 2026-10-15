---
key: 图片生成/文生图/ComfyUI官方示例8：姿势控制ControlNet工作流 _ ComfyUI从入门到精通_1932443425478471681.json
name: ComfyUI官方示例8：姿势控制ControlNet工作流 _ ComfyUI从入门到精通_1932443425478471681
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ComfyUI官方示例8：姿势控制ControlNet工作流 _ ComfyUI从入门到精通_1932443425478471681.json
hash: ffcf3251309a4e56
coverage: 0.923077
learned_at: 2026-10-10 21:26:56
nodes: [ControlNetApplyAdvanced, CLIPTextEncode, ControlNetLoader, VAELoader, EmptyLatentImage, CheckpointLoaderSimple, CLIPSetLastLayer, LoadImage, CLIPTextEncode, VAEDecode, PreviewImage, SaveImage, KSampler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "麦橘majicmixRealistic_v7.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 1024, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 164310667656917, "steps": 20, "width": 1024}
---

# 图片生成/文生图/ComfyUI官方示例8：姿势控制ControlNet工作流 _ ComfyUI从入门到精通_1932443425478471681.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ComfyUI官方示例8：姿势控制ControlNet工作流 _ ComfyUI从入门到精通_1932443425478471681.json`

## 结构

**节点**（13 个）：
- `ControlNetApplyAdvanced`
- `CLIPTextEncode`
- `ControlNetLoader`
- `VAELoader`
- `EmptyLatentImage`
- `CheckpointLoaderSimple`
- `CLIPSetLastLayer`
- `LoadImage`
- `CLIPTextEncode`
- `VAEDecode`
- `PreviewImage`
- `SaveImage`
- `KSampler`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `7`
- `checkpoint` = `麦橘majicmixRealistic_v7.safetensors`
- `controlnet_strength` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `seed` = `164310667656917`
- `steps` = `20`
- `width` = `1024`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`ControlNetApplyAdvanced`、`CLIPTextEncode`、`ControlNetLoader`、`VAELoader`、`EmptyLatentImage`、`CheckpointLoaderSimple`、`CLIPSetLastLayer`、`LoadImage`、`VAEDecode`、`PreviewImage`、`SaveImage`
