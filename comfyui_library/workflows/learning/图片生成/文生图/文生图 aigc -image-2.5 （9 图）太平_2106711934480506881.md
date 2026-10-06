---
key: 图片生成/文生图/文生图 aigc -image-2.5 （9 图）太平_2106711934480506881.json
name: 文生图 aigc -image-2.5 （9 图）太平_2106711934480506881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图 aigc -image-2.5 （9 图）太平_2106711934480506881.json
hash: 9392f5e1f1a74c97
coverage: 0.333333
learned_at: 2026-10-06 21:52:25
nodes: [SaveImage, RH_RhartImageG25SunburstTextToImage, CR Prompt Text]
patterns: []
missing: [RH_RhartImageG25SunburstTextToImage, CR Prompt Text]
discoveries: [次要节点 `RH_RhartImageG25SunburstTextToImage` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/文生图 aigc -image-2.5 （9 图）太平_2106711934480506881.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图 aigc -image-2.5 （9 图）太平_2106711934480506881.json`

## 结构

**生成流程**：Output → Other

**节点**（3 个）：
- `SaveImage`
- `RH_RhartImageG25SunburstTextToImage`
- `CR Prompt Text`

## 知识

覆盖率 **33%**（1/3）

**有卡**：`SaveImage`

**缺卡**（2）：`RH_RhartImageG25SunburstTextToImage`、`CR Prompt Text`

**用到的条目**：SaveImage、sd15-t2i-basic、sd15-t2i-lora、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 学习发现

- 次要节点 `RH_RhartImageG25SunburstTextToImage` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
