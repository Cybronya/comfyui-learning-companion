---
key: 平台全量/ComfyUI官方示例4：Outpainting工作流详解 _ ComfyUI从入门到精通_1931598672390193154.json
name: ComfyUI官方示例4：Outpainting工作流详解 _ ComfyUI从入门到精通_1931598672390193154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ComfyUI官方示例4：Outpainting工作流详解 _ ComfyUI从入门到精通_1931598672390193154.json
hash: 1899ab3d37af8576
coverage: 0.833333
learned_at: 2026-11-14 00:22:28
nodes: [VAEDecode, SaveImage, VAEEncodeForInpaint, KSampler, CLIPTextEncode, LoadImage, CLIPTextEncode, CheckpointLoaderSimple, ImagePadForOutpaint, PreviewImage, MaskToImage, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 7, "checkpoint": "pornmaster_sdxlV4VAE-inpainting.safetensors", "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 960378096036077, "steps": 20}
---

# 平台全量/ComfyUI官方示例4：Outpainting工作流详解 _ ComfyUI从入门到精通_1931598672390193154.json

> 来源文件 `comfyui_library/workflows/平台全量/ComfyUI官方示例4：Outpainting工作流详解 _ ComfyUI从入门到精通_1931598672390193154.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `VAEEncodeForInpaint` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `ImagePadForOutpaint`
- `PreviewImage`
- `MaskToImage`
- `PreviewImage`

## 关键参数

- `seed` = `960378096036077`
- `steps` = `20`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `pornmaster_sdxlV4VAE-inpainting.safetensors`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`VAEDecode`、`SaveImage`、`VAEEncodeForInpaint`、`KSampler`、`CLIPTextEncode`、`LoadImage`、`CheckpointLoaderSimple`、`ImagePadForOutpaint`、`MaskToImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、VAEEncodeForInpaint、SaveImage、ImagePadForOutpaint
