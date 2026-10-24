---
name: unknown_workflow_video_128
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.868
common_nodes: [ACEStepGen, GenerationParameters, GetTextFromJson, IndexTTSRun, JWStringReplace, LayerUtility: PurgeVRAM, LoadAudio, LoadJsonFromText, LoadVideo, MultiLineLyrics, MultiLinePromptACES, PrimitiveStringMultiline, RH_HeyGemNode, RH_LLMAPI_NODE, ReplaceText, SaveAudio, SaveVideo, ShowText, Text Concatenate, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, easy saveText, easy showAnything]
problems: []
missing: []
members: [音频生成/音频生成/HeyGem音乐数字人_仅需主题2分钟生成长视频数字人_1925690454367490050.json, 音频生成/音频生成/Index声音克隆+heygem视频数字人强强联合_1925755292515274753.json]
source: knowledge_consolidation
---

# unknown_workflow_video_128

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/HeyGem音乐数字人_仅需主题2分钟生成长视频数字人_1925690454367490050.json、音频生成/音频生成/Index声音克隆+heygem视频数字人强强联合_1925755292515274753.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `ACEStepGen`
- `GenerationParameters`
- `GetTextFromJson`
- `IndexTTSRun`
- `JWStringReplace`
- `LayerUtility: PurgeVRAM`
- `LoadAudio`
- `LoadJsonFromText`
- `LoadVideo`
- `MultiLineLyrics`
- `MultiLinePromptACES`
- `PrimitiveStringMultiline`
- `RH_HeyGemNode`
- `RH_LLMAPI_NODE`
- `ReplaceText`
- `SaveAudio`
- `SaveVideo`
- `ShowText`
- `Text Concatenate`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy saveText`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
