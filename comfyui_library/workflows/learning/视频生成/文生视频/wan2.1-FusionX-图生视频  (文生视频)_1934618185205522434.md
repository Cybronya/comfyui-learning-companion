---
key: 视频生成/文生视频/wan2.1-FusionX-图生视频  (文生视频)_1934618185205522434.json
name: wan2.1-FusionX-图生视频  (文生视频)_1934618185205522434.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.1-FusionX-图生视频  (文生视频)_1934618185205522434.json
hash: 3a703d468555f6b0
coverage: 1
learned_at: 2026-10-15 22:43:27
nodes: [WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoDecode, WanVideoSLG, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoVAELoader, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, VHS_VideoCombine, WanVideoModelLoader, LoadAndResizeImage]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.1-FusionX-图生视频  (文生视频)_1934618185205522434.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1934618185205522434.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（15 个）：
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoDecode`
- `WanVideoSLG`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `LoadAndResizeImage`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`WanVideoSLG`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`WanVideoTeaCache`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoModelLoader`、`LoadAndResizeImage`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、LoadAndResizeImage、VHS_VideoCombine
