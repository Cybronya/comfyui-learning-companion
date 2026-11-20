---
name: unknown_workflow_inpaint_sampler_clip_12
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8906
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/4.flux-fill+seg去水印_1997528297493958657.json, 图片生成/图生图/FLUX FILL去水印_1906693352803250178.json, 图片生成/图生图/FLUX局部重绘无痕一键生成_1917067321331093506.json, 图片生成/图生图/FLUX局部重绘（无痕）_1901904713074548737.json, 图片生成/图生图/Flux-fill-Oneward万物移除工作流_1986678175293992961.json, 图片生成/图生图/FluxFillOneward万物移除-去掉neo机器人_1986905534173523969.json, 图片生成/图生图/flux_dev_fill_局部重绘_1960248886801674241.json, 图片生成/图生图/flux自动修手，不用画遮罩_2018505151610363906.json, 图片生成/图生图/【修手】FLUX手指手部超强修复_1953386504909410306.json, 平台全量/Flux-OneReward（万物移除工作流）_2015005874351247361.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/4.flux-fill+seg去水印_1997528297493958657.json、图片生成/图生图/FLUX FILL去水印_1906693352803250178.json、图片生成/图生图/FLUX局部重绘无痕一键生成_1917067321331093506.json、图片生成/图生图/FLUX局部重绘（无痕）_1901904713074548737.json、图片生成/图生图/Flux-fill-Oneward万物移除工作流_1986678175293992961.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 9/10 个有
- `Image Comparer (rgthree)` —— 9/10 个有
- `ConditioningZeroOut` —— 8/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `GrowMaskWithBlur` —— 4/10 个有
- `ImageAndMaskPreview` —— 4/10 个有
- `Mask Fill Holes` —— 4/10 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `RH_Translator` —— 3/10 个有
- `CLIPTextEncode (NSP)` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `MaskToImage` —— 2/10 个有
- `AddMask` —— 1/10 个有
- `ImageScaleToTotalPixels` —— 1/10 个有
- `MaskPreview+` —— 1/10 个有
- `SeedVR2LoadDiTModel` —— 1/10 个有
- `SeedVR2LoadVAEModel` —— 1/10 个有
- `SeedVR2VideoUpscaler` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `easy imageSize` —— 1/10 个有
- `easy seed` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 28 | 10 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | beta | - | 10 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 28，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
