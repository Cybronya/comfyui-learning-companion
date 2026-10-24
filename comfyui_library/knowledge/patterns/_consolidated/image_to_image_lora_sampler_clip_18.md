---
name: image_to_image_lora_sampler_clip_18
type: Image To Image
frequency: 11
level: strong
coverage: 0.864091
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConditioningZeroOut, EasyCache, FluxGuidance, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ReferenceLatent, SaveImage, USOStyleReference, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/USO ComfyUI版本图生图_1963415918892257281.json, 图片生成/图生图/USO风格参考_角色一致性(图生图)_1963224410264145921.json, 图片生成/图生图/字节USO ComfyUI风格整合_2043593991303733249.json, 图片生成/图生图/字节USO风格参考-内容+风格参考-ComfyUI官方_1963233819048521730.json, 图片生成/图生图/字节跳动 USO ComfyUI 原生工作流_1967038413457199105.json, 图片生成/图生图/字节跳动 USO ComfyUI 原生工作流_2022224921887248386.json, 图片生成/图生图/风格转绘-字节USO最新模型（图生图）_1964287098624819202.json, 图片生成/文生图/HeGenAI-字节-USO-风格主题混合迁移_1964700301171245058.json, 图片生成/文生图/HeGenAI-字节-USO-风格主题迁移_1964700278945628161.json, 图片生成/文生图/字节USO主体和风格混合参考工作流_1967842931103137793.json, 图片生成/文生图/字节USO参考主体生成图片工作流_1967842899364839426.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/USO ComfyUI版本图生图_1963415918892257281.json、图片生成/图生图/USO风格参考_角色一致性(图生图)_1963224410264145921.json、图片生成/图生图/字节USO ComfyUI风格整合_2043593991303733249.json、图片生成/图生图/字节USO风格参考-内容+风格参考-ComfyUI官方_1963233819048521730.json、图片生成/图生图/字节跳动 USO ComfyUI 原生工作流_1967038413457199105.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
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
- `EmptySD3LatentImage` —— 9/11 个有
- `ImageScaleToMaxDimension` —— 9/11 个有
- `PreviewImage` —— 4/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/11 个有
- `RH_Captioner` —— 3/11 个有
- `CR Text` —— 2/11 个有
- `ImageScaleToTotalPixels` —— 2/11 个有
- `ImageStitch` —— 2/11 个有
- `ImpactInt` —— 2/11 个有
- `ImpactSwitch` —— 2/11 个有
- `ShowText|pysssss` —— 2/11 个有
- `easy int` —— 2/11 个有
- `DeepTranslatorTextNode` —— 1/11 个有
- `GetImageSize` —— 1/11 个有
- `ImageConcatMulti` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 0.9 - 1 | 11 | 97% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，11 个样本，取值集中（一致性 97%）
