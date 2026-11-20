---
name: image_to_image_sampler_vae_22
type: Image To Image
frequency: 5
level: strong
coverage: 0.9024
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToMegapixels, KSampler, LoadImage, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, TextEncodeQwenImageEdit, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Nunchaku qwen image edit 4步图像编辑模型 极速版-StarAI_1965839255085953026.json, 图片生成/图生图/QwenImageEDIT-双节棍光速4步-动漫转真实_1966293441980395522.json, 图片生成/图生图/双节棍4步_千问图像编辑-快速编辑_Qwen+Image+EDIT+nunchaku+Lightni_1966242828240195585.json, 图片生成/图生图/双节棍版光速Qwen Image EDIT工作流_1965791350140637185.json, 图片生成/图生图/双节棍版光速Qwen Image EDIT工作流_2018200493197107201.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_22

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Nunchaku qwen image edit 4步图像编辑模型 极速版-StarAI_1965839255085953026.json、图片生成/图生图/QwenImageEDIT-双节棍光速4步-动漫转真实_1966293441980395522.json、图片生成/图生图/双节棍4步_千问图像编辑-快速编辑_Qwen+Image+EDIT+nunchaku+Lightni_1966242828240195585.json、图片生成/图生图/双节棍版光速Qwen Image EDIT工作流_1965791350140637185.json、图片生成/图生图/双节棍版光速Qwen Image EDIT工作流_2018200493197107201.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToMegapixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `ImageConcanate` —— 3/5 个有
- `CR Text` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `Int` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy float` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 5 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
