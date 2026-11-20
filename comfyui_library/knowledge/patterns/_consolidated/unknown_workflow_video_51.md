---
name: unknown_workflow_video_51
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.955333
common_nodes: [FlashVSRNode, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/FlashVSR V1.1模糊视频高清放大_2018240987654529025.json, 平台全量/FlashVSR 视频高清放大 极速低显存版_1986991085123776514.json, 平台全量/FlashVSR-自用 1.1_1986708239440097281.json, 平台全量/FlashVSR模糊视频高清处理工作流_1981562253055016962.json, 平台全量/FlashVSR模糊视频高清放大_1980654731339153410.json, 视频生成/图生视频/【阡陌】FlashVSR视频超分辨率高清修复放大_1983077919813726210.json]
source: knowledge_consolidation
---

# unknown_workflow_video_51

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/FlashVSR V1.1模糊视频高清放大_2018240987654529025.json、平台全量/FlashVSR 视频高清放大 极速低显存版_1986991085123776514.json、平台全量/FlashVSR-自用 1.1_1986708239440097281.json、平台全量/FlashVSR模糊视频高清处理工作流_1981562253055016962.json、平台全量/FlashVSR模糊视频高清放大_1980654731339153410.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `FlashVSRNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `Float` —— 2/6 个有
- `LoadImage` —— 2/6 个有
- `VHS_VideoInfoLoaded` —— 2/6 个有
- `easy imageConcat` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
