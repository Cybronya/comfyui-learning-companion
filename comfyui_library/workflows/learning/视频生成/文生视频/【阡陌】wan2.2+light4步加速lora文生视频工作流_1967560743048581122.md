---
key: 视频生成/文生视频/【阡陌】wan2.2+light4步加速lora文生视频工作流_1967560743048581122.json
name: 【阡陌】wan2.2+light4步加速lora文生视频工作流_1967560743048581122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1967560743048581122.json
hash: 43c59cf5299529ca
coverage: 1
learned_at: 2026-10-15 22:43:45
nodes: [VAEDecode, LoadImage, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, LoraLoaderModelOnly, KSamplerAdvanced, VAELoader, LoraLoaderModelOnly, UNETLoader, UNETLoader, CreateVideo, SaveVideo, EmptyHunyuanLatentVideo, CLIPLoader]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/【阡陌】wan2.2+light4步加速lora文生视频工作流_1967560743048581122.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1967560743048581122.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `VAEDecode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CreateVideo`
- `SaveVideo`
- `EmptyHunyuanLatentVideo`
- `CLIPLoader`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`VAEDecode`、`LoadImage`、`CLIPTextEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`VAELoader`、`UNETLoader`、`CreateVideo`、`SaveVideo`、`EmptyHunyuanLatentVideo`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
