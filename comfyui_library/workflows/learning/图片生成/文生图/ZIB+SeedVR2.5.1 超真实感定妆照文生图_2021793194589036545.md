---
key: 图片生成/文生图/ZIB+SeedVR2.5.1 超真实感定妆照文生图_2021793194589036545.json
name: ZIB+SeedVR2.5.1 超真实感定妆照文生图_2021793194589036545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ZIB+SeedVR2.5.1 超真实感定妆照文生图_2021793194589036545.json
hash: 7e320220247dd090
coverage: 0.736842
learned_at: 2026-10-19 22:30:08
nodes: [RHHiddenNodes, ShowText|pysssss, WujiUpscaler, SaveImage, WujiSampler, Note, WujiQwenEditor, CLIPLoader, UNETLoader, LoraLoaderModelOnly, VAELoader, WujiQwenEditor, Any Switch (rgthree), WujiSampler, VAELoader, CLIPLoader, UNETLoader, Fast Groups Muter (rgthree), PrimitiveStringMultiline]
patterns: []
missing: []
---

# 图片生成/文生图/ZIB+SeedVR2.5.1 超真实感定妆照文生图_2021793194589036545.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ZIB+SeedVR2.5.1 超真实感定妆照文生图_2021793194589036545.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（19 个）：
- `RHHiddenNodes`
- `ShowText|pysssss`
- `WujiUpscaler`
- `SaveImage`
- `WujiSampler` ★核心
- `Note`
- `WujiQwenEditor`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `WujiQwenEditor`
- `Any Switch (rgthree)`
- `WujiSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `Fast Groups Muter (rgthree)`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`RHHiddenNodes`、`WujiUpscaler`、`SaveImage`、`WujiSampler`、`WujiQwenEditor`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、WujiSampler、WujiUpscaler、SaveImage、RHHiddenNodes
