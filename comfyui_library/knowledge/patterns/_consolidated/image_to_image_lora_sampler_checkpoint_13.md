---
name: image_to_image_lora_sampler_checkpoint_13
type: Image To Image
frequency: 2
level: weak
coverage: 0.914
common_nodes: [CR Text, CheckpointLoaderSimple, ConditioningZeroOut, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/WH-AI-Studio-Qwen2511万能单图修改器_2015621556352847873.json, 图片生成/图生图/WH-AI-Studio-万向镜头可视调节+提示词改动作（Qwen-Edit）_2011066245751246850.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_checkpoint_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/WH-AI-Studio-Qwen2511万能单图修改器_2015621556352847873.json、图片生成/图生图/WH-AI-Studio-万向镜头可视调节+提示词改动作（Qwen-Edit）_2011066245751246850.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `QwenMultiangleCameraNode` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有
- `easy promptConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
