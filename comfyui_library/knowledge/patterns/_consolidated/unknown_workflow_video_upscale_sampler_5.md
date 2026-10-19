---
name: unknown_workflow_video_upscale_sampler_5
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.974
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1896425086226726914.json, 视频生成/图生视频/1908182289698664449.json, 视频生成/图生视频/1912458633853239298.json, 视频生成/图生视频/1909453938431504386.json, 视频生成/文生视频/1934071211976478722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_5

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1896425086226726914.json、视频生成/图生视频/1908182289698664449.json、视频生成/图生视频/1912458633853239298.json、视频生成/图生视频/1909453938431504386.json、视频生成/文生视频/1934071211976478722.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 4/5 个有
- `GIMMVFI_interpolate` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 4/5 个有
- `WanVideoLoraSelect` —— 4/5 个有
- `ImageResizeKJ` —— 3/5 个有
- `UpscaleImageByUsingModel` —— 3/5 个有
- `ImageUpscaleWithModel` —— 2/5 个有
- `INTConstant` —— 1/5 个有
- `ImageResize+` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
