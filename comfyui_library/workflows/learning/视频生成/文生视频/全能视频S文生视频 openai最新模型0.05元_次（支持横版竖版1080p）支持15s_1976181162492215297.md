---
key: 视频生成/文生视频/全能视频S文生视频 openai最新模型0.05元_次（支持横版竖版1080p）支持15s_1976181162492215297.json
name: 全能视频S文生视频 openai最新模型0.05元_次（支持横版竖版1080p）支持15s_1976181162492215297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/全能视频S文生视频 openai最新模型0.05元_次（支持横版竖版1080p）支持15s_1976181162492215297.json
hash: 7eb71afe3f83023c
coverage: 0.714286
learned_at: 2026-10-10 23:11:09
nodes: [CR Prompt Text, SaveText|pysssss, ShowText, SaveVideo, ShowText, ShowText, RH_Sora2_T2V]
patterns: []
missing: [CR Prompt Text, SaveText|pysssss]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `SaveText|pysssss` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/全能视频S文生视频 openai最新模型0.05元_次（支持横版竖版1080p）支持15s_1976181162492215297.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/全能视频S文生视频 openai最新模型0.05元_次（支持横版竖版1080p）支持15s_1976181162492215297.json`

## 结构

**生成流程**：Output → Other

**节点**（7 个）：
- `CR Prompt Text`
- `SaveText|pysssss`
- `ShowText`
- `SaveVideo`
- `ShowText`
- `ShowText`
- `RH_Sora2_T2V`

## 知识

覆盖率 **71%**（5/7）

**有卡**：`ShowText`、`SaveVideo`、`RH_Sora2_T2V`

**缺卡**（2）：`CR Prompt Text`、`SaveText|pysssss`

**用到的条目**：SaveVideo、ShowText、RH_Sora2_T2V、sd15-t2i-basic、sd15-t2i-lora、SaveText、Text、CLIPTextEncode

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `SaveText|pysssss` 仅有 SaveImage 的通用知识，没有该节点自己的说明
