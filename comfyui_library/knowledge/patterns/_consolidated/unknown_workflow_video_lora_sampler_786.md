---
name: unknown_workflow_video_lora_sampler_786
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8095
common_nodes: [DF_Get_image_size, Float, GetImageSizeAndCount, ImageConcanate, ImageFromBatch+, ImageResizeKJv2, Int, JWImageResizeByLongerSide, JWInteger, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PDIMAGE_LongerSize, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy batchAnything, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/（一阶段）全能视频S极致原版修复去闪加细节720P极速版V1_1974427863669673986.json, 视频生成/图生视频/人物一致性SVI顶配版长视频生成_1985379890973319169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_786

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/（一阶段）全能视频S极致原版修复去闪加细节720P极速版V1_1974427863669673986.json、视频生成/图生视频/人物一致性SVI顶配版长视频生成_1985379890973319169.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `DF_Get_image_size`
- `Float`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `Int`
- `JWImageResizeByLongerSide`
- `JWInteger`
- `LayerUtility: PurgeVRAM V2`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PDIMAGE_LongerSize`
- `RepeatImageBatch`
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
- `WanVideoVAELoader`
- `easy batchAnything`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageBatchMulti` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `WanVideoClipVisionEncode` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有
- `WanVideoSetBlockSwap` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `WanVideoVACEStartToEndFrame` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
