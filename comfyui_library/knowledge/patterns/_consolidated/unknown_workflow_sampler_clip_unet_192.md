---
name: unknown_workflow_sampler_clip_unet_192
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.812143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PrimitiveStringMultiline, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Moss-image+Base文生图高质量加速版V2(Un版)_2112816236777267202.json, 图片生成/图生图/Moss-image+SFT文生图高质量加速版V2(Un版)_2112816043226918914.json, 图片生成/图生图/flux3_klein_多参考_2111077778098573313.json, 图片生成/文生图/Moss-Base文生图_2112960420595195905.json, 图片生成/文生图/Moss-Sft文生图-极简_2112960408704339969.json, 图片生成/文生图/Moss-image SFT-观澜（Kook）文生图高质量加速版V2(Un版-可选图像参考)_2113321165979734017.json, 图片生成/文生图/提示词优化Moss-image Base文生图高质量加速版20261022_2112951536082051073.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_192

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Moss-image+Base文生图高质量加速版V2(Un版)_2112816236777267202.json、图片生成/图生图/Moss-image+SFT文生图高质量加速版V2(Un版)_2112816043226918914.json、图片生成/图生图/flux3_klein_多参考_2111077778098573313.json、图片生成/文生图/Moss-Base文生图_2112960420595195905.json、图片生成/文生图/Moss-Sft文生图-极简_2112960408704339969.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MOSSImageBlockCacheT8` —— 4/7 个有
- `MOSSImagePromptEnhancerT8` —— 4/7 个有
- `PreviewAny` —— 4/7 个有
- `LoadImage` —— 3/7 个有
- `easy showAnything` —— 2/7 个有
- `ComfySwitchNode` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `PrimitiveBoolean` —— 1/7 个有
- `ReferenceMultiLatent` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 16 - 50 | 7 | 63% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 7 | 74% |
| 采样算法 | er_sde | - | 7 | 71% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 16 - 50，7 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，7 个样本
- 采样算法 最常用 er_sde，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
