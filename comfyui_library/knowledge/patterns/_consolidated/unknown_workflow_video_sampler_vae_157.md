---
name: unknown_workflow_video_sampler_vae_157
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.75725
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FusionX-Phantom 多图融合14B高清版_1934266873917956097.json, 视频生成/图生视频/FusionX-VACE多图融合_1934249713015156738.json, 视频生成/图生视频/模特产品互动、多人合照、 产品结合、图片结合 WAN 2.1 VACE 14b_1926293882655457281.json, 视频生成/图生视频/视频-破次元融合版-多主体融合 FusionX-VACE_1934523459177250818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_157

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/FusionX-Phantom 多图融合14B高清版_1934266873917956097.json、视频生成/图生视频/FusionX-VACE多图融合_1934249713015156738.json、视频生成/图生视频/模特产品互动、多人合照、 产品结合、图片结合 WAN 2.1 VACE 14b_1926293882655457281.json、视频生成/图生视频/视频-破次元融合版-多主体融合 FusionX-VACE_1934523459177250818.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
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
- `CR Text` —— 3/4 个有
- `ImageConcanate` —— 3/4 个有
- `InspyrenetRembg` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `LayerUtility: ImageRemoveAlpha` —— 3/4 个有
- `MathExpression|pysssss` —— 3/4 个有
- `WanVideoApplyNAG` —— 3/4 个有
- `WanVideoTextEncodeSingle` —— 3/4 个有
- `WanVideoVACEEncode` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `ImagePadKJ` —— 1/4 个有
- `Note _O` —— 1/4 个有
- `WanVideoEncode` —— 1/4 个有
- `WanVideoPhantomEmbeds` —— 1/4 个有
- `WanVideoTeaCache` —— 1/4 个有
- `WanVideoTextEncode` —— 1/4 个有
- `WanVideoVACEModelSelect` —— 1/4 个有
- `easy imageScaleDownToSize` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
