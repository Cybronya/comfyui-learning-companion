---
name: unknown_workflow_generic_1696
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.913
common_nodes: [AudioCrop, Bjornulf_AnythingToText, LoadAudio, MathExpression|pysssss, PreviewImage, SaveImage, SaveVideo, VHS_LoadVideoPath, VHS_SelectImages]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.5 Preview 图生视频，保存尾帧，可连续生成长视频_1971449141417164802.json, 视频生成/文生视频/Wan2.5 Preview 文生视频，保存尾帧，可连续生成长视频_1971617651434909698.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1696

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.5 Preview 图生视频，保存尾帧，可连续生成长视频_1971449141417164802.json、视频生成/文生视频/Wan2.5 Preview 文生视频，保存尾帧，可连续生成长视频_1971617651434909698.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `Bjornulf_AnythingToText`
- `LoadAudio`
- `MathExpression|pysssss`
- `PreviewImage`
- `SaveImage`
- `SaveVideo`
- `VHS_LoadVideoPath`
- `VHS_SelectImages`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `RH_Wan25_I2V` —— 1/2 个有
- `RH_Wan25_T2V` —— 1/2 个有
- `ShellAgentPluginInputText` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
