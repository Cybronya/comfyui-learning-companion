---
name: unknown_workflow_generic_1311
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8285
common_nodes: [AudioSeparation, Label (rgthree), LoadAudio, LoadImage, LoadVideo, MultiTextConcatenate, PreviewAudio, PrimitiveBoolean, RH_LLMAPI_Pro_Node, RH_RhartVideoSparkvideo20MiniMultimodalVideo, SaveVideoNode, Text, easy getAudioFromVideo, easy ifElse, easy saveText, easy showAnything, 忽略多组孤海]
problems: []
missing: []
members: [图片生成/反推提示词/【定制专用】爆款视频一键复刻，支持自定义修改提示词和背景配音_2096889341128822785.json, 图片生成/反推提示词/【定制工作流】爆款视频复刻支持自定义修改提示词和背景音色_2097268725526392833.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1311

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/【定制专用】爆款视频一键复刻，支持自定义修改提示词和背景配音_2096889341128822785.json、图片生成/反推提示词/【定制工作流】爆款视频复刻支持自定义修改提示词和背景音色_2097268725526392833.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioSeparation`
- `Label (rgthree)`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `MultiTextConcatenate`
- `PreviewAudio`
- `PrimitiveBoolean`
- `RH_LLMAPI_Pro_Node`
- `RH_RhartVideoSparkvideo20MiniMultimodalVideo`
- `SaveVideoNode`
- `Text`
- `easy getAudioFromVideo`
- `easy ifElse`
- `easy saveText`
- `easy showAnything`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `OmniVoiceVoiceCloneTTS` —— 1/2 个有
- `Qwen3ASRLoader` —— 1/2 个有
- `Qwen3ASRTranscribe` —— 1/2 个有
- `RH_AlibabaWan30ReferenceToVideo` —— 1/2 个有
- `RH_GetAudioDuration` —— 1/2 个有
- `RH_RhartVideoSparkvideo20MultimodalVideo` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
