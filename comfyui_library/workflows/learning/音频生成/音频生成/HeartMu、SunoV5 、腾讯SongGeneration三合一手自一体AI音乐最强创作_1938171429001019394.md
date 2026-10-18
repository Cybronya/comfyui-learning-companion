---
key: 音频生成/音频生成/HeartMu、SunoV5 、腾讯SongGeneration三合一手自一体AI音乐最强创作_1938171429001019394.json
name: HeartMu、SunoV5 、腾讯SongGeneration三合一手自一体AI音乐最强创作_1938171429001019394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/HeartMu、SunoV5 、腾讯SongGeneration三合一手自一体AI音乐最强创作_1938171429001019394.json
hash: 4fb8a2abe7b1ef3f
coverage: 0.78
learned_at: 2026-10-18 01:23:53
nodes: [TextBox, TextBox, TextBox, TextBox, TextBox, TextBox, TextBox, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, Note, Text Find and Replace, Text Find and Replace, SaveAudio, TextBox, MultiLinePromptACES, SongGeneration_Stage1, SongGeneration_Loader, Text Find and Replace, ImpactSwitch, TextBox, Textbox, Text Find and Replace, Text Find and Replace, Text Find and Replace, Text Find and Replace, Text Find and Replace, TextBox, ImpactSwitch, MultiLineLyrics, Int, ImpactSwitch, LoadAudio, Note, Int, Int, RH_Suno_Custom, SaveAudio, ImpactSwitch, SongGeneration_Stage2, SaveAudio, SongGeneration_Sampler, WujiCleaner, Fast Groups Muter (rgthree), HeartMuLa_Generate, WujiCleaner, RHHiddenNodes, SaveAudio, RHHiddenNodes]
patterns: []
missing: []
---

# 音频生成/音频生成/HeartMu、SunoV5 、腾讯SongGeneration三合一手自一体AI音乐最强创作_1938171429001019394.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/HeartMu、SunoV5 、腾讯SongGeneration三合一手自一体AI音乐最强创作_1938171429001019394.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（50 个）：
- `TextBox`
- `TextBox`
- `TextBox`
- `TextBox`
- `TextBox`
- `TextBox`
- `TextBox`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Note`
- `Text Find and Replace`
- `Text Find and Replace`
- `SaveAudio`
- `TextBox`
- `MultiLinePromptACES`
- `SongGeneration_Stage1`
- `SongGeneration_Loader`
- `Text Find and Replace`
- `ImpactSwitch`
- `TextBox`
- `Textbox`
- `Text Find and Replace`
- `Text Find and Replace`
- `Text Find and Replace`
- `Text Find and Replace`
- `Text Find and Replace`
- `TextBox`
- `ImpactSwitch`
- `MultiLineLyrics`
- `Int`
- `ImpactSwitch`
- `LoadAudio`
- `Note`
- `Int`
- `Int`
- `RH_Suno_Custom`
- `SaveAudio`
- `ImpactSwitch`
- `SongGeneration_Stage2`
- `SaveAudio`
- `SongGeneration_Sampler` ★核心
- `WujiCleaner`
- `Fast Groups Muter (rgthree)`
- `HeartMuLa_Generate`
- `WujiCleaner`
- `RHHiddenNodes`
- `SaveAudio`
- `RHHiddenNodes`

## 知识

覆盖率 **78%**（39/50）

**有卡**：`TextBox`、`Text Find and Replace`、`SaveAudio`、`MultiLinePromptACES`、`SongGeneration_Stage1`、`SongGeneration_Loader`、`Textbox`、`MultiLineLyrics`、`Int`、`LoadAudio`、`RH_Suno_Custom`、`SongGeneration_Stage2`、`SongGeneration_Sampler`、`WujiCleaner`、`HeartMuLa_Generate`、`RHHiddenNodes`

**用到的条目**：SongGeneration_Sampler、MultiLinePromptACES、SaveAudio、Int、LoadAudio、RHHiddenNodes、Textbox、WujiCleaner
