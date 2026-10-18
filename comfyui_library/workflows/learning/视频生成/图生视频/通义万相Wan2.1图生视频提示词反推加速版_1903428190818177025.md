---
key: 视频生成/图生视频/通义万相Wan2.1图生视频提示词反推加速版_1903428190818177025.json
name: 通义万相Wan2.1图生视频提示词反推加速版_1903428190818177025.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/通义万相Wan2.1图生视频提示词反推加速版_1903428190818177025.json
hash: d9700dd96ab0ca6f
coverage: 0.954545
learned_at: 2026-10-15 22:29:25
nodes: [StringFunction|pysssss, VHS_VideoCombine, DownloadAndLoadFlorence2Model, LoadImage, Florence2Run, ShowText|pysssss, WanVideoEnhanceAVideo, WanVideoContextOptions, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, Int, WanVideoImageClipEncode, WanVideoTextEncode, StringFunction|pysssss, ImageResizeKJ, ImageResizeKJ, WanVideoDecode, WanVideoSampler, WanVideoTeaCache]
patterns: []
missing: []
---

# 视频生成/图生视频/通义万相Wan2.1图生视频提示词反推加速版_1903428190818177025.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1903428190818177025.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（22 个）：
- `StringFunction|pysssss`
- `VHS_VideoCombine`
- `DownloadAndLoadFlorence2Model`
- `LoadImage`
- `Florence2Run`
- `ShowText|pysssss`
- `WanVideoEnhanceAVideo`
- `WanVideoContextOptions`
- `LoadWanVideoClipTextEncoder` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `Int`
- `WanVideoImageClipEncode`
- `WanVideoTextEncode`
- `StringFunction|pysssss`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`StringFunction|pysssss`、`VHS_VideoCombine`、`DownloadAndLoadFlorence2Model`、`LoadImage`、`Florence2Run`、`WanVideoEnhanceAVideo`、`WanVideoContextOptions`、`LoadWanVideoClipTextEncoder`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`Int`、`WanVideoImageClipEncode`、`WanVideoTextEncode`、`ImageResizeKJ`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTeaCache`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
