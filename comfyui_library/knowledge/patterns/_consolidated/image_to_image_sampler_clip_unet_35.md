---
name: image_to_image_sampler_clip_unet_35
type: Image To Image
frequency: 10
level: strong
coverage: 0.9508
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千府AI-FLUX Kontext 图片去水印工作流_1929384205183041538.json, 图片生成/图生图/印花提取-商业级 Flux.1 Kontext_2103519336425156610.json, 图片生成/图生图/印花提取-商业级 Flux.1 Kontext_2104433739911745537.json, 图片生成/图生图/印花提取-商业级_Flux.1_Kontext_2108385501811142658.json, 图片生成/图生图/印花提取-商业级_Flux.1_Kontext_2109826006751203329.json, 图片生成/图生图/去水印_水印去除-kontext_1963971515945504769.json, 图片生成/图生图/喜怒哀乐表情包_1949755739474714626.json, 图片生成/图生图/图像高精度去水印与无损修复_2057742605227741185.json, 图片生成/图生图/基础kontext工作流_2005321098000560130.json, 图片生成/图生图/第一个廖先生 图像拼接与融合（Kontext&老杨lora）_1970882716461867010.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_35

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/千府AI-FLUX Kontext 图片去水印工作流_1929384205183041538.json、图片生成/图生图/印花提取-商业级 Flux.1 Kontext_2103519336425156610.json、图片生成/图生图/印花提取-商业级 Flux.1 Kontext_2104433739911745537.json、图片生成/图生图/印花提取-商业级_Flux.1_Kontext_2108385501811142658.json、图片生成/图生图/印花提取-商业级_Flux.1_Kontext_2109826006751203329.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 7/10 个有
- `LoraLoaderModelOnly` —— 7/10 个有
- `Image Comparer (rgthree)` —— 3/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `ImageConcanate` —— 2/10 个有
- `RH_Translator` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `ImageResizeKJ` —— 1/10 个有
- `JoinStringMulti` —— 1/10 个有
- `LayerMask: LoadFlorence2Model` —— 1/10 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/10 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `Text Multiline` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 10 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
