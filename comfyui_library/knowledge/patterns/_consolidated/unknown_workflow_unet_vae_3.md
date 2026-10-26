---
name: unknown_workflow_unet_vae_3
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.873437
common_nodes: [CLIPLoader, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen Image 2.1 PE 文生图_2102401855983808514.json, 图片生成/图生图/BF16小字不崩-Qwen image 2.1图片编辑_2102282925260759042.json, 图片生成/图生图/BF16小字不崩-Qwen_image_2.1图片编辑_2104378058986844161.json, 图片生成/图生图/BFS换脸6步加速版Qwen_Image_2.1图像编辑_2108752507940986881.json, 图片生成/图生图/BFS换脸6步加速版Qwen_Image_2.1图像编辑_2110554314409332737.json, 图片生成/图生图/Qwen 2.1 图像编辑（4步加速）_2102704302576988161.json, 图片生成/图生图/Qwen Image 2.1 PE 图像编辑-t8加速版_2105710865591922690.json, 图片生成/图生图/Qwen Image 2.1 PE 图像编辑2609_2106042591421747201.json, 图片生成/图生图/Qwen Image 2.1 参考人物姿势_2102935036923310081.json, 图片生成/图生图/Qwen Image 2.1 整张图像编辑_2102952588135194626.json, 图片生成/图生图/多图编辑丨Qwen-Image 2.1丨T8加速_2113204332517748738.json, 图片生成/图生图/（最强T8版加速）Qwen Image 2.1 PE（Un） 图像编辑v2_2108627010334584834.json, 图片生成/文生图/AI人像编辑丨Qwen Image 2.1 Turbo_2110593367078952962.json, 图片生成/文生图/Qwen Image 2.1 t8加速PE+int8加速版_2109835098110648321.json, 图片生成/文生图/Qwen Image 2.1 t8加速PE+int8加速版_2110684372931268609.json, 图片生成/文生图/（最强T8版加速）Qwen Image 2.1 PE(Un) 文生图v2_2108631026816868353.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_3

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1 PE 文生图_2102401855983808514.json、图片生成/图生图/BF16小字不崩-Qwen image 2.1图片编辑_2102282925260759042.json、图片生成/图生图/BF16小字不崩-Qwen_image_2.1图片编辑_2104378058986844161.json、图片生成/图生图/BFS换脸6步加速版Qwen_Image_2.1图像编辑_2108752507940986881.json、图片生成/图生图/BFS换脸6步加速版Qwen_Image_2.1图像编辑_2110554314409332737.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 14/16 个有
- `QwenPERewriteT8` —— 14/16 个有
- `easy cleanGpuUsed` —— 14/16 个有
- `easy showAnything` —— 14/16 个有
- `QwenImage21Cache` —— 12/16 个有
- `QwenImage21SageAttentionT8` —— 12/16 个有
- `KSampler` —— 10/16 个有
- `LoraLoaderModelOnly` —— 9/16 个有
- `QwenImage21BlockCacheT8` —— 8/16 个有
- `QwenImage21SpectrumT8` —— 8/16 个有
- `CFGGuider` —— 6/16 个有
- `KSamplerSelect` —— 6/16 个有
- `ManualSigmas` —— 6/16 个有
- `RandomNoise` —— 6/16 个有
- `SamplerCustomAdvanced` —— 6/16 个有
- `ConcatTextOfUtils` —— 2/16 个有
- `LoraLoaderBypassModelOnly` —— 2/16 个有
- `SaveImageAdvanced` —— 2/16 个有
- `孤海注释` —— 2/16 个有
- `AIO_Preprocessor` —— 1/16 个有
- `EmptyImage` —— 1/16 个有
- `PreviewImage` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 4 - 50 | 10 | 34% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1024 | 1024 - 1152 | 16 | 97% |
| 高度 | 1024 | 1024 - 2016 | 16 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 4 - 50，10 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1152，16 个样本，取值集中（一致性 97%）
- 高度 中位数 1024，观测区间 1024 - 2016，16 个样本
