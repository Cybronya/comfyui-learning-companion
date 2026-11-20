---
name: unknown_workflow_generic_1772
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [IndexTTS2Run, LoadAudio, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/40.tonnie-Index TTS2音频克隆（刘禹锡有诗云）_2004254864559538177.json, 音频生成/音频生成/V2配音-API专用_1985683386402516993.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1772

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/40.tonnie-Index TTS2音频克隆（刘禹锡有诗云）_2004254864559538177.json、音频生成/音频生成/V2配音-API专用_1985683386402516993.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `IndexTTS2Run`
- `LoadAudio`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `KepStringLiteral` —— 1/2 个有
- `MultiLinePrompt` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
