---
name: unknown_workflow_generic_1682
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8335
common_nodes: [HAIGC_LoadImagesFromZip, LoadImage, RunningHubRVCOneClickTrain, SaveImage, ShellAgentPluginOutputText, easy saveText]
problems: []
missing: []
members: [音频生成/音频生成/RVC 训练工作流（RH版）_2099755820421570562.json, 音频生成/音频生成/训练你的声音模型-用于翻唱一切歌曲_2101690271791673345.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1682

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/RVC 训练工作流（RH版）_2099755820421570562.json、音频生成/音频生成/训练你的声音模型-用于翻唱一切歌曲_2101690271791673345.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `HAIGC_LoadImagesFromZip`
- `LoadImage`
- `RunningHubRVCOneClickTrain`
- `SaveImage`
- `ShellAgentPluginOutputText`
- `easy saveText`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
