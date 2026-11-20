---
name: unknown_workflow_video_sampler_41
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.95125
common_nodes: [ControlNextDecode, ControlNextDiffusersScheduler, ControlNextGetPoses, ControlNextSampler, DownloadAndLoadControlNeXt, GetImageSizeAndCount, ImageConcatMulti, ImageResize+, ImageScale, LoadImage, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/人物动作，图转视频 controlnext_svd_diffusers_1827319850875408386.json, 平台全量/视频动作迁移controlnext_svd_diffusers_1826524711273811969.json, 平台全量/视频动作迁移controlnext_svd_diffusers_2105101368099950593.json, 平台全量/视频动作迁移controlnext_svd_diffusers_2105470099581919233.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_41

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/人物动作，图转视频 controlnext_svd_diffusers_1827319850875408386.json、平台全量/视频动作迁移controlnext_svd_diffusers_1826524711273811969.json、平台全量/视频动作迁移controlnext_svd_diffusers_2105101368099950593.json、平台全量/视频动作迁移controlnext_svd_diffusers_2105470099581919233.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `ControlNextDecode`
- `ControlNextDiffusersScheduler`
- `ControlNextGetPoses`
- `ControlNextSampler`
- `DownloadAndLoadControlNeXt`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageResize+`
- `ImageScale`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Display Int (rgthree)` —— 3/4 个有
- `PreviewImage` —— 3/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
