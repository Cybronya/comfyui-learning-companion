---
key: 视频生成/文生视频/native图生视频wan2.2-Reward-Pusa-1022lightx2v-Painter_1988874017887096833.json
name: native图生视频wan2.2-Reward-Pusa-1022lightx2v-Painter_1988874017887096833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/native图生视频wan2.2-Reward-Pusa-1022lightx2v-Painter_1988874017887096833.json
hash: 4e2329ff1e388516
coverage: 0.962963
learned_at: 2026-10-15 22:47:30
nodes: [ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, VHS_VideoCombine, VAEDecode, CLIPTextEncode, CLIPTextEncode, CLIPLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, VAELoader, PainterI2V, ImageResizeKJv2, MultiplePathsInput, Qwen3_VQA, easy cleanGpuUsed, easy showAnything, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageLoader]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/native图生视频wan2.2-Reward-Pusa-1022lightx2v-Painter_1988874017887096833.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/native图生视频wan2.2-Reward-Pusa-1022lightx2v-Painter_1988874017887096833.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（27 个）：
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
- `ImageLoader`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`ModelSamplingSD3`、`KSamplerAdvanced`、`VHS_VideoCombine`、`VAEDecode`、`CLIPTextEncode`、`CLIPLoader`、`PathchSageAttentionKJ`、`VAELoader`、`PainterI2V`、`ImageResizeKJv2`、`MultiplePathsInput`、`Qwen3_VQA`、`easy cleanGpuUsed`、`UNETLoader`、`LoraLoaderModelOnly`、`ImageLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、ImageResizeKJv2
