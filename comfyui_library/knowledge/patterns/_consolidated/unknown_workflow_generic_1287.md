---
name: unknown_workflow_generic_1287
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6865
common_nodes: [Joy_caption_two_advanced, Joy_caption_two_load, Joy_extra_options, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, SaveImage, ShowText|pysssss]
problems: []
missing: []
members: [图片生成/反推提示词/JoyCaption 3 图像反推_1993972081836621826.json, 图片生成/反推提示词/提示词反推集合_1991111614755635202.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1287

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/JoyCaption 3 图像反推_1993972081836621826.json、图片生成/反推提示词/提示词反推集合_1991111614755635202.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `Joy_caption_two_advanced`
- `Joy_caption_two_load`
- `Joy_extra_options`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `SaveImage`
- `ShowText|pysssss`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/2 个有
- `Florence2ModelLoader` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `JanusImageUnderstanding` —— 1/2 个有
- `JanusModelLoader` —— 1/2 个有
- `RH_Translator` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
