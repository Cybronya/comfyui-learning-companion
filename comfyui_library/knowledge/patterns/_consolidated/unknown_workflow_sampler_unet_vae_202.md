---
name: unknown_workflow_sampler_unet_vae_202
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.845571
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1自助捏脸生成人物肖像资产_2111410566211391490.json, 图片生成/文生图/Qwen+Image+2.1 PE  文生图+图像编辑_两用_2116426276004261889.json, 图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2109541250159435778.json, 图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2112360202447187970.json, 图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2112365438872154113.json, 视频生成/文生视频/Qwen-Image-2.1-Turbo_7步_亚洲人像文生图_2115237969480212481.json, 视频生成/文生视频/Qwen-Image-2.1-Turbo_7步_亚洲人像文生图_2115246146347159554.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_202

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1自助捏脸生成人物肖像资产_2111410566211391490.json、图片生成/文生图/Qwen+Image+2.1 PE  文生图+图像编辑_两用_2116426276004261889.json、图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2109541250159435778.json、图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2112360202447187970.json、图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2112365438872154113.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 6/7 个有
- `QwenPERewriteT8` —— 6/7 个有
- `Color Grading JK` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `孤海注释` —— 2/7 个有
- `FacialCustomization` —— 1/7 个有
- `Int` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `QwenImage21_T2IPromptRewrite` —— 1/7 个有
- `SaveImageAdvanced` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |
| 采样步数 | 7 | 7 - 40 | 7 | 9% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 7，观测区间 7 - 40，7 个样本，取值分散，一致性仅 9%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足
