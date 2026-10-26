---
name: unknown_workflow_generic_1207
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.863
common_nodes: [Apply Whisper, LoadAudio, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, SaveAudio, ShowText|pysssss]
problems: []
missing: []
members: [音频生成/音频生成/opsv-声音克隆_2061483328276090881.json, 音频生成/音频生成/声音克隆 Qwen3 TTS 真实复制音频   极速版 音色参考_2017868031271116802.json, 音频生成/音频生成/最新Qwen3 TTS 声音克隆_2018610702222626817.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1207

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/opsv-声音克隆_2061483328276090881.json、音频生成/音频生成/声音克隆 Qwen3 TTS 真实复制音频   极速版 音色参考_2017868031271116802.json、音频生成/音频生成/最新Qwen3 TTS 声音克隆_2018610702222626817.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `Apply Whisper`
- `LoadAudio`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `SaveAudio`
- `ShowText|pysssss`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 2/3 个有
- `Float` —— 1/3 个有
- `TextInputBasic` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
