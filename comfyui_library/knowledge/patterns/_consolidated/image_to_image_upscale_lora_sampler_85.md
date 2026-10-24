---
name: image_to_image_upscale_lora_sampler_85
type: Image To Image
frequency: 2
level: weak
coverage: 0.8715
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSize, ImageScale, ImageUpscaleWithModel, KSampler, LayerUtility: BooleanOperatorV2, LayerUtility: If , LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RH_Captioner, SaveImage, SeargeIntegerConstant, ShowText|pysssss, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageScaleDownToSize, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/wan2.2重绘细化 api 最长边 2560_1955465383026180097.json, 图片生成/图生图/wan2.2重绘细化 api_1955513237255196674.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_85

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/wan2.2重绘细化 api 最长边 2560_1955465383026180097.json、图片生成/图生图/wan2.2重绘细化 api_1955513237255196674.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSize`
- `ImageScale`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: If `
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RH_Captioner`
- `SaveImage`
- `SeargeIntegerConstant`
- `ShowText|pysssss`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageScaleDownToSize`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 1/2 个有
- `LayerUtility: GetImageSize` —— 1/2 个有
- `easy float` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | kl_optimal | - | 2 | 100% |
| 重绘幅度 | 0.2 | - | 2 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 kl_optimal，2 个样本，一致性 100%
- 重绘幅度 中位数 0.2，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
