---
name: unknown_workflow_generic_1394
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8
common_nodes: [LayerMask: SegmentAnythingUltra V2, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/抠图_2038543335949869057.json, 图片生成/图生图/语音分割抠图升级版本+SegmentAnything Ultra V2+全节点注释_2056029346262994945.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1394

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/抠图_2038543335949869057.json、图片生成/图生图/语音分割抠图升级版本+SegmentAnything Ultra V2+全节点注释_2056029346262994945.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `MuyeTextEditOutput` —— 1/2 个有
- `TransparentImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
