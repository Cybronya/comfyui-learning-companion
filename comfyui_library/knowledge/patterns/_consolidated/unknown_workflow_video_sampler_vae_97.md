---
name: unknown_workflow_video_sampler_vae_97
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7426
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1934266873917956097.json, 视频生成/图生视频/FusionX-VACE多图融合_1934249713015156738.json, 视频生成/图生视频/1934166540621107202.json, 视频生成/图生视频/1908545903828082690.json, 视频生成/图生视频/1926291391310184449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_97

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1934266873917956097.json、视频生成/图生视频/FusionX-VACE多图融合_1934249713015156738.json、视频生成/图生视频/1934166540621107202.json、视频生成/图生视频/1908545903828082690.json、视频生成/图生视频/1926291391310184449.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 5 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageRemoveAlpha` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `WanVideoVACEEncode` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `DepthAnything_V2` —— 3/5 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 3/5 个有
- `JWInteger` —— 3/5 个有
- `LayerMask: BiRefNetUltraV2` —— 3/5 个有
- `LayerMask: LoadBiRefNetModelV2` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `VHS_LoadVideo` —— 3/5 个有
- `WanVideoApplyNAG` —— 3/5 个有
- `WanVideoTeaCache` —— 3/5 个有
- `WanVideoTextEncodeSingle` —— 3/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `WanVideoTextEncode` —— 2/5 个有
- `WanVideoVACEModelSelect` —— 2/5 个有
- `easy imageSize` —— 2/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `ImagePadKJ` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `InspyrenetRembg` —— 1/5 个有
- `Note _O` —— 1/5 个有
- `Primitive integer [Crystools]` —— 1/5 个有
- `WanVideoEncode` —— 1/5 个有
- `WanVideoPhantomEmbeds` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
