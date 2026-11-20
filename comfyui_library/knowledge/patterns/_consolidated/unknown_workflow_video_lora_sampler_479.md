---
name: unknown_workflow_video_lora_sampler_479
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.869833
common_nodes: [DF_Get_image_size, Float, GetImageSizeAndCount, ImageConcanate, ImageFromBatch+, ImageResizeKJv2, Int, JWImageResizeByLongerSide, JWInteger, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PDIMAGE_LongerSize, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy batchAnything, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/（一阶段）全能视频S极致原版修复去闪加细节720P极速版V1_1974427863669673986.json, 平台全量/（一阶段15秒版）全能视频S极致原版修复去闪加细节极速版V1_1975913780108505089.json, 平台全量/（一阶段）全能视频S极致原版修复去闪加细节720P极速版V1_1973757539986837506.json, 平台全量/（组合版）全能视频S极致修复+口型重塑720P高清极速版V1（6分钟）_1973745770027462657.json, 平台全量/🦖全能视频S闪烁极致修复_1976843592805367809.json, 视频生成/图生视频/人物一致性SVI顶配版长视频生成_1985379890973319169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_479

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/（一阶段）全能视频S极致原版修复去闪加细节720P极速版V1_1974427863669673986.json、平台全量/（一阶段15秒版）全能视频S极致原版修复去闪加细节极速版V1_1975913780108505089.json、平台全量/（一阶段）全能视频S极致原版修复去闪加细节720P极速版V1_1973757539986837506.json、平台全量/（组合版）全能视频S极致修复+口型重塑720P高清极速版V1（6分钟）_1973745770027462657.json、平台全量/🦖全能视频S闪烁极致修复_1976843592805367809.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `CLIPVisionLoader` —— 2/6 个有
- `GetImageRangeFromBatch` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `LayerUtility: PurgeVRAM` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `WanVideoClipVisionEncode` —— 2/6 个有
- `AudioSeparation` —— 1/6 个有
- `CR Prompt Text` —— 1/6 个有
- `ColorMatch` —— 1/6 个有
- `DownloadAndLoadWav2VecModel` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `ImageBatchMulti` —— 1/6 个有
- `InvertMask` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `MultiTalkModelLoader` —— 1/6 个有
- `MultiTalkWav2VecEmbeds` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `VHS_VideoInfo` —— 1/6 个有
- `WanVideoImageToVideoEncode` —— 1/6 个有
- `WanVideoImageToVideoMultiTalk` —— 1/6 个有
- `WanVideoSetBlockSwap` —— 1/6 个有
- `WanVideoTextEncodeCached` —— 1/6 个有
- `WanVideoTorchCompileSettings` —— 1/6 个有
- `WanVideoVACEStartToEndFrame` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
