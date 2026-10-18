---
key: 视频生成/图生视频/捏爆特效 捏扁特效---通义万相wan2.1 图生视频新玩儿法_1899003016236941314.json
name: 捏爆特效 捏扁特效---通义万相wan2.1 图生视频新玩儿法_1899003016236941314.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/捏爆特效 捏扁特效---通义万相wan2.1 图生视频新玩儿法_1899003016236941314.json
hash: 7371534632de7721
coverage: 0.933333
learned_at: 2026-10-15 22:29:20
nodes: [WanVideoDecode, VHS_VideoCombine, WanVideoSampler, Int, LoadImage, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoTextEncode, WanVideoImageClipEncode, Note, WanVideoVAELoader, LoadWanVideoClipTextEncoder, TextInput_]
patterns: []
missing: []
---

# 视频生成/图生视频/捏爆特效 捏扁特效---通义万相wan2.1 图生视频新玩儿法_1899003016236941314.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1899003016236941314.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（15 个）：
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `Int`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoImageClipEncode`
- `Note`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `TextInput_`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSampler`、`Int`、`LoadImage`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoImageClipEncode`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`TextInput_`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
