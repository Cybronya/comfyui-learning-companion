---
key: 视频生成/图生视频/【阡陌】SageAttention+wan2.2+light4步加速lora提速40%图生视频工作流_1968502067780300801.json
name: 【阡陌】SageAttention+wan2.2+light4步加速lora提速40%图生视频工作流_1968502067780300801.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【阡陌】SageAttention+wan2.2+light4步加速lora提速40%图生视频工作流_1968502067780300801.json
hash: 45f9e37fe82c4032
coverage: 1
learned_at: 2026-10-15 22:31:45
nodes: [VAEDecode, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, CreateVideo, SaveVideo, CLIPLoader, KSamplerAdvanced, CLIPTextEncode, VAELoader, LoadImage, LoadImage, ModelPatchTorchSettings, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPTextEncode, WanImageToVideo]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/【阡陌】SageAttention+wan2.2+light4步加速lora提速40%图生视频工作流_1968502067780300801.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1968502067780300801.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CreateVideo`
- `SaveVideo`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`VAEDecode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CreateVideo`、`SaveVideo`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`LoadImage`、`ModelPatchTorchSettings`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
