---
name: unknown_workflow_upscale_lora_clip_2
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.533375
common_nodes: [CLIPTextEncode, GetNode, KOOK_ImageCompression, KOOK_SaveJPGImage, LayerFilter: HDREffects, LoraLoaderModelOnly, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, ShowText|pysssss, StringFunction|pysssss, UNETLoader, VAELoader, easy imageChooser]
problems: []
missing: []
members: [图片生成/文生图/Z-IMAGE 文生图调整(反推_风格_放大_图像选择器_尺寸切换)_2027967002547064833.json, 图片生成/文生图/flux-2-klein-9b-fp8    文生图放大工作流 动态提示词，反推，扩写，图像选择_2012386672792571905.json, 图片生成/文生图/krea2 文生图双采样器生态完整文生图 高清放大 反推 扩写工作流_2076149806799613953.json, 图片生成/文生图/一键运行：boogu 文生图生态完整工作流（反推，扩写，图像选择，高清放大、图片压缩尺寸选择）_2070740330927972353.json, 图片生成/文生图/一键运行：krea2 风格迁移完整生态版 高清放大 提示词优化 反推 扩写 图像选择_2076116607008600065.json, 图片生成/文生图/一键运行：krea2文生图完整工作流（反推，扩写，图像选择，高清放大、图片压缩尺寸选择）_2070696632085213185.json, 图片生成/文生图/一键运行：最新 MIX krea2  融合模型 文生图 高清放大_2071082856201412610.json, 图片生成/文生图/一键运行：最新z-image  Enginee文生图优化 高清放大 发推 扩写 图像选择 图像压缩_2066036033258610689.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_clip_2

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Z-IMAGE 文生图调整(反推_风格_放大_图像选择器_尺寸切换)_2027967002547064833.json、图片生成/文生图/flux-2-klein-9b-fp8    文生图放大工作流 动态提示词，反推，扩写，图像选择_2012386672792571905.json、图片生成/文生图/krea2 文生图双采样器生态完整文生图 高清放大 反推 扩写工作流_2076149806799613953.json、图片生成/文生图/一键运行：boogu 文生图生态完整工作流（反推，扩写，图像选择，高清放大、图片压缩尺寸选择）_2070740330927972353.json、图片生成/文生图/一键运行：krea2 风格迁移完整生态版 高清放大 提示词优化 反推 扩写 图像选择_2076116607008600065.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `GetNode`
- `KOOK_ImageCompression`
- `KOOK_SaveJPGImage`
- `LayerFilter: HDREffects`
- `LoraLoaderModelOnly`
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
- `AILab_QwenVL` —— 7/8 个有
- `CLIPLoader` —— 7/8 个有
- `CR Seed` —— 7/8 个有
- `CR Text Input Switch (4 way)` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 7/8 个有
- `ImageCaptionNode` —— 7/8 个有
- `KSampler (Efficient)` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `PromptExpand` —— 7/8 个有
- `ResolutionMaster` —— 7/8 个有
- `Text Multiline` —— 7/8 个有
- `EmptySD3LatentImage` —— 6/8 个有
- `LatentSwitch` —— 6/8 个有
- `MultiImageLoader` —— 6/8 个有
- `SaveImage` —— 6/8 个有
- `ConditioningZeroOut` —— 5/8 个有
- `Label (rgthree)` —— 5/8 个有
- `LoadImage` —— 3/8 个有
- `Krea2T-Enhancer-Advanced` —— 2/8 个有
- `SeedVarianceEnhancer` —— 2/8 个有
- `Text Concatenate` —— 2/8 个有
- `easy stylesSelector` —— 2/8 个有
- `ClipLoaderGGUF` —— 1/8 个有
- `ConditioningKrea2Rebalance` —— 1/8 个有
- `DPMagicPrompt` —— 1/8 个有
- `EmptyFlux2LatentImage` —— 1/8 个有
- `KSampler Adv. (Efficient)` —— 1/8 个有
- `Krea2StyleReference` —— 1/8 个有
- `Krea2StyleTransfer` —— 1/8 个有
- `LayerUtility: ImageReel` —— 1/8 个有
- `LayerUtility: ImageReelComposit` —— 1/8 个有
- `StylePromptEncoder2 //ZImagePowerNodes` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 9 | 7 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 12 | 8 | 0% |
| 采样算法 | euler_ancestral | - | 8 | 38% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 9，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 12，8 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler_ancestral，8 个样本，一致性 38%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
