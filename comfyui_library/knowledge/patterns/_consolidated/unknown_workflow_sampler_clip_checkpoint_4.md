---
name: unknown_workflow_sampler_clip_checkpoint_4
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.850286
common_nodes: [ApplySageAttention, CLIPTextEncode, CheckpointLoaderSimple, JWInteger, KSampler, LoadImage, ModelSamplingSD3, SaveImage, TT_img_enc, VAEDecode, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/（自用）Wan2.2 Rapid-AIO-Mega V11 模型文生视频极速版_1985333672461148162.json, 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V11模型图生视频极速版_1985334147310829570.json, 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V3.1图生视频极速带音频_1973021430713593858.json, 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V3.1图生视频极速版_1973020589118066690.json, 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V5图生视频极速带音频_1974823195108880385.json, 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V6.1模型图生视频极速版_1976907332506587138.json, 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V6图生视频极速带音频_1975831152592334850.json, 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V6图生视频极速版_1975830994022436866.json, 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V7模型图生视频极速版_1977747995724840961.json, 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega图生视频极速_1967932359611940866.json, 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega图生视频极速带音频_1968344636660035586.json, 视频生成/文生视频/（自用）Qwen-EditWan2.2 Rapid-AIO-Mega V7 模型文生视频极速版 V2_1977742174395793409.json, 视频生成/文生视频/（自用）Wan2.2 Rapid-AIO-Mega V5图生视频_1974823222036271106.json, 视频生成/文生视频/（自用）Wan2.2 Rapid-AIO-Mega V6.1模型文生视频极速版_1977017622829125634.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_4

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/（自用）Wan2.2 Rapid-AIO-Mega V11 模型文生视频极速版_1985333672461148162.json、视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V11模型图生视频极速版_1985334147310829570.json、视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V3.1图生视频极速带音频_1973021430713593858.json、视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V3.1图生视频极速版_1973020589118066690.json、视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V5图生视频极速带音频_1974823195108880385.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 14 个 workflow 都包含：
- `ApplySageAttention`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `JWInteger`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveImage`
- `TT_img_enc`
- `VAEDecode`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 13/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/14 个有
- `WanVideoVACEStartToEndFrame` —— 11/14 个有
- `HunyuanVideoFoley` —— 4/14 个有
- `LayerUtility: PurgeVRAM V2` —— 4/14 个有
- `TT_img_enc_v2` —— 4/14 个有
- `ImageFromBatch+` —— 3/14 个有
- `CLIPLoader` —— 2/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | ipndm | - | 14 | 43% |
| 调度器 | beta | - | 14 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，14 个样本，一致性 43%
- 调度器 最常用 beta，14 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
