---
name: unknown_workflow_video_sampler_clip_115
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.831167
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, INTConstant, KSampler, LoadImage, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/推荐视频：简单出效果的首尾帧_1969960068689108994.json, 视频生成/图生视频/首尾帧Wan2.2 Rapid-AIO-Mega V11N I2V_1977754220172562434.json, 视频生成/图生视频/首尾帧视频-AIO-MegaV7_1968176738117255170.json, 视频生成/文生视频/01 Wan2.2 Smooth Mix I2V 图生视频+全节点注释_2055497064678739970.json, 视频生成/文生视频/Wan2.2 Rapid-AIO-Mega 多合一极速模型_1968982500666195970.json, 视频生成/文生视频/【多功能】Wan2.2 文生图 视频参考 动作迁移Rapid-AIO-Mega_1968469960844562434.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_115

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/推荐视频：简单出效果的首尾帧_1969960068689108994.json、视频生成/图生视频/首尾帧Wan2.2 Rapid-AIO-Mega V11N I2V_1977754220172562434.json、视频生成/图生视频/首尾帧视频-AIO-MegaV7_1968176738117255170.json、视频生成/文生视频/01 Wan2.2 Smooth Mix I2V 图生视频+全节点注释_2055497064678739970.json、视频生成/文生视频/Wan2.2 Rapid-AIO-Mega 多合一极速模型_1968982500666195970.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `INTConstant`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 3/6 个有
- `Primitive integer [Crystools]` —— 3/6 个有
- `DWPreprocessor` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `ImageBlend` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `Zoe-DepthMapPreprocessor` —— 2/6 个有
- `DF_Int_to_Float` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 7 | 6 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | ipndm | - | 6 | 67% |
| 调度器 | sgm_uniform | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 7，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，6 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
