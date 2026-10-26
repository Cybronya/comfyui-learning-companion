---
name: unknown_workflow_video_sampler_checkpoint
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.926571
common_nodes: [ImageOnlyCheckpointLoader, LoadAudio, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/腾讯Sonic数字人-视频声音两种模式_1890649595049844738.json, 视频生成/图生视频/CG迷-简单高效的对口型数字人Sonic_1927032738057191426.json, 视频生成/图生视频/Sonic图片数字人_1918866017932476417.json, 视频生成/图生视频/Sonic图片数字人_1999009654929772545.json, 视频生成/图生视频/Sonic数字人V1_1892161116607520769.json, 视频生成/图生视频/Sonic数字人_1943493647671173122.json, 视频生成/图生视频/Sonic无限制数字人_1915064259728834561.json, 视频生成/图生视频/Sonic真人_卡通数字人工作流_1905890438115692545.json, 视频生成/图生视频/人物照片说话唱歌_音频感知_2085780849454305281.json, 视频生成/图生视频/数字人工作流_图片音频驱动_支持人形五官_sonic_1930219583813357570.json, 视频生成/图生视频/电商定制数字人_1924353663471374338.json, 视频生成/文生视频/Sonic官方工作流-数字人模型_1930267877079728130.json, 音频生成/音频生成/Sonic真人_卡通数字人_1916670312954396674.json, 音频生成/音频生成/sonic_ai数字人口播对口型工作流_2068716274812801026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（数字人/数字人/腾讯Sonic数字人-视频声音两种模式_1890649595049844738.json、视频生成/图生视频/CG迷-简单高效的对口型数字人Sonic_1927032738057191426.json、视频生成/图生视频/Sonic图片数字人_1918866017932476417.json、视频生成/图生视频/Sonic图片数字人_1999009654929772545.json、视频生成/图生视频/Sonic数字人V1_1892161116607520769.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 14 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `LoadAudio`
- `LoadImage`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 2/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `LayerUtility: PurgeVRAM` —— 1/14 个有
- `PrimitiveFloat` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
