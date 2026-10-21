---
key: 图片生成/文生图/动漫短剧Ai短剧人设图生成工作流（Z-image红潮ZIB+SeedVR2.5.1 放大）_2025833136650723329.json
name: 动漫短剧Ai短剧人设图生成工作流（Z-image红潮ZIB+SeedVR2.5.1 放大）_2025833136650723329
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/动漫短剧Ai短剧人设图生成工作流（Z-image红潮ZIB+SeedVR2.5.1 放大）_2025833136650723329.json
hash: 330dc4a42dc7f906
coverage: 0.882353
learned_at: 2026-10-19 22:30:27
nodes: [CLIPLoader, VAELoader, WujiQwenEditor, UNETLoader, WujiSampler, Note, SaveImage, easy promptConcat, easy anythingIndexSwitch, RH_LLMAPI_NODE, RH_LLMAPI_NODE, CR Text, CR Text, ShowText|pysssss, CR Text, WujiUpscaler, PresetTextSelector]
patterns: []
missing: []
---

# 图片生成/文生图/动漫短剧Ai短剧人设图生成工作流（Z-image红潮ZIB+SeedVR2.5.1 放大）_2025833136650723329.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/动漫短剧Ai短剧人设图生成工作流（Z-image红潮ZIB+SeedVR2.5.1 放大）_2025833136650723329.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `VAELoader`
- `WujiQwenEditor`
- `UNETLoader` ★核心
- `WujiSampler` ★核心
- `Note`
- `SaveImage`
- `easy promptConcat`
- `easy anythingIndexSwitch`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `CR Text`
- `CR Text`
- `ShowText|pysssss`
- `CR Text`
- `WujiUpscaler`
- `PresetTextSelector`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`CLIPLoader`、`VAELoader`、`WujiQwenEditor`、`UNETLoader`、`WujiSampler`、`SaveImage`、`easy promptConcat`、`easy anythingIndexSwitch`、`RH_LLMAPI_NODE`、`CR Text`、`WujiUpscaler`、`PresetTextSelector`

**用到的条目**：VAELoader、CLIPLoader、UNETLoader、WujiSampler、WujiUpscaler、easy promptConcat、SaveImage、RH_LLMAPI_NODE
