---
name: image_to_image_controlnet_lora_sampler_25
type: Image To Image
frequency: 2
level: weak
coverage: 0.708
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApply, ControlNetLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoader, PreviewImage, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Ghibli风格一键出图_1839625177389813762.json, 平台全量/动物转动漫_1805104702387380225.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Ghibli风格一键出图_1839625177389813762.json、平台全量/动物转动漫_1805104702387380225.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApply`
- `ControlNetLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CannyEdgePreprocessor` —— 1/2 个有
- `ConcatText_Zho` —— 1/2 个有
- `DepthAnythingPreprocessor` —— 1/2 个有
- `MarigoldDepthEstimation` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `Text _O` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | - | 2 | 100% |
| 采样步数 | 12 | - | 2 | 33% |
| Prompt 约束强度(CFG) | 4.4 | - | 2 | 41% |
| 采样算法 | dpmpp_sde | - | 2 | 50% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.725 | - | 2 | 97% |
| LoRA 模型强度 | 0.8 | - | 2 | 75% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 12，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 4.4，样本不足，未给区间，2 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.725，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
