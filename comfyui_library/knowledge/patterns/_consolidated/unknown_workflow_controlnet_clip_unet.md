---
name: unknown_workflow_controlnet_clip_unet
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.884636
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-lmage-Turbo-Fun-Controlnet(支持多种条件控制)_1996163380232830977.json, 图片生成/图生图/z-image-turbo_fun_controlnet2.0_2000859546035814402.json, 图片生成/图生图/z-image-turbo_fun_controlnet_base_1996418811291115522.json, 图片生成/图生图/z-image-turbo_fun_controlnet_qwenvl_1996420678859497473.json, 图片生成/图生图/z-image-turbo_fun_controlnet_v2.0_1996424354097414146.json, 图片生成/图生图/z-image-turbo_图生图姿态控制_2048304144070479873.json, 图片生成/图生图/千问文字渲染_QWen-Image线稿Canny控制ComfyUI官方_1958771497777197058.json, 图片生成/图生图/千问深度Depth控制_QWen-Image-ComfyUI官方_1958744331945402370.json, 图片生成/图生图/千问线稿Canny控制-QWen-Image-ComfyUI官方_1958717419227344898.json, 图片生成/文生图/SMB根据线稿出图_2019382085378641922.json, 图片生成/文生图/z-image-深度图_1996814449833123841.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_clip_unet

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Z-lmage-Turbo-Fun-Controlnet(支持多种条件控制)_1996163380232830977.json、图片生成/图生图/z-image-turbo_fun_controlnet2.0_2000859546035814402.json、图片生成/图生图/z-image-turbo_fun_controlnet_base_1996418811291115522.json、图片生成/图生图/z-image-turbo_fun_controlnet_qwenvl_1996420678859497473.json、图片生成/图生图/z-image-turbo_fun_controlnet_v2.0_1996424354097414146.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 10/11 个有
- `ConditioningZeroOut` —— 8/11 个有
- `KSamplerAdvanced` —— 6/11 个有
- `DJZImageScaleToTotalPixels` —— 5/11 个有
- `KSampler` —— 5/11 个有
- `ImageStitch` —— 4/11 个有
- `ImageScaleDownToSize` —— 3/11 个有
- `ImageScaleToTotalPixels` —— 3/11 个有
- `LoraLoaderModelOnly` —— 3/11 个有
- `Text Multiline` —— 3/11 个有
- `AILab_QwenVL` —— 2/11 个有
- `CR Image Input Switch (4 way)` —— 1/11 个有
- `JWInteger` —— 1/11 个有
- `LayerUtility: PurgeVRAM` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 11 | 45% |
| Prompt 约束强度(CFG) | 8 | 1 - 10 | 11 | 39% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 11 | 55% |
| 重绘幅度 | simple | - | 11 | 55% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，11 个样本，一致性 45%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 10，11 个样本，取值分散，一致性仅 39%
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，11 个样本，一致性 55%
- 重绘幅度 最常用 simple，11 个样本，一致性 55%
