---
key: 音频生成/音频生成/TTS大模型：SoulX-Podcast，配合ComfyUI生成多人对话音频，支持方言：粤语、河南、四川话_1984899462583762946.json
name: TTS大模型：SoulX-Podcast，配合ComfyUI生成多人对话音频，支持方言：粤语、河南、四川话_1984899462583762946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/TTS大模型：SoulX-Podcast，配合ComfyUI生成多人对话音频，支持方言：粤语、河南、四川话_1984899462583762946.json
hash: 06937f2963f6d54f
coverage: 0.9
learned_at: 2026-10-18 01:46:54
nodes: [SoulXPodcastLoader, MarkdownNote, LoadAudio, Text, Text, SoulXPodcastGenerate, SaveAudio, SoulXPodcastInputParser, LoadAudio, Label (rgthree)]
patterns: []
missing: []
---

# 音频生成/音频生成/TTS大模型：SoulX-Podcast，配合ComfyUI生成多人对话音频，支持方言：粤语、河南、四川话_1984899462583762946.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/TTS大模型：SoulX-Podcast，配合ComfyUI生成多人对话音频，支持方言：粤语、河南、四川话_1984899462583762946.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（10 个）：
- `SoulXPodcastLoader`
- `MarkdownNote`
- `LoadAudio`
- `Text`
- `Text`
- `SoulXPodcastGenerate`
- `SaveAudio`
- `SoulXPodcastInputParser`
- `LoadAudio`
- `Label (rgthree)`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`SoulXPodcastLoader`、`LoadAudio`、`Text`、`SoulXPodcastGenerate`、`SaveAudio`、`SoulXPodcastInputParser`、`Label (rgthree)`

**用到的条目**：SaveAudio、LoadAudio、Text、SoulXPodcastGenerate、SoulXPodcastInputParser、SoulXPodcastLoader、Label (rgthree)、sd15-t2i-basic
