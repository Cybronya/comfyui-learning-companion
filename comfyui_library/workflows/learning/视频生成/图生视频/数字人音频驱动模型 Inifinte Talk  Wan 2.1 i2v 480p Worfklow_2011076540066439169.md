---
key: 视频生成/图生视频/数字人音频驱动模型 Inifinte Talk  Wan 2.1 i2v 480p Worfklow_2011076540066439169.json
name: 数字人音频驱动模型 Inifinte Talk  Wan 2.1 i2v 480p Worfklow_2011076540066439169.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/数字人音频驱动模型 Inifinte Talk  Wan 2.1 i2v 480p Worfklow_2011076540066439169.json
hash: eef9d1764e22c642
coverage: 0.925926
learned_at: 2026-10-15 22:34:21
nodes: [MultiTalkWav2VecEmbeds, WanVideoClipVisionEncode, WanVideoDecode, GetImageSize, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoVAELoader, CLIPVisionLoader, Wav2VecModelLoader, WanVideoBlockSwap, Label (rgthree), Label (rgthree), Label (rgthree), WanVideoTextEncodeCached, Label (rgthree), WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, MarkdownNote, Label (rgthree), LoadImage, LoadAudio, MarkdownNote, ImageScale, VHS_VideoCombine, Label (rgthree), Label (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/数字人音频驱动模型 Inifinte Talk  Wan 2.1 i2v 480p Worfklow_2011076540066439169.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011076540066439169.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（27 个）：
- `MultiTalkWav2VecEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `GetImageSize`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `Wav2VecModelLoader`
- `WanVideoBlockSwap`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `WanVideoTextEncodeCached`
- `Label (rgthree)`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `MarkdownNote`
- `Label (rgthree)`
- `LoadImage`
- `LoadAudio`
- `MarkdownNote`
- `ImageScale`
- `VHS_VideoCombine`
- `Label (rgthree)`
- `Label (rgthree)`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`MultiTalkWav2VecEmbeds`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`GetImageSize`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`Wav2VecModelLoader`、`WanVideoBlockSwap`、`Label (rgthree)`、`WanVideoTextEncodeCached`、`WanVideoImageToVideoMultiTalk`、`WanVideoModelLoader`、`WanVideoSampler`、`LoadImage`、`LoadAudio`、`ImageScale`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader
