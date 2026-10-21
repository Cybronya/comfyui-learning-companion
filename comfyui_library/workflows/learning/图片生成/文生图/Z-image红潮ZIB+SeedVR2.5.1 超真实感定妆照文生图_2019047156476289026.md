---
key: 图片生成/文生图/Z-image红潮ZIB+SeedVR2.5.1 超真实感定妆照文生图_2019047156476289026.json
name: Z-image红潮ZIB+SeedVR2.5.1 超真实感定妆照文生图_2019047156476289026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image红潮ZIB+SeedVR2.5.1 超真实感定妆照文生图_2019047156476289026.json
hash: 8bc0a51b894f5ed2
coverage: 0.642857
learned_at: 2026-10-19 22:30:08
nodes: [PrimitiveStringMultiline, RHHiddenNodes, ShowText|pysssss, Any Switch (rgthree), WujiUpscaler, SaveImage, WujiLoader, WujiSampler, WujiQwenEditor, Fast Groups Muter (rgthree), Note, WujiSampler, WujiQwenEditor, WujiLoader]
patterns: []
missing: []
---

# 图片生成/文生图/Z-image红潮ZIB+SeedVR2.5.1 超真实感定妆照文生图_2019047156476289026.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image红潮ZIB+SeedVR2.5.1 超真实感定妆照文生图_2019047156476289026.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（14 个）：
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `Any Switch (rgthree)`
- `WujiUpscaler`
- `SaveImage`
- `WujiLoader`
- `WujiSampler` ★核心
- `WujiQwenEditor`
- `Fast Groups Muter (rgthree)`
- `Note`
- `WujiSampler` ★核心
- `WujiQwenEditor`
- `WujiLoader`

## 知识

覆盖率 **64%**（9/14）

**有卡**：`RHHiddenNodes`、`WujiUpscaler`、`SaveImage`、`WujiLoader`、`WujiSampler`、`WujiQwenEditor`

**用到的条目**：WujiSampler、WujiUpscaler、SaveImage、RHHiddenNodes、WujiLoader、WujiQwenEditor、sd15-t2i-basic、sd15-t2i-lora
