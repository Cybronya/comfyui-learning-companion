---
name: unknown_workflow_video_sampler_clip_114
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.958
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1894765811745816578.json, 视频生成/图生视频/1913798137197330434.json, 视频生成/图生视频/2006534001057599489.json, 视频生成/图生视频/1935718246421028865.json, 视频生成/图生视频/1950422709600698370.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_114

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1894765811745816578.json、视频生成/图生视频/1913798137197330434.json、视频生成/图生视频/2006534001057599489.json、视频生成/图生视频/1935718246421028865.json、视频生成/图生视频/1950422709600698370.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

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
- `LayerUtility: PurgeVRAM` —— 4/5 个有
- `WanVideoLoraSelect` —— 4/5 个有
- `ImpactInt` —— 3/5 个有
- `JjkText` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `ImageFromBatch+` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `Note _O` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
