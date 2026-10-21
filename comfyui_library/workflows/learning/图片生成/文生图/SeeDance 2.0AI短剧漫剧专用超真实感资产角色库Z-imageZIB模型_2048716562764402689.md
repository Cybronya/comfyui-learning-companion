---
key: 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-imageZIB模型_2048716562764402689.json
name: SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-imageZIB模型_2048716562764402689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-imageZIB模型_2048716562764402689.json
hash: b827b159d7ddac54
coverage: 0.846154
learned_at: 2026-10-21 02:55:05
nodes: [CheckpointLoaderSimple, WujiSampler, WujiCleaner, WujiUpscaler, LoraLoaderModelOnly, LoraLoaderModelOnly, WujiEditor, WujiStyleSelector, RHHiddenNodes, ShowText|pysssss, CompressImages, SaveImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"checkpoint": "WuJi_Z-image-base多风格2603_.safetensors"}
---

# 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-imageZIB模型_2048716562764402689.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-imageZIB模型_2048716562764402689.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（13 个）：
- `CheckpointLoaderSimple` ★核心
- `WujiSampler` ★核心
- `WujiCleaner`
- `WujiUpscaler`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WujiEditor`
- `WujiStyleSelector`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `CompressImages`
- `SaveImage`
- `PrimitiveStringMultiline`

## 关键参数

- `checkpoint` = `WuJi_Z-image-base多风格2603_.safetensors`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`CheckpointLoaderSimple`、`WujiSampler`、`WujiCleaner`、`WujiUpscaler`、`LoraLoaderModelOnly`、`WujiEditor`、`WujiStyleSelector`、`RHHiddenNodes`、`CompressImages`、`SaveImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、WujiSampler、WujiStyleSelector、WujiUpscaler、SaveImage、RHHiddenNodes、WujiCleaner
