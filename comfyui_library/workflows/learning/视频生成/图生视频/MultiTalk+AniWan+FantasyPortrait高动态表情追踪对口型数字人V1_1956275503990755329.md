---
key: 视频生成/图生视频/MultiTalk+AniWan+FantasyPortrait高动态表情追踪对口型数字人V1_1956275503990755329.json
name: MultiTalk+AniWan+FantasyPortrait高动态表情追踪对口型数字人V1_1956275503990755329.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956275503990755329.json
hash: a6b85bef568913dd
coverage: 0.925
learned_at: 2026-10-15 22:31:12
nodes: [WanVideoClipVisionEncode, CLIPVisionLoader, MarkdownNote, WanVideoTextEncodeCached, GetNode, FantasyPortraitFaceDetector, ImageConcatMulti, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageConcatMulti, WanVideoLoraSelect, FantasyPortraitModelLoader, WanVideoModelLoader, WanVideoAddFantasyPortrait, WanVideoDecode, INTConstant, INTConstant, ImageResizeKJv2, INTConstant, WanVideoSampler, ImageResizeKJv2, JWInteger, JWInteger, MultiTalkModelLoader, SimpleMath+, DownloadAndLoadWav2VecModel, SoundFlow_GetLength, WanVideoImageToVideoEncode, WanVideoVAELoader, MultiTalkWav2VecEmbeds, LoadImage, SoundFlow_Fade, ToInt, easy showAnything, VHS_VideoCombine, VHS_VideoInfo, VHS_LoadVideo, VHS_VideoCombine, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/MultiTalk+AniWan+FantasyPortrait高动态表情追踪对口型数字人V1_1956275503990755329.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956275503990755329.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `MarkdownNote`
- `WanVideoTextEncodeCached`
- `GetNode`
- `FantasyPortraitFaceDetector`
- `ImageConcatMulti`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ImageConcatMulti`
- `WanVideoLoraSelect`
- `FantasyPortraitModelLoader`
- `WanVideoModelLoader`
- `WanVideoAddFantasyPortrait`
- `WanVideoDecode`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `INTConstant`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `JWInteger`
- `JWInteger`
- `MultiTalkModelLoader`
- `SimpleMath+`
- `DownloadAndLoadWav2VecModel`
- `SoundFlow_GetLength`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `MultiTalkWav2VecEmbeds`
- `LoadImage`
- `SoundFlow_Fade`
- `ToInt`
- `easy showAnything`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `JWInteger`

## 知识

覆盖率 **92%**（37/40）

**有卡**：`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`FantasyPortraitFaceDetector`、`ImageConcatMulti`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`FantasyPortraitModelLoader`、`WanVideoModelLoader`、`WanVideoAddFantasyPortrait`、`WanVideoDecode`、`INTConstant`、`ImageResizeKJv2`、`WanVideoSampler`、`JWInteger`、`MultiTalkModelLoader`、`SimpleMath+`、`DownloadAndLoadWav2VecModel`、`SoundFlow_GetLength`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`MultiTalkWav2VecEmbeds`、`LoadImage`、`SoundFlow_Fade`、`ToInt`、`VHS_VideoCombine`、`VHS_VideoInfo`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
