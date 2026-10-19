---
name: unknown_workflow_video_sampler_clip_126
type: Unknown Workflow
frequency: 5
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/1896034997206188033.json, 视频生成/文生视频/1895182420566212609.json, 视频生成/文生视频/1934444729025327105.json, 视频生成/文生视频/1909164954489135106.json, 视频生成/文生视频/通义万相文生视频+放大补帧_2072999857343995904.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_126

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/1896034997206188033.json、视频生成/文生视频/1895182420566212609.json、视频生成/文生视频/1934444729025327105.json、视频生成/文生视频/1909164954489135106.json、视频生成/文生视频/通义万相文生视频+放大补帧_2072999857343995904.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 2/5 个有
- `GIMMVFI_interpolate` —— 2/5 个有
- `ImageScaleBy` —— 2/5 个有
- `ImageUpscaleWithModel` —— 2/5 个有
- `UpscaleModelLoader` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 5 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 5 | 100% |
| 采样算法 | uni_pc | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
