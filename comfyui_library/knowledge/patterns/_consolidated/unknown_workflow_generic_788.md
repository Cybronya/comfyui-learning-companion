---
name: unknown_workflow_generic_788
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8805
common_nodes: [LoadImage, MuyeTextEditOutput, PreviewAny, PreviewImage, RH_LLMAPI_Pro_Node, RH_Nano_Banana2_Image2Image, SaveImage, Text Multiline, easy saveText, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/一键成片嘎嘎地（提示词+图片）_2015786171237928962.json, 视频生成/文生视频/s2一键出视频（10并发）_2013964208718749697.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_788

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/一键成片嘎嘎地（提示词+图片）_2015786171237928962.json、视频生成/文生视频/s2一键出视频（10并发）_2013964208718749697.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `MuyeTextEditOutput`
- `PreviewAny`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `Text Multiline`
- `easy saveText`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image_Batch` —— 1/2 个有
- `RH_Sora2_I2V_Batch` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `SaveVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
