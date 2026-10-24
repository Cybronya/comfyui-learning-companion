---
name: image_to_image_inpaint_sampler_clip_2
type: Image To Image
frequency: 9
level: strong
coverage: 0.879444
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DrawMaskOnImage, EmptyFlux2LatentImage, INTConstant, ImageAndMaskPreview, InpaintCropImproved, InpaintStitchImproved, KSampler, LoadImage, ReferenceLatent, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F2K-高分指定替换流_2051486490504515585.json, 图片生成/图生图/FLUX2-Klein局部生成替换_2044340651386478593.json, 图片生成/图生图/FLUX2-Klein局部生成替换_2097875143249973249.json, 图片生成/图生图/FLUX2-Klein局部生成替换_2099410343209562114.json, 图片生成/图生图/▶F2K-高分指定替换流_2053743469604159489.json, 图片生成/图生图/▶Flux2-Klein高分指定替换流 ，换脸_2042053798167846913.json, 图片生成/图生图/哪里不爱点哪里(NDD_-AIGC大赏_2027034236561133569.json, 图片生成/图生图/局部重绘F2K_2058929875309916162.json, 图片生成/图生图/高分辨率图-小区域（小像素区域）-局部重绘_2033553864825249793.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/F2K-高分指定替换流_2051486490504515585.json、图片生成/图生图/FLUX2-Klein局部生成替换_2044340651386478593.json、图片生成/图生图/FLUX2-Klein局部生成替换_2097875143249973249.json、图片生成/图生图/FLUX2-Klein局部生成替换_2099410343209562114.json、图片生成/图生图/▶F2K-高分指定替换流_2053743469604159489.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DrawMaskOnImage`
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
- `Image Comparer (rgthree)` —— 8/9 个有
- `LayerUtility: PurgeVRAM V2` —— 8/9 个有
- `SaveImage` —— 8/9 个有
- `ImageScaleToTotalPixels` —— 7/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `Seed (rgthree)` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `INPAINT_ExpandMask` —— 3/9 个有
- `LayerColor: BrightnessContrastV2` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `ImageToMask` —— 2/9 个有
- `CompressImages` —— 1/9 个有
- `LayerColor: AutoAdjustV2` —— 1/9 个有
- `LoraLoader` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 6 | 9 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 6，9 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（12/9 个样本）：Steps较低可能导致细节不足
