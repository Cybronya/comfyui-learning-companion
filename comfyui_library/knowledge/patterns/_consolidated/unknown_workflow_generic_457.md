---
name: unknown_workflow_generic_457
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.89275
common_nodes: [LoadAudio, SaveAudio, TDQwen3TTSDefineSpeaker, TDQwen3TTSModelLoader, TDQwen3TTSMultiDialog]
problems: []
missing: []
members: [音频生成/音频生成/Qwen TTS 语音克隆_2092151524360278018.json, 音频生成/音频生成/qwen3-TTS 声音克隆_2017938544857190402.json, 音频生成/音频生成/qwen3-TTS 声音克隆_2034529031684628482.json, 音频生成/音频生成/影流配音qwentts3_2029428174693601281.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_457

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/Qwen TTS 语音克隆_2092151524360278018.json、音频生成/音频生成/qwen3-TTS 声音克隆_2017938544857190402.json、音频生成/音频生成/qwen3-TTS 声音克隆_2034529031684628482.json、音频生成/音频生成/影流配音qwentts3_2029428174693601281.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadAudio`
- `SaveAudio`
- `TDQwen3TTSDefineSpeaker`
- `TDQwen3TTSModelLoader`
- `TDQwen3TTSMultiDialog`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `SetNode` —— 1/4 个有
- `TDQwen3TTSBatchGenerateSpeaker` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
