---
name: unknown_workflow_generic_562
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8712
common_nodes: [Apply Whisper, LoadAudio, T8_BreezeTTS_Generate, T8_BreezeTTS_GenerationSettings, T8_BreezeTTS_ModelLoader]
problems: []
missing: []
members: [数字人/数字人/声音克隆（上传参考音频生成任何语音）_2100911017046925313.json, 音频生成/音频生成/Breeze TTS 2 声音克隆工作流-免打标一键复刻_2095712501966135298.json, 音频生成/音频生成/Breeze TTS 2 声音导演工作流-音色不变控情绪_2095712606765015042.json, 音频生成/音频生成/Breeze-TTS2-Clone_2105912504613425153.json, 音频生成/音频生成/TTS Breeze 2 高质量声音克隆｜世界第一开源｜情感控制_2096105647677984769.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_562

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/声音克隆（上传参考音频生成任何语音）_2100911017046925313.json、音频生成/音频生成/Breeze TTS 2 声音克隆工作流-免打标一键复刻_2095712501966135298.json、音频生成/音频生成/Breeze TTS 2 声音导演工作流-音色不变控情绪_2095712606765015042.json、音频生成/音频生成/Breeze-TTS2-Clone_2105912504613425153.json、音频生成/音频生成/TTS Breeze 2 高质量声音克隆｜世界第一开源｜情感控制_2096105647677984769.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `Apply Whisper`
- `LoadAudio`
- `T8_BreezeTTS_Generate`
- `T8_BreezeTTS_GenerationSettings`
- `T8_BreezeTTS_ModelLoader`

**可变部分**（部分 workflow 才有）：
- `T8_BreezeTTS_CloneRequest` —— 4/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `SaveAudioMP3` —— 3/5 个有
- `MuyeTextEditOutput` —— 2/5 个有
- `SaveAudio` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `T8_BreezeTTS_DirectionRequest` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
