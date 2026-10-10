---
key: 视频生成/文生视频/（支持真人-图像参考）SeeDance2.0平替T2V 新版全能G视频15S(贞贞的工坊API版)_2028108211923980289.json
name: （支持真人-图像参考）SeeDance2.0平替T2V 新版全能G视频15S(贞贞的工坊API版)_2028108211923980289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（支持真人-图像参考）SeeDance2.0平替T2V 新版全能G视频15S(贞贞的工坊API版)_2028108211923980289.json
hash: 6b5543f4852f85f4
coverage: 0.375
learned_at: 2026-10-11 03:16:53
nodes: [Comfly_api_set, easy showAnything, easy showAnything, easy showAnything, ComflyGrok3VideoApi, SaveVideo, CR Prompt Text, Note]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/（支持真人-图像参考）SeeDance2.0平替T2V 新版全能G视频15S(贞贞的工坊API版)_2028108211923980289.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（支持真人-图像参考）SeeDance2.0平替T2V 新版全能G视频15S(贞贞的工坊API版)_2028108211923980289.json`

## 结构

**生成流程**：Output → Other

**节点**（8 个）：
- `Comfly_api_set`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `ComflyGrok3VideoApi`
- `SaveVideo`
- `CR Prompt Text`
- `Note`

## 知识

覆盖率 **38%**（3/8）

**有卡**：`Comfly_api_set`、`ComflyGrok3VideoApi`、`SaveVideo`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：SaveVideo、Comfly_api_set、ComflyGrok3VideoApi、sd15-t2i-basic、sd15-t2i-lora、Text、CLIPTextEncode、CLIPLoader

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
