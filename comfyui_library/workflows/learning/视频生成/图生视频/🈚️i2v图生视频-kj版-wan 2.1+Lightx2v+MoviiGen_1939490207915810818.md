---
key: 视频生成/图生视频/🈚️i2v图生视频-kj版-wan 2.1+Lightx2v+MoviiGen_1939490207915810818.json
name: 🈚️i2v图生视频-kj版-wan 2.1+Lightx2v+MoviiGen_1939490207915810818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1939490207915810818.json
hash: 389ef3cbc89cae86
coverage: 0.610619
learned_at: 2026-10-15 22:30:32
nodes: [GetNode, WanVideoEncode, SimpleCondition+, SetNode, SetNode, WanVideoTextEncodeSingle, GetNode, GetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, GetNode, GetNode, WanVideoVAELoader, SetNode, SetNode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, GetNode, GetNode, GetNode, GetNode, GetNode, GIMMVFI_interpolate, ImageSmartSharpen+, SetNode, CR Upscale Image, DownloadAndLoadGIMMVFIModel, LoadWanVideoClipTextEncoder, WanVideoLoraSelect, VHS_VideoCombine, SetNode, WanVideoLoraSelect, WanVideoClipVisionEncode, SetNode, PreviewAny, SetNode, PreviewAny, WanVideoExperimentalArgs, WanVideoDecode, WanVideoUni3C_ControlnetLoader, WanVideoTorchCompileSettings, WanVideoUni3C_embeds, WanVideoFreeInitArgs, LoadWanVideoT5TextEncoder, WanVideoTextEncodeSingle, PreviewImage, PreviewImage, LynxInsightFaceCrop, LoadLynxResampler, LynxEncodeFaceIP, GetNode, GetNode, WanVideoBlockSwap, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoTorchCompileSettings, WanVideoAddLynxEmbeds, easy imageRemBg, WanVideoTextEncodeCached, Reroute, GetNode, WanVideoApplyNAG, GetNode, GetNode, GetNode, GetImageSize, GetNode, SetNode, GetNode, SetNode, WanVideoLoraSelect, GetNode, SeargePromptText, WanVideoSLG, ImageSmartSharpen+, ShowText|pysssss, SetNode, SetNode, VHS_LoadVideo, SetNode, ImageResizeKJ, WanVideoEnhanceAVideo, easy seed, RH_LLMAPI_NODE, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSampler, SeargePromptText, PreviewImage, WanVideoEasyCache, WanVideoModelLoader, SetNode, ImageResizeKJ, WanVideoImageToVideoEncode, GetNode, SetNode, LoadImage, VHS_VideoCombine, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/🈚️i2v图生视频-kj版-wan 2.1+Lightx2v+MoviiGen_1939490207915810818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1939490207915810818.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（113 个）：
- `GetNode`
- `WanVideoEncode`
- `SimpleCondition+`
- `SetNode`
- `SetNode`
- `WanVideoTextEncodeSingle`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GIMMVFI_interpolate`
- `ImageSmartSharpen+`
- `SetNode`
- `CR Upscale Image`
- `DownloadAndLoadGIMMVFIModel`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoClipVisionEncode`
- `SetNode`
- `PreviewAny`
- `SetNode`
- `PreviewAny`
- `WanVideoExperimentalArgs`
- `WanVideoDecode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_embeds`
- `WanVideoFreeInitArgs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncodeSingle`
- `PreviewImage`
- `PreviewImage`
- `LynxInsightFaceCrop`
- `LoadLynxResampler` ★核心
- `LynxEncodeFaceIP`
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoAddLynxEmbeds`
- `easy imageRemBg`
- `WanVideoTextEncodeCached`
- `Reroute`
- `GetNode`
- `WanVideoApplyNAG`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `WanVideoLoraSelect`
- `GetNode`
- `SeargePromptText`
- `WanVideoSLG`
- `ImageSmartSharpen+`
- `ShowText|pysssss`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `ImageResizeKJ`
- `WanVideoEnhanceAVideo`
- `easy seed`
- `RH_LLMAPI_NODE`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `SeargePromptText`
- `PreviewImage`
- `WanVideoEasyCache`
- `WanVideoModelLoader`
- `SetNode`
- `ImageResizeKJ`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `VHS_VideoCombine`
- `Int`

## 知识

覆盖率 **61%**（69/113）

**有卡**：`WanVideoEncode`、`SimpleCondition+`、`WanVideoTextEncodeSingle`、`LoraLoaderModelOnly`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`GIMMVFI_interpolate`、`ImageSmartSharpen+`、`CR Upscale Image`、`DownloadAndLoadGIMMVFIModel`、`LoadWanVideoClipTextEncoder`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoTorchCompileSettings`、`WanVideoUni3C_embeds`、`WanVideoFreeInitArgs`、`LoadWanVideoT5TextEncoder`、`LynxInsightFaceCrop`、`LoadLynxResampler`、`LynxEncodeFaceIP`、`WanVideoBlockSwap`、`WanVideoExtraModelSelect`、`WanVideoAddLynxEmbeds`、`easy imageRemBg`、`WanVideoTextEncodeCached`、`WanVideoApplyNAG`、`GetImageSize`、`SeargePromptText`、`WanVideoSLG`、`VHS_LoadVideo`、`ImageResizeKJ`、`WanVideoEnhanceAVideo`、`easy seed`、`RH_LLMAPI_NODE`、`WanVideoSampler`、`WanVideoEasyCache`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`LoadImage`、`Int`

**用到的条目**：LoraLoaderModelOnly、LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、LoadLynxResampler、easy seed、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder
