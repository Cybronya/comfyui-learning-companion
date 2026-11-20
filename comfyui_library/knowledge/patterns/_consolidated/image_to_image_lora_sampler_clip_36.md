---
name: image_to_image_lora_sampler_clip_36
type: Image To Image
frequency: 7
level: strong
coverage: 0.865
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/003.FLUX.2智能综合007.单-多图编辑_2035254506446917634.json, 图片生成/图生图/003.FLUX.2智能综合009.局部重绘-自动VS手动_2035256920365342722.json, 图片生成/图生图/003.FLUX.2智能综合011.多角度转换-精准_2035262837249024002.json, 图片生成/图生图/003.FLUX.2智能综合013.图像扩展_2035265927343771649.json, 图片生成/图生图/5.其他类型-06.NSF+-06.FLUX.2-007.flux-2-klein-特殊部位局重绘流_2026630078687354881.json, 图片生成/图生图/5.其他类型-06.NSF+-06.FLUX.2-009.flux-2-klein-图像扩展流_2026630120529731585.json, 图片生成/图生图/▶flux-2-klein-局部重绘流_2057425056413872130.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_36

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/003.FLUX.2智能综合007.单-多图编辑_2035254506446917634.json、图片生成/图生图/003.FLUX.2智能综合009.局部重绘-自动VS手动_2035256920365342722.json、图片生成/图生图/003.FLUX.2智能综合011.多角度转换-精准_2035262837249024002.json、图片生成/图生图/003.FLUX.2智能综合013.图像扩展_2035265927343771649.json、图片生成/图生图/5.其他类型-06.NSF+-06.FLUX.2-007.flux-2-klein-特殊部位局重绘流_2026630078687354881.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 6/7 个有
- `UnetLoaderGGUF` —— 6/7 个有
- `DrawMaskOnImage` —— 5/7 个有
- `EasySizeSimpleImage` —— 5/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `RAMCleanup` —— 4/7 个有
- `DifferentialDiffusion` —— 3/7 个有
- `INPAINT_ExpandMask` —— 3/7 个有
- `ImageCompositeMasked` —— 3/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `ImageScaleToTotalPixels` —— 3/7 个有
- `InpaintModelConditioning` —— 3/7 个有
- `ImagePadForOutpaint` —— 2/7 个有
- `CLIPLoaderGGUF` —— 1/7 个有
- `CR Prompt Text` —— 1/7 个有
- `CR Text Concatenate` —— 1/7 个有
- `ImageAndMaskPreview` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `QwenMultiangleCameraNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（10/7 个样本）：Steps较低可能导致细节不足
