---
key: 平台全量/ComfyUI官方示例7：边缘检测ControlNet工作流 _ ComfyUI从入门到精通_1932403183488540674.json
name: ComfyUI官方示例7：边缘检测ControlNet工作流 _ ComfyUI从入门到精通_1932403183488540674
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/ComfyUI官方示例7：边缘检测ControlNet工作流 _ ComfyUI从入门到精通_1932403183488540674.json
hash: 760bb88ed3cdad5f
coverage: 1
learned_at: 2026-11-14 00:22:30
nodes: [EmptyLatentImage, VAEDecode, SaveImage, CLIPTextEncode, CLIPTextEncode, ControlNetApplyAdvanced, VAELoader, ControlNetLoader, LoadImage, KSampler, CheckpointLoaderSimple]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 6, "checkpoint": "indoor outdoor model sd1.5.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 249660755595753, "steps": 20, "width": 1024}
---

# 平台全量/ComfyUI官方示例7：边缘检测ControlNet工作流 _ ComfyUI从入门到精通_1932403183488540674.json

> 来源文件 `comfyui_library/workflows/平台全量/ComfyUI官方示例7：边缘检测ControlNet工作流 _ ComfyUI从入门到精通_1932403183488540674.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（11 个）：
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `VAELoader`
- `ControlNetLoader`
- `LoadImage`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `controlnet_strength` = `1`
- `seed` = `249660755595753`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `checkpoint` = `indoor outdoor model sd1.5.safetensors`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`ControlNetApplyAdvanced`、`VAELoader`、`ControlNetLoader`、`LoadImage`、`KSampler`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced
