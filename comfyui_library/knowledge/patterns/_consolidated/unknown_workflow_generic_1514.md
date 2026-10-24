---
name: unknown_workflow_generic_1514
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.852
common_nodes: [If ANY execute A else B, Image Input Switch, JWString, LoadImageWithSwitch, PreviewImage, RH_Nano_Banana2_Image2Image, SaveImage, String To Combo JK, Text Concatenate, Text Multiline, image_url_download]
problems: []
missing: []
members: [图片生成/文生图/服装_姿态生成_2022492800905908226.json, 图片生成/文生图/造型设计-生成姿态_2022509586565042177.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1514

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/服装_姿态生成_2022492800905908226.json、图片生成/文生图/造型设计-生成姿态_2022509586565042177.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `If ANY execute A else B`
- `Image Input Switch`
- `JWString`
- `LoadImageWithSwitch`
- `PreviewImage`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `String To Combo JK`
- `Text Concatenate`
- `Text Multiline`
- `image_url_download`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
