---
name: text_to_image_controlnet_sampler_clip_6
type: Text To Image
frequency: 6
level: strong
coverage: 0.915667
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetImageSize, ImageConcanate, ImageScaleToTotalPixels, KSampler, LoadImage, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z+Controlnet姿势控制_1996144706801352706.json, 图片生成/图生图/Z-image Controlnet Uion 2.1_2000500536866635778.json, 图片生成/图生图/Z-image Controlnet+lora起效工作流_1996843101358628866.json, 图片生成/图生图/文生图Zimage文生图动作迁移Controlnet+lora(支持cn和lora)加速版_1996857207276851202.json, 图片生成/图生图/🍧Z-image 爆图小钢炮 CN控制🍧_1996449727271018498.json, 图片生成/文生图/Z-Image文生图Controlnet+lora(支持cn和lora)加速版_2003393632608686082.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Z+Controlnet姿势控制_1996144706801352706.json、图片生成/图生图/Z-image Controlnet Uion 2.1_2000500536866635778.json、图片生成/图生图/Z-image Controlnet+lora起效工作流_1996843101358628866.json、图片生成/图生图/文生图Zimage文生图动作迁移Controlnet+lora(支持cn和lora)加速版_1996857207276851202.json、图片生成/图生图/🍧Z-image 爆图小钢炮 CN控制🍧_1996449727271018498.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize`
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 5/6 个有
- `UpscaleModelLoader` —— 5/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `AILab_QwenVL` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageSharpen` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1080 | 6 | 97% |
| 高度 | 1536 | 1536 - 1536 | 6 | 100% |
| 采样步数 | 10 | 10 - 10 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.75 | 0.6 - 1 | 6 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1080，6 个样本，取值集中（一致性 97%）
- 高度 中位数 1536，观测区间 1536 - 1536，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.75，观测区间 0.6 - 1，6 个样本，取值集中（一致性 82%）
