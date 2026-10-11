---
key: 视频生成/文生视频/Seedance2.0多参满血版视频生成_2057668238007431169.json
name: Seedance2.0多参满血版视频生成_2057668238007431169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Seedance2.0多参满血版视频生成_2057668238007431169.json
hash: 32fcffe275d778d2
coverage: 0.875
learned_at: 2026-10-11 19:49:42
nodes: [SaveVideo, LoadImage, LoadImage, LoadAudio, LoadImage, LoadImage, RH_BytedanceSeedance20GlobalMultimodalVideo, CR Prompt Text]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Seedance2.0多参满血版视频生成_2057668238007431169.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Seedance2.0多参满血版视频生成_2057668238007431169.json`

## 结构

**生成流程**：Output → Other

**节点**（8 个）：
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `RH_BytedanceSeedance20GlobalMultimodalVideo`
- `CR Prompt Text`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`SaveVideo`、`LoadImage`、`LoadAudio`、`RH_BytedanceSeedance20GlobalMultimodalVideo`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：LoadImage、RH_BytedanceSeedance20GlobalMultimodalVideo、SaveVideo、LoadAudio、sd15-t2i-basic、sd15-t2i-lora、Seed、Text

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
