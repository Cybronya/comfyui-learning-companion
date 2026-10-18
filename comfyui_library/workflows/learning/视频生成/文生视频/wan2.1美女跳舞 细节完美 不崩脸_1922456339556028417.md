---
key: 视频生成/文生视频/wan2.1美女跳舞 细节完美 不崩脸_1922456339556028417.json
name: wan2.1美女跳舞 细节完美 不崩脸_1922456339556028417.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.1美女跳舞 细节完美 不崩脸_1922456339556028417.json
hash: b7609b4bf267f503
coverage: 1
learned_at: 2026-10-15 22:43:23
nodes: [WanVideoBlockSwap, WanVideoTeaCache, WanVideoSLG, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoImageClipEncode, WanVideoSampler, WanVideoExperimentalArgs, LoadImage, VHS_VideoCombine, WanVideoDecode, WanVideoLoraSelect, WanVideoTextEncode, LoadWanVideoClipTextEncoder]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.1美女跳舞 细节完美 不崩脸_1922456339556028417.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1922456339556028417.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（15 个）：
- `WanVideoBlockSwap`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoImageClipEncode`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `LoadWanVideoClipTextEncoder` ★核心

## 知识

覆盖率 **100%**（15/15）

**有卡**：`WanVideoBlockSwap`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoImageClipEncode`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`LoadImage`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`LoadWanVideoClipTextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
