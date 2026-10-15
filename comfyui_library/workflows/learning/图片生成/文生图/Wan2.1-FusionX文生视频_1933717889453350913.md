---
key: 图片生成/文生图/Wan2.1-FusionX文生视频_1933717889453350913.json
name: Wan2.1-FusionX文生视频_1933717889453350913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.1-FusionX文生视频_1933717889453350913.json
hash: 934ad23f25805c58
coverage: 1
learned_at: 2026-10-15 22:27:34
nodes: [WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoModelLoader, JWInteger, JWInteger, Primitive integer [Crystools], WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoEmptyEmbeds, Text Multiline, WanVideoExperimentalArgs, WanVideoTextEncode, Primitive integer [Crystools], WanVideoSampler, WanVideoDecode, VHS_VideoCombine, WanVideoSLG]
patterns: []
missing: []
---

# 图片生成/文生图/Wan2.1-FusionX文生视频_1933717889453350913.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.1-FusionX文生视频_1933717889453350913.json`

## 结构

**生成流程**：Model → Sampling → Other

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
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSLG`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`JWInteger`、`Primitive integer [Crystools]`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoEmptyEmbeds`、`Text Multiline`、`WanVideoExperimentalArgs`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSLG`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、VHS_VideoCombine、WanVideoBlockSwap、WanVideoModelLoader
