---
key: 视频生成/图生视频/通义万相wan2.1 图生视频 720P高清版_1894738389084602370.json
name: 通义万相wan2.1 图生视频 720P高清版_1894738389084602370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/通义万相wan2.1 图生视频 720P高清版_1894738389084602370.json
hash: e8ee1026435a30d8
coverage: 0.928571
learned_at: 2026-10-15 22:29:16
nodes: [WanVideoBlockSwap, LoadWanVideoClipTextEncoder, WanVideoSampler, WanVideoModelLoader, WanVideoVAELoader, WanVideoImageClipEncode, Int, LoadWanVideoT5TextEncoder, WanVideoTextEncode, VHS_VideoCombine, TextInput_, LoadImage, Note, WanVideoDecode]
patterns: []
missing: []
---

# 视频生成/图生视频/通义万相wan2.1 图生视频 720P高清版_1894738389084602370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1894738389084602370.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（14 个）：
- `WanVideoBlockSwap`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoImageClipEncode`
- `Int`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `TextInput_`
- `LoadImage`
- `Note`
- `WanVideoDecode`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`WanVideoBlockSwap`、`LoadWanVideoClipTextEncoder`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoImageClipEncode`、`Int`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`VHS_VideoCombine`、`TextInput_`、`LoadImage`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
