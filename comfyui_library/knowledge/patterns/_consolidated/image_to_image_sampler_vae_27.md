---
name: image_to_image_sampler_vae_27
type: Image To Image
frequency: 5
level: weak
coverage: 0.6404
common_nodes: [CFGNorm, CLIPLoader, EmptySD3LatentImage, GetNode, ImageScaleToTotalPixels, ImageStitch, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, SetNode, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/双节棍版Qwen-Image模型2509多图编辑_1976884280855085057.json, 图片生成/图生图/双节棍版千问编辑模型_1987197398025965570.json, 图片生成/文生图/一致性角色生成器_1959543923909799937.json, 平台全量/image_qwen_image_edit大杯Plus-Aiwood_1970423010484252673.json, 平台全量/双节棍版千问编辑模型2509大杯_1970848316198162433.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_27

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/双节棍版Qwen-Image模型2509多图编辑_1976884280855085057.json、图片生成/图生图/双节棍版千问编辑模型_1987197398025965570.json、图片生成/文生图/一致性角色生成器_1959543923909799937.json、平台全量/image_qwen_image_edit大杯Plus-Aiwood_1970423010484252673.json、平台全量/双节棍版千问编辑模型2509大杯_1970848316198162433.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `GetNode`
- `ImageScaleToTotalPixels`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `GetImageSize` —— 3/5 个有
- `NunchakuQwenImageDiTLoader` —— 3/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `UNETLoader` —— 2/5 个有
- `AILab_QwenVL_Advanced` —— 1/5 个有
- `JWStringGetLine` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 50 | 5 | 33% |
| Prompt 约束强度(CFG) | 2 | 1 - 4 | 5 | 43% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 50，5 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 4，5 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（9/5 个样本）：Steps较低可能导致细节不足
