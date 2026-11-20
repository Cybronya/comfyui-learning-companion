---
name: unknown_workflow_sampler_unet_vae_3
type: Unknown Workflow
frequency: 29
level: moderate
coverage: 0.739759
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image 2.1图片编辑-1图_2112357928580763649.json, 图片生成/图生图/Qwen image 2.1图片编辑-2图_2112352357722972162.json, 图片生成/图生图/Qwen image 2.1图片编辑-3图_2112358020758990850.json, 图片生成/图生图/Qwen image 2.1图片编辑-4图_2112358074219581441.json, 图片生成/图生图/Qwen image 2.1图片编辑-5图_2112359254878412802.json, 图片生成/图生图/Qwen image 2.1图片编辑-6图_2112359295756099586.json, 图片生成/图生图/Qwen-image-2.1-单图编辑_2104464258397462529.json, 图片生成/图生图/Qwen2.1-图生图12参考-提速版_2112576868661682177.json, 图片生成/图生图/QwenImage2.1-角色三视图-bf16展开版_2106018495979941889.json, 图片生成/图生图/Qwen_Image_2.1_图像编辑_2105116270961192961.json, 图片生成/图生图/Qwen_Image_2.1_图像编辑_2105493174088192002.json, 图片生成/图生图/Qwen_Image_2.1自动分镜_短剧分镜_2102322312635834369.json, 图片生成/图生图/qwen image 2.1 图编辑_2102212148364668930.json, 图片生成/图生图/qwen-image 2.1图像编辑_2101777177351122945.json, 图片生成/图生图/qwen-image-2.1图像编辑_2101918037409615874.json, 图片生成/图生图/qwen_image_2_1_图像编辑-换背景和姿态_2102207016054906881.json, 图片生成/图生图/qwen_image_2_1_图像编辑-换装_2101845419922903041.json, 图片生成/图生图/qwen_image_2_1_图像编辑-文本换装_2101852516261646337.json, 图片生成/图生图/qwen_image_2_1_手持指定物品_2102203525789995009.json, 图片生成/图生图/千问2.1节日表情包_2104578062582108162.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2108811508326166529.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2109545902754066433.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2109573850085281794.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2111996327927312386.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2112074578649509889.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2112076292018495489.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2112081176390361090.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2112091885144727554.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2112093934708150274.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_3

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1图片编辑-1图_2112357928580763649.json、图片生成/图生图/Qwen image 2.1图片编辑-2图_2112352357722972162.json、图片生成/图生图/Qwen image 2.1图片编辑-3图_2112358020758990850.json、图片生成/图生图/Qwen image 2.1图片编辑-4图_2112358074219581441.json、图片生成/图生图/Qwen image 2.1图片编辑-5图_2112359254878412802.json…）

- **类型**：Unknown Workflow
- **样本数**：29
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 29 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 28/29 个有
- `PrimitiveStringMultiline` —— 24/29 个有
- `SaveImageAdvanced` —— 21/29 个有
- `QwenImage21Cache` —— 20/29 个有
- `ResolutionSelector` —— 20/29 个有
- `LoadImage` —— 14/29 个有
- `LoraLoaderModelOnly` —— 11/29 个有
- `PreviewImage` —— 11/29 个有
- `PrimitiveBoolean` —— 10/29 个有
- `QwenImage21_T2IPromptRewrite` —— 9/29 个有
- `RH_QwenImagePromptEnhancer` —— 9/29 个有
- `easy showAnything` —— 9/29 个有
- `Int` —— 6/29 个有
- `SDVN Load Image Url` —— 6/29 个有
- `JjkShowText` —— 1/29 个有
- `QwenPERewriteT8` —— 1/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 50 | 29 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 29 | 100% |
| 采样算法 | euler | - | 29 | 100% |
| 调度器 | simple | - | 29 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 29 | 100% |
| 宽度 | 1024 | 16 - 2048 | 29 | 42% |
| 高度 | 1024 | 720 - 2048 | 29 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/29 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 50，29 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，29 个样本，一致性 100%
- 调度器 最常用 simple，29 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 16 - 2048，29 个样本，取值分散，一致性仅 42%
- 高度 中位数 1024，观测区间 720 - 2048，29 个样本
