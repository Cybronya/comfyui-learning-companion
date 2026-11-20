---
name: unknown_workflow_video_upscale_11
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9172
common_nodes: [FaceRestoreCFWithModel, FaceRestoreModelLoader, ImageResize+, ImageUpscaleWithModel, LayerColor: Brightness & Contrast, LoadImage, ReActorFaceSwap, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/快速换脸_1919744550246481921.json, 平台全量/视频换脸_1815327610992844802.json, 平台全量/视频换脸_1818285423667097602.json, 平台全量/视频换脸_1821411017007239170.json, 视频生成/图生视频/【视频流】Reactor视频换脸_1819030257314758658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_11

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/快速换脸_1919744550246481921.json、平台全量/视频换脸_1815327610992844802.json、平台全量/视频换脸_1818285423667097602.json、平台全量/视频换脸_1821411017007239170.json、视频生成/图生视频/【视频流】Reactor视频换脸_1819030257314758658.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `FaceRestoreCFWithModel`
- `FaceRestoreModelLoader`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `LayerColor: Brightness & Contrast`
- `LoadImage`
- `ReActorFaceSwap`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
