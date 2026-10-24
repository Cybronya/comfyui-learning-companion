---
name: image_to_image_lora_sampler_clip_24
type: Image To Image
frequency: 9
level: weak
coverage: 0.900222
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AniWan2.1  图像修复｜图生图_1947638302482563073.json, 图片生成/图生图/AniWan图生图，修复能力很赞_1945023509128208385.json, 图片生成/图生图/QWEN图生图（4步）极速_2005597184802385922.json, 图片生成/图生图/QWEN图生图（4步）极速_2011037300788039682.json, 图片生成/图生图/Qwen千问图生图_2008423038303342594.json, 图片生成/图生图/Qwen千问图生图【加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_1985616964892733442.json, 图片生成/图生图/Qwen千问图生图【加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_2006636682057097218.json, 图片生成/图生图/WAN2.2_14B超级洗图！_1949865663331483650.json, 图片生成/图生图/万相图生图，修复能力很赞_1945006386529095682.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/AniWan2.1  图像修复｜图生图_1947638302482563073.json、图片生成/图生图/AniWan图生图，修复能力很赞_1945023509128208385.json、图片生成/图生图/QWEN图生图（4步）极速_2005597184802385922.json、图片生成/图生图/QWEN图生图（4步）极速_2011037300788039682.json、图片生成/图生图/Qwen千问图生图_2008423038303342594.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/9 个有
- `JWImageResizeByLongerSide` —— 5/9 个有
- `PreviewImage` —— 5/9 个有
- `BetterFilmGrain` —— 4/9 个有
- `EsesImageEffectBloom` —— 4/9 个有
- `ImageSharpen` —— 4/9 个有
- `ModelSamplingSD3` —— 4/9 个有
- `ImageConcanate` —— 3/9 个有
- `UnetLoaderGGUF` —— 3/9 个有
- `CR Text` —— 1/9 个有
- `EmptyHunyuanLatentVideo` —— 1/9 个有
- `RH_Captioner` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 10 | 9 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 9 | 39% |
| 采样算法 | uni_pc | - | 9 | 33% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 0.75 | 0.1 - 0.75 | 9 | 47% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 10，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，9 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 uni_pc，9 个样本，一致性 33%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 0.75，观测区间 0.1 - 0.75，9 个样本，取值分散，一致性仅 47%
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足
