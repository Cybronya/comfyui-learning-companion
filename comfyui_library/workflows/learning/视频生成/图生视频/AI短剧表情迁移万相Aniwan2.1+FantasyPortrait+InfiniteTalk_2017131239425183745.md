---
key: 视频生成/图生视频/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2017131239425183745.json
name: AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2017131239425183745.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2017131239425183745.json
hash: c7830a9ec0190829
coverage: 0.945946
learned_at: 2026-10-15 22:34:45
nodes: [MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, easy showAnything, SoundFlow_GetLength, SimpleMath+, ToInt, SoundFlow_Fade, VHS_VideoInfo, JWInteger, JWInteger, LoadImage, VHS_LoadVideo, Fast Groups Bypasser (rgthree), ImageResizeKJv2, ImageResizeKJv2, FantasyPortraitFaceDetector, WanVideoTorchCompileSettings, FantasyPortraitModelLoader, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoDecode, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, WanVideoModelLoader, MultiTalkModelLoader, WanVideoAddFantasyPortrait, JWInteger, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2017131239425183745.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2017131239425183745.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `easy showAnything`
- `SoundFlow_GetLength`
- `SimpleMath+`
- `ToInt`
- `SoundFlow_Fade`
- `VHS_VideoInfo`
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `VHS_LoadVideo`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `FantasyPortraitFaceDetector`
- `WanVideoTorchCompileSettings`
- `FantasyPortraitModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `MultiTalkModelLoader`
- `WanVideoAddFantasyPortrait`
- `JWInteger`
- `VHS_VideoCombine`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`SoundFlow_GetLength`、`SimpleMath+`、`ToInt`、`SoundFlow_Fade`、`VHS_VideoInfo`、`JWInteger`、`LoadImage`、`VHS_LoadVideo`、`ImageResizeKJv2`、`FantasyPortraitFaceDetector`、`WanVideoTorchCompileSettings`、`FantasyPortraitModelLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`WanVideoAddFantasyPortrait`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
