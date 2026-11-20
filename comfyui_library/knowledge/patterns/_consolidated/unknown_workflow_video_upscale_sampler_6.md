---
name: unknown_workflow_video_upscale_sampler_6
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.977
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LoadWanVideoT5TextEncoder, UpscaleModelLoader, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.1文生视频fusionX+NAG+视频放大_1942109815802118145.json, 视频生成/文生视频/Wan2.1文生视频fusionX+NAG_1933775109922709506.json, 视频生成/文生视频/[最新文生视频] Wan2.1 美女模特华丽转身视频特效_1947915676540383234.json, 视频生成/文生视频/龙明Wan2.1文生视频fusionX+NAG_1935006868597350401.json, 视频生成/文生视频/🥪【Wan2.1视频】lightx2v 文生视频  超清加速版🥪_1935263970838106114.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_6

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/Wan2.1文生视频fusionX+NAG+视频放大_1942109815802118145.json、视频生成/文生视频/Wan2.1文生视频fusionX+NAG_1933775109922709506.json、视频生成/文生视频/[最新文生视频] Wan2.1 美女模特华丽转身视频特效_1947915676540383234.json、视频生成/文生视频/龙明Wan2.1文生视频fusionX+NAG_1935006868597350401.json、视频生成/文生视频/🥪【Wan2.1视频】lightx2v 文生视频  超清加速版🥪_1935263970838106114.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `LoadWanVideoT5TextEncoder`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToMegapixels` —— 4/5 个有
- `WanVideoSLG` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `WanVideoLoraSelect` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `RIFE VFI` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `WanVideoMagCache` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
