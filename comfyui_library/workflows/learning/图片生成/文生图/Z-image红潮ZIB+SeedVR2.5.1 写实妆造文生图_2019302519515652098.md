---
key: 图片生成/文生图/Z-image红潮ZIB+SeedVR2.5.1 写实妆造文生图_2019302519515652098.json
name: Z-image红潮ZIB+SeedVR2.5.1 写实妆造文生图_2019302519515652098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image红潮ZIB+SeedVR2.5.1 写实妆造文生图_2019302519515652098.json
hash: 884a215252800736
coverage: 0.642857
learned_at: 2026-10-19 22:30:07
nodes: [RHHiddenNodes, ShowText|pysssss, Any Switch (rgthree), WujiUpscaler, WujiLoader, WujiSampler, WujiQwenEditor, Fast Groups Muter (rgthree), WujiSampler, WujiQwenEditor, WujiLoader, Note, PrimitiveStringMultiline, SaveImage]
patterns: []
missing: []
---

# 图片生成/文生图/Z-image红潮ZIB+SeedVR2.5.1 写实妆造文生图_2019302519515652098.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image红潮ZIB+SeedVR2.5.1 写实妆造文生图_2019302519515652098.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（14 个）：
- `RHHiddenNodes`
- `ShowText|pysssss`
- `Any Switch (rgthree)`
- `WujiUpscaler`
- `WujiLoader`
- `WujiSampler` ★核心
- `WujiQwenEditor`
- `Fast Groups Muter (rgthree)`
- `WujiSampler` ★核心
- `WujiQwenEditor`
- `WujiLoader`
- `Note`
- `PrimitiveStringMultiline`
- `SaveImage`

## 知识

覆盖率 **64%**（9/14）

**有卡**：`RHHiddenNodes`、`WujiUpscaler`、`WujiLoader`、`WujiSampler`、`WujiQwenEditor`、`SaveImage`

**用到的条目**：WujiSampler、WujiUpscaler、SaveImage、RHHiddenNodes、WujiLoader、WujiQwenEditor、sd15-t2i-basic、sd15-t2i-lora
