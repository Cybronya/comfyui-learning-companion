---
name: image_to_image_sampler_clip_vae_21
type: Image To Image
frequency: 9
level: strong
coverage: 0.744111
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadAndResizeImage, LoadImage, Primitive integer [Crystools], RH_Translator, ReferenceLatent, SaveImage, TextInput_, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontext-dev_主体参考图换背景_1939260618115358721.json, 图片生成/图生图/Kontext-dev_主体参考图换背景_1945291192747872258.json, 图片生成/图生图/Kontext-换背景-参考图模式_1972867383658483714.json, 图片生成/图生图/Kontext-换背景-参考图模式_2013804200555192322.json, 图片生成/图生图/Kontext-换背景-参考图模式_2029090600431128578.json, 图片生成/图生图/kontext 融合lora_1946477483225178114.json, 图片生成/图生图/kontext-人物一致性-多角度可选_1977891156187119618.json, 图片生成/图生图/kontext本地版-溶图-打光-自动版_1938785222286565378.json, 图片生成/图生图/台灯融合_1943145462301933569.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_21

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Kontext-dev_主体参考图换背景_1939260618115358721.json、图片生成/图生图/Kontext-dev_主体参考图换背景_1945291192747872258.json、图片生成/图生图/Kontext-换背景-参考图模式_1972867383658483714.json、图片生成/图生图/Kontext-换背景-参考图模式_2013804200555192322.json、图片生成/图生图/Kontext-换背景-参考图模式_2029090600431128578.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 9 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `TTP_text_mix` —— 8/9 个有
- `UNETLoader` —— 8/9 个有
- `ImpactSwitch` —— 7/9 个有
- `RH_Captioner` —— 7/9 个有
- `ShowText|pysssss` —— 7/9 个有
- `LoraLoader` —— 6/9 个有
- `CR Text Concatenate` —— 5/9 个有
- `ImagePadForOutpaint` —— 5/9 个有
- `easy imageConcat` —— 5/9 个有
- `RepeatLatentBatch` —— 4/9 个有
- `ImageConcanate` —— 3/9 个有
- `ColorMatch` —— 2/9 个有
- `Int` —— 2/9 个有
- `NunchakuFluxDiTLoader` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `FastCanvas` —— 1/9 个有
- `FastCanvasTool` —— 1/9 个有
- `NunchakuFluxLoraLoader` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `UltimateSDUpscaleNoUpscale` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 9 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
