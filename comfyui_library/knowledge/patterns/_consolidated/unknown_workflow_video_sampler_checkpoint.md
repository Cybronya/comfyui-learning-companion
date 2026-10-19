---
name: unknown_workflow_video_sampler_checkpoint
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.951273
common_nodes: [ImageOnlyCheckpointLoader, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1927032738057191426.json, 视频生成/图生视频/Sonic 数字人（可配置视频尺寸）_2104499076824920066.json, 视频生成/图生视频/1918866017932476417.json, 视频生成/图生视频/1999009654929772545.json, 视频生成/图生视频/1909773433918451714.json, 视频生成/图生视频/1892161116607520769.json, 视频生成/图生视频/1943493647671173122.json, 视频生成/图生视频/2032256428198600706.json, 视频生成/图生视频/1909784768551055362.json, 视频生成/图生视频/1887696642861367297.json, 音频生成/音频生成/seed-vc 快速语音音色转变+sonic对口型_1928023395433070593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/1927032738057191426.json、视频生成/图生视频/Sonic 数字人（可配置视频尺寸）_2104499076824920066.json、视频生成/图生视频/1918866017932476417.json、视频生成/图生视频/1999009654929772545.json、视频生成/图生视频/1909773433918451714.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 11 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `LoadImage`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 10/11 个有
- `easy cleanGpuUsed` —— 5/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/11 个有
- `SaveAudio` —— 3/11 个有
- `ImageResizeKJ` —— 2/11 个有
- `VHS_LoadAudioUpload` —— 2/11 个有
- `PreviewImage` —— 1/11 个有
- `SeedVCNode` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
