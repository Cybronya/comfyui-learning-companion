---
name: unknown_workflow_generic_827
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6905
common_nodes: [CR Prompt Text, FB_Qwen3TTSVoiceDesign, RH_LLMAPI_Pro_Node, SaveAudio, easy showAnything]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3 TTS设计任何声音-音色旁白配音-Smile版_2017085717763072002.json, 音频生成/音频生成/Qwen3 TTS音色设计 + 出配音音色、旁白 + 音色库搭建_2046825672173166594.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_827

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/Qwen3 TTS设计任何声音-音色旁白配音-Smile版_2017085717763072002.json、音频生成/音频生成/Qwen3 TTS音色设计 + 出配音音色、旁白 + 音色库搭建_2046825672173166594.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `FB_Qwen3TTSVoiceDesign`
- `RH_LLMAPI_Pro_Node`
- `SaveAudio`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ShellAgentPluginOutputText` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
