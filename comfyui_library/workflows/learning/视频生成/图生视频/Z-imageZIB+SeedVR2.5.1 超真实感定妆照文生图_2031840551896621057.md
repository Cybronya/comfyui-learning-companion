---
key: 视频生成/图生视频/Z-imageZIB+SeedVR2.5.1 超真实感定妆照文生图_2031840551896621057.json
name: Z-imageZIB+SeedVR2.5.1 超真实感定妆照文生图_2031840551896621057.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2031840551896621057.json
hash: 475a2fab0e23c3ad
coverage: 0.75
learned_at: 2026-10-15 22:35:33
nodes: [VAELoader, WujiUpscaler, CLIPLoaderGGUF, WujiEditor, LoraLoaderModelOnly, Note, SaveImage, WujiSampler, UNETLoader, RHHiddenNodes, PrimitiveStringMultiline, ShowText|pysssss]
patterns: []
missing: []
---

# 视频生成/图生视频/Z-imageZIB+SeedVR2.5.1 超真实感定妆照文生图_2031840551896621057.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031840551896621057.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（12 个）：
- `VAELoader`
- `WujiUpscaler`
- `CLIPLoaderGGUF`
- `WujiEditor`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `SaveImage`
- `WujiSampler` ★核心
- `UNETLoader` ★核心
- `RHHiddenNodes`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`

## 知识

覆盖率 **75%**（9/12）

**有卡**：`VAELoader`、`WujiUpscaler`、`CLIPLoaderGGUF`、`WujiEditor`、`LoraLoaderModelOnly`、`SaveImage`、`WujiSampler`、`UNETLoader`、`RHHiddenNodes`

**用到的条目**：VAELoader、LoraLoaderModelOnly、UNETLoader、WujiSampler、WujiUpscaler、CLIPLoaderGGUF、ClipLoaderGGUF、ClipLoaderGGUF
