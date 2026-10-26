---
name: unknown_workflow_video_sampler_checkpoint_3
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.958333
common_nodes: [ImageOnlyCheckpointLoader, LoadAudio, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/sonic图生视频_1994020314057293826.json, 图片生成/图生图/图片转为gif_1912312375054401538.json, 数字人/数字人/Sonic图片数字人_1991033507801702402.json, 数字人/数字人/Sonic图片数字人_2068963051331735553.json, 数字人/数字人/Sonic数字人_1905107069064908802.json, 数字人/数字人/Sonic数字人生成器新版本_1888963892326948865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_3

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/sonic图生视频_1994020314057293826.json、图片生成/图生图/图片转为gif_1912312375054401538.json、数字人/数字人/Sonic图片数字人_1991033507801702402.json、数字人/数字人/Sonic图片数字人_2068963051331735553.json、数字人/数字人/Sonic数字人_1905107069064908802.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `LoadAudio`
- `LoadImage`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 2/6 个有
- `ImageResizeKJ` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `easy imageSize` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
