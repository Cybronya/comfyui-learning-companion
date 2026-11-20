---
key: 平台全量/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2079560731955130369.json
name: AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2079560731955130369
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2079560731955130369.json
hash: 35504e1c73a91a2b
coverage: 0.945946
learned_at: 2026-11-14 00:16:55
nodes: [MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, easy showAnything, SoundFlow_GetLength, SimpleMath+, ToInt, SoundFlow_Fade, VHS_VideoInfo, JWInteger, JWInteger, VHS_LoadVideo, Fast Groups Bypasser (rgthree), ImageResizeKJv2, ImageResizeKJv2, FantasyPortraitFaceDetector, WanVideoTorchCompileSettings, FantasyPortraitModelLoader, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoDecode, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, WanVideoModelLoader, MultiTalkModelLoader, WanVideoAddFantasyPortrait, JWInteger, LoadImage]
patterns: []
missing: []
---

# 平台全量/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2079560731955130369.json

> 来源文件 `comfyui_library/workflows/平台全量/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2079560731955130369.json`

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
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `MultiTalkModelLoader`
- `WanVideoAddFantasyPortrait`
- `JWInteger`
- `LoadImage`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`SoundFlow_GetLength`、`SimpleMath+`、`ToInt`、`SoundFlow_Fade`、`VHS_VideoInfo`、`JWInteger`、`VHS_LoadVideo`、`ImageResizeKJv2`、`FantasyPortraitFaceDetector`、`WanVideoTorchCompileSettings`、`FantasyPortraitModelLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`WanVideoAddFantasyPortrait`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelect
