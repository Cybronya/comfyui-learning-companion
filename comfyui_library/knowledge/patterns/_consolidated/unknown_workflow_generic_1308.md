---
name: unknown_workflow_generic_1308
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.749
common_nodes: [CXH_DownloadAndLoadFlorence2Model, CXH_Florence2Run, FaceAnalysisModels, FaceBoundingBox, ImageResizeKJ, JoinStrings, PreviewImage, RHBatchImages:, RHUploadZip, SaveImage, ShowText|pysssss, String, ttN textOutput]
problems: []
missing: []
members: [图片生成/反推提示词/lora训练工具之三：炼丹图片批量打标工作流V2_1956208905728786433.json, 图片生成/反推提示词/lora训练工具之三：炼丹图片批量打标工作流_1954687992571031554.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1308

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/lora训练工具之三：炼丹图片批量打标工作流V2_1956208905728786433.json、图片生成/反推提示词/lora训练工具之三：炼丹图片批量打标工作流_1954687992571031554.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CXH_DownloadAndLoadFlorence2Model`
- `CXH_Florence2Run`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `ImageResizeKJ`
- `JoinStrings`
- `PreviewImage`
- `RHBatchImages:`
- `RHUploadZip`
- `SaveImage`
- `ShowText|pysssss`
- `String`
- `ttN textOutput`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
