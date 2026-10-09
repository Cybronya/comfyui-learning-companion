---
key: 图片生成/文生图/SPARK.Chroma_preview 反推文生图_1984856656842473473.json
name: SPARK.Chroma_preview 反推文生图_1984856656842473473.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SPARK.Chroma_preview 反推文生图_1984856656842473473.json
hash: 23b278d5848cceb1
coverage: 1
learned_at: 2026-10-09 20:05:47
nodes: [CLIPLoader, VAELoader, T5TokenizerOptions, CFGGuider, KSamplerSelect, CLIPTextEncode, CLIPTextEncode, VAEDecode, BasicScheduler, SamplerCustomAdvanced, SaveImage, RandomNoise, UNETLoader, EmptySD3LatentImage, AILab_QwenVL, LoadImage]
patterns: []
missing: []
---

# 图片生成/文生图/SPARK.Chroma_preview 反推文生图_1984856656842473473.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1984856656842473473.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `VAELoader`
- `T5TokenizerOptions`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `RandomNoise`
- `UNETLoader` ★核心
- `EmptySD3LatentImage`
- `AILab_QwenVL`
- `LoadImage`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`CLIPLoader`、`VAELoader`、`T5TokenizerOptions`、`CFGGuider`、`KSamplerSelect`、`CLIPTextEncode`、`VAEDecode`、`BasicScheduler`、`SamplerCustomAdvanced`、`SaveImage`、`RandomNoise`、`UNETLoader`、`EmptySD3LatentImage`、`AILab_QwenVL`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
