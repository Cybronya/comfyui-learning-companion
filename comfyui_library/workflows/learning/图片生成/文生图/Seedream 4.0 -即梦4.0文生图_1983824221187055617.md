---
key: 图片生成/文生图/Seedream 4.0 -即梦4.0文生图_1983824221187055617.json
name: Seedream 4.0 -即梦4.0文生图_1983824221187055617.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Seedream 4.0 -即梦4.0文生图_1983824221187055617.json
hash: e6fda17393158bf9
coverage: 0.166667
learned_at: 2026-10-09 20:05:46
nodes: [SaveImage, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, InversionDemoLazyIndexSwitch, JjkText, RH_Jimeng4_Image2Image, SetNode, easy int, Note, CR Text Concatenate, GetNode, CR Text, ShowText|pysssss]
patterns: []
missing: [CR Text, CR Text Concatenate, easy int]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Seedream 4.0 -即梦4.0文生图_1983824221187055617.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1983824221187055617.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（18 个）：
- `SaveImage`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `InversionDemoLazyIndexSwitch`
- `JjkText`
- `RH_Jimeng4_Image2Image`
- `SetNode`
- `easy int`
- `Note`
- `CR Text Concatenate`
- `GetNode`
- `CR Text`
- `ShowText|pysssss`

## 知识

覆盖率 **17%**（3/18）

**有卡**：`SaveImage`、`InversionDemoLazyIndexSwitch`、`RH_Jimeng4_Image2Image`

**缺卡**（3）：`CR Text`、`CR Text Concatenate`、`easy int`

**用到的条目**：SaveImage、InversionDemoLazyIndexSwitch、RH_Jimeng4_Image2Image、sd15-t2i-basic、sd15-t2i-lora、Int、node、ShowText

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
