---
key: 视频生成/文生视频/全能视频S.0丨文生视频(15秒）_1985570883857264642.json
name: 全能视频S.0丨文生视频(15秒）_1985570883857264642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/全能视频S.0丨文生视频(15秒）_1985570883857264642.json
hash: 0b3ceb21e0c78b28
coverage: 0.285714
learned_at: 2026-10-11 02:45:04
nodes: [JjkText, easy showAnything, CR Seed, RH_Sora2_T2V, easy showAnything, easy showAnything, SaveVideo]
patterns: []
missing: [CR Seed]
discoveries: [次要节点 `CR Seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/全能视频S.0丨文生视频(15秒）_1985570883857264642.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/全能视频S.0丨文生视频(15秒）_1985570883857264642.json`

## 结构

**生成流程**：Output → Other

**节点**（7 个）：
- `JjkText`
- `easy showAnything`
- `CR Seed`
- `RH_Sora2_T2V`
- `easy showAnything`
- `easy showAnything`
- `SaveVideo`

## 知识

覆盖率 **29%**（2/7）

**有卡**：`RH_Sora2_T2V`、`SaveVideo`

**缺卡**（1）：`CR Seed`

**用到的条目**：SaveVideo、RH_Sora2_T2V、sd15-t2i-basic、sd15-t2i-lora、Seed、Text、sampler_name 调整经验、steps 调整经验

## 学习发现

- 次要节点 `CR Seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
