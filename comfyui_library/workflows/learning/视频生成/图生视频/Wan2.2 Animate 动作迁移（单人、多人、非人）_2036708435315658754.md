---
key: 视频生成/图生视频/Wan2.2 Animate 动作迁移（单人、多人、非人）_2036708435315658754.json
name: Wan2.2 Animate 动作迁移（单人、多人、非人）_2036708435315658754.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate 动作迁移（单人、多人、非人）_2036708435315658754.json
hash: 1213c34dedc2ad0c
coverage: 1
learned_at: 2026-10-15 22:35:53
nodes: [JWInteger, OnnxDetectionModelLoader, CLIPVisionLoader, WanVideoClipVisionEncode, EmptyImage, PoseAndFaceDetection, DrawViTPose, VHS_VideoCombine, VHS_VideoCombine, WanVideoVAELoader, WanVideoAnimateEmbeds, WanVideoEncode, WanVideoUni3C_embeds, easy cleanGpuUsed, VHS_VideoInfo, WanVideoUni3C_ControlnetLoader, WanVideoTextEncodeCached, WanVideoSampler, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoDecode, WanVideoLoraSelectMulti, VHS_VideoCombine, VHS_LoadVideo, ImageResizeKJv2, LoadImage, JWInteger, Switch any [Crystools]]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate 动作迁移（单人、多人、非人）_2036708435315658754.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2036708435315658754.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `JWInteger`
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `EmptyImage`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoAnimateEmbeds`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `easy cleanGpuUsed`
- `VHS_VideoInfo`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `LoadImage`
- `JWInteger`
- `Switch any [Crystools]`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`JWInteger`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`EmptyImage`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`easy cleanGpuUsed`、`VHS_VideoInfo`、`WanVideoUni3C_ControlnetLoader`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`VHS_LoadVideo`、`ImageResizeKJv2`、`LoadImage`、`Switch any [Crystools]`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
