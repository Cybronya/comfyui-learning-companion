---
key: 图片生成/文生图/Z-image ZIB+SeedVR2.5.1+超真实感定妆照文生图_2018497861872259074.json
name: Z-image ZIB+SeedVR2.5.1+超真实感定妆照文生图_2018497861872259074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image ZIB+SeedVR2.5.1+超真实感定妆照文生图_2018497861872259074.json
hash: e9ef740e45c5a0fa
coverage: 0.642857
learned_at: 2026-10-19 22:30:02
nodes: [RHHiddenNodes, ShowText|pysssss, Any Switch (rgthree), WujiUpscaler, SaveImage, WujiLoader, WujiSampler, WujiQwenEditor, Fast Groups Muter (rgthree), WujiSampler, WujiQwenEditor, WujiLoader, Note, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 图片生成/文生图/Z-image ZIB+SeedVR2.5.1+超真实感定妆照文生图_2018497861872259074.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image ZIB+SeedVR2.5.1+超真实感定妆照文生图_2018497861872259074.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（14 个）：
- `RHHiddenNodes`
- `ShowText|pysssss`
- `Any Switch (rgthree)`
- `WujiUpscaler`
- `SaveImage`
- `WujiLoader`
- `WujiSampler` ★核心
- `WujiQwenEditor`
- `Fast Groups Muter (rgthree)`
- `WujiSampler` ★核心
- `WujiQwenEditor`
- `WujiLoader`
- `Note`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **64%**（9/14）

**有卡**：`RHHiddenNodes`、`WujiUpscaler`、`SaveImage`、`WujiLoader`、`WujiSampler`、`WujiQwenEditor`

**用到的条目**：WujiSampler、WujiUpscaler、SaveImage、RHHiddenNodes、WujiLoader、WujiQwenEditor、sd15-t2i-basic、sd15-t2i-lora
