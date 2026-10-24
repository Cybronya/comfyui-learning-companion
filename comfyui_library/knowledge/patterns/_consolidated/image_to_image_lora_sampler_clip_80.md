---
name: image_to_image_lora_sampler_clip_80
type: Image To Image
frequency: 4
level: moderate
coverage: 0.6555
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, Image Comparer (rgthree), Int, KSampler, KuwaharaBlur, LayerColor: Color of Shadow & Highlight, LayerColor: RGB, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, RHHiddenNodes, SaveImage, VAEDecode, VAEEncode, VAELoader, easy boolean, easy cleanGpuUsed, easy ifElse, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/去AI感，真实感放大_Krea重塑自然美学_2.0_2096400513066688514.json, 图片生成/图生图/去AI感，真实感放大_Krea重塑自然美学_2.0_2096412691257716738.json, 图片生成/图生图/去AI感，真实感放大：Krea重塑自然美学 2.0_2074779436825796609.json, 图片生成/图生图/商业级真实感放大最终章（快捷版本）_2075146234960113665.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_80

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/去AI感，真实感放大_Krea重塑自然美学_2.0_2096400513066688514.json、图片生成/图生图/去AI感，真实感放大_Krea重塑自然美学_2.0_2096412691257716738.json、图片生成/图生图/去AI感，真实感放大：Krea重塑自然美学 2.0_2074779436825796609.json、图片生成/图生图/商业级真实感放大最终章（快捷版本）_2075146234960113665.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `Image Comparer (rgthree)`
- `Int`
- `KSampler`
- `KuwaharaBlur`
- `LayerColor: Color of Shadow & Highlight`
- `LayerColor: RGB`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `GroupExecutor` —— 3/4 个有
- `ImageResize+` —— 3/4 个有
- `KSamplerAdvanced` —— 3/4 个有
- `UNETLoader_Any` —— 3/4 个有
- `AILab_QwenVL` —— 2/4 个有
- `DisTorchPurgeVRAMV2` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `llama_cpp_instruct_adv` —— 2/4 个有
- `llama_cpp_model_loader` —— 2/4 个有
- `Latent Noise Injection` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `UNETLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 4 | 52% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 4 | 50% |
| 重绘幅度 | sgm_uniform | - | 4 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 50%
- 重绘幅度 最常用 sgm_uniform，4 个样本，一致性 75%
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
