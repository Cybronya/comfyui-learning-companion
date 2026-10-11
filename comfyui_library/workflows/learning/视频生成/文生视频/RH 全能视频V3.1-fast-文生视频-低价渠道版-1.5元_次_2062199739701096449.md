---
key: 视频生成/文生视频/RH 全能视频V3.1-fast-文生视频-低价渠道版-1.5元_次_2062199739701096449.json
name: RH 全能视频V3.1-fast-文生视频-低价渠道版-1.5元_次_2062199739701096449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/RH 全能视频V3.1-fast-文生视频-低价渠道版-1.5元_次_2062199739701096449.json
hash: 4b2a74b4a94b3c14
coverage: 0.8
learned_at: 2026-10-11 20:21:29
nodes: [RH_RhartVideoV31FastTextToVideo, VHS_VideoCombine, VHS_VideoCombine, GetVideoComponents, CR Prompt Text]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/RH 全能视频V3.1-fast-文生视频-低价渠道版-1.5元_次_2062199739701096449.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/RH 全能视频V3.1-fast-文生视频-低价渠道版-1.5元_次_2062199739701096449.json`

## 结构

**生成流程**：Other

**节点**（5 个）：
- `RH_RhartVideoV31FastTextToVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetVideoComponents`
- `CR Prompt Text`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`RH_RhartVideoV31FastTextToVideo`、`VHS_VideoCombine`、`GetVideoComponents`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：GetVideoComponents、VHS_VideoCombine、RH_RhartVideoV31FastTextToVideo、sd15-t2i-basic、sd15-t2i-lora、Text、CLIPTextEncode、CLIPLoader

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
