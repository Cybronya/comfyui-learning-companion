---
name: unknown_workflow_generic_1673
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7075
common_nodes: [HeartMuLa_Generate, PrimitiveStringMultiline, SaveAudio, SaveAudioMP3, easy saveText, easy seed, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/音频-歌曲重唱-HeartMuLa_2013839748728627202.json, 音频生成/音频生成/AI一键生成歌词gemini-3-HeartMuLa_2022920245509365761.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1673

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/音频-歌曲重唱-HeartMuLa_2013839748728627202.json、音频生成/音频生成/AI一键生成歌词gemini-3-HeartMuLa_2022920245509365761.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `HeartMuLa_Generate`
- `PrimitiveStringMultiline`
- `SaveAudio`
- `SaveAudioMP3`
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `HeartMuLa_Transcribe` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MemoryCleaner` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
