---
key: 图片生成/图生图/nomi instant character test_1914961987896340482.json
name: nomi instant character test_1914961987896340482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/nomi instant character test_1914961987896340482.json
hash: e78dfb839588eee1
coverage: 0.909091
learned_at: 2026-10-23 11:41:10
nodes: [JWInteger, JWInteger, InstantCharacterLoadModel, InvertMask, PreviewImage, LayerUtility: ImageRemoveAlpha, SaveImage, InstantCharacterGenerateWithStyleLora, CR Prompt Text, ImageRemoveAlpha+, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/nomi instant character test_1914961987896340482.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/nomi instant character test_1914961987896340482.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（11 个）：
- `JWInteger`
- `JWInteger`
- `InstantCharacterLoadModel`
- `InvertMask`
- `PreviewImage`
- `LayerUtility: ImageRemoveAlpha`
- `SaveImage`
- `InstantCharacterGenerateWithStyleLora`
- `CR Prompt Text`
- `ImageRemoveAlpha+`
- `LoadImage`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`JWInteger`、`InstantCharacterLoadModel`、`InvertMask`、`LayerUtility: ImageRemoveAlpha`、`SaveImage`、`InstantCharacterGenerateWithStyleLora`、`CR Prompt Text`、`ImageRemoveAlpha+`、`LoadImage`

**用到的条目**：LoadImage、InstantCharacterGenerateWithStyleLora、CR Prompt Text、SaveImage、InvertMask、JWInteger、InstantCharacterLoadModel、ImageRemoveAlpha+
