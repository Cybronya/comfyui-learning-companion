---
key: 视频生成/图生视频/FlashTalk稳态数字人V1（自适应比例版）林耀2.6_2019693859390885889.json
name: FlashTalk稳态数字人V1（自适应比例版）林耀2.6_2019693859390885889.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2019693859390885889.json
hash: b4d5962bffea200d
coverage: 1
learned_at: 2026-10-15 22:35:03
nodes: [RunningHub FlashTalk Loader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadAudio, SaveVideo, RunningHub FlashTalk Sampler, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/FlashTalk稳态数字人V1（自适应比例版）林耀2.6_2019693859390885889.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2019693859390885889.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（7 个）：
- `RunningHub FlashTalk Loader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadAudio`
- `SaveVideo`
- `RunningHub FlashTalk Sampler` ★核心
- `JWInteger`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`RunningHub FlashTalk Loader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`LoadAudio`、`SaveVideo`、`RunningHub FlashTalk Sampler`、`JWInteger`

**用到的条目**：LoadImage、RunningHub FlashTalk Sampler、SaveVideo、LoadAudio、JWInteger、LayerUtility: ImageScaleByAspectRatio V2、RunningHub FlashTalk Loader、sd15-t2i-basic
