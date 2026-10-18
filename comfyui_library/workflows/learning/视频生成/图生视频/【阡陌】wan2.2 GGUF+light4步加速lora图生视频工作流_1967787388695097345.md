---
key: 视频生成/图生视频/【阡陌】wan2.2 GGUF+light4步加速lora图生视频工作流_1967787388695097345.json
name: 【阡陌】wan2.2 GGUF+light4步加速lora图生视频工作流_1967787388695097345.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【阡陌】wan2.2 GGUF+light4步加速lora图生视频工作流_1967787388695097345.json
hash: e17fbb6663619cd9
coverage: 1
learned_at: 2026-10-15 22:31:42
nodes: [VAEDecode, ModelSamplingSD3, KSamplerAdvanced, CreateVideo, SaveVideo, CLIPLoader, KSamplerAdvanced, CLIPTextEncode, VAELoader, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, WanImageToVideo, CLIPTextEncode, LoadImage, UnetLoaderGGUF, UnetLoaderGGUF, UNETLoader, UNETLoader, ModelSamplingSD3]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/【阡陌】wan2.2 GGUF+light4步加速lora图生视频工作流_1967787388695097345.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967787388695097345.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（20 个）：
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CreateVideo`
- `SaveVideo`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`VAEDecode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CreateVideo`、`SaveVideo`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`LoadImage`、`LoraLoaderModelOnly`、`WanImageToVideo`、`UnetLoaderGGUF`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
