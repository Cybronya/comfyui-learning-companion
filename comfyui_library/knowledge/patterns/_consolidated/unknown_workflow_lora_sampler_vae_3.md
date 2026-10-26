---
name: unknown_workflow_lora_sampler_vae_3
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.937667
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2511 multi angle可视化角度编辑V2_2009735363601895426.json, 图片生成/图生图/Qwen Image Edit 2511-支持多图编辑_2003669560404418561.json, 图片生成/图生图/Qwen2511-multi angle-精准控制图像镜头_2009798078206844929.json, 图片生成/图生图/Qwenedit-2511 多角度可视化角度编辑_2010887390902095874.json, 图片生成/图生图/三视图不同视角 +换装+换脸 角色一致 真人动漫人物模特角人物保持不变 批量生成Qwen edit_2046776274835738626.json, 图片生成/图生图/三视图真人动漫人物一致性_2044054645772918786.json, 图片生成/图生图/三视图真人动漫人物一致性_2096509010789879809.json, 图片生成/图生图/三视图真人动漫人物一致性_2096865661921357826.json, 图片生成/图生图/三视图真人动漫人物一致性千问2511_2027669340207714306.json, 图片生成/图生图/三视图真人动漫人物一致性千问2511_2064291118820446209.json, 图片生成/图生图/人物三视图+8K-4K还原高清放大 -极速修复细节还原 真人动漫人物一致性千问2511_2042414561231380481.json, 图片生成/图生图/免费_开源_2511_角色设计+数字人_三视图真人动漫人物一致性_2105113829679124482.json, 图片生成/图生图/免费_开源_2511_角色设计+数字人_三视图真人动漫人物一致性_2105489655511740417.json, 图片生成/图生图/可视化分镜角度编辑Qwen 2511 multi angle-V2_2011338342184525826.json, 图片生成/图生图/可视化角度编辑 （多机位）Qwen 2511 multi angle_2010360280441692162.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_3

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Qwen 2511 multi angle可视化角度编辑V2_2009735363601895426.json、图片生成/图生图/Qwen Image Edit 2511-支持多图编辑_2003669560404418561.json、图片生成/图生图/Qwen2511-multi angle-精准控制图像镜头_2009798078206844929.json、图片生成/图生图/Qwenedit-2511 多角度可视化角度编辑_2010887390902095874.json、图片生成/图生图/三视图不同视角 +换装+换脸 角色一致 真人动漫人物模特角人物保持不变 批量生成Qwen edit_2046776274835738626.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 15 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 10/15 个有
- `ImageScaleToTotalPixels` —— 10/15 个有
- `UNETLoader` —— 10/15 个有
- `CR Text` —— 9/15 个有
- `SDXL Empty Latent Image` —— 9/15 个有
- `EmptySD3LatentImage` —— 6/15 个有
- `CheckpointLoaderSimple` —— 5/15 个有
- `QwenMultiangleCameraNode` —— 5/15 个有
- `easy promptList` —— 5/15 个有
- `easy showAnything` —— 5/15 个有
- `Fast Groups Bypasser (rgthree)` —— 2/15 个有
- `RH_Translator` —— 1/15 个有
- `ShowText` —— 1/15 个有
- `easy getNode` —— 1/15 个有
- `easy setNode` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 15 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
