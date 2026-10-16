---
key: 视频生成/文生视频/通义万相Wan2.1文生视频高清补帧放大_1897231501354815489.json
name: 通义万相Wan2.1文生视频高清补帧放大_1897231501354815489.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1897231501354815489.json
hash: be196328570eb914
coverage: 1
learned_at: 2026-10-15 22:43:20
nodes: [RIFE VFI, VHS_VideoCombine, WanVideoVAELoader, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoBlockSwap, WanVideoModelLoader, WanVideoDecode, CR Upscale Image, WanVideoTextEncode, LoadWanVideoT5TextEncoder]
patterns: []
missing: []
---

# 视频生成/文生视频/通义万相Wan2.1文生视频高清补帧放大_1897231501354815489.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1897231501354815489.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（11 个）：
- `RIFE VFI`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `CR Upscale Image`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`RIFE VFI`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoEmptyEmbeds`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoDecode`、`CR Upscale Image`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、CR Upscale Image、VHS_VideoCombine、WanVideoBlockSwap
