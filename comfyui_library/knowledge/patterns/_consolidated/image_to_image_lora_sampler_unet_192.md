---
name: image_to_image_lora_sampler_unet_192
type: Image To Image
frequency: 3
level: strong
coverage: 0.383667
common_nodes: [CLIPLoader, CR Simple Image Compare, ConditioningZeroOut, GetImageSize, GetNode, Image Comparer (rgthree), ImageResizeKJv2, JjkText, KSampler, LayerUtility: BooleanOperator, LayerUtility: If , LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen2509服装假模拍摄精修提取3d_2015148606445068289.json, 图片生成/图生图/qwen2509服装精修提取3d_1988178363959394305.json, 图片生成/图生图/tk美女生成_1990661667606454273.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_192

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/qwen2509服装假模拍摄精修提取3d_2015148606445068289.json、图片生成/图生图/qwen2509服装精修提取3d_1988178363959394305.json、图片生成/图生图/tk美女生成_1990661667606454273.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：38%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CR Simple Image Compare`
- `ConditioningZeroOut`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LayerUtility: BooleanOperator`
- `LayerUtility: If `
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `DownloadAndLoadFlorence2Model` —— 1/3 个有
- `Florence2Run` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy float` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
