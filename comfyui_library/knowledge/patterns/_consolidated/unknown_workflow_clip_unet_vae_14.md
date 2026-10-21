---
name: unknown_workflow_clip_unet_vae_14
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.801667
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1977636661217632258.json, 图片生成/文生图/killer Qwen image出图+Contronet+反推+4K修复v2.0_1999339009170079745.json, 图片生成/文生图/killer Z image出图+Contronet+Minicpmv4.5反推+4K放大v1.0_2002006378497622017.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_14

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1977636661217632258.json、图片生成/文生图/killer Qwen image出图+Contronet+反推+4K修复v2.0_1999339009170079745.json、图片生成/文生图/killer Z image出图+Contronet+Minicpmv4.5反推+4K放大v1.0_2002006378497622017.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplyAdvanced` —— 2/3 个有
- `ControlNetLoader` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `KSampler` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `MiniCPM_VQA` —— 2/3 个有
- `SeedVR2LoadDiTModel` —— 2/3 个有
- `SeedVR2LoadVAEModel` —— 2/3 个有
- `SeedVR2VideoUpscaler` —— 2/3 个有
- `SetUnionControlNetType` —— 2/3 个有
- `FSampler` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `ModelPatchLoader` —— 1/3 个有
- `QwenImageDiffsynthControlnet` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | - | 2 | 75% |
| 采样步数 | 15 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1.75 | - | 2 | 57% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.8，样本不足，未给区间，2 个样本
- 采样步数 中位数 15，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1.75，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
