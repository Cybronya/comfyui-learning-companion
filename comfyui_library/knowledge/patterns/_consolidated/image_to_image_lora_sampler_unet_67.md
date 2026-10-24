---
name: image_to_image_lora_sampler_unet_67
type: Image To Image
frequency: 9
level: weak
coverage: 0.770222
common_nodes: [CFGNorm, CLIPLoader, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/Qwen Image Edit 2511 3张参考图生图_2078472969151668226.json, 图片生成/图生图/Qwen edit 2511单图多角度 短剧 动漫 专用_2041503056172425217.json, 图片生成/图生图/Qwen edit 2511单图多角度_2010230488669102081.json, 图片生成/图生图/Qwen-Camera_2068695632642142209.json, 图片生成/图生图/Qwen-Edit-2511 场景多角度工作流_2091522931443716097.json, 图片生成/图生图/firered-image-edit-1.1官方发布版_2030518527010021378.json, 图片生成/图生图/image_firered_image_edit1_图生图_2032289203324723201.json, 图片生成/图生图/一键生成多角度（八角度）+全节点注释_2053298166606376961.json, 图片生成/图生图/人像换发工作流_8hair_2085998735972192257.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_67

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen Image Edit 2511 3张参考图生图_2078472969151668226.json、图片生成/图生图/Qwen edit 2511单图多角度 短剧 动漫 专用_2041503056172425217.json、图片生成/图生图/Qwen edit 2511单图多角度_2010230488669102081.json、图片生成/图生图/Qwen-Camera_2068695632642142209.json、图片生成/图生图/Qwen-Edit-2511 场景多角度工作流_2091522931443716097.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 8/9 个有
- `ComfySwitchNode` —— 5/9 个有
- `FluxKontextMultiReferenceLatentMethod` —— 5/9 个有
- `PrimitiveBoolean` —— 5/9 个有
- `PrimitiveFloat` —— 5/9 个有
- `PrimitiveInt` —— 5/9 个有
- `PreviewAny` —— 4/9 个有
- `QwenMultiangleCameraNode` —— 3/9 个有
- `ReferenceLatent` —— 2/9 个有
- `CR Prompt List` —— 1/9 个有
- `CustomCombo` —— 1/9 个有
- `ImageBatch` —— 1/9 个有
- `JsonExtractString` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `StringConcatenate` —— 1/9 个有
- `Text Multiline` —— 1/9 个有
- `VAEDecodeTiled` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 4 - 40 | 9 | 27% |
| Prompt 约束强度(CFG) | 3 | 1 - 4 | 9 | 47% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/9 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 40，观测区间 4 - 40，9 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4，9 个样本，取值分散，一致性仅 47%
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
