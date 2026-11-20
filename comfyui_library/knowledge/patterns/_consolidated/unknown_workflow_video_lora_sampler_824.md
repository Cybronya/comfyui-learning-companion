---
name: unknown_workflow_video_lora_sampler_824
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.877
common_nodes: [Float, Int, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/全能视频S画质修复_1978740074802204674.json, 平台全量/全能视频S视频工具3：高清放大修复补帧_1973659200888901633.json, 平台全量/去水印之后后期全能视频S画质修复wan2.2修复_1992283225703903234.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_824

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/全能视频S画质修复_1978740074802204674.json、平台全量/全能视频S视频工具3：高清放大修复补帧_1973659200888901633.json、平台全量/去水印之后后期全能视频S画质修复wan2.2修复_1992283225703903234.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `Float`
- `Int`
- `LoadWanVideoT5TextEncoder`
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

**可变部分**（部分 workflow 才有）：
- `FramePackFindNearestBucket` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `ImageUpscaleWithModelBatched` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `RIFE VFI` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `VHS_BatchManager` —— 1/3 个有
- `easy int` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
