---
key: 音频生成/音频生成/IndexTTS2-VectorEmo_Multi_Clone_2068687860949143553.json
name: IndexTTS2-VectorEmo_Multi_Clone_2068687860949143553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/IndexTTS2-VectorEmo_Multi_Clone_2068687860949143553.json
hash: 55812a06cbde126b
coverage: 0.888889
learned_at: 2026-10-18 03:04:50
nodes: [easy downloadIndexTTSAndLoadModel, easy indexTTSEmotionVector, easy indexTTSEmotionMerge, easy indexTTSEmotionVector, PrimitiveStringMultiline, SaveAudioMP3, easy indexTTSGenerateSimple, LoadAudio, LoadAudio]
patterns: []
missing: []
---

# 音频生成/音频生成/IndexTTS2-VectorEmo_Multi_Clone_2068687860949143553.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/IndexTTS2-VectorEmo_Multi_Clone_2068687860949143553.json`

## 结构

**生成流程**：Output → Other

**节点**（9 个）：
- `easy downloadIndexTTSAndLoadModel`
- `easy indexTTSEmotionVector`
- `easy indexTTSEmotionMerge`
- `easy indexTTSEmotionVector`
- `PrimitiveStringMultiline`
- `SaveAudioMP3`
- `easy indexTTSGenerateSimple`
- `LoadAudio`
- `LoadAudio`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`easy downloadIndexTTSAndLoadModel`、`easy indexTTSEmotionVector`、`easy indexTTSEmotionMerge`、`SaveAudioMP3`、`easy indexTTSGenerateSimple`、`LoadAudio`

**用到的条目**：SaveAudioMP3、LoadAudio、easy downloadIndexTTSAndLoadModel、easy indexTTSEmotionVector、easy indexTTSGenerateSimple、easy indexTTSEmotionMerge、sd15-t2i-basic、sd15-t2i-lora
