---
name: unknown_workflow_lora_sampler_clip_221
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.944667
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, GetImageRangeFromBatch, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, RepeatImageBatch, SaveImage, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Wan2.1高阶玩法，电商模特姿势任意摆&衣服随心换_1946080152214532098.json, 图片生成/文生图/人物Lora（yy-1）_1956582232293036033.json, 平台全量/用Wan2.1做卡点变装带货视频，商品植入+模特换装+动作同步！_1946408282665967618.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_221

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Wan2.1高阶玩法，电商模特姿势任意摆&衣服随心换_1946080152214532098.json、图片生成/文生图/人物Lora（yy-1）_1956582232293036033.json、平台全量/用Wan2.1做卡点变装带货视频，商品植入+模特换装+动作同步！_1946408282665967618.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageRangeFromBatch`
- `KSampler`
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
- `GrowMaskWithBlur` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `LayerMask: LoadSegmentAnythingModels` —— 2/3 个有
- `LayerMask: SegmentAnythingUltra V3` —— 2/3 个有
- `MaskRepeatBatch` —— 2/3 个有
- `MaskToImage` —— 2/3 个有
- `Mix Color By Mask` —— 2/3 个有
- `preview_mask` —— 2/3 个有
- `EmptyHunyuanLatentVideo` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `WanVideoVACEStartToEndFrame` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 3 | 86% |
| Prompt 约束强度(CFG) | 1 | 0.9 - 1 | 3 | 95% |
| 采样算法 | uni_pc | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，3 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.9 - 1，3 个样本，取值集中（一致性 95%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.9，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（10/3 个样本）：Steps较低可能导致细节不足
