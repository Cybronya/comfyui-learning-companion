---
name: image_to_image_controlnet_inpaint_sampler_7
type: Image To Image
frequency: 6
level: moderate
coverage: 0.908167
common_nodes: [AnimeLineArtPreprocessor, CLIPTextEncode, CheckpointLoaderSimple, ConstrainImage|pysssss, ControlNetApplyAdvanced, ControlNetLoader, GrowMask, INPAINT_ApplyFooocusInpaint, INPAINT_LoadFooocusInpaint, ImageCompositeMasked, ImageToMask, ImpactDilateMask, KSampler, LaMaInpainting, LayerUtility: ImageBlend, LoadImage, MaskToImage, SaveImage, SetLatentNoiseMask, VAEDecode, VAEEncode, VAEEncodeForInpaint, WD14Tagger|pysssss]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/高级消除_抹除_擦除工作流  一键魔法消除任何图中不想出现的内容 去水印_2107046001218510849.json, 平台全量/一键智能涂抹擦除_无痕填充_1887781099014086657.json, 平台全量/一键消除丨当前最强擦除工具_1841460410993037314.json, 平台全量/移除修复工作流（好用吧）_1900565672219549698.json, 平台全量/高级消除_抹除_擦除工作流  一键魔法消除任何图中不想出现的内容 去水印_1927346916500070402.json, 平台全量/高级消除_抹除_擦除工作流  去水印 去除图中内容_2003489591095115777.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_sampler_7

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/高级消除_抹除_擦除工作流  一键魔法消除任何图中不想出现的内容 去水印_2107046001218510849.json、平台全量/一键智能涂抹擦除_无痕填充_1887781099014086657.json、平台全量/一键消除丨当前最强擦除工具_1841460410993037314.json、平台全量/移除修复工作流（好用吧）_1900565672219549698.json、平台全量/高级消除_抹除_擦除工作流  一键魔法消除任何图中不想出现的内容 去水印_1927346916500070402.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `AnimeLineArtPreprocessor`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `GrowMask`
- `INPAINT_ApplyFooocusInpaint`
- `INPAINT_LoadFooocusInpaint`
- `ImageCompositeMasked`
- `ImageToMask`
- `ImpactDilateMask`
- `KSampler`
- `LaMaInpainting`
- `LayerUtility: ImageBlend`
- `LoadImage`
- `MaskToImage`
- `SaveImage`
- `SetLatentNoiseMask`
- `VAEDecode`
- `VAEEncode`
- `VAEEncodeForInpaint`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `ConstrainImageforVideo|pysssss` —— 1/6 个有
- `DifferentialDiffusion` —— 1/6 个有
- `DualCLIPLoader` —— 1/6 个有
- `FluxGuidance` —— 1/6 个有
- `InpaintModelConditioning` —— 1/6 个有
- `LayerUtility: ImageReel` —— 1/6 个有
- `LayerUtility: ImageReelComposit` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `PreviewBridge` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `ResizeMask` —— 1/6 个有
- `UNETLoader` —— 1/6 个有
- `VAELoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1 | 6 | 100% |
| 采样步数 | 6 | 5 - 20 | 6 | 34% |
| Prompt 约束强度(CFG) | 1.7 | 1 - 2 | 6 | 76% |
| 采样算法 | dpmpp_sde | - | 6 | 83% |
| 调度器 | karras | - | 6 | 83% |
| 重绘幅度 | 1 | 0.8 - 1 | 6 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 6，观测区间 5 - 20，6 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 1.7，观测区间 1 - 2，6 个样本
- 采样算法 最常用 dpmpp_sde，6 个样本，一致性 83%
- 调度器 最常用 karras，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，6 个样本，取值集中（一致性 90%）
- 高发问题（9/6 个样本）：Steps较低可能导致细节不足
