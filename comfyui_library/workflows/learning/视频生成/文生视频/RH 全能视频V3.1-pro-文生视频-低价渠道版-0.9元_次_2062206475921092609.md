---
key: 视频生成/文生视频/RH 全能视频V3.1-pro-文生视频-低价渠道版-0.9元_次_2062206475921092609.json
name: RH 全能视频V3.1-pro-文生视频-低价渠道版-0.9元_次_2062206475921092609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/RH 全能视频V3.1-pro-文生视频-低价渠道版-0.9元_次_2062206475921092609.json
hash: 4b03fce61325aaf2
coverage: 0.8
learned_at: 2026-10-11 20:21:29
nodes: [VHS_VideoCombine, VHS_VideoCombine, GetVideoComponents, RH_RhartVideoV31ProTextToVideo, CR Prompt Text]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/RH 全能视频V3.1-pro-文生视频-低价渠道版-0.9元_次_2062206475921092609.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/RH 全能视频V3.1-pro-文生视频-低价渠道版-0.9元_次_2062206475921092609.json`

## 结构

**生成流程**：Other

**节点**（5 个）：
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetVideoComponents`
- `RH_RhartVideoV31ProTextToVideo`
- `CR Prompt Text`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`VHS_VideoCombine`、`GetVideoComponents`、`RH_RhartVideoV31ProTextToVideo`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：GetVideoComponents、VHS_VideoCombine、RH_RhartVideoV31ProTextToVideo、sd15-t2i-basic、sd15-t2i-lora、Text、CLIPTextEncode、CLIPLoader

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
