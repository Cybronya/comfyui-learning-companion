---
key: wan2.2 lora最好用的林黛玉妹妹工作流和模型-可生成该人物任意写实风-可用于抖音快手等自媒体_1989283451264225282.json
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

# wan2.2 lora最好用的林黛玉妹妹工作流和模型-可生成该人物任意写实风-可用于抖音快手等自媒体_1989283451264225282.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2 lora最好用的林黛玉妹妹工作流和模型-可生成该人物任意写实风-可用于抖音快手等自媒体_1989283451264225282.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（39 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGZeroStar`
- `UNETLoader` ★核心
- `VAELoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `WanVideoNAG`
- `CLIPLoader`
- `ModelSamplingSD3`
- `GetNode`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `GetNode`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `CLIPTextEncode` ★核心
- `JoinStringMulti`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SaveImage`
- `String`
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `JWStringMultiline`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `2.5`
- `scheduler` = `ddim`
- `denoise` = `simple`

## 知识

覆盖率 **62%**（24/39）

**有卡**：`CFGZeroStar`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`WanVideoNAG`、`CLIPLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`KSamplerAdvanced`、`JoinStringMulti`、`VAEDecode`、`VHS_VideoCombine`、`SaveImage`、`String`、`EmptyHunyuanLatentVideo`、`JWStringMultiline`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、CFGZeroStar
