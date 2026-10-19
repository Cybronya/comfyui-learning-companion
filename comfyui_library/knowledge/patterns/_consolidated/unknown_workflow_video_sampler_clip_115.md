---
name: unknown_workflow_video_sampler_clip_115
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9358
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1894957699035693057.json, 视频生成/图生视频/1894765402319159298.json, 视频生成/图生视频/1899884316468600834.json, 视频生成/图生视频/1900639314223448065.json, 视频生成/图生视频/1955654165034930178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_115

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1894957699035693057.json、视频生成/图生视频/1894765402319159298.json、视频生成/图生视频/1899884316468600834.json、视频生成/图生视频/1900639314223448065.json、视频生成/图生视频/1955654165034930178.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `WanVideoLoraSelect` —— 3/5 个有
- `WanVideoTeaCache` —— 3/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `CR Text Replace` —— 2/5 个有
- `Primitive integer [Crystools]` —— 2/5 个有
- `Primitive string [Crystools]` —— 2/5 个有
- `easy imageSize` —— 2/5 个有
- `GetImageSizeAndCount` —— 1/5 个有
- `HyVideoEnhanceAVideo` —— 1/5 个有
- `Int` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `WanVideoFreeInitArgs` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
