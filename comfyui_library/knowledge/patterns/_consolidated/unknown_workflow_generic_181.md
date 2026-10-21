---
name: unknown_workflow_generic_181
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.939714
common_nodes: [FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceDesign, LayerUtility: PurgeVRAM V2, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3 TTS 多角色配音设计_2015669228627562497.json, 音频生成/音频生成/Qwen3 TTS 最多8角色对话配音-音色设计版_2015615072806113282.json, 音频生成/音频生成/Qwen3 TTS 最新多角色对话配音-音色设计版-最多支持8人对话_2015598123204222977.json, 音频生成/音频生成/Qwen3 TTS多角色配音V2_2015075625282838530.json, 音频生成/音频生成/Qwen3 TTS多角色配音_2015413055974285314.json, 音频生成/音频生成/Qwen3 TTS有声书制作   多人语音设计+模仿_2017771927997259777.json, 音频生成/音频生成/🦖多角色对话配音（自定义音色）_2018213546974253057.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_181

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（音频生成/音频生成/Qwen3 TTS 多角色配音设计_2015669228627562497.json、音频生成/音频生成/Qwen3 TTS 最多8角色对话配音-音色设计版_2015615072806113282.json、音频生成/音频生成/Qwen3 TTS 最新多角色对话配音-音色设计版-最多支持8人对话_2015598123204222977.json、音频生成/音频生成/Qwen3 TTS多角色配音V2_2015075625282838530.json、音频生成/音频生成/Qwen3 TTS多角色配音_2015413055974285314.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceDesign`
- `LayerUtility: PurgeVRAM V2`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `VRAMReserver` —— 4/7 个有
- `CR Prompt Text` —— 3/7 个有
- `LoadAudio` —— 2/7 个有
- `Text` —— 2/7 个有
- `WhisperSTT` —— 2/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
