---
key: 数字人/数字人/SeeDance 2.0AI短剧漫剧人物生成机_2026838938404528130.json
name: SeeDance 2.0AI短剧漫剧人物生成机_2026838938404528130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/SeeDance 2.0AI短剧漫剧人物生成机_2026838938404528130.json
hash: 039b8d93d011bc9f
coverage: 0.75
learned_at: 2026-10-26 01:57:20
nodes: [PrimitiveStringMultiline, VAELoader, CLIPLoader, UNETLoader, Note, SaveImage, WujiSampler, WujiCleaner, RHHiddenNodes, ShowText|pysssss, WujiQwenEditor, WujiUpscaler]
patterns: []
missing: []
---

# 数字人/数字人/SeeDance 2.0AI短剧漫剧人物生成机_2026838938404528130.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/SeeDance 2.0AI短剧漫剧人物生成机_2026838938404528130.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（12 个）：
- `PrimitiveStringMultiline`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `Note`
- `SaveImage`
- `WujiSampler` ★核心
- `WujiCleaner`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `WujiQwenEditor`
- `WujiUpscaler`

## 知识

覆盖率 **75%**（9/12）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`SaveImage`、`WujiSampler`、`WujiCleaner`、`RHHiddenNodes`、`WujiQwenEditor`、`WujiUpscaler`

**用到的条目**：VAELoader、CLIPLoader、UNETLoader、WujiSampler、WujiUpscaler、SaveImage、RHHiddenNodes、WujiCleaner
