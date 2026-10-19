---
name: unknown_workflow_video_sampler_vae_88
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.992833
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1915435031794487298.json, 视频生成/图生视频/1935621169481711618.json, 视频生成/图生视频/1933717714491854849.json, 视频生成/图生视频/1917413592033853442.json, 视频生成/图生视频/1942392915929010177.json, 视频生成/图生视频/1934430559047217153.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_88

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1915435031794487298.json、视频生成/图生视频/1935621169481711618.json、视频生成/图生视频/1933717714491854849.json、视频生成/图生视频/1917413592033853442.json、视频生成/图生视频/1942392915929010177.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 6 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 5/6 个有
- `WanVideoExperimentalArgs` —— 5/6 个有
- `WanVideoSLG` —— 5/6 个有
- `WanVideoVACEEncode` —— 4/6 个有
- `WanVideoVACEStartToEndFrame` —— 4/6 个有
- `CR Prompt Text` —— 3/6 个有
- `GetImageSizeAndCount` —— 3/6 个有
- `Int` —— 3/6 个有
- `JWInteger` —— 3/6 个有
- `WanVideoTorchCompileSettings` —— 3/6 个有
- `WanVideoEncode` —— 2/6 个有
- `WanVideoEnhanceAVideo` —— 2/6 个有
- `WanVideoPhantomEmbeds` —— 2/6 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/6 个有
- `GIMMVFI_interpolate` —— 1/6 个有
- `ImagePadKJ` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
