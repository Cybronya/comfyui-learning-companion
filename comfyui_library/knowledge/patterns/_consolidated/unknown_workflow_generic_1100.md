---
name: unknown_workflow_generic_1100
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.9
common_nodes: [LoadAudio, SaveAudio, easy downloadIndexTTSAndLoadModel, easy indexTTSGenerateSimple]
problems: []
missing: []
members: [数字人/数字人/IndexTTS2_1982727809716101121.json, 数字人/数字人/indextts基础款_1972207212905099265.json, 音频生成/音频生成/TTS1与TTS2 声音克隆_2002005150199889922.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1100

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/IndexTTS2_1982727809716101121.json、数字人/数字人/indextts基础款_1972207212905099265.json、音频生成/音频生成/TTS1与TTS2 声音克隆_2002005150199889922.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadAudio`
- `SaveAudio`
- `easy downloadIndexTTSAndLoadModel`
- `easy indexTTSGenerateSimple`

**可变部分**（部分 workflow 才有）：
- `IndexTTS2Run` —— 2/3 个有
- `PreviewAudio` —— 2/3 个有
- `easy indexTTSAudioMerge` —— 2/3 个有
- `AudioCrop` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `Text` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
