---
name: unknown_workflow_upscale_clip_unet
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.533778
common_nodes: [CLIPTextEncode, GetNode, KOOK_ImageCompression, KOOK_SaveJPGImage, LayerFilter: HDREffects, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, ShowText|pysssss, StringFunction|pysssss, UNETLoader, VAELoader, easy imageChooser]
problems: []
missing: []
members: [图片生成/文生图/Z-IMAGE 文生图调整(反推_风格_放大_图像选择器_尺寸切换)_2027967002547064833.json, 图片生成/文生图/flux-2-klein-9b-KV-fp8  文生图  反推 高清放大 提示词优化_2032690780145459201.json, 图片生成/文生图/flux-2-klein-9b-fp8    文生图放大工作流 动态提示词，反推，扩写，图像选择_2012386672792571905.json, 图片生成/文生图/krea2 文生图双采样器生态完整文生图 高清放大 反推 扩写工作流_2076149806799613953.json, 图片生成/文生图/一键运行：boogu 文生图生态完整工作流（反推，扩写，图像选择，高清放大、图片压缩尺寸选择）_2070740330927972353.json, 图片生成/文生图/一键运行：krea2 风格迁移完整生态版 高清放大 提示词优化 反推 扩写 图像选择_2076116607008600065.json, 图片生成/文生图/一键运行：krea2文生图完整工作流（反推，扩写，图像选择，高清放大、图片压缩尺寸选择）_2070696632085213185.json, 图片生成/文生图/一键运行：最新 MIX krea2  融合模型 文生图 高清放大_2071082856201412610.json, 图片生成/文生图/一键运行：最新z-image  Enginee文生图优化 高清放大 发推 扩写 图像选择 图像压缩_2066036033258610689.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_unet

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Z-IMAGE 文生图调整(反推_风格_放大_图像选择器_尺寸切换)_2027967002547064833.json、图片生成/文生图/flux-2-klein-9b-KV-fp8  文生图  反推 高清放大 提示词优化_2032690780145459201.json、图片生成/文生图/flux-2-klein-9b-fp8    文生图放大工作流 动态提示词，反推，扩写，图像选择_2012386672792571905.json、图片生成/文生图/krea2 文生图双采样器生态完整文生图 高清放大 反推 扩写工作流_2076149806799613953.json、图片生成/文生图/一键运行：boogu 文生图生态完整工作流（反推，扩写，图像选择，高清放大、图片压缩尺寸选择）_2070740330927972353.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `GetNode`
- `KOOK_ImageCompression`
- `KOOK_SaveJPGImage`
- `LayerFilter: HDREffects`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAELoader`
- `easy imageChooser`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 8/9 个有
- `CLIPLoader` —— 8/9 个有
- `CR Seed` —— 8/9 个有
- `CR Text Input Switch (4 way)` —— 8/9 个有
- `Fast Groups Bypasser (rgthree)` —— 8/9 个有
- `KSampler (Efficient)` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `PromptExpand` —— 8/9 个有
- `ResolutionMaster` —— 8/9 个有
- `Text Multiline` —— 8/9 个有
- `ImageCaptionNode` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `ConditioningZeroOut` —— 6/9 个有
- `EmptySD3LatentImage` —— 6/9 个有
- `LatentSwitch` —— 6/9 个有
- `MultiImageLoader` —— 6/9 个有
- `SaveImage` —— 6/9 个有
- `Label (rgthree)` —— 5/9 个有
- `LoadImage` —— 4/9 个有
- `Text Concatenate` —— 3/9 个有
- `easy stylesSelector` —— 3/9 个有
- `DPMagicPrompt` —— 2/9 个有
- `Krea2T-Enhancer-Advanced` —— 2/9 个有
- `SeedVarianceEnhancer` —— 2/9 个有
- `ClipLoaderGGUF` —— 1/9 个有
- `ConditioningKrea2Rebalance` —— 1/9 个有
- `EmptyFlux2LatentImage` —— 1/9 个有
- `FluxKVCache` —— 1/9 个有
- `KSampler Adv. (Efficient)` —— 1/9 个有
- `Krea2StyleReference` —— 1/9 个有
- `Krea2StyleTransfer` —— 1/9 个有
- `LayerUtility: ImageReel` —— 1/9 个有
- `LayerUtility: ImageReelComposit` —— 1/9 个有
- `StylePromptEncoder2 //ZImagePowerNodes` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 9 | 8 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 12 | 9 | 0% |
| 采样算法 | euler_ancestral | - | 9 | 33% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 9，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 12，9 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler_ancestral，9 个样本，一致性 33%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
