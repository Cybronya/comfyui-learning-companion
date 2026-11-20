---
name: unknown_workflow_generic_228
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.969
common_nodes: [CR Prompt Text, LoadAudio, Qwen3ASRLoader, Qwen3ASRTranscribe, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/(贞贞lora)VoxCPM2语音极限克隆V1_2049670919605456897.json, 音频生成/音频生成/OmniVoice-双人语音克隆（支持方言）_2042241339672240130.json, 音频生成/音频生成/VOXCPM2声音克隆语音克隆声音_2070445511508840450.json, 音频生成/音频生成/VOXCPM2声音克隆语音克隆声音_2079213870937362434.json, 音频生成/音频生成/VoxCPM2声音克隆 语音设计，支持方言_2067088845816029186.json, 音频生成/音频生成/VoxCPM2声音克隆（完美复刻音色）_2065355902638714882.json, 音频生成/音频生成/VoxCPM2语音克隆+声音设计_2056660403781984257.json, 音频生成/音频生成/VoxCPM2语音克隆_2090280073604718593.json, 音频生成/音频生成/VoxCPM2语音极限克隆V1  企财盈6.17_2067072588702113793.json, 音频生成/音频生成/vox cpm2语音克隆_2056202036819046401.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_228

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（音频生成/音频生成/(贞贞lora)VoxCPM2语音极限克隆V1_2049670919605456897.json、音频生成/音频生成/OmniVoice-双人语音克隆（支持方言）_2042241339672240130.json、音频生成/音频生成/VOXCPM2声音克隆语音克隆声音_2070445511508840450.json、音频生成/音频生成/VOXCPM2声音克隆语音克隆声音_2079213870937362434.json、音频生成/音频生成/VoxCPM2声音克隆 语音设计，支持方言_2067088845816029186.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `CR Prompt Text`
- `LoadAudio`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `RunningHub_VoxCPM_Generate` —— 9/10 个有
- `RunningHub_VoxCPM_LoadModel` —— 9/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `AudioCrop` —— 1/10 个有
- `AudioSeparation` —— 1/10 个有
- `OmniVoiceMultiSpeakerTTS` —— 1/10 个有
- `RunningHub_VoxCPM_MultiSpeaker_ListReference` —— 1/10 个有
- `ShowAnything|Mie` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
