---
name: unknown_workflow_generic_1965
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.95
common_nodes: [BBoxesToSAM2, DownloadAndLoadQwenModel, LayerMask: LoadSAM2Model, LayerMask: SAM2UltraV2, LoadImage, QwenVLDetection, SaveImage]
problems: []
missing: []
members: [平台全量/新手-基础工作中流-精准识别_1951304546226262017.json, 平台全量/自定义抠图_1950093475310166017.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1965

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/新手-基础工作中流-精准识别_1951304546226262017.json、平台全量/自定义抠图_1950093475310166017.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `BBoxesToSAM2`
- `DownloadAndLoadQwenModel`
- `LayerMask: LoadSAM2Model`
- `LayerMask: SAM2UltraV2`
- `LoadImage`
- `QwenVLDetection`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerMask: MaskPreview` —— 1/2 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/2 个有
- `SDVN Translate` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
