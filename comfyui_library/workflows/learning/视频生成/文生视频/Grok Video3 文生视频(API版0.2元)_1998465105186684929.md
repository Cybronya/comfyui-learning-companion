---
key: 视频生成/文生视频/Grok Video3 文生视频(API版0.2元)_1998465105186684929.json
name: Grok Video3 文生视频(API版0.2元)_1998465105186684929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Grok Video3 文生视频(API版0.2元)_1998465105186684929.json
hash: 42b93803910e19f8
coverage: 0.857143
learned_at: 2026-10-11 02:57:35
nodes: [RH_Grok_Video3, GetVideoComponents, JWImageBatchCount, ImageFromBatch+, SaveImage, SaveVideo, LoadImage]
patterns: []
missing: [ImageFromBatch+]
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Grok Video3 文生视频(API版0.2元)_1998465105186684929.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Grok Video3 文生视频(API版0.2元)_1998465105186684929.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（7 个）：
- `RH_Grok_Video3`
- `GetVideoComponents`
- `JWImageBatchCount`
- `ImageFromBatch+`
- `SaveImage`
- `SaveVideo`
- `LoadImage`

## 知识

覆盖率 **86%**（6/7）

**有卡**：`RH_Grok_Video3`、`GetVideoComponents`、`JWImageBatchCount`、`SaveImage`、`SaveVideo`、`LoadImage`

**缺卡**（1）：`ImageFromBatch+`

**用到的条目**：LoadImage、SaveImage、SaveVideo、GetVideoComponents、JWImageBatchCount、RH_Grok_Video3、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
