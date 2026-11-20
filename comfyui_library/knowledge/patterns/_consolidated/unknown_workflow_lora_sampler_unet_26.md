---
name: unknown_workflow_lora_sampler_unet_26
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.953167
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2511单图参考编辑_bf16-基础工作流_2076904369496346625.json, 图片生成/图生图/FireRed-Image-Edit + OpenClaw：打造高考倒计时大屏，每天自动生成不重样！_2025468706289094658.json, 图片生成/图生图/IP18-产线C-剧情配图文_2115261158931390465.json, 图片生成/图生图/Qwen Image Edit 2511-支持多图编辑_2003669560404418561.json, 图片生成/图生图/Qwen2511单图参考编辑-基础工作流_2077929626973855745.json, 图片生成/图生图/Qwen2511单图参考编辑-基础工作流_2078293379229773826.json, 图片生成/图生图/三视图不同视角 +换装+换脸 角色一致 真人动漫人物模特角人物保持不变 批量生成Qwen edit_2046776274835738626.json, 图片生成/图生图/三视图真人动漫人物一致性_2044054645772918786.json, 图片生成/图生图/三视图真人动漫人物一致性_2096509010789879809.json, 图片生成/图生图/三视图真人动漫人物一致性_2096865661921357826.json, 图片生成/图生图/三视图真人动漫人物一致性千问2511_2027669340207714306.json, 图片生成/图生图/三视图真人动漫人物一致性千问2511_2064291118820446209.json, 图片生成/图生图/人物三视图+8K-4K还原高清放大 -极速修复细节还原 真人动漫人物一致性千问2511_2042414561231380481.json, 图片生成/图生图/免费_开源_2511_角色设计+数字人_三视图真人动漫人物一致性_2105113829679124482.json, 图片生成/图生图/免费_开源_2511_角色设计+数字人_三视图真人动漫人物一致性_2105489655511740417.json, 图片生成/文生图/人物三视图-高一致性_2062129476934389761.json, 平台全量/三视图+换装+换脸 色一致性真人动漫人物模特角Qwen edit 千问2511  人物保持不变 批量_2040975191634878466.json, 数字人/数字人/免费 开源 2511 角色设计+数字人 三视图真人动漫人物一致性_2101744942149357570.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_26

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/2511单图参考编辑_bf16-基础工作流_2076904369496346625.json、图片生成/图生图/FireRed-Image-Edit + OpenClaw：打造高考倒计时大屏，每天自动生成不重样！_2025468706289094658.json、图片生成/图生图/IP18-产线C-剧情配图文_2115261158931390465.json、图片生成/图生图/Qwen Image Edit 2511-支持多图编辑_2003669560404418561.json、图片生成/图生图/Qwen2511单图参考编辑-基础工作流_2077929626973855745.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 18 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 14/18 个有
- `ImageConcanate` —— 13/18 个有
- `CR Text` —— 12/18 个有
- `SDXL Empty Latent Image` —— 12/18 个有
- `EmptySD3LatentImage` —— 6/18 个有
- `Fast Groups Bypasser (rgthree)` —— 3/18 个有
- `ResizeImagesByLongerEdge` —— 3/18 个有
- `TTResolutionSelector` —— 3/18 个有
- `UnetLoaderGGUF` —— 3/18 个有
- `Label (rgthree)` —— 1/18 个有
- `Seed (rgthree)` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 12 | 18 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 12，18 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（17/18 个样本）：Steps较低可能导致细节不足
