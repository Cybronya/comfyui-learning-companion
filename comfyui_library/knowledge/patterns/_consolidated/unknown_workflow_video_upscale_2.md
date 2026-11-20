---
name: unknown_workflow_video_upscale_2
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.927111
common_nodes: [VHS_LoadVideo, VHS_VideoCombine, VOSR2ModelLoader, VOSR2Upscale]
problems: []
missing: []
members: [图片生成/文生图/VOSR2超分放大_2098210361257320450.json, 平台全量/VOSR2 视频放大（4x）_2105870375480545282.json, 平台全量/VOSR2视频高清化·级联2K放大_2097529946368471041.json, 平台全量/VOSR2视频高清化·级联2K放大_2100054274343530497.json, 平台全量/VOSR2视频高清化·级联2K放大_2100134918264283138.json, 平台全量/VOSR2超分放大_2098077239966523394.json, 平台全量/Vosr 2视频高清化（级联2K）_2096970443046612993.json, 数字人/数字人/视频超分 Vosr2 DLSS - 2K_2097129015567020033.json, 数字人/数字人/视频高清放大 Vosr 2 （1K-2K）_2097136348686807042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_2

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/VOSR2超分放大_2098210361257320450.json、平台全量/VOSR2 视频放大（4x）_2105870375480545282.json、平台全量/VOSR2视频高清化·级联2K放大_2097529946368471041.json、平台全量/VOSR2视频高清化·级联2K放大_2100054274343530497.json、平台全量/VOSR2视频高清化·级联2K放大_2100134918264283138.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VOSR2ModelLoader`
- `VOSR2Upscale`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoInfo` —— 7/9 个有
- `PDIMAGE_LongerSize` —— 6/9 个有
- `RTXVideoSuperResolution` —— 3/9 个有
- `easy cleanGpuUsed` —— 3/9 个有
- `PreviewAny` —— 2/9 个有
- `VHS_VideoInfoLoaded` —— 2/9 个有
- `RH_DLSS5Enhance` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
