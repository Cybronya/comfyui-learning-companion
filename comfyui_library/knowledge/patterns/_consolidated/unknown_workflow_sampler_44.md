---
name: unknown_workflow_sampler_44
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.75
common_nodes: [LoadAudio, NTCosyVoiceZeroShotSampler, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/Cute-Baby-Voice_1918683888908959745.json, 音频生成/音频生成/克隆声音极简版_1897973393327902722.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_44

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/Cute-Baby-Voice_1918683888908959745.json、音频生成/音频生成/克隆声音极简版_1897973393327902722.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadAudio`
- `NTCosyVoiceZeroShotSampler`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 1/2 个有
- `ShellAgentPluginInputText` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
