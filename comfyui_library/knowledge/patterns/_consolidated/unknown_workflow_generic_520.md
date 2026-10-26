---
name: unknown_workflow_generic_520
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.952333
common_nodes: [FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceDesign, LayerUtility: PurgeVRAM V2, SaveAudio, VRAMReserver]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3 TTS多角色配音V2_2015075625282838530.json, 音频生成/音频生成/Qwen3 TTS多角色配音V2（声音克隆版）_2015094220624764929.json, 音频生成/音频生成/Qwen3 TTS多角色配音_2015413055974285314.json, 音频生成/音频生成/Qwen3 TTS有声书制作   多人语音设计+模仿_2017771927997259777.json, 音频生成/音频生成/Qwen3-TTS多角色多轮对话生成工作流_2014703508829769729.json, 音频生成/音频生成/🦖多角色对话配音（自定义音色）_2018213546974253057.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_520

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（音频生成/音频生成/Qwen3 TTS多角色配音V2_2015075625282838530.json、音频生成/音频生成/Qwen3 TTS多角色配音V2（声音克隆版）_2015094220624764929.json、音频生成/音频生成/Qwen3 TTS多角色配音_2015413055974285314.json、音频生成/音频生成/Qwen3 TTS有声书制作   多人语音设计+模仿_2017771927997259777.json、音频生成/音频生成/Qwen3-TTS多角色多轮对话生成工作流_2014703508829769729.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceDesign`
- `LayerUtility: PurgeVRAM V2`
- `SaveAudio`
- `VRAMReserver`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/6 个有
- `LoadAudio` —— 3/6 个有
- `WhisperSTT` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
