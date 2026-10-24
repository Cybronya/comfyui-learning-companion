---
name: image_to_image_controlnet_lora_sampler_7
type: Image To Image
frequency: 3
level: strong
coverage: 0.829
common_nodes: [CLIPLoader, ControlNetLoader, KSampler, LayerUtility: ImageScaleByAspectRatio, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, OpenposePreprocessor, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 姿态 深度 线稿 3合1（InstantX）_1960490317730426881.json, 图片生成/图生图/Qwen编辑 双人动作迁移_1987056306760691713.json, 图片生成/图生图/Qwen编辑 更换指定姿势_1961357667396730881.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_7

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen 姿态 深度 线稿 3合1（InstantX）_1960490317730426881.json、图片生成/图生图/Qwen编辑 双人动作迁移_1987056306760691713.json、图片生成/图生图/Qwen编辑 更换指定姿势_1961357667396730881.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ControlNetLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `OpenposePreprocessor`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `CLIPTextEncode` —— 2/3 个有
- `ControlNetApplySD3` —— 2/3 个有
- `AFL:QwenEditPlusFastuseV2` —— 1/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `CR Image Input Switch (4 way)` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `TextEncodeQwenImageEdit` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1.15 | - | 2 | 70% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 1.15，样本不足，未给区间，2 个样本
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
