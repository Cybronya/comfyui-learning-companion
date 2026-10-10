---
key: 视频生成/文生视频/Kandinsky 5.0文生视频_1999010879624634370.json
name: Kandinsky 5.0文生视频_1999010879624634370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Kandinsky 5.0文生视频_1999010879624634370.json
hash: 9c515a7befdfc15e
coverage: 1
learned_at: 2026-10-11 02:57:36
nodes: [CLIPTextEncode, CLIPTextEncode, UNETLoader, VAELoader, DualCLIPLoader, KSampler, VAEDecode, Kandinsky5ImageToVideo, ModelSamplingSD3, CreateVideo, SaveVideo]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 41187461029047, "steps": 50}
---

# 视频生成/文生视频/Kandinsky 5.0文生视频_1999010879624634370.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Kandinsky 5.0文生视频_1999010879624634370.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Kandinsky5ImageToVideo`
- `ModelSamplingSD3`
- `CreateVideo`
- `SaveVideo`

## 关键参数

- `seed` = `41187461029047`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`CLIPTextEncode`、`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`KSampler`、`VAEDecode`、`Kandinsky5ImageToVideo`、`ModelSamplingSD3`、`CreateVideo`、`SaveVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、UNETLoader、SaveVideo、CreateVideo、DualCLIPLoader
