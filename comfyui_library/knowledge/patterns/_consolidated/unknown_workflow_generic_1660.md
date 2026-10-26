---
name: unknown_workflow_generic_1660
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6875
common_nodes: [SaveAudio, TDQwen3TTSModelLoader, TDQwen3TTSVoiceDesign]
problems: []
missing: []
members: [数字人/数字人/VoxCPM2语音克隆音色设计全能新王者_2114306949566255106.json, 音频生成/音频生成/A-17 Qwen3-TTS 音色设计 无需录音 文生音频 10国语言_2107472276244484097.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1660

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/VoxCPM2语音克隆音色设计全能新王者_2114306949566255106.json、音频生成/音频生成/A-17 Qwen3-TTS 音色设计 无需录音 文生音频 10国语言_2107472276244484097.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `SaveAudio`
- `TDQwen3TTSModelLoader`
- `TDQwen3TTSVoiceDesign`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
