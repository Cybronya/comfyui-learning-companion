---
name: image_to_image_lora_sampler_unet_175
type: Image To Image
frequency: 4
level: strong
coverage: 0.88675
common_nodes: [CR Text, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, ImageConcanate, ImageStitch, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, RH_LLMAPI_NODE, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit双图模式+LLM大模型提示词（效果更加精准）_1958411317197619202.json, 图片生成/图生图/Qwen-Image-Edit双图模式（效果更加精准）_2072583528436555777.json, 图片生成/图生图/Qwen-edit 明星代言｜手持产品替换_1958455891425181697.json, 平台全量/kontext双图融合（LLM自动提示词+8步加速lora）_1939591507429007361.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_175

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit双图模式+LLM大模型提示词（效果更加精准）_1958411317197619202.json、图片生成/图生图/Qwen-Image-Edit双图模式（效果更加精准）_2072583528436555777.json、图片生成/图生图/Qwen-edit 明星代言｜手持产品替换_1958455891425181697.json、平台全量/kontext双图融合（LLM自动提示词+8步加速lora）_1939591507429007361.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CR Text`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageConcanate`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/4 个有
- `CLIPLoader` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `CLIPTextEncode` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `TextEncodeQwenImageEdit` —— 2/4 个有
- `easy imageScaleDownToSize` —— 2/4 个有
- `DualCLIPLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 4 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
