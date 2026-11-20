---
name: image_to_image_lora_sampler_unet_229
type: Image To Image
frequency: 2
level: weak
coverage: 0.639
common_nodes: [CFGNorm, CLIPLoader, Fast Groups Bypasser (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/产品生成海报溶图_2039993998181404673.json, 图片生成/图生图/基础image_edit_2511图像编辑_2030636158866165761.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_229

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/产品生成海报溶图_2039993998181404673.json、图片生成/图生图/基础image_edit_2511图像编辑_2030636158866165761.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `FastCanvas` —— 1/2 个有
- `FastCanvasTool` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RH_Translator` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | - | 2 | 33% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
