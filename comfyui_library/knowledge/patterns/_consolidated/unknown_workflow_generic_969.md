---
name: unknown_workflow_generic_969
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.83925
common_nodes: [BBoxesToSAM2, DownloadAndLoadQwenModel, DownloadAndLoadSAM2Model, LayerMask: LoadSAM2Model, LayerMask: SAM2UltraV2, LoadImage, MaskToImage, PreviewImage, QwenVLDetection, Sam2Segmentation, SaveImage, easy showAnything]
problems: []
missing: []
members: [平台全量/Qwen2.5-VL 最强精准智能遮罩_1935163347505455105.json, 平台全量/精准遮罩识别神器-QwenVLDetection_1934079838322122754.json, 平台全量/精准遮罩识别神器-QwenVLDetection_1934241970233503745.json, 平台全量/调取api-0606-万物擦除_1934210369529278465.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_969

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Qwen2.5-VL 最强精准智能遮罩_1935163347505455105.json、平台全量/精准遮罩识别神器-QwenVLDetection_1934079838322122754.json、平台全量/精准遮罩识别神器-QwenVLDetection_1934241970233503745.json、平台全量/调取api-0606-万物擦除_1934210369529278465.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `BBoxesToSAM2`
- `DownloadAndLoadQwenModel`
- `DownloadAndLoadSAM2Model`
- `LayerMask: LoadSAM2Model`
- `LayerMask: SAM2UltraV2`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `QwenVLDetection`
- `Sam2Segmentation`
- `SaveImage`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 3/4 个有
- `Text Multiline` —— 2/4 个有
- `EmptyImage` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `TextInput_` —— 1/4 个有
- `preview_mask` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
