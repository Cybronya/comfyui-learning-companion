---
name: unknown_workflow_unet_vae_2
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.858647
common_nodes: [CLIPLoader, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, QwenPERewriteT8, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/提示词自动优化Qwen Image 2.1 PE 多图像编辑-t8的pe高质量版_2102243596664655874.json, 图片生成/图生图/稳定加速版Qwen_Image_2.1_PE_姿势编辑_2108764188251348994.json, 图片生成/图生图/稳定加速版Qwen_Image_2.1_PE_姿势编辑_2110555697225232386.json, 图片生成/图生图/超级加速版Qwen Image 2.1 PE 图像编辑_2103518802859352065.json, 图片生成/图生图/（4步加速-v0.21适配版）Qwen Image 2.1 PE 图像编辑（最多3图）_2103127729746042881.json, 图片生成/图生图/（4步加速-非稳定）Qwen Image 2.1 PE 图像编辑（最多3图）_2102757842590724097.json, 图片生成/图生图/（Pruna-5步加速-非稳定）Qwen Image 2.1 PE 图像编辑_2103704266870448129.json, 图片生成/图生图/（Pruna-8步加速-非稳定）Qwen Image 2.1 PE 图像编辑（最多3图）_2103706738779320321.json, 图片生成/图生图/（Remove模型测试）Qwen Image 2.1 PE 姿势编辑_2106228938317062146.json, 图片生成/图生图/（Remove模型）Qwen Image 2.1 PE 姿势编辑_2106290030498111489.json, 图片生成/图生图/（Remove模型）Qwen Image 2.1 PE 姿势编辑_2106383894743441409.json, 图片生成/图生图/（最强T8版加速）Qwen Image 2.1 PE（Un） 图像编辑v2_2108627010334584834.json, 图片生成/文生图/AI人像编辑丨Qwen Image 2.1 Turbo_2110593367078952962.json, 图片生成/文生图/Qwen Image 2.1 t8加速PE+int8加速版_2109835098110648321.json, 图片生成/文生图/Qwen Image 2.1 t8加速PE+int8加速版_2110684372931268609.json, 图片生成/文生图/（最强T8版加速）Qwen Image 2.1 PE(Un) 文生图v2_2108631026816868353.json, 图片生成/文生图/（稳定加速版）Qwen Image 2.1 PE 文生图_2104081684923772930.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_2

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/提示词自动优化Qwen Image 2.1 PE 多图像编辑-t8的pe高质量版_2102243596664655874.json、图片生成/图生图/稳定加速版Qwen_Image_2.1_PE_姿势编辑_2108764188251348994.json、图片生成/图生图/稳定加速版Qwen_Image_2.1_PE_姿势编辑_2110555697225232386.json、图片生成/图生图/超级加速版Qwen Image 2.1 PE 图像编辑_2103518802859352065.json、图片生成/图生图/（4步加速-v0.21适配版）Qwen Image 2.1 PE 图像编辑（最多3图）_2103127729746042881.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `QwenPERewriteT8`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 15/17 个有
- `QwenImage21Cache` —— 13/17 个有
- `KSampler` —— 12/17 个有
- `QwenImage21SageAttentionT8` —— 12/17 个有
- `LoraLoaderModelOnly` —— 11/17 个有
- `QwenImage21BlockCacheT8` —— 10/17 个有
- `QwenImage21SpectrumT8` —— 10/17 个有
- `KSamplerSelect` —— 6/17 个有
- `ManualSigmas` —— 6/17 个有
- `SamplerCustomAdvanced` —— 6/17 个有
- `CFGGuider` —— 5/17 个有
- `RandomNoise` —— 5/17 个有
- `PathchSageAttentionKJ` —— 4/17 个有
- `孤海注释` —— 3/17 个有
- `LTXVConcatAVLatent` —— 1/17 个有
- `LTXVSeparateAVLatent` —— 1/17 个有
- `LoraLoaderBypassModelOnly` —— 1/17 个有
- `PrimitiveBoolean` —— 1/17 个有
- `VAEEncode` —— 1/17 个有
- `VHS_VideoCombine` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 4 - 40 | 12 | 43% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1024 | 1024 - 1152 | 17 | 97% |
| 高度 | 1024 | 1024 - 2016 | 17 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 4 - 40，12 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1152，17 个样本，取值集中（一致性 97%）
- 高度 中位数 1024，观测区间 1024 - 2016，17 个样本
