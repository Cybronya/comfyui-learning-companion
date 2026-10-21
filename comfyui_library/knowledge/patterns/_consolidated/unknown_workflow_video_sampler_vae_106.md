---
name: unknown_workflow_video_sampler_vae_106
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9614
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1936289706663399425.json, 视频生成/文生视频/1934582390809370626.json, 视频生成/文生视频/1934499736151871490.json, 视频生成/文生视频/1936061298029285377.json, 视频生成/文生视频/1942109815802118145.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_106

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1936289706663399425.json、视频生成/文生视频/1934582390809370626.json、视频生成/文生视频/1934499736151871490.json、视频生成/文生视频/1936061298029285377.json、视频生成/文生视频/1942109815802118145.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 2/5 个有
- `UpscaleModelLoader` —— 2/5 个有
- `ImageResizeKJ` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `RIFE VFI` —— 1/5 个有
- `WanVideoImageToVideoEncode` —— 1/5 个有
- `WanVideoMagCache` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy clearCacheAll` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
