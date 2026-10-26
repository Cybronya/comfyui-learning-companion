---
name: unknown_workflow_video_39
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.97225
common_nodes: [LatentSyncNode, LoadAudio, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [数字人/数字人/上传视频对口型Latentsync1.5=艾橘溪_1902669964103561217.json, 数字人/数字人/简易版快速无遮挡_少量遮挡对口型_2050875271661793281.json, 数字人/数字人/精准视频口型同步，保持脸部特征，只需一段原视频 + 一段目标音频_2046494511848755201.json, 视频生成/图生视频/精准视频口型同步，保持脸部特征，只需一段原视频 + 一段目标音频_2068726028138278913.json]
source: knowledge_consolidation
---

# unknown_workflow_video_39

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/上传视频对口型Latentsync1.5=艾橘溪_1902669964103561217.json、数字人/数字人/简易版快速无遮挡_少量遮挡对口型_2050875271661793281.json、数字人/数字人/精准视频口型同步，保持脸部特征，只需一段原视频 + 一段目标音频_2046494511848755201.json、视频生成/图生视频/精准视频口型同步，保持脸部特征，只需一段原视频 + 一段目标音频_2068726028138278913.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `LatentSyncNode`
- `LoadAudio`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `VideoLengthAdjuster` —— 3/4 个有
- `JWImageResizeByLongerSide` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
