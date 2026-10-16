---
key: 视频生成/文生视频/wan2.2-TI2V-5B-文生视频_1950094689354563586.json
name: wan2.2-TI2V-5B-文生视频_1950094689354563586.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950094689354563586.json
hash: 474fea846b67593c
coverage: 0.9375
learned_at: 2026-10-15 22:43:34
nodes: [UNETLoader, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, VAELoader, VAEDecodeTiled, CreateVideo, CLIPLoader, KSampler, Wan22ImageToVideoLatent, DF_Integer, MathExpression|pysssss, JjkText, DF_Integer, DF_Integer, SaveVideo]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 787967878170183, "steps": 20}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/wan2.2-TI2V-5B-文生视频_1950094689354563586.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950094689354563586.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `CLIPLoader`
- `KSampler` ★核心
- `Wan22ImageToVideoLatent`
- `DF_Integer`
- `MathExpression|pysssss`
- `JjkText`
- `DF_Integer`
- `DF_Integer`
- `SaveVideo`

## 关键参数

- `seed` = `787967878170183`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`UNETLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAELoader`、`VAEDecodeTiled`、`CreateVideo`、`CLIPLoader`、`KSampler`、`Wan22ImageToVideoLatent`、`DF_Integer`、`MathExpression|pysssss`、`SaveVideo`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、VAEDecodeTiled、Wan22ImageToVideoLatent、SaveVideo

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
