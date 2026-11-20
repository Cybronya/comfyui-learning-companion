---
name: image_to_image_lora_sampler_unet_126
type: Image To Image
frequency: 5
level: moderate
coverage: 0.8312
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit扁平转3D，多材质预设_1960598660016988161.json, 图片生成/图生图/Qwen Edit标准流4步加速版（采样7秒）_1960010546181517314.json, 图片生成/图生图/Qwen Image Edit  三图融合_1962314713319325698.json, 图片生成/图生图/Qwen-Image-Edit单图编辑+LLM大模型提示词+API调用_1966433487458906114.json, 图片生成/图生图/千问Qwen Edit 提示词预设 多功能编辑工作流_1968589171730337793.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_126

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Edit扁平转3D，多材质预设_1960598660016988161.json、图片生成/图生图/Qwen Edit标准流4步加速版（采样7秒）_1960010546181517314.json、图片生成/图生图/Qwen Image Edit  三图融合_1962314713319325698.json、图片生成/图生图/Qwen-Image-Edit单图编辑+LLM大模型提示词+API调用_1966433487458906114.json、图片生成/图生图/千问Qwen Edit 提示词预设 多功能编辑工作流_1968589171730337793.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 4/5 个有
- `CR Prompt List` —— 2/5 个有
- `ImpactInt` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `LayerUtility: ExtendCanvas` —— 1/5 个有
- `PIP_图像联结` —— 1/5 个有
- `StringFunction|pysssss` —— 1/5 个有
- `ZhipuAPIConfig` —— 1/5 个有
- `ZhipuTextChat` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 5 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.7 - 1 | 5 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，5 个样本，取值集中（一致性 87%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
