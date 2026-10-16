---
key: 视频生成/图生视频/wan2.1美女跳舞细节精准把控_1943857684569292801.json
name: wan2.1美女跳舞细节精准把控_1943857684569292801.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1943857684569292801.json
hash: fbe1eda294199409
coverage: 1
learned_at: 2026-10-15 22:30:39
nodes: [WanVideoLoraSelect, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTeaCache, WanVideoSLG, WanVideoTextEncode, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoImageClipEncode, WanVideoSampler, WanVideoExperimentalArgs, VHS_VideoCombine, WanVideoDecode, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1美女跳舞细节精准把控_1943857684569292801.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1943857684569292801.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（15 个）：
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoImageClipEncode`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `LoadImage`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoImageClipEncode`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`VHS_VideoCombine`、`WanVideoDecode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
