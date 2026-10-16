---
key: 视频生成/图生视频/【阿良绘】数字人讲话（图生视频）_高动态Infinite talk（Lightx2v+Rcm）_1960200175715299330.json
name: 【阿良绘】数字人讲话（图生视频）_高动态Infinite talk（Lightx2v+Rcm）_1960200175715299330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1960200175715299330.json
hash: 5d509467b17677c4
coverage: 0.9375
learned_at: 2026-10-15 22:31:25
nodes: [WanVideoTextEncode, WanVideoImageToVideoMultiTalk, WanVideoClipVisionEncode, GetImageSize, WanVideoDecode, WanVideoModelLoader, WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, WanVideoSampler, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, AudioSeparation, PreviewAny, CR Text, Audio Duration (mtb), MathExpression|pysssss, MathExpression|pysssss, LoadAudio, INTConstant, LoadImage, AudioCrop, MultiTalkModelLoader, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoVAELoader, CLIPVisionLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, DF_Float]
patterns: []
missing: []
---

# 视频生成/图生视频/【阿良绘】数字人讲话（图生视频）_高动态Infinite talk（Lightx2v+Rcm）_1960200175715299330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1960200175715299330.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（32 个）：
- `WanVideoTextEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoClipVisionEncode`
- `GetImageSize`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `AudioSeparation`
- `PreviewAny`
- `CR Text`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LoadAudio`
- `INTConstant`
- `LoadImage`
- `AudioCrop`
- `MultiTalkModelLoader`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `DF_Float`

## 知识

覆盖率 **94%**（30/32）

**有卡**：`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoClipVisionEncode`、`GetImageSize`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`AudioSeparation`、`CR Text`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`LoadAudio`、`INTConstant`、`LoadImage`、`AudioCrop`、`MultiTalkModelLoader`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelect`、`DF_Float`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
