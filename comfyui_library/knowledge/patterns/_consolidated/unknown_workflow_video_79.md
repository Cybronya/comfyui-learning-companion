---
name: unknown_workflow_video_79
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5902
common_nodes: [GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), ImageBatchGet, ImageToMask, LayerUtility: LaMa, MaskToImage, PreviewImage, SAMModelLoader (segment anything), SetNode, VHS_DuplicateMasks, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/视频去水印-稳定高效版_1926653656307802114.json, 平台全量/视频去水印（全自动检测水印）_1939853209941020673.json, 平台全量/视频去水印（全自动）_1963978194095325186.json, 平台全量/视频自动祛除-固定文字水印、字幕、logo_2014336777544278017.json, 视频生成/图生视频/视频去水印（全自动）_1915249937083469825.json]
source: knowledge_consolidation
---

# unknown_workflow_video_79

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/视频去水印-稳定高效版_1926653656307802114.json、平台全量/视频去水印（全自动检测水印）_1939853209941020673.json、平台全量/视频去水印（全自动）_1963978194095325186.json、平台全量/视频自动祛除-固定文字水印、字幕、logo_2014336777544278017.json、视频生成/图生视频/视频去水印（全自动）_1915249937083469825.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 5 个 workflow 都包含：
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `ImageBatchGet`
- `ImageToMask`
- `LayerUtility: LaMa`
- `MaskToImage`
- `PreviewImage`
- `SAMModelLoader (segment anything)`
- `SetNode`
- `VHS_DuplicateMasks`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 4/5 个有
- `Bjornulf_ShowFloat` —— 2/5 个有
- `Bjornulf_ShowInt` —— 2/5 个有
- `CR Text` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
