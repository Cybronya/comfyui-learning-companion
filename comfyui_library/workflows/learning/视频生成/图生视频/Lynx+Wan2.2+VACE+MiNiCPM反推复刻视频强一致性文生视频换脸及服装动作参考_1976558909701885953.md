---
key: 视频生成/图生视频/Lynx+Wan2.2+VACE+MiNiCPM反推复刻视频强一致性文生视频换脸及服装动作参考_1976558909701885953.json
name: Lynx+Wan2.2+VACE+MiNiCPM反推复刻视频强一致性文生视频换脸及服装动作参考_1976558909701885953.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Lynx+Wan2.2+VACE+MiNiCPM反推复刻视频强一致性文生视频换脸及服装动作参考_1976558909701885953.json
hash: 462fbe1316a6c816
coverage: 0.893617
learned_at: 2026-10-15 22:32:11
nodes: [WanVideoDecode, Wan22PromptSelector, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, RHHiddenNodes, LoadImage, GetImageSizeAndCount, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, ImageResizeKJv2, DWPreprocessor, SimpleMath+, Int, Int, WanVideoSampler, ImageResizeKJv2, LynxInsightFaceCrop, LoadLynxResampler, LoadImage, VHS_LoadVideo, WanVideoTorchCompileSettings, LynxEncodeFaceIP, easy clearCacheAll, WanVideoAddLynxEmbeds, WanVideoExtraModelSelect, RHHiddenNodes, WanVideoModelLoader, WanVideoTextEncode, easy clearCacheAll, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, easy clearCacheAll, WanVideoVACEEncode, PrimitiveString, CR Text, easy clearCacheAll, easy clearCacheAll, WanVideoTextEncode, RHHiddenNodes, easy showAnything, Note, easy anythingIndexSwitch, Fast Groups Muter (rgthree), Note]
patterns: []
missing: []
---

# 视频生成/图生视频/Lynx+Wan2.2+VACE+MiNiCPM反推复刻视频强一致性文生视频换脸及服装动作参考_1976558909701885953.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1976558909701885953.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（47 个）：
- `WanVideoDecode`
- `Wan22PromptSelector`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `RHHiddenNodes`
- `LoadImage`
- `GetImageSizeAndCount`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `SimpleMath+`
- `Int`
- `Int`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `LynxInsightFaceCrop`
- `LoadLynxResampler` ★核心
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoTorchCompileSettings`
- `LynxEncodeFaceIP`
- `easy clearCacheAll`
- `WanVideoAddLynxEmbeds`
- `WanVideoExtraModelSelect`
- `RHHiddenNodes`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `easy clearCacheAll`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `easy clearCacheAll`
- `WanVideoVACEEncode`
- `PrimitiveString`
- `CR Text`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `WanVideoTextEncode`
- `RHHiddenNodes`
- `easy showAnything`
- `Note`
- `easy anythingIndexSwitch`
- `Fast Groups Muter (rgthree)`
- `Note`

## 知识

覆盖率 **89%**（42/47）

**有卡**：`WanVideoDecode`、`Wan22PromptSelector`、`WanVideoExtraModelSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`RHHiddenNodes`、`LoadImage`、`GetImageSizeAndCount`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`ImageResizeKJv2`、`DWPreprocessor`、`SimpleMath+`、`Int`、`WanVideoSampler`、`LynxInsightFaceCrop`、`LoadLynxResampler`、`VHS_LoadVideo`、`WanVideoTorchCompileSettings`、`LynxEncodeFaceIP`、`easy clearCacheAll`、`WanVideoAddLynxEmbeds`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVACEEncode`、`CR Text`、`easy anythingIndexSwitch`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
