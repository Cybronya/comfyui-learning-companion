---
name: unknown_workflow_sampler_30
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.975
common_nodes: [LoadAudio, LoadImage, RunningHub FlashTalk Loader, RunningHub FlashTalk Sampler, SaveVideo]
problems: []
missing: []
members: [数字人/数字人/FlashTalk实时数字人_2016663666405412866.json, 数字人/数字人/艾希 无限时长FlashTalk实时数字人工作流 V1.0_2016408423792906242.json, 视频生成/图生视频/MILA无限时长实时数字人工作流 V1.0_2057318257446711297.json, 视频生成/文生视频/FlashTalk 无限时长实时数字人工作流   高保真 直播数字人 超强_2057451172184809474.json, 视频生成/文生视频/SoulX-FlashTalk数字人_2017233700479569922.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_30

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/FlashTalk实时数字人_2016663666405412866.json、数字人/数字人/艾希 无限时长FlashTalk实时数字人工作流 V1.0_2016408423792906242.json、视频生成/图生视频/MILA无限时长实时数字人工作流 V1.0_2057318257446711297.json、视频生成/文生视频/FlashTalk 无限时长实时数字人工作流   高保真 直播数字人 超强_2057451172184809474.json、视频生成/文生视频/SoulX-FlashTalk数字人_2017233700479569922.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadAudio`
- `LoadImage`
- `RunningHub FlashTalk Loader`
- `RunningHub FlashTalk Sampler`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio` —— 3/5 个有
- `AudioCrop` —— 2/5 个有
- `FluxKontextImageScale` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
