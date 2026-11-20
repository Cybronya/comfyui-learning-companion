---
name: image_to_image_sampler_clip_vae_36
type: Image To Image
frequency: 6
level: strong
coverage: 0.849333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, NunchakuFluxDiTLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux Kontext-真人转动漫 Nunchaku加速版_1964121930297167874.json, 图片生成/图生图/Flux-kontext+LLM提示词优化+nunchaku加速_1947162963498807297.json, 图片生成/图生图/Flux1-Kontext图像外扩加速-Nunchaku_1950438024939266049.json, 图片生成/图生图/kontext 动漫转真人（双截棍）_1975110263445827585.json, 图片生成/图生图/kontext+LLM提示词优化+nunchaku加速工作流_1939506026280566785.json, 平台全量/Kontext动漫角色人物三视图快速生成器_1939524868318871554.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_36

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux Kontext-真人转动漫 Nunchaku加速版_1964121930297167874.json、图片生成/图生图/Flux-kontext+LLM提示词优化+nunchaku加速_1947162963498807297.json、图片生成/图生图/Flux1-Kontext图像外扩加速-Nunchaku_1950438024939266049.json、图片生成/图生图/kontext 动漫转真人（双截棍）_1975110263445827585.json、图片生成/图生图/kontext+LLM提示词优化+nunchaku加速工作流_1939506026280566785.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 5/6 个有
- `DualCLIPLoader` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `NunchakuFluxLoraLoader` —— 3/6 个有
- `RH_LLMAPI_NODE` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `LayerUtility: PurgeVRAM` —— 2/6 个有
- `NunchakuTextEncoderLoaderV2` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `LayerUtility: ExtendCanvas` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `Text Multiline` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 6 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
