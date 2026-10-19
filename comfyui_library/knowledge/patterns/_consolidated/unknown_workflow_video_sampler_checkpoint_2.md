---
name: unknown_workflow_video_sampler_checkpoint_2
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.916
common_nodes: [ImageOnlyCheckpointLoader, LoadAudio, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1915064259728834561.json, 视频生成/图生视频/1905890438115692545.json, 视频生成/图生视频/人物照片说话唱歌_音频感知_2085780849454305281.json, 视频生成/图生视频/1891734244585287681.json, 视频生成/图生视频/1924353663471374338.json, 视频生成/文生视频/1930267877079728130.json, 音频生成/音频生成/Sonic真人_卡通数字人_1916670312954396674.json, 音频生成/音频生成/sonic_ai数字人口播对口型工作流_2068716274812801026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1915064259728834561.json、视频生成/图生视频/1905890438115692545.json、视频生成/图生视频/人物照片说话唱歌_音频感知_2085780849454305281.json、视频生成/图生视频/1891734244585287681.json、视频生成/图生视频/1924353663471374338.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：92%

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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
