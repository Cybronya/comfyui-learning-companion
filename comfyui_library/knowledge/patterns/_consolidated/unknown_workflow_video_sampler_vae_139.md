---
name: unknown_workflow_video_sampler_vae_139
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6505
common_nodes: [Anything Everywhere, BBoxesToSAM2, CR String To Number, CR Text, DownloadAndLoadQwenModel, GetNode, GrowMaskWithBlur, ImageBatchGet, ImageCompositeMasked, ImageResize+, LayerColor: AutoBrightness, LayerMask: SAM2VideoUltra, LoadWanVideoT5TextEncoder, MaskPreview+, MaskToImage, MathExpression|pysssss, QwenVLDetection, SetNode, SolidMask, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy clearCacheAll, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/【视频万物消除】MiniMax-Remover1.3B（全自动）_1983150046390722562.json, 平台全量/【视频万物消除】MiniMax-Remover1.3B（全自动）_1936098803994775553.json, 平台全量/视频去字幕(静态_动态字幕)_20251014_1976553723432443906.json, 平台全量/视频去字幕_2033767321893867522.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_139

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【视频万物消除】MiniMax-Remover1.3B（全自动）_1983150046390722562.json、平台全量/【视频万物消除】MiniMax-Remover1.3B（全自动）_1936098803994775553.json、平台全量/视频去字幕(静态_动态字幕)_20251014_1976553723432443906.json、平台全量/视频去字幕_2033767321893867522.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere`
- `BBoxesToSAM2`
- `CR String To Number`
- `CR Text`
- `DownloadAndLoadQwenModel`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageBatchGet`
- `ImageCompositeMasked`
- `ImageResize+`
- `LayerColor: AutoBrightness`
- `LayerMask: SAM2VideoUltra`
- `LoadWanVideoT5TextEncoder`
- `MaskPreview+`
- `MaskToImage`
- `MathExpression|pysssss`
- `QwenVLDetection`
- `SetNode`
- `SolidMask`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DrawMaskOnImage` —— 2/4 个有
- `Float` —— 2/4 个有
- `FluxResolutionNode` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `ImageUpscaleWithModelBatched` —— 2/4 个有
- `Int` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `PlaySound|pysssss` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `ToFloat` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `VHS_VideoInfoSource` —— 2/4 个有
- `WanVideoLoraSelect` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
