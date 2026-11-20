---
key: 平台全量/4高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）(1)_2118258030931435522.json
name: 4高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）(1)_2118258030931435522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/4高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）(1)_2118258030931435522.json
hash: 03bcc1262256e211
coverage: 0.864865
learned_at: 2026-11-14 00:13:33
nodes: [WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoDecode, MultiTalkModelLoader, WanVideoLoraSelect, WanVideoTextEncode, VHS_VideoCombine, WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, CLIPVisionLoader, LoadWanVideoT5TextEncoder, WanVideoClipVisionEncode, IndexTTS2Run, Note, WanVideoVAELoader, JWInteger, CR Prompt Text, LayerUtility: PurgeVRAM V2, ImpactSwitch, DownloadAndLoadWav2VecModel, ToInt, SimpleMath+, Fast Groups Bypasser (rgthree), SaveAudio, SoundFlow_GetLength, Bjornulf_ShowFloat, Bjornulf_ShowInt, easy int, MultiTalkWav2VecEmbeds, LoadAudio, PrimitiveString, LoadAudio, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 平台全量/4高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）(1)_2118258030931435522.json

> 来源文件 `comfyui_library/workflows/平台全量/4高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）(1)_2118258030931435522.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（37 个）：
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `WanVideoDecode`
- `MultiTalkModelLoader`
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
- `Note`
- `WanVideoVAELoader`
- `JWInteger`
- `CR Prompt Text`
- `LayerUtility: PurgeVRAM V2`
- `ImpactSwitch`
- `DownloadAndLoadWav2VecModel`
- `ToInt`
- `SimpleMath+`
- `Fast Groups Bypasser (rgthree)`
- `SaveAudio`
- `SoundFlow_GetLength`
- `Bjornulf_ShowFloat`
- `Bjornulf_ShowInt`
- `easy int`
- `MultiTalkWav2VecEmbeds`
- `LoadAudio`
- `PrimitiveString`
- `LoadAudio`
- `LoadImage`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **86%**（32/37）

**有卡**：`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoDecode`、`MultiTalkModelLoader`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSizeAndCount`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoClipVisionEncode`、`IndexTTS2Run`、`WanVideoVAELoader`、`JWInteger`、`CR Prompt Text`、`LayerUtility: PurgeVRAM V2`、`DownloadAndLoadWav2VecModel`、`ToInt`、`SimpleMath+`、`SaveAudio`、`SoundFlow_GetLength`、`Bjornulf_ShowFloat`、`Bjornulf_ShowInt`、`easy int`、`MultiTalkWav2VecEmbeds`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
