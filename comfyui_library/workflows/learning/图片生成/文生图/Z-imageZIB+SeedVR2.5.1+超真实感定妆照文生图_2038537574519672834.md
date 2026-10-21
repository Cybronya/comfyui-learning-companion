---
key: 图片生成/文生图/Z-imageZIB+SeedVR2.5.1+超真实感定妆照文生图_2038537574519672834.json
name: Z-imageZIB+SeedVR2.5.1+超真实感定妆照文生图_2038537574519672834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-imageZIB+SeedVR2.5.1+超真实感定妆照文生图_2038537574519672834.json
hash: ced51cb533272cf4
coverage: 0.777778
learned_at: 2026-10-21 02:56:17
nodes: [WujiSampler, WujiCleaner, WujiUpscaler, CheckpointLoaderSimple, WujiEditor, RHHiddenNodes, ShowText|pysssss, SaveImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"checkpoint": "WuJi_Z-image-base多风格2603_.safetensors"}
---

# 图片生成/文生图/Z-imageZIB+SeedVR2.5.1+超真实感定妆照文生图_2038537574519672834.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-imageZIB+SeedVR2.5.1+超真实感定妆照文生图_2038537574519672834.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（9 个）：
- `WujiSampler` ★核心
- `WujiCleaner`
- `WujiUpscaler`
- `CheckpointLoaderSimple` ★核心
- `WujiEditor`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `SaveImage`
- `PrimitiveStringMultiline`

## 关键参数

- `checkpoint` = `WuJi_Z-image-base多风格2603_.safetensors`

## 知识

覆盖率 **78%**（7/9）

**有卡**：`WujiSampler`、`WujiCleaner`、`WujiUpscaler`、`CheckpointLoaderSimple`、`WujiEditor`、`RHHiddenNodes`、`SaveImage`

**用到的条目**：CheckpointLoaderSimple、WujiSampler、WujiUpscaler、SaveImage、RHHiddenNodes、WujiCleaner、WujiEditor、sd15-t2i-basic
