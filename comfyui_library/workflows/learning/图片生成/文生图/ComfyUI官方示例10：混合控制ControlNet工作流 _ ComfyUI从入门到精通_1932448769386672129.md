---
key: 图片生成/文生图/ComfyUI官方示例10：混合控制ControlNet工作流 _ ComfyUI从入门到精通_1932448769386672129.json
name: ComfyUI官方示例10：混合控制ControlNet工作流 _ ComfyUI从入门到精通_1932448769386672129
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ComfyUI官方示例10：混合控制ControlNet工作流 _ ComfyUI从入门到精通_1932448769386672129.json
hash: 004aaed7376c8915
coverage: 1
learned_at: 2026-10-10 21:26:53
nodes: [ControlNetApplyAdvanced, CLIPTextEncode, CLIPTextEncode, VAEDecode, SaveImage, ControlNetApplyAdvanced, EmptyLatentImage, ControlNetLoader, CheckpointLoaderSimple, VAELoader, ControlNetLoader, LoadImage, LoadImage, KSampler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 6, "checkpoint": "awpainting_v14.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 1024, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 498215374689016, "steps": 20, "width": 1024}
---

# 图片生成/文生图/ComfyUI官方示例10：混合控制ControlNet工作流 _ ComfyUI从入门到精通_1932448769386672129.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ComfyUI官方示例10：混合控制ControlNet工作流 _ ComfyUI从入门到精通_1932448769386672129.json`

## 结构

**节点**（14 个）：
- `ControlNetApplyAdvanced`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `VAEDecode`
- `SaveImage`
- `ControlNetApplyAdvanced`
- `EmptyLatentImage`
- `ControlNetLoader`
- `CheckpointLoaderSimple`
- `VAELoader`
- `ControlNetLoader`
- `LoadImage`
- `LoadImage`
- `KSampler`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `6`
- `checkpoint` = `awpainting_v14.safetensors`
- `controlnet_strength` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `seed` = `498215374689016`
- `steps` = `20`
- `width` = `1024`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`ControlNetApplyAdvanced`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`ControlNetLoader`、`CheckpointLoaderSimple`、`VAELoader`、`LoadImage`、`KSampler`
