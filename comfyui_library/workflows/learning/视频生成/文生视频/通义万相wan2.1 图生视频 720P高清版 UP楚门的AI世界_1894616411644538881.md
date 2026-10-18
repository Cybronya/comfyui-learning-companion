---
key: 视频生成/文生视频/通义万相wan2.1 图生视频 720P高清版 UP楚门的AI世界_1894616411644538881.json
name: 通义万相wan2.1 图生视频 720P高清版 UP楚门的AI世界_1894616411644538881.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/通义万相wan2.1 图生视频 720P高清版 UP楚门的AI世界_1894616411644538881.json
hash: 206d346b68823f4e
coverage: 0.928571
learned_at: 2026-10-15 22:43:19
nodes: [WanVideoBlockSwap, LoadWanVideoClipTextEncoder, WanVideoDecode, VHS_VideoCombine, WanVideoSampler, WanVideoModelLoader, LoadImage, WanVideoVAELoader, WanVideoImageClipEncode, Int, WanVideoTextEncode, TextInput_, Note, LoadWanVideoT5TextEncoder]
patterns: []
missing: []
---

# 视频生成/文生视频/通义万相wan2.1 图生视频 720P高清版 UP楚门的AI世界_1894616411644538881.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1894616411644538881.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（14 个）：
- `WanVideoBlockSwap`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `LoadImage`
- `WanVideoVAELoader`
- `WanVideoImageClipEncode`
- `Int`
- `WanVideoTextEncode`
- `TextInput_`
- `Note`
- `LoadWanVideoT5TextEncoder`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`WanVideoBlockSwap`、`LoadWanVideoClipTextEncoder`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoModelLoader`、`LoadImage`、`WanVideoVAELoader`、`WanVideoImageClipEncode`、`Int`、`WanVideoTextEncode`、`TextInput_`、`LoadWanVideoT5TextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
