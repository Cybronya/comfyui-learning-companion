---
name: unknown_workflow_video_sampler_vae_35
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.931636
common_nodes: [ImageConcatMulti, ImagePadKJ, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/09.电商带货FusionX-Phantom加速版14B_2000793096378085378.json, 视频生成/图生视频/FusionX-Phantom电商带货14B加速版_1934826257706065921.json, 视频生成/图生视频/Phantom多图组合视频生成_1918902394158256130.json, 视频生成/图生视频/Plantom一致性多图组合视频生成（适用电商场景展示）_1922106634145841154.json, 视频生成/图生视频/Plantom一致性多图组合视频生成（适用电商场景展示）_1991787446910267394.json, 视频生成/图生视频/【FusionX】模特产品展示动态｜加速版_1934517435972419585.json, 视频生成/图生视频/数字人电商带货FusionX-Phantom加速版14B_2039636071985713154.json, 视频生成/图生视频/数字人电商带货FusionX-Phantom加速版14B_2064931253647929346.json, 视频生成/图生视频/电商带货FusionX-Phantom加速版14B_1934089550950260738.json, 视频生成/图生视频/电商带货服装包包直播视频生成FusionX-Phantom加速版_1934241189509951489.json, 视频生成/文生视频/电商带货替换_1935520036046176257.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_35

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/09.电商带货FusionX-Phantom加速版14B_2000793096378085378.json、视频生成/图生视频/FusionX-Phantom电商带货14B加速版_1934826257706065921.json、视频生成/图生视频/Phantom多图组合视频生成_1918902394158256130.json、视频生成/图生视频/Plantom一致性多图组合视频生成（适用电商场景展示）_1922106634145841154.json、视频生成/图生视频/Plantom一致性多图组合视频生成（适用电商场景展示）_1991787446910267394.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 11 个 workflow 都包含：
- `ImageConcatMulti`
- `ImagePadKJ`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Primitive integer [Crystools]` —— 10/11 个有
- `easy clearCacheAll` —— 7/11 个有
- `WanVideoTeaCache` —— 3/11 个有
- `AddLabel` —— 1/11 个有
- `DF_Integer` —— 1/11 个有
- `EmptyImage` —— 1/11 个有
- `GetImageSize` —— 1/11 个有
- `JWInteger` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `MathExpression|pysssss` —— 1/11 个有
- `SimpleMath+` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
