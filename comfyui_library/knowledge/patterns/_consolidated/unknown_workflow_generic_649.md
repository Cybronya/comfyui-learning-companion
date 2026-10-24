---
name: unknown_workflow_generic_649
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.966
common_nodes: [FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceDesign, LayerUtility: PurgeVRAM V2, SaveAudio]
problems: []
missing: []
members: [图片生成/图生图/QWEN-TTS多合一工作流_音色克隆_音色自定义_多轮对话_2073307423431024641.json, 音频生成/音频生成/Qwen3 TTS 多角色配音设计_2015669228627562497.json, 音频生成/音频生成/Qwen3 TTS 最多8角色对话配音-音色设计版_2015615072806113282.json, 音频生成/音频生成/Qwen3 TTS 最新多角色对话配音-音色设计版-最多支持8人对话_2015598123204222977.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_649

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/QWEN-TTS多合一工作流_音色克隆_音色自定义_多轮对话_2073307423431024641.json、音频生成/音频生成/Qwen3 TTS 多角色配音设计_2015669228627562497.json、音频生成/音频生成/Qwen3 TTS 最多8角色对话配音-音色设计版_2015615072806113282.json、音频生成/音频生成/Qwen3 TTS 最新多角色对话配音-音色设计版-最多支持8人对话_2015598123204222977.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceDesign`
- `LayerUtility: PurgeVRAM V2`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `Text` —— 2/4 个有
- `FB_Qwen3TTSCustomVoice` —— 1/4 个有
- `HeartMuLa_Transcribe` —— 1/4 个有
- `LoadAudio` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
