---
name: unknown_workflow_sampler_checkpoint_vae_4
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.873071
common_nodes: [CFGNorm, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, GetImageSize, ImageScaleToTotalPixels, ImpactMinMax, KSampler, LoadImage, QwenEditConfigPreparer, SaveImage, Text Multiline, TextEncodeQwenImageEditPlusCustom_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenRapid-AIO-融图-去塑料感-v2.0_2046133973675417602.json, 图片生成/图生图/双图融合 图生图 图片编辑 人物一致性 mage-Edit-Rapid-AIO_2038154176668110849.json, 图片生成/图生图/双图融合_2007253741270994945.json, 图片生成/图生图/双图融合_多图融合_Image-Edit-Rapid-AIO_2020505121804783617.json, 图片生成/图生图/双图融合_多图融合_Image-Edit-Rapid-AIO_2021147361774411777.json, 图片生成/图生图/图生图_双图融合_多图融合_Image-Edit-Rapid-AIO_2021480774813356033.json, 图片生成/图生图/多功能融合神器Image-Edit-Rapid-AIO_2041679706919014401.json, 图片生成/图生图/多图融合-Image-Edit-Rapid-AIO-工作流_2009136391069896706.json, 图片生成/图生图/阿里 _ Qwen-Rapid-AIO _ 双图融合 _ 多图融合_2038856590266212353.json, 图片生成/文生图/Demo-单图绘画工作流_2022228609880035330.json, 图片生成/文生图/Demo-文生图工作流_2029110682951618561.json, 图片生成/文生图/文生图新工作流_2029132515297992705.json, 图片生成/文生图/最新QwenEdit-Rapid-AIO-V18多功能融合模型_2009902909454028802.json, 图片生成/文生图/最新v18 Image-Edit-Rapid-AIO多功能融合模型_1975733915887472642.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_4

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/QwenRapid-AIO-融图-去塑料感-v2.0_2046133973675417602.json、图片生成/图生图/双图融合 图生图 图片编辑 人物一致性 mage-Edit-Rapid-AIO_2038154176668110849.json、图片生成/图生图/双图融合_2007253741270994945.json、图片生成/图生图/双图融合_多图融合_Image-Edit-Rapid-AIO_2020505121804783617.json、图片生成/图生图/双图融合_多图融合_Image-Edit-Rapid-AIO_2021147361774411777.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGNorm`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImpactMinMax`
- `KSampler`
- `LoadImage`
- `QwenEditConfigPreparer`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 13/14 个有
- `ImpactInt` —— 13/14 个有
- `ImpactSwitch` —— 13/14 个有
- `RH_LLMAPI_NODE` —— 13/14 个有
- `easy showAnything` —— 13/14 个有
- `Fast Groups Bypasser (rgthree)` —— 11/14 个有
- `ImageConcanate` —— 11/14 个有
- `ImageConcatMulti` —— 11/14 个有
- `QwenEditOutputExtractor` —— 11/14 个有
- `AIO_Preprocessor` —— 10/14 个有
- `PreviewImage` —— 10/14 个有
- `BDXTestInt` —— 3/14 个有
- `Anything Everywhere3` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler_ancestral | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 512 | 512 - 1080 | 14 | 64% |
| 高度 | 512 | 512 - 1792 | 14 | 41% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 1080，14 个样本
- 高度 中位数 512，观测区间 512 - 1792，14 个样本，取值分散，一致性仅 41%
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
