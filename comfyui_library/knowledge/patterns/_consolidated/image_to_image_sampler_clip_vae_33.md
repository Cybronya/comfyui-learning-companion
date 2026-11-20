---
name: image_to_image_sampler_clip_vae_33
type: Image To Image
frequency: 5
level: strong
coverage: 0.8508
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, NunchakuFluxDiTLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux Kontext-真人转动漫 Nunchaku加速版_1964121930297167874.json, 图片生成/图生图/Flux-kontext+LLM提示词优化+nunchaku加速_1947162963498807297.json, 图片生成/图生图/Flux1-Kontext图像外扩加速-Nunchaku_1950438024939266049.json, 图片生成/图生图/kontext 动漫转真人（双截棍）_1975110263445827585.json, 图片生成/图生图/kontext+LLM提示词优化+nunchaku加速工作流_1939506026280566785.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_33

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux Kontext-真人转动漫 Nunchaku加速版_1964121930297167874.json、图片生成/图生图/Flux-kontext+LLM提示词优化+nunchaku加速_1947162963498807297.json、图片生成/图生图/Flux1-Kontext图像外扩加速-Nunchaku_1950438024939266049.json、图片生成/图生图/kontext 动漫转真人（双截棍）_1975110263445827585.json、图片生成/图生图/kontext+LLM提示词优化+nunchaku加速工作流_1939506026280566785.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `DualCLIPLoader` —— 3/5 个有
- `NunchakuFluxLoraLoader` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `NunchakuTextEncoderLoaderV2` —— 2/5 个有
- `RH_LLMAPI_NODE` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `LayerUtility: ExtendCanvas` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 5 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
