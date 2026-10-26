---
name: image_to_image_inpaint_sampler_clip_2
type: Image To Image
frequency: 9
level: moderate
coverage: 0.877
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, INTConstant, ImageAndMaskPreview, InpaintCropImproved, InpaintStitchImproved, KSampler, LoadImage, ReferenceLatent, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F2K-高分指定替换流_2051486490504515585.json, 图片生成/图生图/F2K单-双图编辑_2114519724871741442.json, 图片生成/图生图/FLUX2-Klein局部生成替换_2044340651386478593.json, 图片生成/图生图/FLUX2-Klein局部生成替换_2097875143249973249.json, 图片生成/图生图/FLUX2-Klein局部生成替换_2099410343209562114.json, 图片生成/图生图/▶F2K-高分指定替换流_2053743469604159489.json, 图片生成/图生图/▶Flux2-Klein高分指定替换流 ，换脸_2042053798167846913.json, 图片生成/图生图/哪里不爱点哪里(NDD_-AIGC大赏_2027034236561133569.json, 图片生成/图生图/局部重绘F2K_2058929875309916162.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/F2K-高分指定替换流_2051486490504515585.json、图片生成/图生图/F2K单-双图编辑_2114519724871741442.json、图片生成/图生图/FLUX2-Klein局部生成替换_2044340651386478593.json、图片生成/图生图/FLUX2-Klein局部生成替换_2097875143249973249.json、图片生成/图生图/FLUX2-Klein局部生成替换_2099410343209562114.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `INTConstant`
- `ImageAndMaskPreview`
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 8/9 个有
- `DrawMaskOnImage` —— 8/9 个有
- `Image Comparer (rgthree)` —— 8/9 个有
- `LayerUtility: PurgeVRAM V2` —— 8/9 个有
- `SaveImage` —— 8/9 个有
- `ImageScaleToTotalPixels` —— 7/9 个有
- `Seed (rgthree)` —— 6/9 个有
- `Fast Groups Bypasser (rgthree)` —— 5/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `INPAINT_ExpandMask` —— 4/9 个有
- `LayerColor: BrightnessContrastV2` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `ImageToMask` —— 2/9 个有
- `CLIPLoaderGGUF` —— 1/9 个有
- `CompressImages` —— 1/9 个有
- `LayerColor: AutoAdjustV2` —— 1/9 个有
- `LoraLoader` —— 1/9 个有
- `UnetLoaderGGUF` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 20 | 9 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 20，9 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（11/9 个样本）：Steps较低可能导致细节不足
