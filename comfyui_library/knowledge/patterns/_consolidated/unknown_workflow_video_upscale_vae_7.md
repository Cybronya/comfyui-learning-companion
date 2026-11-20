---
name: unknown_workflow_video_upscale_vae_7
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.81325
common_nodes: [DownloadAndLoadGIMMVFIModel, Fast Groups Bypasser (rgthree), GIMMVFI_interpolate, ImageScaleBy, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/SeedVR2 视频  4K无损高清放大工作流_2066393064779894786.json, 平台全量/视频超分+补帧_2055155604913704961.json, 平台全量/视频超分+补帧_2055160311501606913.json, 平台全量/视频高清+自动补帧_2006086271487188993.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_vae_7

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/SeedVR2 视频  4K无损高清放大工作流_2066393064779894786.json、平台全量/视频超分+补帧_2055155604913704961.json、平台全量/视频超分+补帧_2055160311501606913.json、平台全量/视频高清+自动补帧_2006086271487188993.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `Fast Groups Bypasser (rgthree)`
- `GIMMVFI_interpolate`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有
- `RIFE VFI` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有
- `VHS_VideoInfoLoaded` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
