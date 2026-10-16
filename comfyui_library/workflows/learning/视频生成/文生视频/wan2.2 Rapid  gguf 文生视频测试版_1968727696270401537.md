---
key: 视频生成/文生视频/wan2.2 Rapid  gguf 文生视频测试版_1968727696270401537.json
name: wan2.2 Rapid  gguf 文生视频测试版_1968727696270401537.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1968727696270401537.json
hash: 9e6ba7a3ef0e7467
coverage: 1
learned_at: 2026-10-15 22:43:46
nodes: [CLIPTextEncode, ModelSamplingSD3, VAEDecode, wanBlockSwap, TorchCompileModelWanVideoV2, VHS_VideoCombine, UnetLoaderGGUF, CLIPLoaderGGUF, PathchSageAttentionKJ, CLIPTextEncode, EmptyHunyuanLatentVideo, VAELoader, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 430147491186470, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.2 Rapid  gguf 文生视频测试版_1968727696270401537.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1968727696270401537.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（13 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `wanBlockSwap`
- `TorchCompileModelWanVideoV2`
- `VHS_VideoCombine`
- `UnetLoaderGGUF` ★核心
- `CLIPLoaderGGUF`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `KSampler` ★核心

## 关键参数

- `seed` = `430147491186470`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`VAEDecode`、`wanBlockSwap`、`TorchCompileModelWanVideoV2`、`VHS_VideoCombine`、`UnetLoaderGGUF`、`CLIPLoaderGGUF`、`PathchSageAttentionKJ`、`EmptyHunyuanLatentVideo`、`VAELoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、EmptyHunyuanLatentVideo、CLIPLoaderGGUF、ClipLoaderGGUF、ClipLoaderGGUF

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
