---
name: unknown_workflow_video_lora_sampler_434
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.922
common_nodes: [CLIPLoader, CLIPTextEncode, ImageFromBatch+, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1950024322967584770.json, 视频生成/图生视频/1950473499028738049.json, 视频生成/图生视频/1950473543098290177.json, 视频生成/图生视频/1950544723431903234.json, 视频生成/图生视频/1950053355886436353.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_434

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1950024322967584770.json、视频生成/图生视频/1950473499028738049.json、视频生成/图生视频/1950473543098290177.json、视频生成/图生视频/1950544723431903234.json、视频生成/图生视频/1950053355886436353.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageFromBatch+`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 4/5 个有
- `ImageBatch` —— 3/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `ImageToMask` —— 3/5 个有
- `MaskToImage` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `RepeatImageBatch` —— 3/5 个有
- `SolidMask` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `ImageConcanate` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `SDVN Image Repeat` —— 2/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 60% |
| Prompt 约束强度(CFG) | 10 | 8 - 10 | 5 | 89% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | lcm | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 10，观测区间 8 - 10，5 个样本，取值集中（一致性 89%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
