---
name: unknown_workflow_generic_1509
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.875
common_nodes: [Float, RH_RhartImageG2TextToImage, RTXVideoSuperResolution, SaveImage, Text]
problems: []
missing: []
members: [图片生成/文生图/地表最强-全能图片G-Image-2-文生图-高清直出-0.1元_次_2066174217036582914.json, 图片生成/文生图/地表最强-全能图片G2-GP-T-Image-2-文生图-0.1元_次_2047337678131175426.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1509

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/地表最强-全能图片G-Image-2-文生图-高清直出-0.1元_次_2066174217036582914.json、图片生成/文生图/地表最强-全能图片G2-GP-T-Image-2-文生图-0.1元_次_2047337678131175426.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `Float`
- `RH_RhartImageG2TextToImage`
- `RTXVideoSuperResolution`
- `SaveImage`
- `Text`

**可变部分**（部分 workflow 才有）：
- `FlashVSRNode` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
