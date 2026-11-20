---
key: 平台全量/Wan Animate2.2动作迁移（无限时长）_2005534329495322626.json
name: Wan Animate2.2动作迁移（无限时长）_2005534329495322626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan Animate2.2动作迁移（无限时长）_2005534329495322626.json
hash: d34cc2fb4b2ff8ea
coverage: 0.888889
learned_at: 2026-11-14 01:04:00
nodes: [MarkdownNote, WanVideoDecode, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoAnimateEmbeds, ImageResizeKJv2, CR Prompt Text, WanVideoTextEncodeCached, WanVideoSampler, WanVideoModelLoader, Note, Note, Note, JWInteger, WanVideoVAELoader, SimpleMath+, OnnxDetectionModelLoader, WanVideoLoraSelectMulti, JWInteger, DrawViTPose, PoseAndFaceDetection, VHS_LoadVideo, JWInteger, JWInteger, LoadImage, VHS_VideoInfo, WanVideoUni3C_embeds, WanVideoUni3C_ControlnetLoader, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoEncode]
patterns: []
missing: []
---

# 平台全量/Wan Animate2.2动作迁移（无限时长）_2005534329495322626.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan Animate2.2动作迁移（无限时长）_2005534329495322626.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `MarkdownNote`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoAnimateEmbeds`
- `ImageResizeKJv2`
- `CR Prompt Text`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `Note`
- `Note`
- `Note`
- `JWInteger`
- `WanVideoVAELoader`
- `SimpleMath+`
- `OnnxDetectionModelLoader`
- `WanVideoLoraSelectMulti`
- `JWInteger`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `VHS_VideoInfo`
- `WanVideoUni3C_embeds`
- `WanVideoUni3C_ControlnetLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoEncode`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoAnimateEmbeds`、`ImageResizeKJv2`、`CR Prompt Text`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoModelLoader`、`JWInteger`、`WanVideoVAELoader`、`SimpleMath+`、`OnnxDetectionModelLoader`、`WanVideoLoraSelectMulti`、`DrawViTPose`、`PoseAndFaceDetection`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoInfo`、`WanVideoUni3C_embeds`、`WanVideoUni3C_ControlnetLoader`、`VHS_VideoCombine`、`WanVideoEncode`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader
