---
name: text_to_image_sampler_clip_unet_98
type: Text To Image
frequency: 7
level: moderate
coverage: 0.921286
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/QWEN2512_T2I_油光_2042047802875846657.json, 图片生成/文生图/QWEN2512加速文生图_2045334643985096706.json, 图片生成/文生图/Qwen Image 2512 文生图_2011450632992989185.json, 图片生成/文生图/Z-image文生图V2（Lora）_2026213692454477825.json, 图片生成/文生图/Z-image美女IP角色工作流（单图训练的lora）_2008089851932975106.json, 图片生成/文生图/【极速版】Krea2 Trubo 美商极高文生图 V2_2098689048914259969.json, 图片生成/文生图/文生图ZImage_2064901103308861442.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_98

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/QWEN2512_T2I_油光_2042047802875846657.json、图片生成/文生图/QWEN2512加速文生图_2045334643985096706.json、图片生成/文生图/Qwen Image 2512 文生图_2011450632992989185.json、图片生成/文生图/Z-image文生图V2（Lora）_2026213692454477825.json、图片生成/文生图/Z-image美女IP角色工作流（单图训练的lora）_2008089851932975106.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `CR Text` —— 4/7 个有
- `MultipleLoraLoader5|cgem156` —— 2/7 个有
- `PromptBatchQueue` —— 2/7 个有
- `Seed Generator` —— 2/7 个有
- `JjkText` —— 1/7 个有
- `LatentRotate` —— 1/7 个有
- `SaveLatent` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 6 - 30 | 7 | 36% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 7 | 0% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 928 | 720 - 1152 | 7 | 83% |
| 高度 | 1280 | 1024 - 1920 | 7 | 81% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | meinv26_5.safetensors | - | 2 | 50% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 6 - 30，7 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，7 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 928，观测区间 720 - 1152，7 个样本，取值集中（一致性 83%）
- 高度 中位数 1280，观测区间 1024 - 1920，7 个样本，取值集中（一致性 81%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 最常用 meinv26_5.safetensors，2 个样本，一致性 50%
