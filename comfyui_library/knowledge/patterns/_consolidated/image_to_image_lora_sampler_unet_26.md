---
name: image_to_image_lora_sampler_unet_26
type: Image To Image
frequency: 16
level: strong
coverage: 0.916625
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2026最新定制多角度工作流_2098278239079849985.json, 图片生成/图生图/2511 qwen-多姿势-多角度-场景人物一致性-林耀_2014624380260716546.json, 图片生成/图生图/2511 qwen-多姿势-多角度-场景人物一致性_2001919636952236034.json, 图片生成/图生图/2511任意模特角度、产品角度（自用工具）_2044794023109464066.json, 图片生成/图生图/2511可视化多角度变化_2013079283643715586.json, 图片生成/图生图/AI脑洞狮--相机多角度出图_2033939766948925441.json, "图片生成/图生图/Qwen Edit 2511+镜头多角度控制,一张图片变换多个角度+全节点注释_2052228383840452610.json", 图片生成/图生图/Qwen edit 2511 单图出多镜头（3d可视化操作）_2010373825388613634.json, 图片生成/图生图/Qwen-Edit-2511可视化视角编辑 直观改变万物视角_2010541642947764225.json, 图片生成/图生图/Qwen2511-AI漫剧分镜视角生成（极速版）_2010535252258725889.json, 图片生成/图生图/Qwen_Edit_2511_Multiangle图片角度自由控制_2077221377760911362.json, 图片生成/图生图/qwen_image_edit  _ 精准镜头控制器 _ 模特套图_2037780822270418946.json, 图片生成/图生图/qwen_image_edit 精准镜头控制器  模特套图 商品套图_2034504749021663233.json, 图片生成/图生图/qwen_image_edit 精准镜头视角控制器  模特套图 商品套图_2037729340846252034.json, 图片生成/图生图/【阡陌】Qwen-Eidt-2511可视化视角控制生成工作流_2011005734066069506.json, 图片生成/图生图/一键五视图+可控多镜头（Qwen Multiangle Camera）_2010989708263821313.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_26

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/2026最新定制多角度工作流_2098278239079849985.json、图片生成/图生图/2511 qwen-多姿势-多角度-场景人物一致性-林耀_2014624380260716546.json、图片生成/图生图/2511 qwen-多姿势-多角度-场景人物一致性_2001919636952236034.json、图片生成/图生图/2511任意模特角度、产品角度（自用工具）_2044794023109464066.json、图片生成/图生图/2511可视化多角度变化_2013079283643715586.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenMultiangleCameraNode` —— 14/16 个有
- `ModelSamplingAuraFlow` —— 13/16 个有
- `CFGNorm` —— 12/16 个有
- `FluxKontextMultiReferenceLatentMethod` —— 12/16 个有
- `ImageScaleToTotalPixels` —— 12/16 个有
- `easy promptList` —— 9/16 个有
- `easy showAnything` —— 6/16 个有
- `ConditioningZeroOut` —— 4/16 个有
- `FluxKontextImageScale` —— 3/16 个有
- `Int` —— 3/16 个有
- `PreviewImage` —— 2/16 个有
- `RHHiddenNodes` —— 2/16 个有
- `easy cleanGpuUsed` —— 2/16 个有
- `AspectRatio` —— 1/16 个有
- `Compare` —— 1/16 个有
- `EmptySD3LatentImage` —— 1/16 个有
- `InversionDemoLazySwitch` —— 1/16 个有
- `JjkText` —— 1/16 个有
- `PlaySound|pysssss` —— 1/16 个有
- `UnetLoaderGGUF` —— 1/16 个有
- `easy promptLine` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 16 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 88% |
| 调度器 | simple | - | 16 | 88% |
| 重绘幅度 | 1 | 0.95 - 1 | 16 | 99% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，16 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 88%
- 调度器 最常用 simple，16 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 0.95 - 1，16 个样本，取值集中（一致性 99%）
- 高发问题（17/16 个样本）：Steps较低可能导致细节不足
