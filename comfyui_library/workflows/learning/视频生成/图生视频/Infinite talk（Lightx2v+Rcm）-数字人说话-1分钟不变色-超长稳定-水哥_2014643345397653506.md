---
key: 视频生成/图生视频/Infinite talk（Lightx2v+Rcm）-数字人说话-1分钟不变色-超长稳定-水哥_2014643345397653506.json
name: Infinite talk（Lightx2v+Rcm）-数字人说话-1分钟不变色-超长稳定-水哥_2014643345397653506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Infinite talk（Lightx2v+Rcm）-数字人说话-1分钟不变色-超长稳定-水哥_2014643345397653506.json
hash: 9be29a27e968a98d
coverage: 0.9375
learned_at: 2026-10-15 22:34:36
nodes: [WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoVAELoader, LoadWanVideoT5TextEncoder, Reroute, GetImageSizeAndCount, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoClipVisionEncode, MultiTalkWav2VecEmbeds, PreviewAny, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoModelLoader, JWFloat, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoDecode, DownloadAndLoadWav2VecModel, WanVideoTextEncode, SimpleMath+, Float, JWInteger, VHS_VideoCombine, CR Prompt Text, LoadImage, LoadAudio, AudioSeparation, Audio Duration (mtb), Audio Cut (mtb), Int, SimpleMath+]
patterns: []
missing: []
---

# 视频生成/图生视频/Infinite talk（Lightx2v+Rcm）-数字人说话-1分钟不变色-超长稳定-水哥_2014643345397653506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2014643345397653506.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
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
- `WanVideoTextEncode`
- `SimpleMath+`
- `Float`
- `JWInteger`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `LoadImage`
- `LoadAudio`
- `AudioSeparation`
- `Audio Duration (mtb)`
- `Audio Cut (mtb)`
- `Int`
- `SimpleMath+`

## 知识

覆盖率 **94%**（30/32）

**有卡**：`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`GetImageSizeAndCount`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoClipVisionEncode`、`MultiTalkWav2VecEmbeds`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`JWFloat`、`WanVideoBlockSwap`、`WanVideoDecode`、`DownloadAndLoadWav2VecModel`、`WanVideoTextEncode`、`SimpleMath+`、`Float`、`JWInteger`、`VHS_VideoCombine`、`CR Prompt Text`、`LoadImage`、`LoadAudio`、`AudioSeparation`、`Audio Duration (mtb)`、`Audio Cut (mtb)`、`Int`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
