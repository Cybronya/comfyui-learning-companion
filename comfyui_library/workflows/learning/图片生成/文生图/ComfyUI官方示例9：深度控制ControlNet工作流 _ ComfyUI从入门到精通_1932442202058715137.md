---
key: 图片生成/文生图/ComfyUI官方示例9：深度控制ControlNet工作流 _ ComfyUI从入门到精通_1932442202058715137.json
name: ComfyUI官方示例9：深度控制ControlNet工作流 _ ComfyUI从入门到精通_1932442202058715137
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ComfyUI官方示例9：深度控制ControlNet工作流 _ ComfyUI从入门到精通_1932442202058715137.json
hash: ae505ea70a30acea
coverage: 1
learned_at: 2026-10-10 21:26:57
nodes: [ControlNetApplyAdvanced, VAEDecode, SaveImage, EmptyLatentImage, CLIPTextEncode, ControlNetLoader, CLIPTextEncode, CheckpointLoaderSimple, LoadImage, KSampler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "比鲁斯建筑室内通用大模型SD1.5_SD1.5.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 1024, "sampler_name": "euler_ancestral", "scheduler": "normal", "seed": 1002364322755070, "steps": 20, "width": 1024}
---

# 图片生成/文生图/ComfyUI官方示例9：深度控制ControlNet工作流 _ ComfyUI从入门到精通_1932442202058715137.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ComfyUI官方示例9：深度控制ControlNet工作流 _ ComfyUI从入门到精通_1932442202058715137.json`

## 结构

**节点**（10 个）：
- `ControlNetApplyAdvanced`
- `VAEDecode`
- `SaveImage`
- `EmptyLatentImage`
- `CLIPTextEncode`
- `ControlNetLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `LoadImage`
- `KSampler`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `7`
- `checkpoint` = `比鲁斯建筑室内通用大模型SD1.5_SD1.5.safetensors`
- `controlnet_strength` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `normal`
- `seed` = `1002364322755070`
- `steps` = `20`
- `width` = `1024`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`ControlNetApplyAdvanced`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`CLIPTextEncode`、`ControlNetLoader`、`CheckpointLoaderSimple`、`LoadImage`、`KSampler`
