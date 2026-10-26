---
name: unknown_workflow_video_sampler_checkpoint_10
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.516
common_nodes: [GetNode, ImageOnlyCheckpointLoader, LoadAudio, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, SetNode, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/sonic数字人带货-测试版，_2047593415470223361.json, 视频生成/图生视频/Sonic 数字人，一键对口型_1891727710027206657.json, 视频生成/图生视频/啊癫 sonic数字人带货_1907741322999177217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_10

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/sonic数字人带货-测试版，_2047593415470223361.json、视频生成/图生视频/Sonic 数字人，一键对口型_1891727710027206657.json、视频生成/图生视频/啊癫 sonic数字人带货_1907741322999177217.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 3 个 workflow 都包含：
- `GetNode`
- `ImageOnlyCheckpointLoader`
- `LoadAudio`
- `LoadImage`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `SetNode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `PlaySound|pysssss` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy float` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
