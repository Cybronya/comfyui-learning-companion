---
name: unknown_workflow_generic_1970
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.655
common_nodes: [CR Text Concatenate, Int, JjkText, LoadImage, RHHiddenNodes, RH_LLMAPI_Pro_Node, RH_RhartImageG2ImageToImage, RH_Utils, SaveImage, ShowAnything|Mie, TextInput_, easy showAnything, ttN concat]
problems: []
missing: []
members: [平台全量/电商带货视频 九宫格图，简单剧情 生成分镜提示词 适合 LTX2.3  全能视频S  SEEDANCE_2059312753956974594.json, 视频生成/图生视频/剧情电商带货  seedance mini 版本   1080p 0.88元_S  效果可以_2071176299367981057.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1970

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/电商带货视频 九宫格图，简单剧情 生成分镜提示词 适合 LTX2.3  全能视频S  SEEDANCE_2059312753956974594.json、视频生成/图生视频/剧情电商带货  seedance mini 版本   1080p 0.88元_S  效果可以_2071176299367981057.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text Concatenate`
- `Int`
- `JjkText`
- `LoadImage`
- `RHHiddenNodes`
- `RH_LLMAPI_Pro_Node`
- `RH_RhartImageG2ImageToImage`
- `RH_Utils`
- `SaveImage`
- `ShowAnything|Mie`
- `TextInput_`
- `easy showAnything`
- `ttN concat`

**可变部分**（部分 workflow 才有）：
- `ImageGridSplitter` —— 1/2 个有
- `ImageRGBChannel` —— 1/2 个有
- `LayerColor: Levels` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_RhartVideoSparkvideo20MiniImageToVideo` —— 1/2 个有
- `SaveVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
