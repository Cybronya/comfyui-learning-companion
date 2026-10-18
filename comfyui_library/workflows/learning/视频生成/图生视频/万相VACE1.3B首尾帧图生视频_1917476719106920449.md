---
key: 视频生成/图生视频/万相VACE1.3B首尾帧图生视频_1917476719106920449.json
name: 万相VACE1.3B首尾帧图生视频_1917476719106920449.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/万相VACE1.3B首尾帧图生视频_1917476719106920449.json
hash: 7ef8a1a35671522b
coverage: 1
learned_at: 2026-10-15 22:29:40
nodes: [WanVideoTeaCache, VHS_VideoCombine, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoTorchCompileSettings, WanVideoVACEStartToEndFrame, WanVideoVAELoader, WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoModelLoader, LoadImage, LoadImage, ImageResizeKJ, ImageResizeKJ, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/万相VACE1.3B首尾帧图生视频_1917476719106920449.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1917476719106920449.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（16 个）：
- `WanVideoTeaCache`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `Int`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`WanVideoTeaCache`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoVACEEncode`、`WanVideoTorchCompileSettings`、`WanVideoVACEStartToEndFrame`、`WanVideoVAELoader`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`LoadImage`、`ImageResizeKJ`、`Int`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、ImageResizeKJ
