---
key: 图片生成/文生图/Wan2.1-FusionX文生视频_1933717889453350913.json
name: Wan2.1-FusionX文生视频_1933717889453350913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.1-FusionX文生视频_1933717889453350913.json
hash: 934ad23f25805c58
coverage: 0.833333
learned_at: 2026-10-10 20:59:13
nodes: [WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoModelLoader, JWInteger, JWInteger, Primitive integer [Crystools], WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoEmptyEmbeds, Text Multiline, WanVideoExperimentalArgs, WanVideoTextEncode, Primitive integer [Crystools], WanVideoSampler, WanVideoDecode, VHS_VideoCombine, WanVideoSLG]
patterns: []
missing: [Primitive integer [Crystools], Primitive integer [Crystools], Text Multiline]
discoveries: [次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Wan2.1-FusionX文生视频_1933717889453350913.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.1-FusionX文生视频_1933717889453350913.json`

## 结构

**节点**（18 个）：
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `JWInteger`
- `JWInteger`
- `Primitive integer [Crystools]`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoEmptyEmbeds`
- `Text Multiline`
- `WanVideoExperimentalArgs`
- `WanVideoTextEncode`
- `Primitive integer [Crystools]`
- `WanVideoSampler`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSLG`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`JWInteger`、`Primitive integer [Crystools]`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoEmptyEmbeds`、`Text Multiline`、`WanVideoExperimentalArgs`、`WanVideoTextEncode`、`WanVideoSampler`

**缺卡**（3）：`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`Text Multiline`

## 学习发现

- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
