---
name: unknown_workflow_generic_1802
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7
common_nodes: [LoadAudio, PrimitiveStringMultiline, SaveAudioMP3]
problems: []
missing: []
members: [音频生成/音频生成/IndexTTS2情感声音克隆-参考音色工作流_2094568109851111426.json, 音频生成/音频生成/IndexTTS2情感迁移-参考音色工作流_2094575121431355393.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1802

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/IndexTTS2情感声音克隆-参考音色工作流_2094568109851111426.json、音频生成/音频生成/IndexTTS2情感迁移-参考音色工作流_2094575121431355393.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadAudio`
- `PrimitiveStringMultiline`
- `SaveAudioMP3`

**可变部分**（部分 workflow 才有）：
- `IndexTTS2EmotionAudioNode` —— 1/2 个有
- `IndexTTS2EmotionTextNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
