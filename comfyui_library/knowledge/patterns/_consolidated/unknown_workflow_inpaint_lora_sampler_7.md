---
name: unknown_workflow_inpaint_lora_sampler_7
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.8992
common_nodes: [CLIPLoader, ConditioningZeroOut, InpaintModelConditioning, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2511——局部重绘(4K直出)-改字_改图_无痕迹_2003712604600213506.json, 图片生成/图生图/Qwen2511——局部重绘(4K直出)-改字_改图_无痕迹_2061627000284078082.json, 图片生成/图生图/Qwen2511——局部重绘(4K直出)-改字_改图_无痕迹_2094263287616720898.json, 图片生成/图生图/Qwen2511局部重绘(4K直出)——改字_改图_消除_2042052010853273601.json, 图片生成/图生图/Qwen2511局部重绘原图尺寸贴回——适用于SDPPP替代创成式填充_2073349898552041473.json, 图片生成/图生图/Qwen_Rapid_局部重绘_2017588748258643969.json, 图片生成/图生图/qwen2511局部重绘-改字_改图_无痕迹_2057305907763179521.json, 图片生成/图生图/qwen2511局部重绘-改字_改图_无痕迹_2067954497997074434.json, "图片生成/图生图/神都猫缩头术,把头变小一点点_1988948880278556674.json", 图片生成/图生图/老孙AI Qwen2511局部重绘 原图贴回_2087044751177633794.json, 图片生成/图生图/蒙版重绘贴图替换（双图）_2024117929792507906.json, 平台全量/Qwen-Image-Edit-2511 局部重绘 _ 单图 _ 双图编辑工作流，合集_2003746404071841793.json, 平台全量/Qwen2511局部重绘_2099296821368680449.json, 平台全量/qwen2511局部重绘-duck_2088228575064449026.json, 平台全量/qwen2511局部重绘-改字_改图_无痕迹_2003631127782932482.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_7

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Qwen2511——局部重绘(4K直出)-改字_改图_无痕迹_2003712604600213506.json、图片生成/图生图/Qwen2511——局部重绘(4K直出)-改字_改图_无痕迹_2061627000284078082.json、图片生成/图生图/Qwen2511——局部重绘(4K直出)-改字_改图_无痕迹_2094263287616720898.json、图片生成/图生图/Qwen2511局部重绘(4K直出)——改字_改图_消除_2042052010853273601.json、图片生成/图生图/Qwen2511局部重绘原图尺寸贴回——适用于SDPPP替代创成式填充_2073349898552041473.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `InpaintCropImproved` —— 14/15 个有
- `InpaintStitchImproved` —— 14/15 个有
- `CFGNorm` —— 13/15 个有
- `ModelSamplingAuraFlow` —— 13/15 个有
- `PreviewImage` —— 13/15 个有
- `CR Text` —— 12/15 个有
- `MaskPreview+` —— 12/15 个有
- `Image Comparer (rgthree)` —— 5/15 个有
- `PrimitiveFloat` —— 3/15 个有
- `MaskBlur+` —— 2/15 个有
- `DuckHideNode` —— 1/15 个有
- `EmptySD3LatentImage` —— 1/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/15 个有
- `GrowMask` —— 1/15 个有
- `ImageResizeKJv2` —— 1/15 个有
- `LayerMask: PersonMaskUltra V2` —— 1/15 个有
- `Text` —— 1/15 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 15 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（14/15 个样本）：Steps较低可能导致细节不足
