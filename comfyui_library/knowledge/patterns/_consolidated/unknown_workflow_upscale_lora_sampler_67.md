---
name: unknown_workflow_upscale_lora_sampler_67
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.859333
common_nodes: [CFGNorm, CLIPLoader, CR Text, ConditioningZeroOut, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEditPlusPro_lrzjason, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/产品模仿-电商专用_2066812202677526530.json, 图片生成/图生图/产品模仿-电商专用_2092157040092340226.json, 图片生成/图生图/电商专用-教学版（千问编辑模型）_2087136169623638017.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_67

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/产品模仿-电商专用_2066812202677526530.json、图片生成/图生图/产品模仿-电商专用_2092157040092340226.json、图片生成/图生图/电商专用-教学版（千问编辑模型）_2087136169623638017.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DepthAnythingPreprocessor` —— 2/3 个有
- `OpenposePreprocessor` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `JWImageResizeByShorterSide` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
