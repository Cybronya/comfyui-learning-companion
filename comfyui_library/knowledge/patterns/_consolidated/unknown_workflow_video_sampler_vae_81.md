---
name: unknown_workflow_video_sampler_vae_81
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.925333
common_nodes: [ImageConcatMulti, ImagePadKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1934826257706065921.json, 视频生成/图生视频/1918902394158256130.json, 视频生成/图生视频/1922106634145841154.json, 视频生成/图生视频/1991787446910267394.json, 视频生成/图生视频/1934517435972419585.json, 视频生成/图生视频/1927557646478643202.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_81

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1934826257706065921.json、视频生成/图生视频/1918902394158256130.json、视频生成/图生视频/1922106634145841154.json、视频生成/图生视频/1991787446910267394.json、视频生成/图生视频/1934517435972419585.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ImageResizeKJ` —— 5/6 个有
- `Text Multiline` —— 5/6 个有
- `Primitive integer [Crystools]` —— 4/6 个有
- `WanVideoTeaCache` —— 4/6 个有
- `EmptyImage` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `AddLabel` —— 1/6 个有
- `DF_Integer` —— 1/6 个有
- `GetImageSize` —— 1/6 个有
- `Int` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有
- `easy int` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
