---
name: unknown_workflow_controlnet_lora_sampler_6
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.756167
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptySD3LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingAuraFlow, QwenImageDiffsynthControlnet, SaveImage, Text Concatenate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image双采样洗图_自动反推提示词图生图_Union Controlnet 2.0_2041050643850334210.json, 图片生成/图生图/Z-image双采样洗图_自动反推提示词图生图_Union Controlnet 2.0_2077032005547683841.json, 图片生成/图生图/刁钻角度 摄影姿势控制 教程示例 （高手无视）_2057439380989628418.json, 图片生成/图生图/（自用）Z-image完美版自动提示词多条件Union Controlnet 2.0控制V1_2000551311915483138.json, 图片生成/文生图/刁钻角度 摄影姿势控制 教程示例_1999133193754341378.json, 图片生成/文生图/刁钻角度 摄影姿势控制 教程示例_2057355157473681409.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Z-image双采样洗图_自动反推提示词图生图_Union Controlnet 2.0_2041050643850334210.json、图片生成/图生图/Z-image双采样洗图_自动反推提示词图生图_Union Controlnet 2.0_2077032005547683841.json、图片生成/图生图/刁钻角度 摄影姿势控制 教程示例 （高手无视）_2057439380989628418.json、图片生成/图生图/（自用）Z-image完美版自动提示词多条件Union Controlnet 2.0控制V1_2000551311915483138.json、图片生成/文生图/刁钻角度 摄影姿势控制 教程示例_1999133193754341378.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 6 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `ImageScaleToMaxDimension` —— 4/6 个有
- `LayerUtility: PurgeVRAM` —— 4/6 个有
- `Qwen3_VQA` —— 4/6 个有
- `TT_img_enc` —— 4/6 个有
- `easy anythingIndexSwitch` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `TTResolutionSelector` —— 3/6 个有
- `Canny` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `ZML_AnyTypeSwitchFive` —— 2/6 个有
- `easy int` —— 2/6 个有
- `GetImageSize` —— 1/6 个有
- `Int` —— 1/6 个有
- `TT_img_enc_v2` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 6 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | ddim_uniform | - | 6 | 67% |
| 重绘幅度 | 0.65 | 0.65 - 1 | 6 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，6 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 ddim_uniform，6 个样本，一致性 67%
- 重绘幅度 中位数 0.65，观测区间 0.65 - 1，6 个样本
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
