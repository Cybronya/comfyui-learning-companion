---
name: unknown_workflow_video_sampler_clip_28
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.927714
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1932259606163353602.json, 视频生成/图生视频/1894784892549398529.json, 视频生成/图生视频/1895025130055794689.json, 视频生成/图生视频/1894625480669069313.json, 视频生成/图生视频/1899083552049512450.json, 视频生成/图生视频/1925461590995292161.json, 视频生成/文生视频/1931880994263990273.json, 视频生成/文生视频/1933729063255367681.json, 视频生成/文生视频/1932238187564101633.json, 视频生成/文生视频/1932596754137411585.json, 视频生成/文生视频/1932262844979736577.json, 视频生成/文生视频/1942406850870710274.json, 视频生成/文生视频/1940983307876331522.json, 视频生成/文生视频/1942044343698145281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/1932259606163353602.json、视频生成/图生视频/1894784892549398529.json、视频生成/图生视频/1895025130055794689.json、视频生成/图生视频/1894625480669069313.json、视频生成/图生视频/1899083552049512450.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 14 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 11/14 个有
- `Int` —— 10/14 个有
- `ImageSizeAndBatchSize` —— 9/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/14 个有
- `MathExpression|pysssss` —— 9/14 个有
- `easy cleanGpuUsed` —— 8/14 个有
- `WanVideoTorchCompileSettings` —— 3/14 个有
- `GetImageRangeFromBatch` —— 1/14 个有
- `Image Batch` —— 1/14 个有
- `ImageResizeKJ` —— 1/14 个有
- `LayerUtility: PurgeVRAM` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
