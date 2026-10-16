---
key: 视频生成/图生视频/InfiniteTalk（Lightx2v+Rcm） -数字人唱歌-长时稳定不变色_2014949900475174914.json
name: InfiniteTalk（Lightx2v+Rcm） -数字人唱歌-长时稳定不变色_2014949900475174914.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2014949900475174914.json
hash: c5a0ec977f663b66
coverage: 0.903226
learned_at: 2026-10-15 22:34:37
nodes: [WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoVAELoader, LoadWanVideoT5TextEncoder, Reroute, Reroute, GetImageSizeAndCount, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoClipVisionEncode, MultiTalkWav2VecEmbeds, PreviewAny, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoModelLoader, JWFloat, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoDecode, DownloadAndLoadWav2VecModel, Audio Duration (mtb), WanVideoTextEncode, SimpleMath+, VHS_VideoCombine, Float, LoadImage, LoadAudio, JWInteger, AudioCrop, AudioSeparation, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/InfiniteTalk（Lightx2v+Rcm） -数字人唱歌-长时稳定不变色_2014949900475174914.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2014949900475174914.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `Reroute`
- `Reroute`
- `GetImageSizeAndCount`
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoClipVisionEncode`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `JWFloat`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoDecode`
- `DownloadAndLoadWav2VecModel`
- `Audio Duration (mtb)`
- `WanVideoTextEncode`
- `SimpleMath+`
- `VHS_VideoCombine`
- `Float`
- `LoadImage`
- `LoadAudio`
- `JWInteger`
- `AudioCrop`
- `AudioSeparation`
- `CR Prompt Text`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`GetImageSizeAndCount`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoClipVisionEncode`、`MultiTalkWav2VecEmbeds`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`JWFloat`、`WanVideoBlockSwap`、`WanVideoDecode`、`DownloadAndLoadWav2VecModel`、`Audio Duration (mtb)`、`WanVideoTextEncode`、`SimpleMath+`、`VHS_VideoCombine`、`Float`、`LoadImage`、`LoadAudio`、`JWInteger`、`AudioCrop`、`AudioSeparation`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
