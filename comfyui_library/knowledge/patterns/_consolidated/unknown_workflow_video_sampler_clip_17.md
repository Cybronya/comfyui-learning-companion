---
name: unknown_workflow_video_sampler_clip_17
type: Unknown Workflow
frequency: 22
level: strong
coverage: 0.885
common_nodes: [ApplySageAttention, CLIPTextEncode, CheckpointLoaderSimple, JWInteger, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, VAEDecode, WanVaceToVideo, WanVideoVACEStartToEndFrame]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/68tushengship_2052455720964108290.json, 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V3图生视频极速版_1969938692712374273.json, 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V4图生视频极速版_1973027412923518977.json, 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V4首尾帧极速版_1973020572286324737.json, 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V5图生视频极速版_1974823579739099138.json, 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V5图生视频极速版_1975785104662507522.json, 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V5首尾帧极速版_1974823466853642241.json, 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V5首尾帧极速版_1975842469181042690.json, 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V6图生视频极速版_1975830949797695489.json, 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V6首尾帧极速版_1975830980877529090.json, 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega图生视频极速版_1967882318759231490.json, 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega图生视频极速版_2052639403599773698.json, 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega首尾帧极速版_1967872715644350466.json, 视频生成/图生视频/Wan2.2+Rapid 超长视频生成 极速图生视频 保留真实细节生视频 AIO Mega_2026891616392318977.json, 视频生成/图生视频/图生视频Wan2.2 Rapid-AIO-Mega极速版_2015371737944297474.json, 视频生成/图生视频/图生视频极速版Wan2.2 Rapid-AIO-Mega_2054818446705217538.json, 视频生成/图生视频/图生视频极速版Wan2.2 Rapid-AIO-Mega（极速版）_1967954562684432386.json, 视频生成/图生视频/图生视频极速版Wan2.2 Rapid-AIO-Mega（极速版）_1972635208992399362.json, 视频生成/图生视频/图生视频极速版Wan2.2 Rapid-AIO-Mega（极速版）_2051858183349645314.json, 视频生成/图生视频/图生视频极速版Wan2.2+Rapid-AIO-Mega（极速版）_2052263751210029058.json, 视频生成/图生视频/极速图生视频 保留真实细节生视频 Wan2.2 Rapid-AIO-Mega 超级加速版_2026459324947632130.json, 视频生成/文生视频/Wan2.2+Rapid  极速图生视频  AIO Mega_2069600144449957889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/反推提示词/68tushengship_2052455720964108290.json、视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V3图生视频极速版_1969938692712374273.json、视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V4图生视频极速版_1973027412923518977.json、视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V4首尾帧极速版_1973020572286324737.json、视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V5图生视频极速版_1974823579739099138.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 22 个 workflow 都包含：
- `ApplySageAttention`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `JWInteger`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `VAEDecode`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 21/22 个有
- `ImageConcanate` —— 16/22 个有
- `PDIMAGE_LongerSize` —— 16/22 个有
- `LayerUtility: PurgeVRAM V2` —— 11/22 个有
- `MathExpression|pysssss` —— 10/22 个有
- `CR Prompt Text` —— 5/22 个有
- `ImageResizeKJv2` —— 5/22 个有
- `CreateVideo` —— 1/22 个有
- `RTXVideoSuperResolution` —— 1/22 个有
- `SaveVideo` —— 1/22 个有
- `easy imageSize` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 22 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 22 | 100% |
| 采样算法 | ipndm | - | 22 | 95% |
| 调度器 | sgm_uniform | - | 22 | 77% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，22 个样本，一致性 95%
- 调度器 最常用 sgm_uniform，22 个样本，一致性 77%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 高发问题（22/22 个样本）：Steps较低可能导致细节不足
