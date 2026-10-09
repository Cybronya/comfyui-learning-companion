---
key: 图片生成/文生图/wan2.2洗稿文生图_1985878501448396802.json
name: wan2.2洗稿文生图_1985878501448396802.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2洗稿文生图_1985878501448396802.json
hash: facd291d9dc2fd97
coverage: 0.904762
learned_at: 2026-10-09 20:13:11
nodes: [CLIPTextEncode, CLIPTextEncode, VAEDecode, VAELoader, ModelSamplingSD3, SamplerCustomAdvanced, RandomNoise, CFGGuider, BasicScheduler, KSamplerSelect, SamplerCustomAdvanced, DisableNoise, SplitSigmas, WanVideoNAG, SaveImage, EmptyHunyuanLatentVideo, Note, CLIPLoader, LoraLoaderModelOnly, Note, UNETLoader]
patterns: []
missing: []
---

# 图片生成/文生图/wan2.2洗稿文生图_1985878501448396802.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1985878501448396802.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（21 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `DisableNoise`
- `SplitSigmas`
- `WanVideoNAG`
- `SaveImage`
- `EmptyHunyuanLatentVideo`
- `Note`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `UNETLoader` ★核心

## 知识

覆盖率 **90%**（19/21）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`VAELoader`、`ModelSamplingSD3`、`SamplerCustomAdvanced`、`RandomNoise`、`CFGGuider`、`BasicScheduler`、`KSamplerSelect`、`DisableNoise`、`SplitSigmas`、`WanVideoNAG`、`SaveImage`、`EmptyHunyuanLatentVideo`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、CFGGuider、KSamplerSelect
