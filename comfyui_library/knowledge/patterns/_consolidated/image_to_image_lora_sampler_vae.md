---
name: image_to_image_lora_sampler_vae
type: Image To Image
frequency: 2
level: weak
coverage: 0.836
common_nodes: [CFGNorm, CLIPLoader, EmptySD3LatentImage, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveStringMultiline, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy imageRemBg]
members: [图片生成/文生图/1983740366849548289.json, 图片生成/文生图/三图参考生成组合_1993498915181969409.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1983740366849548289.json、图片生成/文生图/三图参考生成组合_1993498915181969409.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `DiffusionModelLoaderKJ` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `StringListToString` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.25 | - | 1 | 100% |
| LoRA 文本强度 | 0.25 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy imageRemBg
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
