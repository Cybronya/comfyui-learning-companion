---
name: unknown_workflow_sampler_25
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.886
common_nodes: [Apply Whisper, AudioCrop, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/IndexTTS2长文本音频-克隆音色带情感_2052017251003445249.json, 音频生成/音频生成/Qwen3-tts声音克隆_2051922867775918081.json, 音频生成/音频生成/韩老魔来当配音员辣-声音克隆_2012083044638789633.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_25

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/IndexTTS2长文本音频-克隆音色带情感_2052017251003445249.json、音频生成/音频生成/Qwen3-tts声音克隆_2051922867775918081.json、音频生成/音频生成/韩老魔来当配音员辣-声音克隆_2012083044638789633.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `Apply Whisper`
- `AudioCrop`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 2/3 个有
- `Qwen3TTSModelLoader` —— 2/3 个有
- `Qwen3TTSVoiceClone` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `IndexTTS2Run` —— 1/3 个有
- `Text` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
