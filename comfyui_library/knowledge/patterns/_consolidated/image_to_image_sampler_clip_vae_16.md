---
name: image_to_image_sampler_clip_vae_16
type: Image To Image
frequency: 16
level: strong
coverage: 0.754875
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadAndResizeImage, LoadImage, Primitive integer [Crystools], RH_Translator, ReferenceLatent, SaveImage, TextInput_, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontext-dev_主体参考图换背景_1939260618115358721.json, 图片生成/图生图/Kontext-dev_主体参考图换背景_1945291192747872258.json, 图片生成/图生图/Kontext-换背景-参考图模式_1972867383658483714.json, 图片生成/图生图/Kontext-换背景-参考图模式_2013804200555192322.json, 图片生成/图生图/Kontext-换背景-参考图模式_2029090600431128578.json, 图片生成/图生图/Kontext-换背景-参考图模式_2115285718590382081.json, 图片生成/图生图/Kontext-换背景-参考图模式_2115433574387240962.json, 图片生成/图生图/Kontext-换背景-参考图模式_2115659198884311041.json, 图片生成/图生图/kontext 融合lora_1946477483225178114.json, 图片生成/图生图/kontext-人物一致性-多角度可选_1977891156187119618.json, 图片生成/图生图/kontext-人物一致性-多角度可选_2115618995868102658.json, 图片生成/图生图/kontext本地版-溶图-打光-自动版_1938785222286565378.json, 图片生成/图生图/kontext本地版-溶图-打光-自动版_2115280118292770818.json, 图片生成/图生图/台灯融合_1943145462301933569.json, 平台全量/Kontext-换背景-参考图模式_1938797079550418946.json, 平台全量/kontext-人物一致性-多角度可选_1940235441394110466.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_16

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Kontext-dev_主体参考图换背景_1939260618115358721.json、图片生成/图生图/Kontext-dev_主体参考图换背景_1945291192747872258.json、图片生成/图生图/Kontext-换背景-参考图模式_1972867383658483714.json、图片生成/图生图/Kontext-换背景-参考图模式_2013804200555192322.json、图片生成/图生图/Kontext-换背景-参考图模式_2029090600431128578.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadAndResizeImage`
- `LoadImage`
- `Primitive integer [Crystools]`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `TextInput_`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TTP_text_mix` —— 15/16 个有
- `UNETLoader` —— 15/16 个有
- `Image Comparer (rgthree)` —— 14/16 个有
- `ImpactSwitch` —— 14/16 个有
- `LoraLoader` —— 13/16 个有
- `PreviewImage` —— 13/16 个有
- `RH_Captioner` —— 12/16 个有
- `ShowText|pysssss` —— 12/16 个有
- `CR Text Concatenate` —— 9/16 个有
- `ImagePadForOutpaint` —— 9/16 个有
- `easy imageConcat` —— 9/16 个有
- `RepeatLatentBatch` —— 7/16 个有
- `ImageConcanate` —— 6/16 个有
- `NunchakuFluxDiTLoader` —— 4/16 个有
- `ColorMatch` —— 3/16 个有
- `NunchakuFluxLoraLoader` —— 3/16 个有
- `Int` —— 2/16 个有
- `Fast Groups Bypasser (rgthree)` —— 1/16 个有
- `FastCanvas` —— 1/16 个有
- `FastCanvasTool` —— 1/16 个有
- `RHHiddenNodes` —— 1/16 个有
- `UltimateSDUpscaleNoUpscale` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 16 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 13 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，16 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
