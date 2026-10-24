---
name: image_to_image_lora_sampler_checkpoint_2
type: Image To Image
frequency: 7
level: strong
coverage: 0.888857
common_nodes: [CFGNorm, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, FluxKontextMultiReferenceLatentMethod, ImageStitch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit 2511+AnyPose+CN+F2P差异权重姿势控制V1（3控制+强人脸）_2007474854060105730.json, 图片生成/图生图/QwenEdit 2511+AnyPose+CN差异权重姿势控制V1（3控制强姿态）_2007472806010818562.json, 图片生成/图生图/QwenEdit 2511+AnyPose差异权重姿势控制V1（强人脸）_2007457424667578369.json, 图片生成/图生图/QwenEdit 2511+AnyPose差异权重姿势控制V1（强场景）_2007325676130541569.json, 图片生成/图生图/（自用）QwenEdit 2511+AnyPose+CN+F2P差异权重姿势控制V2（3控制）_2007480556543545346.json, 图片生成/图生图/（自用）QwenEdit 2511+AnyPose差异权重姿势控制V1（强场景）_2007468382089650178.json, 图片生成/图生图/（自用）QwenEdit 2511+F2P+AnyPose差异权重姿势控制V1（强人物）_2007470655058485250.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/QwenEdit 2511+AnyPose+CN+F2P差异权重姿势控制V1（3控制+强人脸）_2007474854060105730.json、图片生成/图生图/QwenEdit 2511+AnyPose+CN差异权重姿势控制V1（3控制强姿态）_2007472806010818562.json、图片生成/图生图/QwenEdit 2511+AnyPose差异权重姿势控制V1（强人脸）_2007457424667578369.json、图片生成/图生图/QwenEdit 2511+AnyPose差异权重姿势控制V1（强场景）_2007325676130541569.json、图片生成/图生图/（自用）QwenEdit 2511+AnyPose+CN+F2P差异权重姿势控制V2（3控制）_2007480556543545346.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageStitch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplySD3` —— 3/7 个有
- `ControlNetLoader` —— 3/7 个有
- `DWPreprocessor` —— 3/7 个有
- `DuckHideNode` —— 3/7 个有
- `JWInteger` —— 3/7 个有
- `SetUnionControlNetType` —— 3/7 个有
- `TT_img_enc` —— 3/7 个有
- `TT_img_enc_v2` —— 3/7 个有
- `easy anythingIndexSwitch` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `easy showAnything` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 512 | 512 - 512 | 7 | 100% |
| 高度 | 512 | 512 - 512 | 7 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，7 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，7 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
