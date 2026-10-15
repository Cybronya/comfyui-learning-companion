---
key: 图片生成/文生图/wan2.2洗稿文生图_1985878501448396802.json
name: wan2.2洗稿文生图_1985878501448396802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2洗稿文生图_1985878501448396802.json
hash: facd291d9dc2fd97
coverage: 0.904762
learned_at: 2026-10-10 20:59:27
nodes: [CLIPTextEncode, CLIPTextEncode, VAEDecode, VAELoader, ModelSamplingSD3, SamplerCustomAdvanced, RandomNoise, CFGGuider, BasicScheduler, KSamplerSelect, SamplerCustomAdvanced, DisableNoise, SplitSigmas, WanVideoNAG, SaveImage, EmptyHunyuanLatentVideo, Note, CLIPLoader, LoraLoaderModelOnly, Note, UNETLoader]
patterns: []
missing: []
---

# 图片生成/文生图/wan2.2洗稿文生图_1985878501448396802.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2洗稿文生图_1985878501448396802.json`

## 结构

**节点**（21 个）：
- `CLIPTextEncode`
- `CLIPTextEncode`
- `VAEDecode`
- `VAELoader`
- `ModelSamplingSD3`
- `SamplerCustomAdvanced`
- `RandomNoise`
- `CFGGuider`
- `BasicScheduler`
- `KSamplerSelect`
- `SamplerCustomAdvanced`
- `DisableNoise`
- `SplitSigmas`
- `WanVideoNAG`
- `SaveImage`
- `EmptyHunyuanLatentVideo`
- `Note`
- `CLIPLoader`
- `LoraLoaderModelOnly`
- `Note`
- `UNETLoader`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`VAELoader`、`ModelSamplingSD3`、`SamplerCustomAdvanced`、`RandomNoise`、`CFGGuider`、`BasicScheduler`、`KSamplerSelect`、`DisableNoise`、`SplitSigmas`、`WanVideoNAG`、`SaveImage`、`EmptyHunyuanLatentVideo`、`Note`、`CLIPLoader`、`LoraLoaderModelOnly`
