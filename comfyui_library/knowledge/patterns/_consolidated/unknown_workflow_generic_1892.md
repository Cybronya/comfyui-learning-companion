---
name: unknown_workflow_generic_1892
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9115
common_nodes: [DramaBoxLoader, DramaBoxTTS, DramaBoxVoiceClone, Fast Groups Bypasser (rgthree), LoadAudio, SaveAudio]
problems: []
missing: []
members: [平台全量/DramaBox TTS-声音设计及克隆_2057818010886430721.json, 音频生成/音频生成/DramaBox TTS 文生语音 声音克隆 音色迁移 高表现力 导演级情绪化语音合成_2056607103107821570.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1892

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/DramaBox TTS-声音设计及克隆_2057818010886430721.json、音频生成/音频生成/DramaBox TTS 文生语音 声音克隆 音色迁移 高表现力 导演级情绪化语音合成_2056607103107821570.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `DramaBoxLoader`
- `DramaBoxTTS`
- `DramaBoxVoiceClone`
- `Fast Groups Bypasser (rgthree)`
- `LoadAudio`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `Textbox` —— 1/2 个有
- `TrimAudioDuration` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
