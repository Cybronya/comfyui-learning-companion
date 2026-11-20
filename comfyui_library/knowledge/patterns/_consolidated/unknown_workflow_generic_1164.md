---
name: unknown_workflow_generic_1164
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.847333
common_nodes: [CR Prompt Text, FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, LayerUtility: PurgeVRAM V2, SaveAudio, VRAMReserver, easy float, easy int]
problems: []
missing: []
members: [音频生成/音频生成/AA--Qwen3 TTS多人配音--声音克隆版本-三角色-漫剧_推文_有声书_2015768667132268546.json, 音频生成/音频生成/AA--Qwen3 TTS多人配音-声音设计版本--三角色-漫剧_推文_有声书_2015768802629259265.json, 音频生成/音频生成/AA--增强版Qwen3TTS-语音克隆-说话情感和断句节奏自定义-单人版本_2016508411113906178.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1164

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/AA--Qwen3 TTS多人配音--声音克隆版本-三角色-漫剧_推文_有声书_2015768667132268546.json、音频生成/音频生成/AA--Qwen3 TTS多人配音-声音设计版本--三角色-漫剧_推文_有声书_2015768802629259265.json、音频生成/音频生成/AA--增强版Qwen3TTS-语音克隆-说话情感和断句节奏自定义-单人版本_2016508411113906178.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Prompt Text`
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `LayerUtility: PurgeVRAM V2`
- `SaveAudio`
- `VRAMReserver`
- `easy float`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 2/3 个有
- `WhisperSTT` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/3 个有
- `IndexTTS2Run` —— 1/3 个有
- `LayerUtility: TextJoin` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
