---
name: unknown_workflow_video_sampler_vae_60
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.912375
common_nodes: [ImageConcatMulti, ImagePadKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FusionX-Phantom电商带货14B加速版_1934826257706065921.json, 视频生成/图生视频/Phantom多图组合视频生成_1918902394158256130.json, 视频生成/图生视频/Plantom一致性多图组合视频生成（适用电商场景展示）_1922106634145841154.json, 视频生成/图生视频/Plantom一致性多图组合视频生成（适用电商场景展示）_1991787446910267394.json, 视频生成/图生视频/【FusionX】模特产品展示动态｜加速版_1934517435972419585.json, 视频生成/图生视频/上传一张图生成电商产品展示视频（phantom主体一致性）_1917815570186567682.json, 视频生成/图生视频/字节Phantom14B_最新多图参考一致性视频(电商带货)_1916395426835005442.json, 视频生成/图生视频/字节Phantom14B单主体(电商广告视频生成)_1927557646478643202.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_60

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/FusionX-Phantom电商带货14B加速版_1934826257706065921.json、视频生成/图生视频/Phantom多图组合视频生成_1918902394158256130.json、视频生成/图生视频/Plantom一致性多图组合视频生成（适用电商场景展示）_1922106634145841154.json、视频生成/图生视频/Plantom一致性多图组合视频生成（适用电商场景展示）_1991787446910267394.json、视频生成/图生视频/【FusionX】模特产品展示动态｜加速版_1934517435972419585.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `ImageConcatMulti`
- `ImagePadKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
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
- `ImageResizeKJ` —— 7/8 个有
- `Text Multiline` —— 7/8 个有
- `Primitive integer [Crystools]` —— 6/8 个有
- `WanVideoTeaCache` —— 6/8 个有
- `EmptyImage` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `RH_Translator` —— 2/8 个有
- `AddLabel` —— 1/8 个有
- `DF_Integer` —— 1/8 个有
- `GetImageSize` —— 1/8 个有
- `Int` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `easy clearCacheAll` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
