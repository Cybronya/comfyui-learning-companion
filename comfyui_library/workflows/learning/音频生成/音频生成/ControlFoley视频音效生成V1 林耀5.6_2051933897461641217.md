---
key: 音频生成/音频生成/ControlFoley视频音效生成V1 林耀5.6_2051933897461641217.json
name: ControlFoley视频音效生成V1 林耀5.6_2051933897461641217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ControlFoley视频音效生成V1 林耀5.6_2051933897461641217.json
hash: 4e71fa5290a9c5a2
coverage: 0.75
learned_at: 2026-10-18 03:04:48
nodes: [RunningHubControlFoleyModelLoader, GetVideoComponents, GetVideoComponents, CreateVideo, RunningHubControlFoleyGenerator, SaveAudio, GetVideoComponents, Any To Any, VHS_VideoCombine, CR Prompt Text, VHS_SelectFilename, Qwen3_VQA, easy showAnything, SaveVideo, MarkdownNote, LoadVideo]
patterns: []
missing: [RunningHubControlFoleyGenerator, RunningHubControlFoleyModelLoader]
discoveries: [次要节点 `RunningHubControlFoleyGenerator` 知识库中没有该节点类型的任何知识, 次要节点 `RunningHubControlFoleyModelLoader` 知识库中没有该节点类型的任何知识]
---

# 音频生成/音频生成/ControlFoley视频音效生成V1 林耀5.6_2051933897461641217.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ControlFoley视频音效生成V1 林耀5.6_2051933897461641217.json`

## 结构

**生成流程**：Output → Other

**节点**（16 个）：
- `RunningHubControlFoleyModelLoader`
- `GetVideoComponents`
- `GetVideoComponents`
- `CreateVideo`
- `RunningHubControlFoleyGenerator`
- `SaveAudio`
- `GetVideoComponents`
- `Any To Any`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `VHS_SelectFilename`
- `Qwen3_VQA`
- `easy showAnything`
- `SaveVideo`
- `MarkdownNote`
- `LoadVideo`

## 知识

覆盖率 **75%**（12/16）

**有卡**：`GetVideoComponents`、`CreateVideo`、`SaveAudio`、`Any To Any`、`VHS_VideoCombine`、`CR Prompt Text`、`VHS_SelectFilename`、`Qwen3_VQA`、`SaveVideo`、`LoadVideo`

**缺卡**（2）：`RunningHubControlFoleyGenerator`、`RunningHubControlFoleyModelLoader`

**用到的条目**：CR Prompt Text、SaveAudio、SaveVideo、CreateVideo、GetVideoComponents、LoadVideo、Qwen3_VQA、VHS_VideoCombine

## 学习发现

- 次要节点 `RunningHubControlFoleyGenerator` 知识库中没有该节点类型的任何知识
- 次要节点 `RunningHubControlFoleyModelLoader` 知识库中没有该节点类型的任何知识
