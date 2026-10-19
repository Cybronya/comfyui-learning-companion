---
name: unknown_workflow_video_sampler_checkpoint_12
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.845
common_nodes: [CM_IntToFloat, Fast Groups Bypasser (rgthree), ImageOnlyCheckpointLoader, JjkText, LayerUtility: PurgeVRAM, LoadAudio, LoadImage, Note _O, Primitive integer [Crystools], Primitive string [Crystools], SONICSampler, SONICTLoader, SONIC_PreData, SaveAudio, ShowText|pysssss, VHS_VideoCombine, YUE_Stage_A_Loader, YUE_Stage_A_Sampler, YUE_Stage_B_Loader, YUE_Stage_B_Sampler]
problems: []
missing: []
members: [视频生成/图生视频/1896960355950600194.json, 音频生成/音频生成/DiffRhythm+Sonic+Yue数字人唱歌工作流V3_1904056515828031489.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_12

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1896960355950600194.json、音频生成/音频生成/DiffRhythm+Sonic+Yue数字人唱歌工作流V3_1904056515828031489.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CM_IntToFloat`
- `Fast Groups Bypasser (rgthree)`
- `ImageOnlyCheckpointLoader`
- `JjkText`
- `LayerUtility: PurgeVRAM`
- `LoadAudio`
- `LoadImage`
- `Note _O`
- `Primitive integer [Crystools]`
- `Primitive string [Crystools]`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `SaveAudio`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `YUE_Stage_A_Loader`
- `YUE_Stage_A_Sampler`
- `YUE_Stage_B_Loader`
- `YUE_Stage_B_Sampler`

**可变部分**（部分 workflow 才有）：
- `DiffRhythmRun` —— 1/2 个有
- `MultiLinePrompt` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
