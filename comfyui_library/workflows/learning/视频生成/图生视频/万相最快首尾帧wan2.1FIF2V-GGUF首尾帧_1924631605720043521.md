---
key: 视频生成/图生视频/万相最快首尾帧wan2.1FIF2V-GGUF首尾帧_1924631605720043521.json
name: 万相最快首尾帧wan2.1FIF2V-GGUF首尾帧_1924631605720043521.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1924631605720043521.json
hash: 8969e84322b65391
coverage: 0.978723
learned_at: 2026-10-15 22:29:50
nodes: [ModelSamplingSD3, WanVideoEnhanceAVideoKJ, SamplerCustomAdvanced, TorchCompileModelWanVideo, WanVideoTeaCacheKJ, CFGZeroStar, SamplerCustomAdvanced, VHS_VideoCombine, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, CLIPTextEncode, CLIPTextEncode, VHS_VideoCombine, UnetLoaderGGUF, LoadImage, LoadImage, VAEDecode, RandomNoise, LoraLoaderModelOnly, CR Text, VAELoader, SkipLayerGuidanceWanVideo, CLIPVisionEncode, CR Text, ColorMatch, KSamplerSelect, VHS_VideoCombine, wanBlockSwap, WanSkipEndFrameImages_F2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, WanImageToVideo_F2, PrimitiveNode, CFGGuider, PathchSageAttentionKJ, CFGGuider, KSamplerSelect, BasicScheduler, CLIPLoader, CLIPVisionLoader, SplitSigmas, ImageNoiseAugmentation, ImageNoiseAugmentation, Int, Int, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/万相最快首尾帧wan2.1FIF2V-GGUF首尾帧_1924631605720043521.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1924631605720043521.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（47 个）：
- `ModelSamplingSD3`
- `WanVideoEnhanceAVideoKJ`
- `SamplerCustomAdvanced` ★核心
- `TorchCompileModelWanVideo`
- `WanVideoTeaCacheKJ`
- `CFGZeroStar`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `UnetLoaderGGUF` ★核心
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `VAELoader`
- `SkipLayerGuidanceWanVideo`
- `CLIPVisionEncode`
- `CR Text`
- `ColorMatch`
- `KSamplerSelect` ★核心
- `VHS_VideoCombine`
- `wanBlockSwap`
- `WanSkipEndFrameImages_F2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `WanImageToVideo_F2`
- `PrimitiveNode`
- `CFGGuider`
- `PathchSageAttentionKJ`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CLIPLoader`
- `CLIPVisionLoader`
- `SplitSigmas`
- `ImageNoiseAugmentation`
- `ImageNoiseAugmentation`
- `Int`
- `Int`
- `Int`

## 知识

覆盖率 **98%**（46/47）

**有卡**：`ModelSamplingSD3`、`WanVideoEnhanceAVideoKJ`、`SamplerCustomAdvanced`、`TorchCompileModelWanVideo`、`WanVideoTeaCacheKJ`、`CFGZeroStar`、`VHS_VideoCombine`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`CLIPTextEncode`、`UnetLoaderGGUF`、`LoadImage`、`VAEDecode`、`RandomNoise`、`LoraLoaderModelOnly`、`CR Text`、`VAELoader`、`SkipLayerGuidanceWanVideo`、`CLIPVisionEncode`、`ColorMatch`、`KSamplerSelect`、`wanBlockSwap`、`WanSkipEndFrameImages_F2`、`LayerUtility: PurgeVRAM V2`、`WanImageToVideo_F2`、`CFGGuider`、`PathchSageAttentionKJ`、`BasicScheduler`、`CLIPLoader`、`CLIPVisionLoader`、`SplitSigmas`、`ImageNoiseAugmentation`、`Int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider、KSamplerSelect
