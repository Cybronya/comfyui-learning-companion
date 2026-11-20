---
name: unknown_workflow_generic_489
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.821714
common_nodes: [CreateVideo, SaveVideo, VHS_LoadVideo]
problems: []
missing: []
members: [平台全量/视频去水印+超分工作流｜OCR+ProPainter+FlashVSR_2095203326672592897.json, 平台全量/视频去水印免蒙版工作流｜OCR字幕自动检测_2095175003745640450.json, 平台全量/视频补帧+超分工作流｜RIFE+FlashVSR_2095279683964325889.json, 视频生成/图生视频/AI丝滑慢动作-RIFE慢放工作流_2094993897243107330.json, 视频生成/图生视频/FlashVSR视频超分工作流_2094999239066738689.json, 视频生成/图生视频/视频补帧到60帧-RIFE工作流_2094993862648492034.json, 视频生成/文生视频/视频去水印+超分工作流｜OCR+ProPainter+FlashVSR_2098339836649369602.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_489

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/视频去水印+超分工作流｜OCR+ProPainter+FlashVSR_2095203326672592897.json、平台全量/视频去水印免蒙版工作流｜OCR字幕自动检测_2095175003745640450.json、平台全量/视频补帧+超分工作流｜RIFE+FlashVSR_2095279683964325889.json、视频生成/图生视频/AI丝滑慢动作-RIFE慢放工作流_2094993897243107330.json、视频生成/图生视频/FlashVSR视频超分工作流_2094999239066738689.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `CreateVideo`
- `SaveVideo`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `GetVideoComponents` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `Video Slice` —— 6/7 个有
- `FlashVSRNode` —— 4/7 个有
- `FL_RIFE` —— 3/7 个有
- `SubtitleDetectorRapidOCR` —— 3/7 个有
- `SubtitleEraserProPainter` —— 3/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
