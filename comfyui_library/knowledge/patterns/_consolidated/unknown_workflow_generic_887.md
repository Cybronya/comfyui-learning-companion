---
name: unknown_workflow_generic_887
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.68
common_nodes: [DF_Text_Box, Fast Groups Muter (rgthree), LoadAudio, LoadImage, PreviewAny, PrimitiveBoolean, RH_LLMAPI_NODE, RH_Translator, SaveVideo, ShowText|pysssss, TextCombinerTwo, VHS_LoadVideoFFmpeg, WhisperSTT, easy ifElse, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1991792893413388289.json, 视频生成/图生视频/2000383536815370241.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_887

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1991792893413388289.json、视频生成/图生视频/2000383536815370241.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `DF_Text_Box`
- `Fast Groups Muter (rgthree)`
- `LoadAudio`
- `LoadImage`
- `PreviewAny`
- `PrimitiveBoolean`
- `RH_LLMAPI_NODE`
- `RH_Translator`
- `SaveVideo`
- `ShowText|pysssss`
- `TextCombinerTwo`
- `VHS_LoadVideoFFmpeg`
- `WhisperSTT`
- `easy ifElse`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_Sora2_I2V` —— 1/2 个有
- `RH_Sora2_I2V_Batch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
