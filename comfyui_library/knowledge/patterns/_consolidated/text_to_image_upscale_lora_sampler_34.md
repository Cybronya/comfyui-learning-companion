---
name: text_to_image_upscale_lora_sampler_34
type: Text To Image
frequency: 7
level: moderate
coverage: 0.944714
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageColorMatch+, ImageScaleToTotalPixels, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 双图编辑 - 更好的角色一致性_2075436000674934786.json, 图片生成/图生图/Krea2 双图编辑 高度角色一致性_2076174644968775682.json, 图片生成/图生图/Krea2 图像编辑（保持人物一致性）_2079504244268425218.json, 图片生成/图生图/Krea2 图像编辑（保持人物一致性）_2079745338142973953.json, 图片生成/图生图/boogu+KREA2二次元转真人，真实感洗图-B站AIGC大赏_2075155455009189889.json, 图片生成/图生图/重磅!krea2真双图编辑模型!-超强一致性首发-AIGC大赏_2075769378708221953.json, 图片生成/图生图/重磅!krea2真编辑模型!-超强一致性首发-AIGC大赏_2075767249423650818.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_34

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Krea2 双图编辑 - 更好的角色一致性_2075436000674934786.json、图片生成/图生图/Krea2 双图编辑 高度角色一致性_2076174644968775682.json、图片生成/图生图/Krea2 图像编辑（保持人物一致性）_2079504244268425218.json、图片生成/图生图/Krea2 图像编辑（保持人物一致性）_2079745338142973953.json、图片生成/图生图/boogu+KREA2二次元转真人，真实感洗图-B站AIGC大赏_2075155455009189889.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageColorMatch+`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 6/7 个有
- `Int` —— 6/7 个有
- `Krea2EditGroundedEncode` —— 6/7 个有
- `Krea2EditModelPatch` —— 6/7 个有
- `ImageConcatMulti` —— 4/7 个有
- `PrimitiveStringMultiline` —— 3/7 个有
- `BasicScheduler` —— 1/7 个有
- `ColorCorrect` —— 1/7 个有
- `CompressImages` —— 1/7 个有
- `JoinStrings` —— 1/7 个有
- `SamplerCustom` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `Text` —— 1/7 个有
- `TextEncodeBooguEdit` —— 1/7 个有
- `llama_cpp_instruct_adv` —— 1/7 个有
- `llama_cpp_model_loader` —— 1/7 个有
- `llama_cpp_parameters` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 7 - 8 | 7 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | sgm_uniform | - | 7 | 86% |
| 重绘幅度 | 1 | 0.2 - 1 | 7 | 68% |
| 宽度 | 1024 | 512 - 1024 | 7 | 81% |
| 高度 | 1536 | 512 - 1536 | 7 | 74% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 7 - 8，7 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 sgm_uniform，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，7 个样本
- 宽度 中位数 1024，观测区间 512 - 1024，7 个样本，取值集中（一致性 81%）
- 高度 中位数 1536，观测区间 512 - 1536，7 个样本
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
