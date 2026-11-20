---
key: 平台全量/手枪凭空消失术，MiniMax-Remover精准抹除+NAG强化控制+MagCache加速生成_1937854211000569857.json
name: 手枪凭空消失术，MiniMax-Remover精准抹除+NAG强化控制+MagCache加速生成_1937854211000569857
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/手枪凭空消失术，MiniMax-Remover精准抹除+NAG强化控制+MagCache加速生成_1937854211000569857.json
hash: 431929b4c4eaf4b1
coverage: 0.916667
learned_at: 2026-11-14 02:04:52
nodes: [WanVideoEncode, WanVideoTorchCompileSettings, ImageFromBatch, WanVideoVAELoader, LayerUtility: PurgeVRAM V2, ImageResizeKJv2, WanVideoMiniMaxRemoverEmbeds, WanVideoEnhanceAVideo, WanVideoSampler, LoadWanVideoT5TextEncoder, MaskToImage, WanVideoEncode, SetNode, WanVideoMagCache, LayerMask: LoadSegmentAnythingModels, LayerUtility: PurgeVRAM V2, GrowMaskWithBlur, MaskPreview+, WanVideoDecode, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, WanVideoApplyNAG, GetNode, VHS_VideoCombine, WanVideoModelLoader, LayerMask: SegmentAnythingUltra V3, PrimitiveString, Bookmark (rgthree), Bookmark (rgthree), Bookmark (rgthree), Bookmark (rgthree), Bookmark (rgthree), Bookmark (rgthree), VHS_LoadVideo, Bookmark (rgthree), Label (rgthree)]
patterns: []
missing: []
---

# 平台全量/手枪凭空消失术，MiniMax-Remover精准抹除+NAG强化控制+MagCache加速生成_1937854211000569857.json

> 来源文件 `comfyui_library/workflows/平台全量/手枪凭空消失术，MiniMax-Remover精准抹除+NAG强化控制+MagCache加速生成_1937854211000569857.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoEncode`
- `WanVideoTorchCompileSettings`
- `ImageFromBatch`
- `WanVideoVAELoader`
- `LayerUtility: PurgeVRAM V2`
- `ImageResizeKJv2`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `WanVideoEncode`
- `SetNode`
- `WanVideoMagCache`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerUtility: PurgeVRAM V2`
- `GrowMaskWithBlur`
- `MaskPreview+`
- `WanVideoDecode`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `LayerMask: SegmentAnythingUltra V3`
- `PrimitiveString`
- `Bookmark (rgthree)`
- `Bookmark (rgthree)`
- `Bookmark (rgthree)`
- `Bookmark (rgthree)`
- `Bookmark (rgthree)`
- `Bookmark (rgthree)`
- `VHS_LoadVideo`
- `Bookmark (rgthree)`
- `Label (rgthree)`

## 知识

覆盖率 **92%**（33/36）

**有卡**：`WanVideoEncode`、`WanVideoTorchCompileSettings`、`ImageFromBatch`、`WanVideoVAELoader`、`LayerUtility: PurgeVRAM V2`、`ImageResizeKJv2`、`WanVideoMiniMaxRemoverEmbeds`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`MaskToImage`、`WanVideoMagCache`、`LayerMask: LoadSegmentAnythingModels`、`GrowMaskWithBlur`、`MaskPreview+`、`WanVideoDecode`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`VHS_VideoCombine`、`WanVideoModelLoader`、`LayerMask: SegmentAnythingUltra V3`、`Bookmark (rgthree)`、`VHS_LoadVideo`、`Label (rgthree)`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeSingle、WanVideoVAELoader、ImageResizeKJv2、MaskPreview+
