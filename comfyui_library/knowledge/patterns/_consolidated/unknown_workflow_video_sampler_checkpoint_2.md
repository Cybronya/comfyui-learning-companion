---
name: unknown_workflow_video_sampler_checkpoint_2
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.947875
common_nodes: [ImageOnlyCheckpointLoader, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/Sonic数字人解决方案，唱歌，口播无所不能！_1921799292338520065.json, 数字人/数字人/Sonic真人数字人_2066858697283956738.json, 数字人/数字人/sonic数字人_1904756089903321090.json, 数字人/数字人/sonic数字人_1925078177524477954.json, 数字人/数字人/数字人一键唱歌_1898634893637668866.json, 视频生成/图生视频/Sonic 数字人（可配置视频尺寸）_2104499076824920066.json, 视频生成/图生视频/Sonic数字人-Dawn_1909773433918451714.json, 视频生成/图生视频/图生视频-Sonic数字人唱歌对口型_1909784768551055362.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/Sonic数字人解决方案，唱歌，口播无所不能！_1921799292338520065.json、数字人/数字人/Sonic真人数字人_2066858697283956738.json、数字人/数字人/sonic数字人_1904756089903321090.json、数字人/数字人/sonic数字人_1925078177524477954.json、数字人/数字人/数字人一键唱歌_1898634893637668866.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `LoadImage`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 6/8 个有
- `VHS_LoadAudioUpload` —— 3/8 个有
- `easy cleanGpuUsed` —— 3/8 个有
- `ImageResizeKJ` —— 2/8 个有
- `PreviewImage` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
