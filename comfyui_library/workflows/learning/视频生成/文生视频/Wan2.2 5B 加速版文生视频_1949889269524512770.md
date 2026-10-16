---
key: 视频生成/文生视频/Wan2.2 5B 加速版文生视频_1949889269524512770.json
name: Wan2.2 5B 加速版文生视频_1949889269524512770.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1949889269524512770.json
hash: c4e7f5638c791c2d
coverage: 0.9375
learned_at: 2026-10-15 22:43:33
nodes: [CLIPTextEncode, KSampler, VAELoader, CLIPLoader, UNETLoader, CLIPTextEncode, ModelSamplingSD3, VAEDecode, PathchSageAttentionKJ, TeaCache, Note, Wan22ImageToVideoLatent, JWInteger, JWInteger, JWInteger, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 596270260278732, "steps": 30}
---

# 视频生成/文生视频/Wan2.2 5B 加速版文生视频_1949889269524512770.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1949889269524512770.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（16 个）：
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `TeaCache`
- `Note`
- `Wan22ImageToVideoLatent`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `596270260278732`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`CLIPTextEncode`、`KSampler`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`ModelSamplingSD3`、`VAEDecode`、`PathchSageAttentionKJ`、`TeaCache`、`Wan22ImageToVideoLatent`、`JWInteger`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、Wan22ImageToVideoLatent、ModelSamplingSD3
