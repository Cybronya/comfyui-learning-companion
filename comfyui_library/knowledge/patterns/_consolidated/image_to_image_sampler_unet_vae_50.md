---
name: image_to_image_sampler_unet_vae_50
type: Image To Image
frequency: 6
level: weak
coverage: 0.9495
common_nodes: [CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/成图以后再次bfs edit qwen 2511换脸_2034920099492143105.json, 图片生成/图生图/简单极速图片去水印_2027576063118811138.json, 图片生成/图生图/🔥Qwen Image Edit多角度相机控制：拖拽手柄即可生成96种摄像机角度_2010767191389507586.json, 平台全量/全量qwen edit 2512单图编辑工作流_2068303224184074241.json, 平台全量/千问图片局部修改_换背景_2059170170379268098.json, 视频生成/图生视频/Qwen  2511 去水印_2039186389039845377.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_50

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/成图以后再次bfs edit qwen 2511换脸_2034920099492143105.json、图片生成/图生图/简单极速图片去水印_2027576063118811138.json、图片生成/图生图/🔥Qwen Image Edit多角度相机控制：拖拽手柄即可生成96种摄像机角度_2010767191389507586.json、平台全量/全量qwen edit 2512单图编辑工作流_2068303224184074241.json、平台全量/千问图片局部修改_换背景_2059170170379268098.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `ModelSamplingAuraFlow` —— 5/6 个有
- `FluxKontextImageScale` —— 4/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `CR Prompt Text` —— 1/6 个有
- `ImageResize` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `QwenMultiangleCameraNode` —— 1/6 个有
- `RH_Nano_Banana_Image2Image` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `SeargePreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 40 | 6 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 25% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 40，6 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
