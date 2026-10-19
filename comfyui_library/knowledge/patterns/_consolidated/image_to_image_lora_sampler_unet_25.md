---
name: image_to_image_lora_sampler_unet_25
type: Image To Image
frequency: 2
level: weak
coverage: 0.791
common_nodes: [CLIPLoader, CR Prompt Text, Fast Groups Bypasser (rgthree), JWStringConcat, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Qwen3_VQA, SaveImage, Text Multiline, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/qwen-edit-Lora分镜生图 场景生图_2092240467063824386.json, 视频生成/图生视频/1983046436193468417.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_25

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/qwen-edit-Lora分镜生图 场景生图_2092240467063824386.json、视频生成/图生视频/1983046436193468417.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `JWStringConcat`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Qwen3_VQA`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `CFGNorm` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `ProcessString` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
