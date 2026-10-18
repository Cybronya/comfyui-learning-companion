---
key: 音频生成/音频生成/歌曲生成 _ ACE-Step1.5_2021444202046955521.json
name: 歌曲生成 _ ACE-Step1.5_2021444202046955521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/歌曲生成 _ ACE-Step1.5_2021444202046955521.json
hash: aca30b40ca1ca69b
coverage: 0.769231
learned_at: 2026-10-18 02:07:11
nodes: [easy ifElse, RunningHub ACE-Step Loader, RunningHub ACE-Step Creator, SaveAudioMP3, PrimitiveBoolean, RunningHub ACE-Step GenerationParams, Int, String, String, Float, SimpleMath+, Float, Text Multiline, easy ifElse, ShowText|pysssss, ShowText|pysssss, RH_Suno_Lyrics, Float, ShowText|pysssss, TextListSelelct, IO_input_any, ShellAgentPluginOutputText, ShowText|pysssss, Text Multiline, CR Text, ACE_TextSelector]
patterns: []
missing: []
---

# 音频生成/音频生成/歌曲生成 _ ACE-Step1.5_2021444202046955521.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/歌曲生成 _ ACE-Step1.5_2021444202046955521.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（26 个）：
- `easy ifElse`
- `RunningHub ACE-Step Loader`
- `RunningHub ACE-Step Creator`
- `SaveAudioMP3`
- `PrimitiveBoolean`
- `RunningHub ACE-Step GenerationParams`
- `Int`
- `String`
- `String`
- `Float`
- `SimpleMath+`
- `Float`
- `Text Multiline`
- `easy ifElse`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `RH_Suno_Lyrics`
- `Float`
- `ShowText|pysssss`
- `TextListSelelct`
- `IO_input_any`
- `ShellAgentPluginOutputText`
- `ShowText|pysssss`
- `Text Multiline`
- `CR Text`
- `ACE_TextSelector`

## 知识

覆盖率 **77%**（20/26）

**有卡**：`RunningHub ACE-Step Loader`、`RunningHub ACE-Step Creator`、`SaveAudioMP3`、`PrimitiveBoolean`、`RunningHub ACE-Step GenerationParams`、`Int`、`String`、`Float`、`SimpleMath+`、`Text Multiline`、`RH_Suno_Lyrics`、`TextListSelelct`、`IO_input_any`、`ShellAgentPluginOutputText`、`CR Text`、`ACE_TextSelector`

**用到的条目**：ShellAgentPluginOutputText、SaveAudioMP3、Int、PrimitiveBoolean、Float、String、TextListSelelct、CR Text
