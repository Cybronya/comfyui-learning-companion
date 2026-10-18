---
key: 视频生成/图生视频/Wan2.1图生视频_1992496405681950721.json
name: Wan2.1图生视频_1992496405681950721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1图生视频_1992496405681950721.json
hash: 182649dc86bbeb5e
coverage: 1
learned_at: 2026-10-15 22:33:16
nodes: [WanVideoModelLoader, WanVideoBlockSwap, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoTextEncode, VHS_VideoCombine, WanVideoDecode, VHS_VideoCombine, ImageCASharpening+, WanVideoVAELoader, WanVideoSEImageClipEncode, ImageResize+, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1图生视频_1992496405681950721.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1992496405681950721.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（14 个）：
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `LoadWanVideoClipTextEncoder` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ImageCASharpening+`
- `WanVideoVAELoader`
- `WanVideoSEImageClipEncode`
- `ImageResize+`
- `LoadImage`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`WanVideoModelLoader`、`WanVideoBlockSwap`、`LoadWanVideoClipTextEncoder`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoDecode`、`ImageCASharpening+`、`WanVideoVAELoader`、`WanVideoSEImageClipEncode`、`ImageResize+`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoSEImageClipEncode
