---
key: 视频生成/文生视频/最新全能视频S文生视频（RH API版-国庆0.05元_10秒）_1973574689153003522.json
name: 最新全能视频S文生视频（RH API版-国庆0.05元_10秒）_1973574689153003522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/最新全能视频S文生视频（RH API版-国庆0.05元_10秒）_1973574689153003522.json
hash: d7e1ffa7da76af9a
coverage: 0.333333
learned_at: 2026-10-10 23:13:24
nodes: [SaveVideo, easy showAnything, easy showAnything, RH_Sora2_T2V, Text Concatenate, CR Prompt Text, CR Prompt Text, VHS_LoadVideo, MarkdownNote]
patterns: []
missing: [Text Concatenate, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/最新全能视频S文生视频（RH API版-国庆0.05元_10秒）_1973574689153003522.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/最新全能视频S文生视频（RH API版-国庆0.05元_10秒）_1973574689153003522.json`

## 结构

**生成流程**：Output → Other

**节点**（9 个）：
- `SaveVideo`
- `easy showAnything`
- `easy showAnything`
- `RH_Sora2_T2V`
- `Text Concatenate`
- `CR Prompt Text`
- `CR Prompt Text`
- `VHS_LoadVideo`
- `MarkdownNote`

## 知识

覆盖率 **33%**（3/9）

**有卡**：`SaveVideo`、`RH_Sora2_T2V`、`VHS_LoadVideo`

**缺卡**（3）：`Text Concatenate`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：SaveVideo、VHS_LoadVideo、RH_Sora2_T2V、sd15-t2i-basic、sd15-t2i-lora、LoadVideo、Text、CLIPTextEncode

## 学习发现

- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
