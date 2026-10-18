---
key: 视频生成/图生视频/Wan2.1阿里通义万相图生视频工作流_1894957699035693057.json
name: Wan2.1阿里通义万相图生视频工作流_1894957699035693057.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1阿里通义万相图生视频工作流_1894957699035693057.json
hash: b33e6e57f0e043a1
coverage: 1
learned_at: 2026-10-15 22:29:17
nodes: [WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, LoadImage, Primitive integer [Crystools], VHS_VideoCombine, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoBlockSwap, Primitive string [Crystools], LoadWanVideoT5TextEncoder, WanVideoImageClipEncode, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1阿里通义万相图生视频工作流_1894957699035693057.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1894957699035693057.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（14 个）：
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `LoadImage`
- `Primitive integer [Crystools]`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoBlockSwap`
- `Primitive string [Crystools]`
- `LoadWanVideoT5TextEncoder`
- `WanVideoImageClipEncode`
- `WanVideoTextEncode`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`LoadImage`、`Primitive integer [Crystools]`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoBlockSwap`、`Primitive string [Crystools]`、`LoadWanVideoT5TextEncoder`、`WanVideoImageClipEncode`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
