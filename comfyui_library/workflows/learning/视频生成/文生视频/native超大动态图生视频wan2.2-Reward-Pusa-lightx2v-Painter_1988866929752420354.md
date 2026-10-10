---
key: 视频生成/文生视频/native超大动态图生视频wan2.2-Reward-Pusa-lightx2v-Painter_1988866929752420354.json
name: native超大动态图生视频wan2.2-Reward-Pusa-lightx2v-Painter_1988866929752420354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/native超大动态图生视频wan2.2-Reward-Pusa-lightx2v-Painter_1988866929752420354.json
hash: edfdeb2ce38f6867
coverage: 0.928571
learned_at: 2026-10-11 02:57:39
nodes: [ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, VHS_VideoCombine, VAEDecode, CLIPTextEncode, CLIPTextEncode, CLIPLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, VAELoader, PainterI2V, ImageLoader, ImageResizeKJv2, MultiplePathsInput, Qwen3_VQA, easy cleanGpuUsed, easy showAnything, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: [easy cleanGpuUsed]
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/native超大动态图生视频wan2.2-Reward-Pusa-lightx2v-Painter_1988866929752420354.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/native超大动态图生视频wan2.2-Reward-Pusa-lightx2v-Painter_1988866929752420354.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `VAELoader`
- `PainterI2V`
- `ImageLoader`
- `ImageResizeKJv2`
- `MultiplePathsInput`
- `Qwen3_VQA`
- `easy cleanGpuUsed`
- `easy showAnything`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`ModelSamplingSD3`、`KSamplerAdvanced`、`VHS_VideoCombine`、`VAEDecode`、`CLIPTextEncode`、`CLIPLoader`、`PathchSageAttentionKJ`、`VAELoader`、`PainterI2V`、`ImageLoader`、`ImageResizeKJv2`、`MultiplePathsInput`、`Qwen3_VQA`、`UNETLoader`、`LoraLoaderModelOnly`

**缺卡**（1）：`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、ImageResizeKJv2

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
