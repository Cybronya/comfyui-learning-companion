---
name: unknown_workflow_generic_783
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9475
common_nodes: [ACEStepGen, GenerationParameters, GetTextFromJson, LoadJsonFromText, MultiLineLyrics, MultiLinePromptACES, RH_Translator, SaveAudio, ShowText, Text Concatenate, Text Multiline]
problems: []
missing: []
members: [音频生成/音频生成/ACE-STEP最强开源音乐生成模型_1920236045869187073.json, 音频生成/音频生成/用音乐自由抒发心情(ACE-Step遇见LLM)_1920169949044871169.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_783

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/ACE-STEP最强开源音乐生成模型_1920236045869187073.json、音频生成/音频生成/用音乐自由抒发心情(ACE-Step遇见LLM)_1920169949044871169.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `ACEStepGen`
- `GenerationParameters`
- `GetTextFromJson`
- `LoadJsonFromText`
- `MultiLineLyrics`
- `MultiLinePromptACES`
- `RH_Translator`
- `SaveAudio`
- `ShowText`
- `Text Concatenate`
- `Text Multiline`

**可变部分**（部分 workflow 才有）：
- `> Text Replace` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ReplaceText` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
