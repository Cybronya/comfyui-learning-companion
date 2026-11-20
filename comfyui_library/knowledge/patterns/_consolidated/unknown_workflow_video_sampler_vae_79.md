---
name: unknown_workflow_video_sampler_vae_79
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.948714
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/FusionX VACE视频姿态动作迁移_1943303858234028034.json, 平台全量/FusionX高质量视频转绘_1937320279192584194.json, "平台全量/Phantom+VACE,高一致性图像参考+姿态引导_1933788164274479106.json", 视频生成/图生视频/FusionX VACE首尾帧视频_1943184080722944001.json, 视频生成/图生视频/FusionX高质量Phantom姿态和深度引导图生视频支持负面NAG_1935150460091179009.json, 视频生成/图生视频/lightx2v-高质量加速模型测试_1935325590822256642.json, 视频生成/图生视频/🦖FusionX高质量Phantom图生视频_1935591885543243777.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_79

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/FusionX VACE视频姿态动作迁移_1943303858234028034.json、平台全量/FusionX高质量视频转绘_1937320279192584194.json、平台全量/Phantom+VACE,高一致性图像参考+姿态引导_1933788164274479106.json、视频生成/图生视频/FusionX VACE首尾帧视频_1943184080722944001.json、视频生成/图生视频/FusionX高质量Phantom姿态和深度引导图生视频支持负面NAG_1935150460091179009.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 6/7 个有
- `VHS_LoadVideo` —— 6/7 个有
- `GetImageSize+` —— 5/7 个有
- `INTConstant` —— 5/7 个有
- `ImageResizeKJv2` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `WanVideoApplyNAG` —— 5/7 个有
- `WanVideoExperimentalArgs` —— 5/7 个有
- `WanVideoTextEncodeSingle` —— 5/7 个有
- `AIO_Preprocessor` —— 4/7 个有
- `ImageBlend` —— 4/7 个有
- `WanVideoTeaCache` —— 4/7 个有
- `GetImageSizeAndCount` —— 3/7 个有
- `ImageResizeKJ` —— 3/7 个有
- `WanVideoTorchCompileSettings` —— 3/7 个有
- `WanVideoVACEStartToEndFrame` —— 3/7 个有
- `easy imageConcat` —— 3/7 个有
- `WanVideoMagCache` —— 2/7 个有
- `WanVideoTextEncode` —— 2/7 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/7 个有
- `GIMMVFI_interpolate` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `ImageBatchMulti` —— 1/7 个有
- `MaskBatchMulti` —— 1/7 个有
- `String Literal` —— 1/7 个有
- `WanVideoLoraSelect` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
