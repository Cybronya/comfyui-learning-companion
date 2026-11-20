---
name: text_to_image_sampler_clip_unet_125
type: Text To Image
frequency: 6
level: moderate
coverage: 0.9345
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/QWEN2512_T2I_油光_2042047802875846657.json, 图片生成/文生图/QWEN2512加速文生图_2045334643985096706.json, 图片生成/文生图/Qwen Image 2512 文生图_2011450632992989185.json, 图片生成/文生图/krea2+Lora文生图_2082750366432718849.json, 图片生成/文生图/krea2文生图+官方LORA_2069978232052600834.json, 图片生成/文生图/【极速版】Krea2 Trubo 美商极高文生图 V2_2098689048914259969.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_125

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/QWEN2512_T2I_油光_2042047802875846657.json、图片生成/文生图/QWEN2512加速文生图_2045334643985096706.json、图片生成/文生图/Qwen Image 2512 文生图_2011450632992989185.json、图片生成/文生图/krea2+Lora文生图_2082750366432718849.json、图片生成/文生图/krea2文生图+官方LORA_2069978232052600834.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `CR Text` —— 4/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `MultipleLoraLoader5|cgem156` —— 2/6 个有
- `Seed Generator` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `JoinStringMulti` —— 1/6 个有
- `LatentRotate` —— 1/6 个有
- `SaveLatent` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 6 - 30 | 6 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 6 | 2% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 976 | 720 - 1536 | 6 | 73% |
| 高度 | 1600 | 1024 - 2048 | 6 | 78% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | meinv26_5.safetensors | - | 2 | 50% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 6 - 30，6 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，6 个样本，取值分散，一致性仅 2%
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 976，观测区间 720 - 1536，6 个样本
- 高度 中位数 1600，观测区间 1024 - 2048，6 个样本
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 最常用 meinv26_5.safetensors，2 个样本，一致性 50%
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
