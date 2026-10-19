---
key: 数字人/数字人/高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）_2090261460101459969.json
name: 高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）_2090261460101459969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）_2090261460101459969.json
hash: 03ddaa0c114343ba
coverage: 0.864865
learned_at: 2026-10-18 22:17:18
nodes: [WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoDecode, WanVideoLoraSelect, WanVideoTextEncode, VHS_VideoCombine, WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, CLIPVisionLoader, LoadWanVideoT5TextEncoder, WanVideoClipVisionEncode, IndexTTS2Run, MultiTalkWav2VecEmbeds, PrimitiveString, Note, WanVideoVAELoader, JWInteger, LoadImage, LayerUtility: PurgeVRAM V2, LoadAudio, ImpactSwitch, DownloadAndLoadWav2VecModel, ToInt, SimpleMath+, Fast Groups Bypasser (rgthree), easy int, SaveAudio, SoundFlow_GetLength, Bjornulf_ShowFloat, Bjornulf_ShowInt, LoadAudio, CR Prompt Text, MultiTalkModelLoader, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 数字人/数字人/高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）_2090261460101459969.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）_2090261460101459969.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（37 个）：
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `CLIPVisionLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoClipVisionEncode`
- `IndexTTS2Run`
- `MultiTalkWav2VecEmbeds`
- `PrimitiveString`
- `Note`
- `WanVideoVAELoader`
- `JWInteger`
- `LoadImage`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `ImpactSwitch`
- `DownloadAndLoadWav2VecModel`
- `ToInt`
- `SimpleMath+`
- `Fast Groups Bypasser (rgthree)`
- `easy int`
- `SaveAudio`
- `SoundFlow_GetLength`
- `Bjornulf_ShowFloat`
- `Bjornulf_ShowInt`
- `LoadAudio`
- `CR Prompt Text`
- `MultiTalkModelLoader`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **86%**（32/37）

**有卡**：`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoDecode`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSizeAndCount`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoClipVisionEncode`、`IndexTTS2Run`、`MultiTalkWav2VecEmbeds`、`WanVideoVAELoader`、`JWInteger`、`LoadImage`、`LayerUtility: PurgeVRAM V2`、`LoadAudio`、`DownloadAndLoadWav2VecModel`、`ToInt`、`SimpleMath+`、`easy int`、`SaveAudio`、`SoundFlow_GetLength`、`Bjornulf_ShowFloat`、`Bjornulf_ShowInt`、`CR Prompt Text`、`MultiTalkModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
