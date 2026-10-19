---
name: unknown_workflow_video_91
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.95
common_nodes: [CR Text, FloatProcess, IndexTTSNode, LoadAudio, LoadFloatModels, LoadImage, SaveAudio, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1925755963368755201.json, 音频生成/音频生成/Index-TTS 1.5极速语音克隆数字人_1925542299747676161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_91

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1925755963368755201.json、音频生成/音频生成/Index-TTS 1.5极速语音克隆数字人_1925542299747676161.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `FloatProcess`
- `IndexTTSNode`
- `LoadAudio`
- `LoadFloatModels`
- `LoadImage`
- `SaveAudio`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
