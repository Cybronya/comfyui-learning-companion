---
name: unknown_workflow_sampler_clip_unet_67
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.928308
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/003.FLUX.2智能综合001.lora文生图_2035170208612098050.json, 图片生成/文生图/2031285736095358978.json, 图片生成/文生图/ComfyUI Z-Image-Turbo工作流详解｜8步照片级出图+中英文文字渲染+全节点注释_2059594391173554177.json, 图片生成/文生图/EDGE OF QWEN文生图工作流_1957357556198993922.json, 图片生成/文生图/ERNIE 满血版+Turbo版两条工作流，百度大模型_2055111279836180481.json, 图片生成/文生图/ERNIE-Image-Turbo（文生图）_2045418640316567553.json, 图片生成/文生图/ERNIE文生图_2048690063034294273.json, 图片生成/文生图/Erine Turbo文生图_2044755147204599809.json, 图片生成/文生图/Flux2 Klein 文生图9B_10秒出图_2012086959107219458.json, 图片生成/文生图/Flux2_Klein 文生图9B版-官方版-4步_2012020314640748545.json, 图片生成/文生图/Qwen Image 2512 平铺商品摄影｜LoRA 商品棚拍_2091542940056375297.json, 图片生成/文生图/Qwen Image+Lora文生图-K采样器版本_1955444043092299778.json, 图片生成/文生图/Qwen-image局部重绘_1956259506659446786.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_67

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/003.FLUX.2智能综合001.lora文生图_2035170208612098050.json、图片生成/文生图/2031285736095358978.json、图片生成/文生图/ComfyUI Z-Image-Turbo工作流详解｜8步照片级出图+中英文文字渲染+全节点注释_2059594391173554177.json、图片生成/文生图/EDGE OF QWEN文生图工作流_1957357556198993922.json、图片生成/文生图/ERNIE 满血版+Turbo版两条工作流，百度大模型_2055111279836180481.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/13 个有
- `EmptyFlux2LatentImage` —— 8/13 个有
- `EmptySD3LatentImage` —— 4/13 个有
- `LoadImage` —— 4/13 个有
- `LoraLoader` —— 4/13 个有
- `ModelSamplingAuraFlow` —— 4/13 个有
- `CR Text` —— 3/13 个有
- `Fast Groups Muter (rgthree)` —— 1/13 个有
- `ImageResizeKJv2` —— 1/13 个有
- `InpaintModelConditioning` —— 1/13 个有
- `JjkText` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 8 | 4 - 50 | 13 | 17% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 13 | 31% |
| 采样算法 | euler | - | 13 | 85% |
| 调度器 | simple | - | 13 | 77% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 4 - 50，13 个样本，取值分散，一致性仅 17%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，13 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler，13 个样本，一致性 85%
- 调度器 最常用 simple，13 个样本，一致性 77%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（9/13 个样本）：Steps较低可能导致细节不足
