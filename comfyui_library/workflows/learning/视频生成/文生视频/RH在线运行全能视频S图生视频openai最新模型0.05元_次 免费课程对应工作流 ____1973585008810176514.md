---
key: 视频生成/文生视频/RH在线运行全能视频S图生视频openai最新模型0.05元_次 免费课程对应工作流 ____1973585008810176514.json
name: RH在线运行全能视频S图生视频openai最新模型0.05元_次 免费课程对应工作流 ____1973585008810176514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/RH在线运行全能视频S图生视频openai最新模型0.05元_次 免费课程对应工作流 ____1973585008810176514.json
hash: 901287a862b4793a
coverage: 0.583333
learned_at: 2026-10-10 23:05:09
nodes: [easy showAnything, LoadImage, SaveVideo, easy showAnything, RH_Sora2_I2V, CR Prompt Text, RH_Sora2_T2V, ShowText, RH_LLMAPI_NODE, Fast Groups Muter (rgthree), CR Text, SaveVideo]
patterns: []
missing: [CR Text, CR Prompt Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/RH在线运行全能视频S图生视频openai最新模型0.05元_次 免费课程对应工作流 ____1973585008810176514.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/RH在线运行全能视频S图生视频openai最新模型0.05元_次 免费课程对应工作流 ____1973585008810176514.json`

## 结构

**生成流程**：Output → Other

**节点**（12 个）：
- `easy showAnything`
- `LoadImage`
- `SaveVideo`
- `easy showAnything`
- `RH_Sora2_I2V`
- `CR Prompt Text`
- `RH_Sora2_T2V`
- `ShowText`
- `RH_LLMAPI_NODE`
- `Fast Groups Muter (rgthree)`
- `CR Text`
- `SaveVideo`

## 知识

覆盖率 **58%**（7/12）

**有卡**：`LoadImage`、`SaveVideo`、`RH_Sora2_I2V`、`RH_Sora2_T2V`、`ShowText`、`RH_LLMAPI_NODE`

**缺卡**（2）：`CR Text`、`CR Prompt Text`

**用到的条目**：LoadImage、SaveVideo、RH_LLMAPI_NODE、ShowText、RH_Sora2_I2V、RH_Sora2_T2V、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
