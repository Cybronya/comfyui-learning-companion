---
key: 数字人/数字人/最新Wan2.2 Multitalk数字人单人版-图片+音频=高质量数字人_1955987498365276161.json
name: 最新Wan2.2 Multitalk数字人单人版-图片+音频=高质量数字人_1955987498365276161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/最新Wan2.2 Multitalk数字人单人版-图片+音频=高质量数字人_1955987498365276161.json
hash: 29d57ecb98f12dd1
coverage: 0.783333
learned_at: 2026-10-26 02:03:32
nodes: [WanVideoUni3C_embeds, WanVideoUni3C_ControlnetLoader, VHS_DuplicateImages, easy imageScaleDownToSize, WanVideoEncode, ImpactSwitch, easy compare, easy imageSize, easy ifElse, Note, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoVAELoader, SetNode, LayerUtility: ImageScaleByAspectRatio V2, AudioCrop, WanVideoTextEncode, GetNode, DownloadAndLoadWav2VecModel, easy cleanGpuUsed, WanVideoSampler, GetNode, GetNode, GetNode, AudioSeparation, GetNode, LoadWanVideoT5TextEncoder, SetNode, MultiTalkModelLoader, SetNode, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, CLIPVisionLoader, RH_LLMAPI_NODE, Audio Duration (mtb), MultiTalkWav2VecEmbeds, RHHiddenNodes, JWInteger, LoadAudio, VHS_VideoCombine, easy showAnything, LoadImage, CR Text, JWInteger, MathExpression|pysssss, ImageFromBatch+, WanVideoLoraSelect, WanVideoLoraSelect, CreateCFGScheduleFloatList, MathExpression|pysssss, Primitive integer [Crystools], WanVideoSampler, WanVideoDecode]
patterns: []
missing: []
---

# 数字人/数字人/最新Wan2.2 Multitalk数字人单人版-图片+音频=高质量数字人_1955987498365276161.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/最新Wan2.2 Multitalk数字人单人版-图片+音频=高质量数字人_1955987498365276161.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（60 个）：
- `WanVideoUni3C_embeds`
- `WanVideoUni3C_ControlnetLoader`
- `VHS_DuplicateImages`
- `easy imageScaleDownToSize`
- `WanVideoEncode`
- `ImpactSwitch`
- `easy compare`
- `easy imageSize`
- `easy ifElse`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AudioCrop`
- `WanVideoTextEncode`
- `GetNode`
- `DownloadAndLoadWav2VecModel`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `AudioSeparation`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `MultiTalkModelLoader`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `RH_LLMAPI_NODE`
- `Audio Duration (mtb)`
- `MultiTalkWav2VecEmbeds`
- `RHHiddenNodes`
- `JWInteger`
- `LoadAudio`
- `VHS_VideoCombine`
- `easy showAnything`
- `LoadImage`
- `CR Text`
- `JWInteger`
- `MathExpression|pysssss`
- `ImageFromBatch+`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `WanVideoSampler` ★核心
- `WanVideoDecode`

## 知识

覆盖率 **78%**（47/60）

**有卡**：`WanVideoUni3C_embeds`、`WanVideoUni3C_ControlnetLoader`、`VHS_DuplicateImages`、`easy imageScaleDownToSize`、`WanVideoEncode`、`easy compare`、`easy imageSize`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`AudioCrop`、`WanVideoTextEncode`、`DownloadAndLoadWav2VecModel`、`easy cleanGpuUsed`、`WanVideoSampler`、`AudioSeparation`、`LoadWanVideoT5TextEncoder`、`MultiTalkModelLoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`RH_LLMAPI_NODE`、`Audio Duration (mtb)`、`MultiTalkWav2VecEmbeds`、`RHHiddenNodes`、`JWInteger`、`LoadAudio`、`VHS_VideoCombine`、`LoadImage`、`CR Text`、`MathExpression|pysssss`、`ImageFromBatch+`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`Primitive integer [Crystools]`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
