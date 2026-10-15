---
key: 视频生成/文生视频/HunyuanVideo 1.5 720P 20步优化版文生视频_1992813591025831937.json
name: HunyuanVideo 1.5 720P 20步优化版文生视频_1992813591025831937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/HunyuanVideo 1.5 720P 20步优化版文生视频_1992813591025831937.json
hash: e1f8fff18a630922
coverage: 0.863636
learned_at: 2026-10-15 22:44:28
nodes: [DualCLIPLoader, VAELoader, EasyCache, CLIPTextEncode, Note, Note, EmptyHunyuanVideo15Latent, UNETLoader, MarkdownNote, BasicScheduler, RandomNoise, KSamplerSelect, CFGGuider, SaveVideo, SamplerCustomAdvanced, CreateVideo, VAEDecodeTiled, VAEDecode, ModelSamplingSD3, CLIPTextEncode, JWInteger, JWInteger]
patterns: []
missing: []
---

# 视频生成/文生视频/HunyuanVideo 1.5 720P 20步优化版文生视频_1992813591025831937.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/HunyuanVideo 1.5 720P 20步优化版文生视频_1992813591025831937.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `DualCLIPLoader`
- `VAELoader`
- `EasyCache`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `EmptyHunyuanVideo15Latent`
- `UNETLoader` ★核心
- `MarkdownNote`
- `BasicScheduler`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SaveVideo`
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `JWInteger`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`DualCLIPLoader`、`VAELoader`、`EasyCache`、`CLIPTextEncode`、`EmptyHunyuanVideo15Latent`、`UNETLoader`、`BasicScheduler`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`SaveVideo`、`SamplerCustomAdvanced`、`CreateVideo`、`VAEDecodeTiled`、`VAEDecode`、`ModelSamplingSD3`、`JWInteger`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled
