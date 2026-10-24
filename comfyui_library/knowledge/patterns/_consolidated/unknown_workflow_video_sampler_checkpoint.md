---
name: unknown_workflow_video_sampler_checkpoint
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8823
common_nodes: [ImageOnlyCheckpointLoader, LoadAudio, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/电商定制数字人_1924353663471374338.json, 视频生成/图生视频/腾讯Sonic数字人对口型(任意宽高设置)_2059545377682051074.json, 视频生成/图生视频/腾讯Sonic数字人对口型(任意宽高设置)_2070787575148793858.json, 视频生成/图生视频/腾讯Sonic数字人对口型(任意宽高设置)_2070791704621445121.json, 视频生成/图生视频/腾讯开源 Sonic-虚拟AI数字人唱歌对口型口播_1911060748980711425.json, 视频生成/文生视频/Sonic官方工作流-数字人模型_1930267877079728130.json, 音频生成/音频生成/Sonic真人_卡通数字人_1916670312954396674.json, 音频生成/音频生成/sonic_ai数字人口播对口型工作流_2068716274812801026.json, 音频生成/音频生成/腾讯Sonic数字人对口型(任意宽高设置)_1890418394431410177.json, 音频生成/音频生成/腾讯Sonic数字人对口型_2034523663965360129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/电商定制数字人_1924353663471374338.json、视频生成/图生视频/腾讯Sonic数字人对口型(任意宽高设置)_2059545377682051074.json、视频生成/图生视频/腾讯Sonic数字人对口型(任意宽高设置)_2070787575148793858.json、视频生成/图生视频/腾讯Sonic数字人对口型(任意宽高设置)_2070791704621445121.json、视频生成/图生视频/腾讯开源 Sonic-虚拟AI数字人唱歌对口型口播_1911060748980711425.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `LoadAudio`
- `LoadImage`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 6/10 个有
- `CM_IntToFloat` —— 5/10 个有
- `Primitive integer [Crystools]` —— 5/10 个有
- `VHS_LoadVideo` —— 5/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
