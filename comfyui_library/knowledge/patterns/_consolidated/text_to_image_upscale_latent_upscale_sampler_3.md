---
name: text_to_image_upscale_latent_upscale_sampler_3
type: Text To Image
frequency: 2
level: weak
coverage: 0.686
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, LatentUpscaleBy, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 文生图双采样4K版_2092280334065946625.json, 图片生成/文生图/krea2 文生图 工作流+全节点注释_2077385249922834434.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_sampler_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Krea2 文生图双采样4K版_2092280334065946625.json、图片生成/文生图/krea2 文生图 工作流+全节点注释_2077385249922834434.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LatentUpscaleBy`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningKrea2Rebalance` —— 1/2 个有
- `Float` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1472 | - | 2 | 87% |
| 高度 | 1232 | - | 2 | 75% |
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 0.8 | - | 2 | 75% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1472，样本不足，未给区间，2 个样本，取值集中（一致性 87%）
- 高度 中位数 1232，样本不足，未给区间，2 个样本
- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 0.8，样本不足，未给区间，2 个样本
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
