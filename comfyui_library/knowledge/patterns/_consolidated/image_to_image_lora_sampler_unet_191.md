---
name: image_to_image_lora_sampler_unet_191
type: Image To Image
frequency: 3
level: strong
coverage: 0.788333
common_nodes: [CFGNorm, CLIPLoader, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen-imaget批直出电商多图 自定义姿态与图片数量提示词控制图片数量_2097728974460903425.json, 图片生成/图生图/qwen-imaget直出电商多图【智能逻辑】【自定义姿态与图片数量_使用方法请查看工作流介绍_】_2057372450048008194.json, 图片生成/图生图/图片转桌面手办（Qwen+编辑）_1962479307606110209.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_191

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/qwen-imaget批直出电商多图 自定义姿态与图片数量提示词控制图片数量_2097728974460903425.json、图片生成/图生图/qwen-imaget直出电商多图【智能逻辑】【自定义姿态与图片数量_使用方法请查看工作流介绍_】_2057372450048008194.json、图片生成/图生图/图片转桌面手办（Qwen+编辑）_1962479307606110209.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageSharpen` —— 2/3 个有
- `Qwen3_VQA` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `workflow>内部提示词` —— 2/3 个有
- `workflow>文本处理` —— 2/3 个有
- `workflow>逻辑判断` —— 2/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
