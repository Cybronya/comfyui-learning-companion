---
key: 视频生成/文生视频/HunyuanVideo 1.5 480P 8步LightX2V文生视频加速版V1_1992951299952099329.json
name: HunyuanVideo 1.5 480P 8步LightX2V文生视频加速版V1_1992951299952099329
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/HunyuanVideo 1.5 480P 8步LightX2V文生视频加速版V1_1992951299952099329.json
hash: 3a1728a2840d20e2
coverage: 0.869565
learned_at: 2026-10-11 02:57:35
nodes: [DualCLIPLoader, VAELoader, EasyCache, CLIPTextEncode, Note, Note, MarkdownNote, KSamplerSelect, SaveVideo, VAEDecodeTiled, VAEDecode, CLIPTextEncode, JWInteger, JWInteger, EmptyHunyuanVideo15Latent, CreateVideo, LoraLoaderModelOnly, SamplerCustomAdvanced, UNETLoader, CFGGuider, ModelSamplingSD3, BasicScheduler, RandomNoise]
patterns: []
missing: []
---

# 视频生成/文生视频/HunyuanVideo 1.5 480P 8步LightX2V文生视频加速版V1_1992951299952099329.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/HunyuanVideo 1.5 480P 8步LightX2V文生视频加速版V1_1992951299952099329.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（23 个）：
- `DualCLIPLoader`
- `VAELoader`
- `EasyCache`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `SaveVideo`
- `VAEDecodeTiled` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `JWInteger`
- `JWInteger`
- `EmptyHunyuanVideo15Latent`
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `CFGGuider`
- `ModelSamplingSD3`
- `BasicScheduler`
- `RandomNoise`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`DualCLIPLoader`、`VAELoader`、`EasyCache`、`CLIPTextEncode`、`KSamplerSelect`、`SaveVideo`、`VAEDecodeTiled`、`VAEDecode`、`JWInteger`、`EmptyHunyuanVideo15Latent`、`CreateVideo`、`LoraLoaderModelOnly`、`SamplerCustomAdvanced`、`UNETLoader`、`CFGGuider`、`ModelSamplingSD3`、`BasicScheduler`、`RandomNoise`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
