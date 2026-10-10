---
key: 🔥即梦 Seedream 5.0 PRO 文生图工作流，出图质量绝了！_2106676453466263554.json
name: 🔥即梦 Seedream 5.0 PRO 文生图工作流，出图质量绝了！_2106676453466263554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/🔥即梦 Seedream 5.0 PRO 文生图工作流，出图质量绝了！_2106676453466263554.json
hash: 5e3978188fe5ac91
coverage: 0.666667
learned_at: 2026-10-10 21:00:01
nodes: [SaveImage, Text, RH_SeedreamV5ProTextToImage]
patterns: []
missing: [RH_SeedreamV5ProTextToImage]
discoveries: [次要节点 `RH_SeedreamV5ProTextToImage` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 🔥即梦 Seedream 5.0 PRO 文生图工作流，出图质量绝了！_2106676453466263554.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/🔥即梦 Seedream 5.0 PRO 文生图工作流，出图质量绝了！_2106676453466263554.json`

## 结构

**生成流程**：Output → Other

**节点**（3 个）：
- `SaveImage`
- `Text`
- `RH_SeedreamV5ProTextToImage`

## 知识

覆盖率 **67%**（2/3）

**有卡**：`SaveImage`、`Text`

**缺卡**（1）：`RH_SeedreamV5ProTextToImage`

**用到的条目**：SaveImage、Text、sd15-t2i-basic、sd15-t2i-lora、Seed、sampler_name 调整经验、steps 调整经验、cfg 调整经验

## 学习发现

- 次要节点 `RH_SeedreamV5ProTextToImage` 仅有 KSampler 的通用知识，没有该节点自己的说明
