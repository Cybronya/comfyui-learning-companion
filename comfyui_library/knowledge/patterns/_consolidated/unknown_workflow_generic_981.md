---
name: unknown_workflow_generic_981
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.65025
common_nodes: [HeartMuLa_Generate, PrimitiveStringMultiline, SaveAudio, SaveAudioMP3, easy saveText, easy seed, easy showAnything]
problems: []
missing: []
members: [平台全量/推理-生成歌词gemini-3-HeartMuLa_2013827207310876674.json, 平台全量/音频-生成歌曲-HeartMuLa_2013834865921236994.json, 数字人/数字人/音频-歌曲重唱-HeartMuLa_2013839748728627202.json, 音频生成/音频生成/AI一键生成歌词gemini-3-HeartMuLa_2022920245509365761.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_981

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/推理-生成歌词gemini-3-HeartMuLa_2013827207310876674.json、平台全量/音频-生成歌曲-HeartMuLa_2013834865921236994.json、数字人/数字人/音频-歌曲重唱-HeartMuLa_2013839748728627202.json、音频生成/音频生成/AI一键生成歌词gemini-3-HeartMuLa_2022920245509365761.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 4 个 workflow 都包含：
- `HeartMuLa_Generate`
- `PrimitiveStringMultiline`
- `SaveAudio`
- `SaveAudioMP3`
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_Pro_Node` —— 3/4 个有
- `HeartMuLa_Transcribe` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `MemoryCleaner` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
