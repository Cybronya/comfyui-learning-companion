---
name: unknown_workflow_generic_1295
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8035
common_nodes: [AILab_MiniCPM_4_V, LayerUtility: PurgeVRAM, LoadImage, LoadVideo, SaveImage, ShellAgentPluginOutputText, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/MiniCpm 4.5视频反推打标神器_1962065895927562241.json, 视频生成/图生视频/MiniCpm V4.5视频反推-二创神器_1976505950364372994.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1295

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/MiniCpm 4.5视频反推打标神器_1962065895927562241.json、视频生成/图生视频/MiniCpm V4.5视频反推-二创神器_1976505950364372994.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_MiniCPM_4_V`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadVideo`
- `SaveImage`
- `ShellAgentPluginOutputText`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerMask: RemBgUltra` —— 1/2 个有
- `RH_Translator` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
