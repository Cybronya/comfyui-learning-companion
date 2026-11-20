---
name: image_to_image_lora_sampler_clip_120
type: Image To Image
frequency: 4
level: strong
coverage: 0.877
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConditioningZeroOut, EasyCache, FluxGuidance, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ReferenceLatent, SaveImage, USOStyleReference, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/文生图/字节跳动 USO ComfyUI 原生工作流_2069386592745250818.json, 平台全量/主体+风格参考（FLUX+USO+CN）主体一致+风格参考V1版本_1964147858997956609.json, 平台全量/字节USO风格参考-内容+风格参考-ComfyUI官方_1963599562907930626.json, 平台全量/工作流进阶功能篇4-字节跳动 USO ComfyUI 原生工作流_2036360135102177282.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_120

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/字节跳动 USO ComfyUI 原生工作流_2069386592745250818.json、平台全量/主体+风格参考（FLUX+USO+CN）主体一致+风格参考V1版本_1964147858997956609.json、平台全量/字节USO风格参考-内容+风格参考-ComfyUI官方_1963599562907930626.json、平台全量/工作流进阶功能篇4-字节跳动 USO ComfyUI 原生工作流_2036360135102177282.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EasyCache`
- `FluxGuidance`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ReferenceLatent`
- `SaveImage`
- `USOStyleReference`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/4 个有
- `ImageScaleToMaxDimension` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `ControlNetApplyAdvanced` —— 1/4 个有
- `ControlNetLoader` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `SetUnionControlNetType` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 0.8 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
