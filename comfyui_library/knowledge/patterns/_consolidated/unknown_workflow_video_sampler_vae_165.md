---
name: unknown_workflow_video_sampler_vae_165
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.897333
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1918479213039386625.json, 视频生成/图生视频/1945368931681095682.json, 视频生成/图生视频/1952583718227652610.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_165

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1918479213039386625.json、视频生成/图生视频/1945368931681095682.json、视频生成/图生视频/1952583718227652610.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `WanVideoSLG` —— 2/3 个有
- `WanVideoVACEModelSelect` —— 2/3 个有
- `DepthAnythingPreprocessor` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoadLatent` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `SaveLatent` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `Text` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
