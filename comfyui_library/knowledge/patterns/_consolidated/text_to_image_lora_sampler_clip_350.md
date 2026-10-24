---
name: text_to_image_lora_sampler_clip_350
type: Text To Image
frequency: 5
level: strong
coverage: 0.9182
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, SaveImage, USOStyleReference, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/USO原图是风格图＋提示词根据风格生成_1965057299112935425.json, 图片生成/图生图/字节USO风格参考-仅风格参考-ComfyUI官方_1963231601104752642.json, 图片生成/文生图/USO ComfyUI版本文生图_1963393267503181826.json, 图片生成/文生图/字节USO参考风格生成图片工作流_1967842885922095105.json, 图片生成/文生图/风格转绘-字节USO最新模型（文生图）_1964534917965168641.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_350

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/USO原图是风格图＋提示词根据风格生成_1965057299112935425.json、图片生成/图生图/字节USO风格参考-仅风格参考-ComfyUI官方_1963231601104752642.json、图片生成/文生图/USO ComfyUI版本文生图_1963393267503181826.json、图片生成/文生图/字节USO参考风格生成图片工作流_1967842885922095105.json、图片生成/文生图/风格转绘-字节USO最新模型（文生图）_1964534917965168641.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `SaveImage`
- `USOStyleReference`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `EasyCache` —— 4/5 个有
- `PreviewImage` —— 3/5 个有
- `RH_Translator` —— 3/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `GetImageSizeAndCount` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `Text` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
