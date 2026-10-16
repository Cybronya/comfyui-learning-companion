---
key: 视频生成/图生视频/InfiniteTalk+wan2.1单图片_视频生成口播数字人视频_1958754013288296450.json
name: InfiniteTalk+wan2.1单图片_视频生成口播数字人视频_1958754013288296450.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1958754013288296450.json
hash: 84e2fc868d937726
coverage: 0.818182
learned_at: 2026-10-15 22:31:23
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, AudioCrop, ImageResizeKJv2, PrimitiveInt, Note, PrimitiveInt, WanVideoClipVisionEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, WanVideoImageToVideoMultiTalk, MultiTalkWav2VecEmbeds, WanVideoUni3C_embeds, WanVideoUni3C_ControlnetLoader, WanVideoEncode, WanVideoSampler, WanVideoTextEncode, WanVideoDecode, VHS_VideoCombine, Note, Note, Note, JWIntegerToString, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoVAELoader, WanVideoModelLoader, AudioSeparation, VHS_LoadVideo, Text Multiline, LoadAudio, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/InfiniteTalk+wan2.1单图片_视频生成口播数字人视频_1958754013288296450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958754013288296450.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `AudioCrop`
- `ImageResizeKJv2`
- `PrimitiveInt`
- `Note`
- `PrimitiveInt`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `WanVideoImageToVideoMultiTalk`
- `MultiTalkWav2VecEmbeds`
- `WanVideoUni3C_embeds`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `Note`
- `JWIntegerToString`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `AudioSeparation`
- `VHS_LoadVideo`
- `Text Multiline`
- `LoadAudio`
- `JWInteger`

## 知识

覆盖率 **82%**（27/33）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`AudioCrop`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`DownloadAndLoadWav2VecModel`、`WanVideoImageToVideoMultiTalk`、`MultiTalkWav2VecEmbeds`、`WanVideoUni3C_embeds`、`WanVideoUni3C_ControlnetLoader`、`WanVideoEncode`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoDecode`、`VHS_VideoCombine`、`JWIntegerToString`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoVAELoader`、`WanVideoModelLoader`、`AudioSeparation`、`VHS_LoadVideo`、`Text Multiline`、`LoadAudio`、`JWInteger`

**用到的条目**：WanVideoUni3C_ControlnetLoader、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoEncode
