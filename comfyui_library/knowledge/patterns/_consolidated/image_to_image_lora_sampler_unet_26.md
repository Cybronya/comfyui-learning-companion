---
name: image_to_image_lora_sampler_unet_26
type: Image To Image
frequency: 15
level: strong
coverage: 0.892067
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/2026最新定制多角度工作流_2098278239079849985.json, 图片生成/图生图/2511 qwen-多姿势-多角度-场景人物一致性-林耀_2014624380260716546.json, 图片生成/图生图/2511 qwen-多姿势-多角度-场景人物一致性_2001919636952236034.json, 图片生成/图生图/2511任意模特角度、产品角度（自用工具）_2044794023109464066.json, 图片生成/图生图/42. 专业级证件照生成，参数区输入证件照模版和处理图片+背景+服装+领带，即可出单张和9张图片_1974772408315940866.json, "图片生成/图生图/Qwen Edit 2511+镜头多角度控制,一张图片变换多个角度+全节点注释_2052228383840452610.json", 图片生成/图生图/Qwen Image Edit2511 -改变角度_2033741078267957249.json, 图片生成/图生图/Qwen Multiangle Camera 多角度切换_2009905557972459522.json, 图片生成/图生图/Qwen edit 2511 单图出多镜头（3d可视化操作）_2010373825388613634.json, 图片生成/图生图/Qwen-Multiangle-任意角度镜头切换_2026976393363460098.json, 图片生成/图生图/九个视角 人物道具 场景视角 加速版_2034191846393520129.json, 图片生成/图生图/千问多角度控制lora_2013230266269044737.json, 图片生成/图生图/千问多角度控制lora_2016779041151393794.json, 图片生成/图生图/千问多角度控制lora，手动控制_2013226905612324866.json, 图片生成/图生图/千问多角度控制lora，手动控制_2033440618382364673.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_26

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/2026最新定制多角度工作流_2098278239079849985.json、图片生成/图生图/2511 qwen-多姿势-多角度-场景人物一致性-林耀_2014624380260716546.json、图片生成/图生图/2511 qwen-多姿势-多角度-场景人物一致性_2001919636952236034.json、图片生成/图生图/2511任意模特角度、产品角度（自用工具）_2044794023109464066.json、图片生成/图生图/42. 专业级证件照生成，参数区输入证件照模版和处理图片+背景+服装+领带，即可出单张和9张图片_1974772408315940866.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 14/15 个有
- `CFGNorm` —— 12/15 个有
- `ImageScaleToTotalPixels` —— 12/15 个有
- `ModelSamplingAuraFlow` —— 12/15 个有
- `QwenMultiangleCameraNode` —— 12/15 个有
- `FluxKontextMultiReferenceLatentMethod` —— 11/15 个有
- `PreviewAny` —— 8/15 个有
- `easy promptList` —— 7/15 个有
- `ConditioningZeroOut` —— 5/15 个有
- `Int` —— 3/15 个有
- `RHHiddenNodes` —— 3/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/15 个有
- `easy cleanGpuUsed` —— 2/15 个有
- `PathchSageAttentionKJ` —— 1/15 个有
- `PrimitiveString` —— 1/15 个有
- `RBGImageStitchPlus` —— 1/15 个有
- `easy imageConcat` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 8 | 15 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 80% |
| 调度器 | simple | - | 15 | 80% |
| 重绘幅度 | 1 | 0.95 - 1 | 15 | 99% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/15 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 8，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 80%
- 调度器 最常用 simple，15 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.95 - 1，15 个样本，取值集中（一致性 99%）
- 高发问题（16/15 个样本）：Steps较低可能导致细节不足
