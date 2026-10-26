---
name: image_to_image_upscale_lora_sampler_39
type: Image To Image
frequency: 4
level: moderate
coverage: 0.62925
common_nodes: [AILab_QwenVL, Any Switch (rgthree), CLIPLoader, CLIPTextEncode, CR Image Grid Panel, CR String To Number, CR Text, CR Text Concatenate, ConditioningZeroOut, Fast Groups Muter (rgthree), GetNode, ImageBlend, ImageListToBatch+, ImageScaleBy, ImageUpscaleWithModel, ImpactSwitch, Int, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, ProcessString, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, SaveImage, SetNode, ShellAgentPluginOutputText, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageIndexSwitch, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI电影分镜制作+Z-image写实洗图_2006979481432494081.json, 图片生成/图生图/亿薪AI分镜制作（真人）_2017320281571860482.json, 图片生成/图生图/提示词+分镜图压缩包自动打包！AI短剧_AI漫剧_AI电影分镜图工作流+Z-image写实洗图_2044432724458475522.json, 图片生成/图生图/电影动漫分镜制作Z-image写实洗图_2014155916240756738.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_39

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/AI电影分镜制作+Z-image写实洗图_2006979481432494081.json、图片生成/图生图/亿薪AI分镜制作（真人）_2017320281571860482.json、图片生成/图生图/提示词+分镜图压缩包自动打包！AI短剧_AI漫剧_AI电影分镜图工作流+Z-image写实洗图_2044432724458475522.json、图片生成/图生图/电影动漫分镜制作Z-image写实洗图_2014155916240756738.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_QwenVL`
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Image Grid Panel`
- `CR String To Number`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `ImageBlend`
- `ImageListToBatch+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactSwitch`
- `Int`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveFloat`
- `ProcessString`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `SaveImage`
- `SetNode`
- `ShellAgentPluginOutputText`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageIndexSwitch`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `HAIGC_SaveImagesToZip` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 4 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 0.78 - 1 | 4 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.78 - 1，4 个样本，取值集中（一致性 90%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
