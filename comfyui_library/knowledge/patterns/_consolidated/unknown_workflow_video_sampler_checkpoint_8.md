---
name: unknown_workflow_video_sampler_checkpoint_8
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.676
common_nodes: [ImageOnlyCheckpointLoader, ImageResize+, LoadAudio, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, SimpleMath+, VHS_VideoCombine, easy float, easy seed]
problems: []
missing: []
members: [图片生成/图生图/最强开源数字人，通杀真人动漫各种风格_1900899027012198402.json, 视频生成/图生视频/[音频驱动]sonic真实数字人  角色说话_1922851551227035649.json, 视频生成/文生视频/各种风格真人动漫_1933419602271449089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_8

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/最强开源数字人，通杀真人动漫各种风格_1900899027012198402.json、视频生成/图生视频/[音频驱动]sonic真实数字人  角色说话_1922851551227035649.json、视频生成/文生视频/各种风格真人动漫_1933419602271449089.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `ImageResize+`
- `LoadAudio`
- `LoadImage`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `SimpleMath+`
- `VHS_VideoCombine`
- `easy float`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Bookmark (rgthree)` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `JoinStrings` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `String Literal` —— 2/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
