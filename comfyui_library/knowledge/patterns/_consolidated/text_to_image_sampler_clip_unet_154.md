---
name: text_to_image_sampler_clip_unet_154
type: Text To Image
frequency: 2
level: weak
coverage: 0.768
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, ModelSamplingAuraFlow, PrimitiveFloat, PrimitiveInt, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima _ Z-anime _ Wai-Illustrious三模型文生图工作流_2051672724375908354.json, 图片生成/文生图/Anima-turbo加速工作流_2061092508771381250.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_154

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Anima _ Z-anime _ Wai-Illustrious三模型文生图工作流_2051672724375908354.json、图片生成/文生图/Anima-turbo加速工作流_2061092508771381250.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `ModelSamplingAuraFlow`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `ComfyMathExpression` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有
- `VRAM_Debug` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5.5 | - | 2 | 73% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 896 | - | 2 | 100% |
| 高度 | 1152 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5.5，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1152，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
