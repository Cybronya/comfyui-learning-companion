---
name: image_to_image_sampler_clip_unet_78
type: Image To Image
frequency: 6
level: strong
coverage: 0.939167
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/fluxkontext_一键生成字效_1929844250890944514.json, 图片生成/图生图/kontext单图_1938771721912508418.json, 图片生成/图生图/kontext单图_1981602295718789122.json, 图片生成/图生图/kontext官方工作流 双图编辑模式_1938780307606982657.json, 图片生成/图生图/三视图_Kontext-Dev_1944234284179918849.json, 图片生成/图生图/旧照片精准修复+放大_1992858360515022850.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_78

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/fluxkontext_一键生成字效_1929844250890944514.json、图片生成/图生图/kontext单图_1938771721912508418.json、图片生成/图生图/kontext单图_1981602295718789122.json、图片生成/图生图/kontext官方工作流 双图编辑模式_1938780307606982657.json、图片生成/图生图/三视图_Kontext-Dev_1944234284179918849.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
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
- `ConditioningZeroOut` —— 5/6 个有
- `FluxKontextImageScale` —— 5/6 个有
- `RH_Translator` —— 5/6 个有
- `ConstrainImage|pysssss` —— 4/6 个有
- `PreviewImage` —— 3/6 个有
- `easy imageConcat` —— 3/6 个有
- `ImageUpscaleWithModel` —— 2/6 个有
- `UpscaleModelLoader` —— 2/6 个有
- `ImageResize` —— 1/6 个有
- `JWImageResizeByLongerSide` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `ShowText` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 26 | 6 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 26，6 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
