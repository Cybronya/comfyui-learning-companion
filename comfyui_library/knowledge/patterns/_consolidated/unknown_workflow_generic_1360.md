---
name: unknown_workflow_generic_1360
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.769
common_nodes: [Display Any (rgthree), FluxKontextImageScale, ImageStitch, ImpactSwitch, LoadImage, RH_LLMAPI_NODE, SaveImage, Text Multiline, easy int]
problems: []
missing: []
members: [图片生成/图生图/即梦4图像编辑模型单图版_1970755117802790914.json, 图片生成/图生图/谷歌全能图片V1最强一致性模型单图编辑版_1961616752289452033.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1360

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/即梦4图像编辑模型单图版_1970755117802790914.json、图片生成/图生图/谷歌全能图片V1最强一致性模型单图编辑版_1961616752289452033.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `Display Any (rgthree)`
- `FluxKontextImageScale`
- `ImageStitch`
- `ImpactSwitch`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `Text Multiline`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `RH_Jimeng4_Image2Image` —— 1/2 个有
- `RH_Nano_Banana_Image2Image` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
