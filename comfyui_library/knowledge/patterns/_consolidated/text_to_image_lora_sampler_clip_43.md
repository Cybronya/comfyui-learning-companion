---
name: text_to_image_lora_sampler_clip_43
type: Text To Image
frequency: 18
level: strong
coverage: 0.902056
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 i2i图生图洗图工作流｜人像写真写实风格_2089723666648100865.json, 图片生成/图生图/Krea2图生图洗图工作流｜人像写真写实精修处理_2096305555949309954.json, 图片生成/图生图/Krea2多图参考融合 视觉设计时尚摄影图生图工具_2114064749150433282.json, 图片生成/图生图/Krea2自用图生图低幅度重绘｜图生图制作_2090406596852674562.json, 图片生成/图生图/i2i图生图洗图工作流｜krea2人像写真写实图片编辑_2088215973361967105.json, 图片生成/图生图/krea2 i2i一键洗图 图生图加洗图工作流_2105441879230869506.json, 图片生成/图生图/krea2 i2i一键洗图工作流｜图生图快速洗图去AI感提质_2106227080387190786.json, 图片生成/图生图/krea2 i2i图生图洗图｜图片重绘风格优化工作流_2089418222180331521.json, 图片生成/图生图/krea2加i2i洗图组合｜Image重生成加重处理双保险_2101551863228362754.json, 图片生成/图生图/krea2多图参考多图融合｜视觉设计时尚摄影人像写真_2114078512557674497.json, 图片生成/图生图/krea2洗图方案，Image Generation加Processing i2i图生图_2110542715338448898.json, 图片生成/图生图/krea2洗图方案，Image_Generation加Processing_i2i图生图_2110886706835705857.json, 图片生成/图生图/krea2洗图方案，Image_Generation加Processing_i2i图生图_2114264503419490305.json, 图片生成/图生图/krea2洗图方案，Image_Generation加i2i图生图_2111601032122945537.json, 图片生成/图生图/一键洗图重绘｜krea2 i2i写实图生图工作流_2091214487880818690.json, 图片生成/图生图/写真人像救星｜krea2 i2i图生图洗图二合一_2096542081866100737.json, 图片生成/图生图/洗图Image Generation加Image Processing krea2加i2i 图生图方_2109400629008490498.json, 图片生成/图生图/洗图Image Generation加Image Processing krea2加i2i 图生图方_2109797199356981249.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_43

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/Krea2 i2i图生图洗图工作流｜人像写真写实风格_2089723666648100865.json、图片生成/图生图/Krea2图生图洗图工作流｜人像写真写实精修处理_2096305555949309954.json、图片生成/图生图/Krea2多图参考融合 视觉设计时尚摄影图生图工具_2114064749150433282.json、图片生成/图生图/Krea2自用图生图低幅度重绘｜图生图制作_2090406596852674562.json、图片生成/图生图/i2i图生图洗图工作流｜krea2人像写真写实图片编辑_2088215973361967105.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `VAEEncode` —— 16/18 个有
- `孤海注释` —— 16/18 个有
- `AILab_QwenVL` —— 15/18 个有
- `ImageResizeKJv2` —— 15/18 个有
- `PrimitiveInt` —— 15/18 个有
- `EmptyImage` —— 3/18 个有
- `PreviewImage` —— 3/18 个有
- `ComfyUI-Krea2T-Enhancer` —— 2/18 个有
- `ConditioningConcat` —— 2/18 个有
- `ConditioningKrea2Rebalance` —— 2/18 个有
- `Krea2EncodeRebalance` —— 2/18 个有
- `PrimitiveStringMultiline` —— 2/18 个有
- `ResolutionSelector` —— 2/18 个有
- `Seed (rgthree)` —— 2/18 个有
- `ImageScaleToTotalPixels` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（28/18 个样本）：Steps较低可能导致细节不足
