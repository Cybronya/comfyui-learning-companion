---
name: text_to_image_sampler_clip_unet_23
type: Text To Image
frequency: 13
level: weak
coverage: 0.895385
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image超极速文生图（魔君降临--拳打nunchaku，脚踢Flux2）_1994262703730524162.json, 图片生成/文生图/Z-image轻量级 AI 图像生成_1994293019830665217.json, 图片生成/文生图/Z-image造像-文生图（最强写实人像）_1994314682653671425.json, 图片生成/文生图/Z-image，出图 效果炸裂，效果超越Flux2_1993931824883843074.json, 图片生成/文生图/Z-image，最强文生图_1994408486224207874.json, 图片生成/文生图/Zimage文生图-基础_2003639567171395585.json, 图片生成/文生图/Zimage文生图_1993848041241329666.json, 图片生成/文生图/Zimage超越Flux2的国产图像模型（支持真人的国产加速模型）_1993888771909369858.json, 图片生成/文生图/Zimage超越Flux2的国产图像模型（支持真人的国产加速模型）_1995004425267818497.json, 图片生成/文生图/Zimage（支持真人的国产加速模型）_2027694676630835201.json, 图片生成/文生图/Zimage（支持真人的国产加速模型）_2027695408717238273.json, 图片生成/文生图/z-image文生图 基础版 lora模型加载_2001116171342577665.json, 图片生成/文生图/【GUGU】CG唯美画风LORA工作流_2001845384953643010.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_23

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Z-image超极速文生图（魔君降临--拳打nunchaku，脚踢Flux2）_1994262703730524162.json、图片生成/文生图/Z-image轻量级 AI 图像生成_1994293019830665217.json、图片生成/文生图/Z-image造像-文生图（最强写实人像）_1994314682653671425.json、图片生成/文生图/Z-image，出图 效果炸裂，效果超越Flux2_1993931824883843074.json、图片生成/文生图/Z-image，最强文生图_1994408486224207874.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 5/13 个有
- `PrimitiveStringMultiline` —— 4/13 个有
- `ImageUpscaleWithModel` —— 2/13 个有
- `LoraLoaderModelOnly` —— 2/13 个有
- `ModelSamplingAuraFlow` —— 2/13 个有
- `Upscale Model Loader` —— 2/13 个有
- `EmptySD3LatentImage` —— 1/13 个有
- `PathchSageAttentionKJ` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 50 | 13 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 5.5 | 13 | 24% |
| 采样算法 | euler | - | 13 | 92% |
| 调度器 | simple | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 1080 | 512 - 1920 | 13 | 64% |
| 高度 | 1280 | 512 - 1920 | 13 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 50，13 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5.5，13 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，13 个样本，一致性 92%
- 调度器 最常用 simple，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 512 - 1920，13 个样本
- 高度 中位数 1280，观测区间 512 - 1920，13 个样本
