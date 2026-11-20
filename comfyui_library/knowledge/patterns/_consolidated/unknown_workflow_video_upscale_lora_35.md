---
name: unknown_workflow_video_upscale_lora_35
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8465
common_nodes: [Float, FramePackFindNearestBucket, ImageResizeKJv2, ImageUpscaleWithModelBatched, Int, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, RIFE VFI, SimpleMath+, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/全能视频S画质修复（WAN2.2修复）_1974717795143430146.json, 平台全量/全能视频S画质修复（wan2.2）+去水印_1973645236897492994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_35

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/全能视频S画质修复（WAN2.2修复）_1974717795143430146.json、平台全量/全能视频S画质修复（wan2.2）+去水印_1973645236897492994.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `Float`
- `FramePackFindNearestBucket`
- `ImageResizeKJv2`
- `ImageUpscaleWithModelBatched`
- `Int`
- `LayerUtility: PurgeVRAM V2`
- `LoadWanVideoT5TextEncoder`
- `RIFE VFI`
- `SimpleMath+`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DiffuEraserLoader` —— 1/2 个有
- `DiffuEraserSampler` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `ImageToMask` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `RepeatImageBatch` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `easy compare` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
