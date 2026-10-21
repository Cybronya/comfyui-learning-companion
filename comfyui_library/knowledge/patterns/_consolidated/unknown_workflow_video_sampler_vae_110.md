---
name: unknown_workflow_video_sampler_vae_110
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6978
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1913228889936855042.json, 视频生成/图生视频/1912169450282647553.json, 视频生成/图生视频/1926293882655457281.json, 视频生成/图生视频/1945694756720582658.json, 视频生成/图生视频/1908024334332342274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_110

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1913228889936855042.json、视频生成/图生视频/1912169450282647553.json、视频生成/图生视频/1926293882655457281.json、视频生成/图生视频/1945694756720582658.json、视频生成/图生视频/1908024334332342274.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：70%

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
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `MaskPreview+` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `WanVideoVACEStartToEndFrame` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `WanVideoVACEModelSelect` —— 3/5 个有
- `Note Plus (mtb)` —— 2/5 个有
- `ImageBatchMulti` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `ImageFromBatch+` —— 1/5 个有
- `InspyrenetRembg` —— 1/5 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `Note _O` —— 1/5 个有
- `WanVideoLoraSelect` —— 1/5 个有
- `WanVideoVRAMManagement` —— 1/5 个有
- `easy imageScaleDownToSize` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
