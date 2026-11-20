---
name: unknown_workflow_video_101
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.97225
common_nodes: [ImageScaleBy, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/SeedVR2超分视频放大工作流_2100490385469566978.json, 平台全量/seedvr2 视频高清放大_1972921766718951425.json, 平台全量/视频-放大高清修复_1965396499062472706.json, 平台全量/视频超分-10-23B-SeedVR-video-upscaler_1981269246154014722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_101

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/SeedVR2超分视频放大工作流_2100490385469566978.json、平台全量/seedvr2 视频高清放大_1972921766718951425.json、平台全量/视频-放大高清修复_1965396499062472706.json、平台全量/视频超分-10-23B-SeedVR-video-upscaler_1981269246154014722.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageScaleBy`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoInfo` —— 3/4 个有
- `PlaySound|pysssss` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
