---
name: unknown_workflow_video_upscale_18
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.952333
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, VOSR2ModelLoader, VOSR2Upscale]
problems: []
missing: []
members: [平台全量/VOSR2_视频逐帧放大-适合低显存-文字不乱码_2104581698083180546.json, 平台全量/Vosr 2视频高清放大-文字不乱码_2104847913410187266.json, 平台全量/视频超分高清放大_2097487263541321729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_18

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/VOSR2_视频逐帧放大-适合低显存-文字不乱码_2104581698083180546.json、平台全量/Vosr 2视频高清放大-文字不乱码_2104847913410187266.json、平台全量/视频超分高清放大_2097487263541321729.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `VOSR2ModelLoader`
- `VOSR2Upscale`

**可变部分**（部分 workflow 才有）：
- `easy int` —— 2/3 个有
- `GH_AudioVideoMerger` —— 1/3 个有
- `RebatchImages` —— 1/3 个有
- `VHS_Unbatch` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
