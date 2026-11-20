---
name: unknown_workflow_generic_1415
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7435
common_nodes: [BatchCount+, CR Text, ImageScale, PreviewAny, PreviewImage, RHExtractImage, RHUploadZip, RH_Captioner_Pro, SaveImage, easy batchAnything, easy forLoopEnd, easy forLoopStart]
problems: []
missing: []
members: [图片生成/图生图/midjourny异步循环批量自动化出图_2105211919916421122.json, 图片生成/图生图/异步循环批量生成带人物汽车美图_2108366577967132673.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1415

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/midjourny异步循环批量自动化出图_2105211919916421122.json、图片生成/图生图/异步循环批量生成带人物汽车美图_2108366577967132673.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `BatchCount+`
- `CR Text`
- `ImageScale`
- `PreviewAny`
- `PreviewImage`
- `RHExtractImage`
- `RHUploadZip`
- `RH_Captioner_Pro`
- `SaveImage`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `RH_RhartImageNProOfficialEdit` —— 1/2 个有
- `RH_YouchuanTextToImageV82Fast` —— 1/2 个有
- `RH_YouchuanTextToImageV82Turbo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
