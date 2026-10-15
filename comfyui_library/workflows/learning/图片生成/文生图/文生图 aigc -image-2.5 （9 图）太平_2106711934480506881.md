---
key: 图片生成/文生图/文生图 aigc -image-2.5 （9 图）太平_2106711934480506881.json
name: 文生图 aigc -image-2.5 （9 图）太平_2106711934480506881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图 aigc -image-2.5 （9 图）太平_2106711934480506881.json
hash: 9392f5e1f1a74c97
coverage: 0.666667
learned_at: 2026-10-10 20:59:46
nodes: [SaveImage, RH_RhartImageG25SunburstTextToImage, CR Prompt Text]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/文生图 aigc -image-2.5 （9 图）太平_2106711934480506881.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图 aigc -image-2.5 （9 图）太平_2106711934480506881.json`

## 结构

**节点**（3 个）：
- `SaveImage`
- `RH_RhartImageG25SunburstTextToImage`
- `CR Prompt Text`

## 知识

覆盖率 **67%**（2/3）

**有卡**：`SaveImage`、`RH_RhartImageG25SunburstTextToImage`

**缺卡**（1）：`CR Prompt Text`

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
