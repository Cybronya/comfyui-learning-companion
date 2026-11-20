---
name: unknown_workflow_sampler_clip_unet_155
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.718556
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/MOSS sft Comfyui官方工作流_2112732679153209345.json, 图片生成/图生图/Moss-image+Base文生图高质量加速版V2(Un版)_2112816236777267202.json, 图片生成/图生图/Moss-image+SFT文生图高质量加速版V2(Un版)_2112816043226918914.json, 图片生成/图生图/flux3_klein_多参考_2111077778098573313.json, 图片生成/图生图/flux3_klein图片编辑_2112072362408628226.json, 图片生成/图生图/图像编辑 FLUX 3 Image Klein（官方版）_2112793727075971074.json, 图片生成/图生图/图像编辑 FLUX 3 Image Klein（官方版）_2113091207365742593.json, 图片生成/文生图/Moss-image SFT-观澜（Kook）文生图高质量加速版V2(Un版-可选图像参考)_2113321165979734017.json, 图片生成/文生图/图像编辑 FLUX 3 Image Klein_2112063690060156930.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_155

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/MOSS sft Comfyui官方工作流_2112732679153209345.json、图片生成/图生图/Moss-image+Base文生图高质量加速版V2(Un版)_2112816236777267202.json、图片生成/图生图/Moss-image+SFT文生图高质量加速版V2(Un版)_2112816043226918914.json、图片生成/图生图/flux3_klein_多参考_2111077778098573313.json、图片生成/图生图/flux3_klein图片编辑_2112072362408628226.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 8/9 个有
- `LoadImage` —— 7/9 个有
- `ResolutionSelector` —— 6/9 个有
- `ComfySwitchNode` —— 5/9 个有
- `ReferenceMultiLatent` —— 5/9 个有
- `TextGenerate` —— 5/9 个有
- `BatchImagesNode` —— 4/9 个有
- `MOSSImageBlockCacheT8` —— 3/9 个有
- `MOSSImagePromptEnhancerT8` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `easy showAnything` —— 2/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `PrimitiveBoolean` —— 1/9 个有
- `SkipLayerGuidanceDiTSimple` —— 1/9 个有
- `Text` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 16 - 50 | 9 | 75% |
| Prompt 约束强度(CFG) | 3 | 1 - 3.5 | 9 | 65% |
| 采样算法 | euler | - | 9 | 56% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 16 - 50，9 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3.5，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 56%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
