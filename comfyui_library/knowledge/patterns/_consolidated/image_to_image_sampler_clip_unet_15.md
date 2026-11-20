---
name: image_to_image_sampler_clip_unet_15
type: Image To Image
frequency: 13
level: strong
coverage: 0.822538
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX Kontext dev 图生图工作流_1946449845256089601.json, 图片生成/图生图/FLUX krea 人像洗图真实感_1951921534116024322.json, 图片生成/图生图/FLUX.1 Kontext [dev] 基础工作流_1938329277471330305.json, 图片生成/图生图/Flux Kontext本地部署_1939329294118338561.json, 图片生成/图生图/Flux+Kontext老照片修复_1949376700114731009.json, 图片生成/图生图/Kontext 十大优质lora模型使用_1941855678447382529.json, 图片生成/图生图/Kontext+lora角度编辑器_1942022786829467649.json, 图片生成/图生图/Kontext三视图（三张大图呈现）_1953727580824326145.json, 图片生成/图生图/Kontext优化精准移除物体_1945338596477870082.json, 图片生成/图生图/kontext-dev创程式填充_1942603916720672769.json, 图片生成/图生图/kontext-dev填_1942841076824608770.json, 图片生成/图生图/kontext-dev红框标记新玩法_1942839973647159298.json, 图片生成/图生图/kontext-dev超越PS创程式填充_1942838696930381825.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_15

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/FLUX Kontext dev 图生图工作流_1946449845256089601.json、图片生成/图生图/FLUX krea 人像洗图真实感_1951921534116024322.json、图片生成/图生图/FLUX.1 Kontext [dev] 基础工作流_1938329277471330305.json、图片生成/图生图/Flux Kontext本地部署_1939329294118338561.json、图片生成/图生图/Flux+Kontext老照片修复_1949376700114731009.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 12/13 个有
- `PreviewImage` —— 12/13 个有
- `ReferenceLatent` —— 12/13 个有
- `LoraLoaderModelOnly` —— 9/13 个有
- `CR Text` —— 8/13 个有
- `DeepTranslatorTextNode` —— 7/13 个有
- `ShowText|pysssss` —— 6/13 个有
- `CR Latent Batch Size` —— 5/13 个有
- `FastCanvas` —— 5/13 个有
- `Image Comparer (rgthree)` —— 5/13 个有
- `LayerMask: MaskPreview` —— 5/13 个有
- `RH_LLMAPI_NODE` —— 5/13 个有
- `SetNode` —— 5/13 个有
- `ImageStitch` —— 3/13 个有
- `easy cleanGpuUsed` —— 2/13 个有
- `CR Prompt List` —— 1/13 个有
- `ImageScale` —— 1/13 个有
- `PrimitiveStringMultiline` —— 1/13 个有
- `easy promptConcat` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 30 | 13 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 92% |
| 重绘幅度 | 1 | 0.8 - 1 | 13 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 30，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，13 个样本，取值集中（一致性 95%）
