---
name: unknown_workflow_generic_1352
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8945
common_nodes: [CR Text, RHHiddenNodes, RH_LLMAPI_NODE, RH_Nano_Banana_Image2Image, SaveImage, easy imageConcat, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/全能视频S-分镜头制作-图（以URL方式上传）生分镜头_1992902561994788866.json, 视频生成/图生视频/电商产品分镜制作，全能视频生成_2017177175027359745.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1352

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/全能视频S-分镜头制作-图（以URL方式上传）生分镜头_1992902561994788866.json、视频生成/图生视频/电商产品分镜制作，全能视频生成_2017177175027359745.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `RHHiddenNodes`
- `RH_LLMAPI_NODE`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`
- `easy imageConcat`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Light-Tool: LoadImageFromURL` —— 1/2 个有
- `LoadImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
