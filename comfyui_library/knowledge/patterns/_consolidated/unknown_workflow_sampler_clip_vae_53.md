---
name: unknown_workflow_sampler_clip_vae_53
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.907
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, JWInteger, KSampler, LayerUtility: PurgeVRAM V2, ModelSamplingAuraFlow, PresetTextSelector, PrimitiveStringMultiline, RHHiddenNodes, SaveImage, SeedVR2ExtraArgs, SeedVR2GGUF, ShowText|pysssss, VAEDecode, VAELoader, easy anythingIndexSwitch, easy promptConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AI 短剧 文生空场景 专用 Qwen-image 自动扩写 专用提示词_2010356412597149698.json, 图片生成/文生图/AI 短剧 文生空场景 专用 Qwen-image 自动扩写 专用提示词_2010369760147546114.json, 图片生成/文生图/AI短剧定妆照Qwen-image Nunchaku极速文生图_1981626710930137089.json, 图片生成/文生图/Qwen-imageQ8去AI味文生图最真实的人像特写真实肤感_1976636559145476098.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_53

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/AI 短剧 文生空场景 专用 Qwen-image 自动扩写 专用提示词_2010356412597149698.json、图片生成/文生图/AI 短剧 文生空场景 专用 Qwen-image 自动扩写 专用提示词_2010369760147546114.json、图片生成/文生图/AI短剧定妆照Qwen-image Nunchaku极速文生图_1981626710930137089.json、图片生成/文生图/Qwen-imageQ8去AI味文生图最真实的人像特写真实肤感_1976636559145476098.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `JWInteger`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingAuraFlow`
- `PresetTextSelector`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `SaveImage`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `ShowText|pysssss`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `NunchakuQwenImageDiTLoader` —— 3/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `NunchakuQwenImageLoraStack` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 40 | 4 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 4 | 13% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 40，4 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，4 个样本，取值分散，一致性仅 13%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
