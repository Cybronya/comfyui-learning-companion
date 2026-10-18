---
key: 视频生成/图生视频/wan2.1 MAGREF 3倍加速图生视频_1941396132272750594.json
name: wan2.1 MAGREF 3倍加速图生视频_1941396132272750594.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1 MAGREF 3倍加速图生视频_1941396132272750594.json
hash: 4bcb6245cc6dd72a
coverage: 0.916667
learned_at: 2026-10-15 22:30:35
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoBlockSwap, CLIPVisionLoader, DF_Integer, DF_Integer, WanVideoVAELoader, PreviewImage, WanVideoClipVisionEncode, WanVideoTextEncode, WanVideoImageToVideoEncode, WanVideoDecode, DF_Integer, WanVideoSampler, DF_Integer, DF_Integer, LoadImage, JjkText, LoadWanVideoT5TextEncoder, easy imageRemBg, SimpleMath+, ImageResizeKJv2, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1 MAGREF 3倍加速图生视频_1941396132272750594.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1941396132272750594.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（24 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `DF_Integer`
- `DF_Integer`
- `WanVideoVAELoader`
- `PreviewImage`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoDecode`
- `DF_Integer`
- `WanVideoSampler` ★核心
- `DF_Integer`
- `DF_Integer`
- `LoadImage`
- `JjkText`
- `LoadWanVideoT5TextEncoder`
- `easy imageRemBg`
- `SimpleMath+`
- `ImageResizeKJv2`
- `VHS_VideoCombine`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`DF_Integer`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`WanVideoSampler`、`LoadImage`、`LoadWanVideoT5TextEncoder`、`easy imageRemBg`、`SimpleMath+`、`ImageResizeKJv2`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
