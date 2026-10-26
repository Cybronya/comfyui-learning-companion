---
name: unknown_workflow_video_sampler_vae_81
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.667833
common_nodes: [CLIPVisionLoader, EmptyImage, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageBatch, ImageBatchMulti, ImageBatchRepeatInterleaving, ImageConcatMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan SkyReels-A2多物体参考工作流_1910194560243564546.json, 视频生成/图生视频/Wan SkyReels-A2多物体视频_1910218456598544385.json, 视频生成/图生视频/Wan2.1 SkyReels 双图参考 人+物体_1948673217209741314.json, 视频生成/图生视频/Wan2.1 skyreels 多图参考_1948677526125182978.json, 视频生成/图生视频/双分支图像融合一致性Wan Skyreels视频工作流V1_1909312671357743106.json, 视频生成/图生视频/最新王炸Wan2.1+SkyReels  自定义角色+物体+背景  超高还原_1911449763139547137.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_81

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Wan SkyReels-A2多物体参考工作流_1910194560243564546.json、视频生成/图生视频/Wan SkyReels-A2多物体视频_1910218456598544385.json、视频生成/图生视频/Wan2.1 SkyReels 双图参考 人+物体_1948673217209741314.json、视频生成/图生视频/Wan2.1 skyreels 多图参考_1948677526125182978.json、视频生成/图生视频/双分支图像融合一致性Wan Skyreels视频工作流V1_1909312671357743106.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `EmptyImage`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBatch`
- `ImageBatchMulti`
- `ImageBatchRepeatInterleaving`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `ImageRemoveBackground+` —— 5/6 个有
- `SimpleMath+` —— 5/6 个有
- `TransparentBGSession+` —— 5/6 个有
- `ImageCompositeMasked` —— 4/6 个有
- `Note Plus (mtb)` —— 3/6 个有
- `WanVideoTorchCompileSettings` —— 3/6 个有
- `ImagePadKJ` —— 2/6 个有
- `LayerUtility: ImageBlendAdvance V3` —— 2/6 个有
- `LayerUtility: ImageRemoveAlpha` —— 2/6 个有
- `LoadImageFromUrl` —— 2/6 个有
- `WanVideoVRAMManagement` —— 2/6 个有
- `CLIPLoader` —— 1/6 个有
- `CLIPTextEncode` —— 1/6 个有
- `DF_Integer` —— 1/6 个有
- `Evaluate Integers` —— 1/6 个有
- `JWImageResizeByLongerSide` —— 1/6 个有
- `LayerMask: RmBgUltra V2` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `WanVideoEnhanceAVideo` —— 1/6 个有
- `WanVideoTextEmbedBridge` —— 1/6 个有
- `easy getNode` —— 1/6 个有
- `easy imageScaleDownToSize` —— 1/6 个有
- `easy setNode` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
