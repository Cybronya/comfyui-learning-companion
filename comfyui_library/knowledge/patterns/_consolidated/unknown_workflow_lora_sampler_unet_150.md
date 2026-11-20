---
name: unknown_workflow_lora_sampler_unet_150
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 1
common_nodes: [CFGNorm, CLIPLoader, CR Text, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/next shoot Qwen edit fish cut web APP_v1.1_2001316096290549761.json, 图片生成/图生图/next shoot Qwen edit fish cut web APP_v1.2_2001357640313827329.json, 图片生成/图生图/qwen_Edit_2511_角色三视图_2004958259977089025.json, 图片生成/图生图/最新编辑【换装】  可以设置分辨率_2048304011274620929.json, 图片生成/图生图/柏辰电商-宠物图变为德文猫V3_1989152999404613634.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_150

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/next shoot Qwen edit fish cut web APP_v1.1_2001316096290549761.json、图片生成/图生图/next shoot Qwen edit fish cut web APP_v1.2_2001357640313827329.json、图片生成/图生图/qwen_Edit_2511_角色三视图_2004958259977089025.json、图片生成/图生图/最新编辑【换装】  可以设置分辨率_2048304011274620929.json、图片生成/图生图/柏辰电商-宠物图变为德文猫V3_1989152999404613634.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 4/5 个有
- `CR Text Concatenate` —— 2/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/5 个有
- `ImageResize+` —— 1/5 个有
- `Int` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `SizeSelector` —— 1/5 个有
- `easy imageSize` —— 1/5 个有
- `图像缩放V2_孤海` —— 1/5 个有
- `孤海图像缩放按像素` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 5 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1344 | 1080 - 1504 | 5 | 90% |
| 高度 | 768 | 752 - 1920 | 5 | 58% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1344，观测区间 1080 - 1504，5 个样本，取值集中（一致性 90%）
- 高度 中位数 768，观测区间 752 - 1920，5 个样本
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
