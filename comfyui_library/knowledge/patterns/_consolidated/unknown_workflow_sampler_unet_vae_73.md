---
name: unknown_workflow_sampler_unet_vae_73
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.971636
common_nodes: [CLIPLoader, CR Text, ConditioningZeroOut, KSampler, LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/003.FLUX.2智能综合006.提示词优化单图编辑-精简_2035251644513918978.json, 图片生成/图生图/C-模特换装（4K版）-V5_2038522798334812162.json, 图片生成/图生图/FLUX.2-klein 图像编辑- 图像编辑-快速出图图像生成zip输出_2022641416794542081.json, 图片生成/图生图/FLUX.2-klein 图像编辑-亚秒级图像生成_2012112860427591681.json, 图片生成/图生图/FireRed-Image-Edit-三图融合-一致性加强版本_2027291315473489922.json, 图片生成/图生图/Fk2-图像编辑低限版_2032400294235082754.json, 图片生成/图生图/Fk2-图像编辑低限版_2037529896523669505.json, 图片生成/图生图/Qwen-Edit-2511-多图融合-一致性加强版本_2003661742527946754.json, 图片生成/图生图/一键生成三视图（人物版）-Qwen-Edit-2511_2024368464114225154.json, 图片生成/图生图/三视图-三视图一键生成-Qwen-Edit-2511_2012814594942705666.json, 图片生成/图生图/人物四视图影视短剧角色资产图一键生成_Qwen-Edit-2511_2094804202357870593.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_73

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/003.FLUX.2智能综合006.提示词优化单图编辑-精简_2035251644513918978.json、图片生成/图生图/C-模特换装（4K版）-V5_2038522798334812162.json、图片生成/图生图/FLUX.2-klein 图像编辑- 图像编辑-快速出图图像生成zip输出_2022641416794542081.json、图片生成/图生图/FLUX.2-klein 图像编辑-亚秒级图像生成_2012112860427591681.json、图片生成/图生图/FireRed-Image-Edit-三图融合-一致性加强版本_2027291315473489922.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 10/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/11 个有
- `SaveImage` —— 10/11 个有
- `LoraLoaderModelOnly` —— 6/11 个有
- `EmptyFlux2LatentImage` —— 5/11 个有
- `EmptySD3LatentImage` —— 5/11 个有
- `PreviewImage` —— 2/11 个有
- `CR Text Concatenate` —— 1/11 个有
- `CompressImages` —— 1/11 个有
- `EmptyLatentImage` —— 1/11 个有
- `INTConstant` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `Text` —— 1/11 个有
- `TextInput_` —— 1/11 个有
- `easy imageConcat` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 25 | 11 | 49% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 55% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 768 | - | 1 | 100% |
| 高度 | 1344 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 25，11 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 55%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
