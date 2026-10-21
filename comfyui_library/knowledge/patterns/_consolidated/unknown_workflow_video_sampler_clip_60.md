---
name: unknown_workflow_video_sampler_clip_60
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.940222
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1900072045734932482.json, 视频生成/图生视频/1901173335622066177.json, 视频生成/图生视频/1914997055247347713.json, 视频生成/图生视频/1927650029039960065.json, 视频生成/图生视频/1926260024211894274.json, 视频生成/图生视频/1926859927644704769.json, 视频生成/图生视频/1907747905766367234.json, 视频生成/图生视频/1896064173954695170.json, 视频生成/图生视频/1949494090500579330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_60

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1900072045734932482.json、视频生成/图生视频/1901173335622066177.json、视频生成/图生视频/1914997055247347713.json、视频生成/图生视频/1927650029039960065.json、视频生成/图生视频/1926260024211894274.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
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
- `WanVideoEnhanceAVideo` —— 7/9 个有
- `ImageResizeKJ` —— 6/9 个有
- `WanVideoTeaCache` —— 6/9 个有
- `WanVideoTorchCompileSettings` —— 6/9 个有
- `Int` —— 5/9 个有
- `WanVideoLoraSelect` —— 5/9 个有
- `CR Upscale Image` —— 4/9 个有
- `JjkText` —— 4/9 个有
- `WanVideoExperimentalArgs` —— 4/9 个有
- `RIFE VFI` —— 3/9 个有
- `WanVideoSLG` —— 3/9 个有
- `ImageSizeAndBatchSize` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `WanVideoMagCache` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
