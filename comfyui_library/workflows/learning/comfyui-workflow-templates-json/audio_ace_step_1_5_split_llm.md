---
key: comfyui-workflow-templates-json/audio_ace_step_1_5_split_llm.json
name: audio_ace_step_1_5_split_llm
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step_1_5_split_llm.json
hash: 606af2b2c9a95a73
official: true
coverage: 0.571429
learned_at: 2026-10-10 22:46:56
nodes: [PreviewAny, RegexExtract, 7aaae2b3-4151-4452-854b-653cf02fb752, RegexExtract, MarkdownNote, SaveAudioAdvanced, GeminiNodeV2]
patterns: []
missing: [7aaae2b3-4151-4452-854b-653cf02fb752]
discoveries: [次要节点 `7aaae2b3-4151-4452-854b-653cf02fb752` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/audio_ace_step_1_5_split_llm.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step_1_5_split_llm.json`

## 结构

**生成流程**：Output → Other

**节点**（7 个）：
- `PreviewAny`
- `RegexExtract`
- `7aaae2b3-4151-4452-854b-653cf02fb752`
- `RegexExtract`
- `MarkdownNote`
- `SaveAudioAdvanced`
- `GeminiNodeV2`

## 知识

覆盖率 **57%**（4/7）

**有卡**：`RegexExtract`、`SaveAudioAdvanced`、`GeminiNodeV2`

**缺卡**（1）：`7aaae2b3-4151-4452-854b-653cf02fb752`

**用到的条目**：SaveAudioAdvanced、RegexExtract、GeminiNodeV2、sd15-t2i-basic、sd15-t2i-lora、SaveAudio、node、v2

## 学习发现

- 次要节点 `7aaae2b3-4151-4452-854b-653cf02fb752` 知识库中没有该节点类型的任何知识
