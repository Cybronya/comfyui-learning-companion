---
key: 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库QwenRapidAIO_2026534890396721154.json
name: SeeDance 2.0AI短剧漫剧专用超真实感资产道具库QwenRapidAIO_2026534890396721154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库QwenRapidAIO_2026534890396721154.json
hash: f02dd215f61095db
coverage: 0.916667
learned_at: 2026-10-19 22:29:54
nodes: [SaveImage, WujiSampler, WujiCleaner, WujiUpscaler, CR Text, RHHiddenNodes, easy showAnything, CheckpointLoaderSimple, ModelSamplingAuraFlow, LoraLoaderModelOnly, LoraLoaderModelOnly, WujiSuperEditor]
patterns: []
missing: []
parameters: {"checkpoint": "WuJi_Qwen2511-AIONSFW聚合版_2603.safetensors"}
---

# 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库QwenRapidAIO_2026534890396721154.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库QwenRapidAIO_2026534890396721154.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（12 个）：
- `SaveImage`
- `WujiSampler` ★核心
- `WujiCleaner`
- `WujiUpscaler`
- `CR Text`
- `RHHiddenNodes`
- `easy showAnything`
- `CheckpointLoaderSimple` ★核心
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WujiSuperEditor`

## 关键参数

- `checkpoint` = `WuJi_Qwen2511-AIONSFW聚合版_2603.safetensors`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`SaveImage`、`WujiSampler`、`WujiCleaner`、`WujiUpscaler`、`CR Text`、`RHHiddenNodes`、`CheckpointLoaderSimple`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`WujiSuperEditor`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、WujiSampler、WujiUpscaler、SaveImage、ModelSamplingAuraFlow、RHHiddenNodes、WujiCleaner
