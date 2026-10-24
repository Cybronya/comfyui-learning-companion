---
name: unknown_workflow_video_117
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8085
common_nodes: [ACEStepGen, AudioCrop, Fast Groups Bypasser (rgthree), FloatProcess, GenerationParameters, GetTextFromJson, LayerUtility: PurgeVRAM, LoadAudio, LoadFloatModels, LoadImage, LoadJsonFromText, MultiLineLyrics, MultiLinePromptACES, PrimitiveFloat, RH_LLMAPI_NODE, ReplaceText, SaveAudio, ShowText, Text Concatenate, Text Multiline, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/音乐无限_仅需主题一键生成带字幕音乐数字人_1921955597195886593.json, 视频生成/文生视频/极速FLOAT 数字人遇见ACE-Step和LLM音乐数字人无限_1920266162955812865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_117

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/音乐无限_仅需主题一键生成带字幕音乐数字人_1921955597195886593.json、视频生成/文生视频/极速FLOAT 数字人遇见ACE-Step和LLM音乐数字人无限_1920266162955812865.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `ACEStepGen`
- `AudioCrop`
- `Fast Groups Bypasser (rgthree)`
- `FloatProcess`
- `GenerationParameters`
- `GetTextFromJson`
- `LayerUtility: PurgeVRAM`
- `LoadAudio`
- `LoadFloatModels`
- `LoadImage`
- `LoadJsonFromText`
- `MultiLineLyrics`
- `MultiLinePromptACES`
- `PrimitiveFloat`
- `RH_LLMAPI_NODE`
- `ReplaceText`
- `SaveAudio`
- `ShowText`
- `Text Concatenate`
- `Text Multiline`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Add Subtitles To Frames` —— 1/2 个有
- `Apply Whisper` —— 1/2 个有
- `DF_Int_to_Float` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy mathInt` —— 1/2 个有
- `easy saveText` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
