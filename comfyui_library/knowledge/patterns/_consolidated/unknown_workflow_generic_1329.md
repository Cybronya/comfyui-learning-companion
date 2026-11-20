---
name: unknown_workflow_generic_1329
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.889
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewAny, RH_LLMAPI_NODE, RH_Nano_Banana2_Image2Image, SaveImage, Text Multiline]
problems: []
missing: []
members: [图片生成/图生图/-全能图片V12pro全面升级！多图闪电编辑，效率革命！图像编辑、服装上身、迁移、人物一致性_1966392130149232641.json, 图片生成/图生图/bnnn_2004179169615462401.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1329

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/-全能图片V12pro全面升级！多图闪电编辑，效率革命！图像编辑、服装上身、迁移、人物一致性_1966392130149232641.json、图片生成/图生图/bnnn_2004179169615462401.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewAny`
- `RH_LLMAPI_NODE`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `Text Multiline`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
