---
key: 平台全量/Wan2.2+Animate：角色动作迁移 美女跳舞 角色替换、动作迁移、图生视频_1981904836633477121.json
name: Wan2.2+Animate：角色动作迁移 美女跳舞 角色替换、动作迁移、图生视频_1981904836633477121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2+Animate：角色动作迁移 美女跳舞 角色替换、动作迁移、图生视频_1981904836633477121.json
hash: 59324057be8dc5eb
coverage: 0.964286
learned_at: 2026-11-14 01:05:51
nodes: [ImageConcatMulti, PixelPerfectResolution, DWPreprocessor, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, MarkdownNote, WanVideoSetLoRAs, ImageResizeKJv2, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, Text, JWInteger, WanVideoSampler, ImageConcatMulti, GetImageSizeAndCount, WanVideoDecode, VHS_VideoCombine, VHS_LoadVideo, VHS_VideoCombine, RHHiddenNodes, JWInteger, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoLoraSelectMulti, LoadImage]
patterns: []
missing: []
---

# 平台全量/Wan2.2+Animate：角色动作迁移 美女跳舞 角色替换、动作迁移、图生视频_1981904836633477121.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2+Animate：角色动作迁移 美女跳舞 角色替换、动作迁移、图生视频_1981904836633477121.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `ImageConcatMulti`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `MarkdownNote`
- `WanVideoSetLoRAs`
- `ImageResizeKJv2`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `Text`
- `JWInteger`
- `WanVideoSampler` ★核心
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `JWInteger`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `LoadImage`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`ImageConcatMulti`、`PixelPerfectResolution`、`DWPreprocessor`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`Text`、`JWInteger`、`WanVideoSampler`、`GetImageSizeAndCount`、`WanVideoDecode`、`VHS_VideoCombine`、`VHS_LoadVideo`、`RHHiddenNodes`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
