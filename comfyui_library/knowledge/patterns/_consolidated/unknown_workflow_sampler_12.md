---
name: unknown_workflow_sampler_12
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8448
common_nodes: [HeartMuLa_Transcribe, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, SaveAudio, ShowText|pysssss, easy saveText]
problems: []
missing: []
members: [音频生成/音频生成/Mel-Band RoFormer歌曲人声分离，伴奏提取_2033376555807805442.json, 音频生成/音频生成/MelBandRoFormer 音乐歌音色翻唱_2110357146150985730.json, 音频生成/音频生成/歌曲音色替换翻唱_2041502168951300097.json, 音频生成/音频生成/歌曲音色翻唱MelBandRoFormer_2109892669165096962.json, 音频生成/音频生成/歌曲音色翻唱_2041437118723006465.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_12

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（音频生成/音频生成/Mel-Band RoFormer歌曲人声分离，伴奏提取_2033376555807805442.json、音频生成/音频生成/MelBandRoFormer 音乐歌音色翻唱_2110357146150985730.json、音频生成/音频生成/歌曲音色替换翻唱_2041502168951300097.json、音频生成/音频生成/歌曲音色翻唱MelBandRoFormer_2109892669165096962.json、音频生成/音频生成/歌曲音色翻唱_2041437118723006465.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `HeartMuLa_Transcribe`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `SaveAudio`
- `ShowText|pysssss`
- `easy saveText`

**可变部分**（部分 workflow 才有）：
- `AudioCombine` —— 4/5 个有
- `SaveAudioMP3` —— 4/5 个有
- `SeedVCRun` —— 4/5 个有
- `AdjustAudio` —— 1/5 个有
- `AudioAdjustVolume` —— 1/5 个有
- `Int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
