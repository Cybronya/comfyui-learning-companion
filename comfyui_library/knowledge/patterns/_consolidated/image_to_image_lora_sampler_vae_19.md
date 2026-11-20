---
name: image_to_image_lora_sampler_vae_19
type: Image To Image
frequency: 6
level: moderate
coverage: 0.8385
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物多角度一键生成《Next Scene》_1984265817120522242.json, 图片生成/图生图/图像编辑 _ Qwen-Edit_2511_1948316912116740098.json, 图片生成/图生图/多景镜头人物一致性-Qwen-Edit-2511_2012351159188594690.json, 图片生成/文生图/Qwen-Image-Edit-2511图片人物+场景+打光+全节点注释_2055894861483651073.json, 图片生成/文生图/一键多角度+全节点注释_2056923210242936834.json, 平台全量/人物多角度一键生成《Next Scene》_1997516718685753346.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_19

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/人物多角度一键生成《Next Scene》_1984265817120522242.json、图片生成/图生图/图像编辑 _ Qwen-Edit_2511_1948316912116740098.json、图片生成/图生图/多景镜头人物一致性-Qwen-Edit-2511_2012351159188594690.json、图片生成/文生图/Qwen-Image-Edit-2511图片人物+场景+打光+全节点注释_2055894861483651073.json、图片生成/文生图/一键多角度+全节点注释_2056923210242936834.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 5/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `UNETLoader` —— 4/6 个有
- `easy promptLine` —— 4/6 个有
- `RHHiddenNodes` —— 3/6 个有
- `ConstrainImage|pysssss` —— 2/6 个有
- `GetImageSizeAndCount` —— 2/6 个有
- `Int` —— 2/6 个有
- `ReferenceLatent` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `DyPE_FLUX` —— 1/6 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `JjkText` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 20 | 6 | 29% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 20，6 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
