---
key: 视频生成/图生视频/音乐数字人（单人唱歌） wan2.2 multiTalk_1957437861178044418.json
name: 音乐数字人（单人唱歌） wan2.2 multiTalk_1957437861178044418.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/音乐数字人（单人唱歌） wan2.2 multiTalk_1957437861178044418.json
hash: 3f4c4ea285a67a35
coverage: 0.90625
learned_at: 2026-10-15 22:31:16
nodes: [WanVideoSetBlockSwap, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, INTConstant, WanVideoSampler, WanVideoDecode, Note, WanVideoModelLoader, MultiTalkModelLoader, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoSampler, DownloadAndLoadWav2VecModel, VHS_VideoCombine, WanVideoLoraSelect, CLIPVisionLoader, CreateCFGScheduleFloatList, INTConstant, WanVideoBlockSwap, JjkText, MultiTalkWav2VecEmbeds, LoadImage, easy int, ImageResizeKJv2, LoadAudio, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/音乐数字人（单人唱歌） wan2.2 multiTalk_1957437861178044418.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957437861178044418.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `Note`
- `WanVideoModelLoader`
- `MultiTalkModelLoader`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `DownloadAndLoadWav2VecModel`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `CLIPVisionLoader`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `WanVideoBlockSwap`
- `JjkText`
- `MultiTalkWav2VecEmbeds`
- `LoadImage`
- `easy int`
- `ImageResizeKJv2`
- `LoadAudio`
- `Note`

## 知识

覆盖率 **91%**（29/32）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`INTConstant`、`WanVideoSampler`、`WanVideoDecode`、`MultiTalkModelLoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`DownloadAndLoadWav2VecModel`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`CLIPVisionLoader`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`MultiTalkWav2VecEmbeds`、`LoadImage`、`easy int`、`ImageResizeKJv2`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
