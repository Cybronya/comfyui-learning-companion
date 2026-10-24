---
name: unknown_workflow_sampler_unet_vae_16
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.73
common_nodes: [CLIPLoader, DF_Text_Box, GoohaiRatioAndResolution, GoohaiRouteBlocker, KSampler, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, QwenImagePromptOptimizer, RestoreQwenImage21GH, SaveImage, TextEncodeQwenImage21GH, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen Image 2.1 文生、图像编辑一体化_2103270694288183297.json, 图片生成/反推提示词/Qwen Image 2.1 文生、图像编辑一体化_2105315513315450881.json, 图片生成/图生图/AI图像创作丨Qwen Image 2.1丨文生图 _ 图像编辑_2112739173701607425.json, 图片生成/图生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词_2111365987026169857.json, 图片生成/图生图/AI生图编辑丨Qwen-Image_2.1丨多图参考·智能提示词_2110913318310469634.json, 图片生成/图生图/AI生图编辑丨Qwen-Image_2.1丨多图参考·智能提示词_2111733672293519361.json, 图片生成/图生图/Qwen Image 2.1 图像扩展_2107511073355161601.json, 图片生成/图生图/Qwen Image 2.1 图像编辑、多图编辑_2109090992728137730.json, 图片生成/图生图/Qwen Image 2.1 局部修改_2107669259315924994.json, 图片生成/图生图/Qwen Image 2.1 文生、图像编辑一体化_2111080180189061121.json, 图片生成/图生图/Qwen Image 2.1 文生、图像编辑一体化工作台_2105131610982141954.json, 图片生成/图生图/Qwen Image 2.1 文生、多图像编辑一体化_2105870849386573825.json, 图片生成/图生图/Qwen Image 2.1 文生图_单图编辑、多图编辑图像编辑一体化_2105160468577996801.json, 图片生成/图生图/Qwen_Image_2.1_局部修改_2111275285760012290.json, 图片生成/图生图/服装迁移图像编辑Clothing Transfer Image Editing Qwen  2.1_2111978235830562818.json, 图片生成/图生图/服装迁移图像编辑一体化Qwen Image 2.1_2110580002868781057.json, 图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词_2108120997114245121.json, 图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词_2110936615257464834.json, 图片生成/文生图/Qwen Image 2.1 文生+图像编辑一体化_2105178276711976962.json, 图片生成/文生图/Qwen-Image-2.1 T8加速简洁版（中文繁体招牌王）_2111331245375451137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_16

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1 文生、图像编辑一体化_2103270694288183297.json、图片生成/反推提示词/Qwen Image 2.1 文生、图像编辑一体化_2105315513315450881.json、图片生成/图生图/AI图像创作丨Qwen Image 2.1丨文生图 _ 图像编辑_2112739173701607425.json、图片生成/图生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词_2111365987026169857.json、图片生成/图生图/AI生图编辑丨Qwen-Image_2.1丨多图参考·智能提示词_2110913318310469634.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `DF_Text_Box`
- `GoohaiRatioAndResolution`
- `GoohaiRouteBlocker`
- `KSampler`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `QwenImage21SpectrumT8`
- `QwenImagePromptOptimizer`
- `RestoreQwenImage21GH`
- `SaveImage`
- `TextEncodeQwenImage21GH`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 19/20 个有
- `LoadImageGoohai` —— 18/20 个有
- `Image Comparer (rgthree)` —— 17/20 个有
- `LoadImage` —— 17/20 个有
- `忽略多组孤海` —— 17/20 个有
- `GetNode` —— 15/20 个有
- `SetNode` —— 15/20 个有
- `孤海注释` —— 13/20 个有
- `ComfySwitchNode` —— 5/20 个有
- `PrimitiveBoolean` —— 5/20 个有
- `CM_FloatToInt` —— 1/20 个有
- `GoohaiAnyExists` —— 1/20 个有
- `GoohaiDisplayAny` —— 1/20 个有
- `LoraLoaderModelOnly` —— 1/20 个有
- `easy ifElse` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 20 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
