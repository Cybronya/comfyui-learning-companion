---
key: 图片生成/文生图/Z-imageZIB+SeedVR2.5.1+超真实感定AI短剧定妆照文生图_2042067900999143426.json
name: Z-imageZIB+SeedVR2.5.1+超真实感定AI短剧定妆照文生图_2042067900999143426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-imageZIB+SeedVR2.5.1+超真实感定AI短剧定妆照文生图_2042067900999143426.json
hash: 17496748e1deb4f1
coverage: 0.727273
learned_at: 2026-10-21 02:56:17
nodes: [WujiCleaner, SaveImage, CheckpointLoaderSimple, WujiSampler, WujiEditor, WujiUpscaler, RHHiddenNodes, ShowText|pysssss, LoraLoaderModelOnly, Note, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"checkpoint": "WuJi_Z-image-base多风格2603_.safetensors"}
---

# 图片生成/文生图/Z-imageZIB+SeedVR2.5.1+超真实感定AI短剧定妆照文生图_2042067900999143426.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-imageZIB+SeedVR2.5.1+超真实感定AI短剧定妆照文生图_2042067900999143426.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（11 个）：
- `WujiCleaner`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `WujiSampler` ★核心
- `WujiEditor`
- `WujiUpscaler`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `PrimitiveStringMultiline`

## 关键参数

- `checkpoint` = `WuJi_Z-image-base多风格2603_.safetensors`

## 知识

覆盖率 **73%**（8/11）

**有卡**：`WujiCleaner`、`SaveImage`、`CheckpointLoaderSimple`、`WujiSampler`、`WujiEditor`、`WujiUpscaler`、`RHHiddenNodes`、`LoraLoaderModelOnly`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、WujiSampler、WujiUpscaler、SaveImage、RHHiddenNodes、WujiCleaner、WujiEditor
