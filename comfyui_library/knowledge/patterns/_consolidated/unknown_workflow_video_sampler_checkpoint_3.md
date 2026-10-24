---
name: unknown_workflow_video_sampler_checkpoint_3
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.902333
common_nodes: [ImageOnlyCheckpointLoader, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/sonic图生视频_1994020314057293826.json, 图片生成/图生图/图片转为gif_1912312375054401538.json, 视频生成/图生视频/CG迷-简单高效的对口型数字人Sonic_1927032738057191426.json, 视频生成/图生视频/Sonic 数字人（可配置视频尺寸）_2104499076824920066.json, 视频生成/图生视频/Sonic 数字人，一键对口型_1891727710027206657.json, 视频生成/图生视频/Sonic数字人-Dawn_1909773433918451714.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_3

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/sonic图生视频_1994020314057293826.json、图片生成/图生图/图片转为gif_1912312375054401538.json、视频生成/图生视频/CG迷-简单高效的对口型数字人Sonic_1927032738057191426.json、视频生成/图生视频/Sonic 数字人（可配置视频尺寸）_2104499076824920066.json、视频生成/图生视频/Sonic 数字人，一键对口型_1891727710027206657.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `LoadImage`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 5/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `VHS_LoadAudioUpload` —— 2/6 个有
- `GetNode` —— 1/6 个有
- `ImageResizeKJ` —— 1/6 个有
- `PlaySound|pysssss` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `easy float` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
