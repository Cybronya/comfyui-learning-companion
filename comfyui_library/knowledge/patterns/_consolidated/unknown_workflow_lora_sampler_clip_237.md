---
name: unknown_workflow_lora_sampler_clip_237
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9295
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, GetImageRangeFromBatch, KSampler, Label (rgthree), LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, RepeatImageBatch, SaveImage, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Wan2.1高阶玩法，电商模特姿势任意摆&衣服随心换_1946080152214532098.json, 图片生成/文生图/人物Lora（yy-1）_1956582232293036033.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_237

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Wan2.1高阶玩法，电商模特姿势任意摆&衣服随心换_1946080152214532098.json、图片生成/文生图/人物Lora（yy-1）_1956582232293036033.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageRangeFromBatch`
- `KSampler`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `RepeatImageBatch`
- `SaveImage`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/2 个有
- `MaskRepeatBatch` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `Mix Color By Mask` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `preview_mask` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | - | 2 | 86% |
| Prompt 约束强度(CFG) | 0.95 | - | 2 | 95% |
| 采样算法 | uni_pc | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 0.95，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.9，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（6/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
