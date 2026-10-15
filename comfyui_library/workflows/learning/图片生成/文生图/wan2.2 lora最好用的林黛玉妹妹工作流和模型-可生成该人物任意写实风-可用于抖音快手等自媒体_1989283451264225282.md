---
key: 图片生成/文生图/wan2.2 lora最好用的林黛玉妹妹工作流和模型-可生成该人物任意写实风-可用于抖音快手等自媒体_1989283451264225282.json
name: wan2.2 lora最好用的林黛玉妹妹工作流和模型-可生成该人物任意写实风-可用于抖音快手等自媒体_1989283451264225282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2 lora最好用的林黛玉妹妹工作流和模型-可生成该人物任意写实风-可用于抖音快手等自媒体_1989283451264225282.json
hash: 23537ce4ef73e134
coverage: 0.615385
learned_at: 2026-10-10 20:59:27
nodes: [SetNode, GetNode, GetNode, GetNode, CFGZeroStar, UNETLoader, VAELoader, SetNode, LoraLoaderModelOnly, GetNode, SetNode, LoraLoaderModelOnly, UNETLoader, SetNode, WanVideoNAG, CLIPLoader, ModelSamplingSD3, GetNode, ModelSamplingSD3, PathchSageAttentionKJ, GetNode, MarkdownNote, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, SetNode, CLIPTextEncode, JoinStringMulti, VAEDecode, SetNode, GetNode, VHS_VideoCombine, SetNode, SaveImage, String, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, JWStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 2.5, "scheduler": "ddim", "seed": "enable", "steps": "randomize"}
---

# 图片生成/文生图/wan2.2 lora最好用的林黛玉妹妹工作流和模型-可生成该人物任意写实风-可用于抖音快手等自媒体_1989283451264225282.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2 lora最好用的林黛玉妹妹工作流和模型-可生成该人物任意写实风-可用于抖音快手等自媒体_1989283451264225282.json`

## 结构

**节点**（39 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGZeroStar`
- `UNETLoader`
- `VAELoader`
- `SetNode`
- `LoraLoaderModelOnly`
- `GetNode`
- `SetNode`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `SetNode`
- `WanVideoNAG`
- `CLIPLoader`
- `ModelSamplingSD3`
- `GetNode`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `GetNode`
- `MarkdownNote`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `KSamplerAdvanced`
- `SetNode`
- `CLIPTextEncode`
- `JoinStringMulti`
- `VAEDecode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SaveImage`
- `String`
- `LoraLoaderModelOnly`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly`
- `JWStringMultiline`

## 关键参数

- `cfg` = `8`
- `denoise` = `simple`
- `sampler_name` = `2.5`
- `scheduler` = `ddim`
- `seed` = `enable`
- `steps` = `randomize`

## 知识

覆盖率 **62%**（24/39）

**有卡**：`SetNode`、`GetNode`、`CFGZeroStar`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`WanVideoNAG`、`CLIPLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`MarkdownNote`、`CLIPTextEncode`、`KSamplerAdvanced`
