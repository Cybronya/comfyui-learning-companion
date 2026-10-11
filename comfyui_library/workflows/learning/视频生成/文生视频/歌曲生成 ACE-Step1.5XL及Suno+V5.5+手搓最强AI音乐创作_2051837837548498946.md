---
key: 视频生成/文生视频/歌曲生成 ACE-Step1.5XL及Suno+V5.5+手搓最强AI音乐创作_2051837837548498946.json
name: 歌曲生成 ACE-Step1.5XL及Suno+V5.5+手搓最强AI音乐创作_2051837837548498946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/歌曲生成 ACE-Step1.5XL及Suno+V5.5+手搓最强AI音乐创作_2051837837548498946.json
hash: e5ee4b01220aed8c
coverage: 0.5
learned_at: 2026-10-11 19:49:50
nodes: [ShowText|pysssss, ShowText|pysssss, RH_Screenwriter, WujiMusicianACEStep15XL, Fast Groups Muter (rgthree), Note, CR Text, RH_RhartAudioSunoV55Single, SaveAudio, SaveAudio, WujiLyricistNode, PrimitiveFloat]
patterns: []
missing: [CR Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/歌曲生成 ACE-Step1.5XL及Suno+V5.5+手搓最强AI音乐创作_2051837837548498946.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/歌曲生成 ACE-Step1.5XL及Suno+V5.5+手搓最强AI音乐创作_2051837837548498946.json`

## 结构

**生成流程**：Output → Other

**节点**（12 个）：
- `ShowText|pysssss`
- `ShowText|pysssss`
- `RH_Screenwriter`
- `WujiMusicianACEStep15XL`
- `Fast Groups Muter (rgthree)`
- `Note`
- `CR Text`
- `RH_RhartAudioSunoV55Single`
- `SaveAudio`
- `SaveAudio`
- `WujiLyricistNode`
- `PrimitiveFloat`

## 知识

覆盖率 **50%**（6/12）

**有卡**：`RH_Screenwriter`、`WujiMusicianACEStep15XL`、`RH_RhartAudioSunoV55Single`、`SaveAudio`、`WujiLyricistNode`

**缺卡**（1）：`CR Text`

**用到的条目**：SaveAudio、RH_Screenwriter、RH_RhartAudioSunoV55Single、WujiLyricistNode、WujiMusicianACEStep15XL、sd15-t2i-basic、sd15-t2i-lora、node

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
