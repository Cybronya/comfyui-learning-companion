---
name: image_to_image_lora_sampler_unet_73
type: Image To Image
frequency: 8
level: moderate
coverage: 0.993375
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image Edit 2511-万物一键三视图_2005152885329588225.json, 图片生成/图生图/Qwen Image Edit 2511-三视图_2004960784432201729.json, 图片生成/图生图/Qwen Image Edit2511 -改变角度_2033741078267957249.json, 图片生成/图生图/Qwen Multiangle 千问多角度一致性工作流_1953384744518123521.json, 图片生成/图生图/Qwen Multiangle 千问多角度一致性工作流_2052365470401089538.json, 图片生成/图生图/Qwen-Edit-2511 多视角效果转换工作流_2038916153908666369.json, 图片生成/图生图/Qwen-Edit-2511-图片无限多视角转换_2011064723831263234.json, 图片生成/图生图/QwenEdit-图生图工作流_2095499580333973505.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_73

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Image Edit 2511-万物一键三视图_2005152885329588225.json、图片生成/图生图/Qwen Image Edit 2511-三视图_2004960784432201729.json、图片生成/图生图/Qwen Image Edit2511 -改变角度_2033741078267957249.json、图片生成/图生图/Qwen Multiangle 千问多角度一致性工作流_1953384744518123521.json、图片生成/图生图/Qwen Multiangle 千问多角度一致性工作流_2052365470401089538.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenMultiangleCameraNode` —— 5/8 个有
- `ImageScaleToTotalPixels` —— 4/8 个有
- `KepStringList` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `ImageBatch` —— 2/8 个有
- `ImageConcatFromBatch` —— 2/8 个有
- `ImageListToBatch+` —— 2/8 个有
- `ImageUpscaleWithModel` —— 2/8 个有
- `UpscaleModelLoader` —— 2/8 个有
- `easy promptList` —— 2/8 个有
- `FluxKontextImageScale` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `VAEEncodeTiled` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 8 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 0.4 - 1 | 8 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，8 个样本
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
