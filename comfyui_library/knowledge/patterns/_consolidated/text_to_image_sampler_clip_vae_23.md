---
name: text_to_image_sampler_clip_vae_23
type: Text To Image
frequency: 7
level: moderate
coverage: 0.947143
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/换装两种模式+身材调节！_2053010156153253889.json, 图片生成/图生图/服装穿搭：平铺视图生成_2021482132035608577.json, 图片生成/图生图/穿搭解析黑科技：ComfyUI服装平铺视图生成_1990362142790569985.json, 图片生成/图生图/穿搭解析黑科技：ComfyUI服装平铺视图生成_1995485264170639362.json, 图片生成/图生图/穿搭解析黑科技：ComfyUI服装平铺视图生成_2034849943915077633.json, 图片生成/图生图/穿搭解析黑科技：加载带人物图像，一键轻松提出人物身上服装 ， ComfyUI服装平铺视图生成_2029088439232106498.json, 图片生成/文生图/Kontext一键去水印前后对比工作流，文生图图生图去水印处理工具_2107559098299535361.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_23

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/换装两种模式+身材调节！_2053010156153253889.json、图片生成/图生图/服装穿搭：平铺视图生成_2021482132035608577.json、图片生成/图生图/穿搭解析黑科技：ComfyUI服装平铺视图生成_1990362142790569985.json、图片生成/图生图/穿搭解析黑科技：ComfyUI服装平铺视图生成_1995485264170639362.json、图片生成/图生图/穿搭解析黑科技：ComfyUI服装平铺视图生成_2034849943915077633.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 6/7 个有
- `LoraLoader` —— 6/7 个有
- `CLIPLoader` —— 2/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `UNETLoader` —— 2/7 个有
- `EmptyFlux2LatentImage` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `LazySwitch1way` —— 1/7 个有
- `PrimitiveBoolean` —— 1/7 个有
- `TTResolutionSelector` —— 1/7 个有
- `solarL_SaveImagesToZip` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 7 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 7 | 18% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 80 - 1024 | 7 | 63% |
| 高度 | 1536 | 80 - 1536 | 7 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，7 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 80 - 1024，7 个样本
- 高度 中位数 1536，观测区间 80 - 1536，7 个样本
