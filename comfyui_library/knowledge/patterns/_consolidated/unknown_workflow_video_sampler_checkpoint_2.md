---
name: unknown_workflow_video_sampler_checkpoint_2
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.902375
common_nodes: [ImageOnlyCheckpointLoader, LoadAudio, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Sonic图片数字人_1918866017932476417.json, 视频生成/图生视频/Sonic图片数字人_1999009654929772545.json, 视频生成/图生视频/Sonic对口型数字人_1922467727339094018.json, 视频生成/图生视频/Sonic数字人V1_1892161116607520769.json, 视频生成/图生视频/Sonic数字人_1943493647671173122.json, 视频生成/图生视频/Sonic无限制数字人_1915064259728834561.json, 视频生成/图生视频/Sonic真人_卡通数字人工作流_1905890438115692545.json, 视频生成/图生视频/啊癫 sonic数字人带货_1907741322999177217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Sonic图片数字人_1918866017932476417.json、视频生成/图生视频/Sonic图片数字人_1999009654929772545.json、视频生成/图生视频/Sonic对口型数字人_1922467727339094018.json、视频生成/图生视频/Sonic数字人V1_1892161116607520769.json、视频生成/图生视频/Sonic数字人_1943493647671173122.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `LoadAudio`
- `LoadImage`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 2/8 个有
- `GetNode` —— 1/8 个有
- `ImageScale` —— 1/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `easy imageSize` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
