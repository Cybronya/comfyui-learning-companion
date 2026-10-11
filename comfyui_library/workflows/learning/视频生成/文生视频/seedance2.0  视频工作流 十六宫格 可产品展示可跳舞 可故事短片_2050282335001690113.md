---
key: 视频生成/文生视频/seedance2.0  视频工作流 十六宫格 可产品展示可跳舞 可故事短片_2050282335001690113.json
name: seedance2.0  视频工作流 十六宫格 可产品展示可跳舞 可故事短片_2050282335001690113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/seedance2.0  视频工作流 十六宫格 可产品展示可跳舞 可故事短片_2050282335001690113.json
hash: b561ca02c25c9f8f
coverage: 0.636364
learned_at: 2026-10-11 19:49:44
nodes: [LoadImage, LoadImage, RH_RhartImageG2ImageToImage, LoadImage, LoadImage, CR Text, easy imageSave, Preview from image [Crystools], RH_BytedanceSeedance20GlobalMultimodalVideo, CR Text, SaveVideo]
patterns: []
missing: [CR Text, CR Text, Preview from image [Crystools], easy imageSave]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Preview from image [Crystools]` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSave` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/seedance2.0  视频工作流 十六宫格 可产品展示可跳舞 可故事短片_2050282335001690113.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/seedance2.0  视频工作流 十六宫格 可产品展示可跳舞 可故事短片_2050282335001690113.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（11 个）：
- `LoadImage`
- `LoadImage`
- `RH_RhartImageG2ImageToImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `easy imageSave`
- `Preview from image [Crystools]`
- `RH_BytedanceSeedance20GlobalMultimodalVideo`
- `CR Text`
- `SaveVideo`

## 知识

覆盖率 **64%**（7/11）

**有卡**：`LoadImage`、`RH_RhartImageG2ImageToImage`、`RH_BytedanceSeedance20GlobalMultimodalVideo`、`SaveVideo`

**缺卡**（4）：`CR Text`、`CR Text`、`Preview from image [Crystools]`、`easy imageSave`

**用到的条目**：LoadImage、RH_BytedanceSeedance20GlobalMultimodalVideo、SaveVideo、RH_RhartImageG2ImageToImage、sd15-t2i-basic、sd15-t2i-lora、Seed、Text

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Preview from image [Crystools]` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSave` 仅有 SaveImage 的通用知识，没有该节点自己的说明
