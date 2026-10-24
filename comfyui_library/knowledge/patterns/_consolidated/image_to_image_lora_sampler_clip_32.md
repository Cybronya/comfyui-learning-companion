---
name: image_to_image_lora_sampler_clip_32
type: Image To Image
frequency: 8
level: strong
coverage: 0.904
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux-Kontext文生图_局部重绘_2039270148548333570.json, 图片生成/图生图/flux_1_kontext+flux lora工作流_1944430917349986305.json, 图片生成/图生图/flux_1_kontext_生成封面图_1940659961330561026.json, 图片生成/图生图/kontext 超完美转手办卡通人物一致性高_1944805495855304705.json, 图片生成/图生图/kontext（开源版）实现重打光效果，不改变人物动作场景_1938433384328921090.json, 图片生成/图生图/▶Kontext扩图流_1956304739745103874.json, 图片生成/图生图/人像精修_2076044034824564738.json, 图片生成/图生图/人像精修工作流_2048591215414747137.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/flux-Kontext文生图_局部重绘_2039270148548333570.json、图片生成/图生图/flux_1_kontext+flux lora工作流_1944430917349986305.json、图片生成/图生图/flux_1_kontext_生成封面图_1940659961330561026.json、图片生成/图生图/kontext 超完美转手办卡通人物一致性高_1944805495855304705.json、图片生成/图生图/kontext（开源版）实现重打光效果，不改变人物动作场景_1938433384328921090.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `Image Comparer (rgthree)` —— 4/8 个有
- `ImageResize+` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `PathchSageAttentionKJ` —— 3/8 个有
- `StringConcatenate` —— 3/8 个有
- `StringConstantMultiline` —— 3/8 个有
- `EmptySD3LatentImage` —— 2/8 个有
- `RH_Translator` —— 2/8 个有
- `RepeatLatentBatch` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `ImagePadForOutpaint` —— 1/8 个有
- `Kontext Inpainting Conditioning` —— 1/8 个有
- `RMBG` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 25 | 8 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 25，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
