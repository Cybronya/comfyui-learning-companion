---
key: 视频生成/文生视频/歌曲创作 音频生成+AI歌曲音乐+SunoV5.5+歌词生成+数字人唱歌_2062398119878418434.json
name: 歌曲创作 音频生成+AI歌曲音乐+SunoV5.5+歌词生成+数字人唱歌_2062398119878418434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/歌曲创作 音频生成+AI歌曲音乐+SunoV5.5+歌词生成+数字人唱歌_2062398119878418434.json
hash: a7ba24f2f53108cd
coverage: 0.366667
learned_at: 2026-10-11 20:21:36
nodes: [easy showAnything, SaveAudio, SaveAudio, Comfly_suno_custom, CR Prompt Text, easy showAnything, easy showAnything, easy showAnything, Note, ShowText, ShowText, JjkText, JjkText, SaveAudio, easy showAnything, SaveAudio, JjkText, RH_RhartAudioSunoV55Single, easy showAnything, RH_RhartAudioSunoV55Custom, Label (rgthree), Fast Groups Bypasser (rgthree), CR Prompt Text, CR Prompt Text, MarkdownNote, LoadImage, JjkText, Comfly_api_set, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree)]
patterns: []
missing: [Label (rgthree), CR Prompt Text, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/歌曲创作 音频生成+AI歌曲音乐+SunoV5.5+歌词生成+数字人唱歌_2062398119878418434.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/歌曲创作 音频生成+AI歌曲音乐+SunoV5.5+歌词生成+数字人唱歌_2062398119878418434.json`

## 结构

**生成流程**：Output → Other

**节点**（30 个）：
- `easy showAnything`
- `SaveAudio`
- `SaveAudio`
- `Comfly_suno_custom`
- `CR Prompt Text`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `Note`
- `ShowText`
- `ShowText`
- `JjkText`
- `JjkText`
- `SaveAudio`
- `easy showAnything`
- `SaveAudio`
- `JjkText`
- `RH_RhartAudioSunoV55Single`
- `easy showAnything`
- `RH_RhartAudioSunoV55Custom`
- `Label (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `CR Prompt Text`
- `CR Prompt Text`
- `MarkdownNote`
- `LoadImage`
- `JjkText`
- `Comfly_api_set`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **37%**（11/30）

**有卡**：`SaveAudio`、`Comfly_suno_custom`、`ShowText`、`RH_RhartAudioSunoV55Single`、`RH_RhartAudioSunoV55Custom`、`LoadImage`、`Comfly_api_set`

**缺卡**（4）：`Label (rgthree)`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：LoadImage、SaveAudio、ShowText、Comfly_api_set、RH_RhartAudioSunoV55Single、Comfly_suno_custom、RH_RhartAudioSunoV55Custom、sd15-t2i-basic

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
