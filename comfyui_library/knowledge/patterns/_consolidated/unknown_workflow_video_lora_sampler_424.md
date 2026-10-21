---
name: unknown_workflow_video_lora_sampler_424
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.744
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1925407407495913474.json, 视频生成/图生视频/1922976069052526594.json, 视频生成/图生视频/1923351461173129217.json, 视频生成/图生视频/1927701391375253506.json, 视频生成/图生视频/1955521868151361537.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_424

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1925407407495913474.json、视频生成/图生视频/1922976069052526594.json、视频生成/图生视频/1923351461173129217.json、视频生成/图生视频/1927701391375253506.json、视频生成/图生视频/1955521868151361537.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `WanVideoModelLoader` —— 4/5 个有
- `WanVideoTeaCache` —— 4/5 个有
- `AIO_Preprocessor` —— 3/5 个有
- `VHS_LoadVideo` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `ImageUpscaleWithModel` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `UpscaleModelLoader` —— 2/5 个有
- `WanVideoVACEStartToEndFrame` —— 2/5 个有
- `AddLabel` —— 1/5 个有
- `ColorMatch` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `ImageBlend` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
