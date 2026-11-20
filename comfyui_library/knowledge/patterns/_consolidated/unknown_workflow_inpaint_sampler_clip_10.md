---
name: unknown_workflow_inpaint_sampler_clip_10
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.862091
common_nodes: [LoadImage, SaveImage, TransparentImage]
problems: []
missing: []
members: [图片生成/图生图/一键抠图获取透明图像Segment_anything语义分割)_2117022339706736641.json, 图片生成/图生图/一键抠图获取透明图像_2003072026501873666.json, 图片生成/图生图/一键抠图获取透明图像_2006620350502674434.json, 图片生成/图生图/一键抠图获取透明图像（Segment+anything语义分割）_1990626347234070530.json, 图片生成/图生图/语义分割任何元素+黑白背景SegmentAnything+全节点注释_2056026873137778690.json, 图片生成/图生图/透明_2068898137724514305.json, 平台全量/一键抠图获取透明图像工作流_1980467784993955841.json, 平台全量/一键抠图获取透明图像（Segment anything语义分割)）_1953707851367809026.json, 平台全量/一键抠图获取透明图像（Segment anything语义分割)）_2030902411618947073.json, 平台全量/批量_一键抠图获取透明图像 (SegmentAnything_Ultra_V2)_1985601847018901506.json, 平台全量/批量_一键抠图获取透明图像 (SegmentAnything_Ultra_V2)_2008000690962046978.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/一键抠图获取透明图像Segment_anything语义分割)_2117022339706736641.json、图片生成/图生图/一键抠图获取透明图像_2003072026501873666.json、图片生成/图生图/一键抠图获取透明图像_2006620350502674434.json、图片生成/图生图/一键抠图获取透明图像（Segment+anything语义分割）_1990626347234070530.json、图片生成/图生图/语义分割任何元素+黑白背景SegmentAnything+全节点注释_2056026873137778690.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `TransparentImage`

**可变部分**（部分 workflow 才有）：
- `GroundingDinoModelLoader (segment anything)` —— 10/11 个有
- `GroundingDinoSAMSegment (segment anything)` —— 10/11 个有
- `LayerMask: SegmentAnythingUltra V2` —— 10/11 个有
- `MaskToImage` —— 10/11 个有
- `PreviewImage` —— 10/11 个有
- `SAMLoader` —— 10/11 个有
- `CLIPTextEncode` —— 1/11 个有
- `CheckpointLoaderSimple` —— 1/11 个有
- `KSampler` —— 1/11 个有
- `RHHiddenNodes` —— 1/11 个有
- `VAEDecode` —— 1/11 个有
- `VAEEncodeForInpaint` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 1 | 100% |
| 采样算法 | dpmpp_2m | - | 1 | 100% |
| 调度器 | karras | - | 1 | 100% |
| 重绘幅度 | 0.5 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
