---
name: text_to_image_lora_sampler_clip_146
type: Text To Image
frequency: 11
level: strong
coverage: 0.823273
common_nodes: [Anything Everywhere, CLIPLoader, CLIPTextEncode, CR Text Concatenate, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, ImageScaleToTotalPixels, ImageSharpen, KSampler, LoadImage, LoraLoaderModelOnly, MuyeTextEditOutput, ReferenceLatent, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, workflow>Qwen3.5反推, workflow>Qwen3.5自动提示词, workflow>自定义采样器]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ERNIE+ZIT+Klein三采样自动提示词_2056199922793369602.json, 图片生成/文生图/Boogu+Klein放大_生图_洗图_反推提示词_2070367779223592961.json, 图片生成/文生图/Boogu+Klein放大_生图_洗图_自动提示词_2067885710153175041.json, 图片生成/文生图/ERNIE+ZIT+Klein+三采样_文生图_图生图_反推提示词_2070373915993657345.json, 图片生成/文生图/ERNIE+ZIT+Klein三采样_文生图_图生图_自动提示词_2053295521384681473.json, 图片生成/文生图/ERNIE+ZIT+Klein三采样_文生图_图生图_自动提示词_2059435133127712769.json, 图片生成/文生图/ERNIE+ZIT+Klein三采样_文生图_图生图_自动提示词_2063913882598592514.json, 图片生成/文生图/Krea2+Klein放大_生图_洗图_2070354064461881345.json, 图片生成/文生图/Krea2+Klein放大_生图_洗图_自动提示词_2069596012766916609.json, 图片生成/文生图/Krea2风格参考_迁移_文生图&图生图_2074844990458646529.json, 图片生成/文生图/超好用🔥三采样-文生图-图生图-自动提示词-反推提示词_2056296757281251329.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_146

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/ERNIE+ZIT+Klein三采样自动提示词_2056199922793369602.json、图片生成/文生图/Boogu+Klein放大_生图_洗图_反推提示词_2070367779223592961.json、图片生成/文生图/Boogu+Klein放大_生图_洗图_自动提示词_2067885710153175041.json、图片生成/文生图/ERNIE+ZIT+Klein+三采样_文生图_图生图_反推提示词_2070373915993657345.json、图片生成/文生图/ERNIE+ZIT+Klein三采样_文生图_图生图_自动提示词_2053295521384681473.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 11 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MuyeTextEditOutput`
- `ReferenceLatent`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `workflow>Qwen3.5反推`
- `workflow>Qwen3.5自动提示词`
- `workflow>自定义采样器`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 6/11 个有
- `Krea2StyleReference` —— 1/11 个有
- `Krea2StyleTransfer` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 11 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 55% |
| 调度器 | simple | - | 11 | 82% |
| 重绘幅度 | 1 | 0.15 - 1 | 11 | 61% |
| 宽度 | 1080 | 1024 - 1080 | 11 | 98% |
| 高度 | 1624 | 1600 - 1960 | 11 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 55%
- 调度器 最常用 simple，11 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，11 个样本
- 宽度 中位数 1080，观测区间 1024 - 1080，11 个样本，取值集中（一致性 98%）
- 高度 中位数 1624，观测区间 1600 - 1960，11 个样本，取值集中（一致性 92%）
- 高发问题（17/11 个样本）：Steps较低可能导致细节不足
