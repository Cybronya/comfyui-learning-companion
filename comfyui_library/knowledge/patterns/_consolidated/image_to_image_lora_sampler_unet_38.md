---
name: image_to_image_lora_sampler_unet_38
type: Image To Image
frequency: 12
level: strong
coverage: 0.73925
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/42. 专业级证件照生成，参数区输入证件照模版和处理图片+背景+服装+领带，即可出单张和9张图片_1974772408315940866.json, 图片生成/图生图/GS-多视角人物场景都可_2061465943561293825.json, 图片生成/图生图/QWEN一键单图直出多角度场景图生图_2061991338425536513.json, 图片生成/图生图/QWEN快速换装秒出图_1985441625268699137.json, 图片生成/图生图/Qwen去水印+高清处理_2011600241761456129.json, 图片生成/图生图/人物动作迁移 保持一致性 Qwen-edit多图编辑_1973243474298449922.json, 图片生成/图生图/人物动作迁移_2004095655121436673.json, 图片生成/图生图/人物换衣服_2095498989033578497.json, 图片生成/图生图/人物换衣服加速版qwen edit plus+全节点注释_2055626898692157442.json, 图片生成/图生图/人物换衣服加速版qwen+edit+plus+全节点注释_2060616197187657729.json, 图片生成/图生图/人物生成换装工作流_2065382569604116482.json, 图片生成/文生图/人物换衣服加速版qwen edit plus+全节点注释_2055669100139040769.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_38

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/42. 专业级证件照生成，参数区输入证件照模版和处理图片+背景+服装+领带，即可出单张和9张图片_1974772408315940866.json、图片生成/图生图/GS-多视角人物场景都可_2061465943561293825.json、图片生成/图生图/QWEN一键单图直出多角度场景图生图_2061991338425536513.json、图片生成/图生图/QWEN快速换装秒出图_1985441625268699137.json、图片生成/图生图/Qwen去水印+高清处理_2011600241761456129.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 11/12 个有
- `VAEDecode` —— 11/12 个有
- `ConditioningZeroOut` —— 10/12 个有
- `easy imageConcat` —— 7/12 个有
- `CR Simple Image Compare` —— 6/12 个有
- `PreviewImage` —— 5/12 个有
- `DWPreprocessor` —— 2/12 个有
- `RHHiddenNodes` —— 2/12 个有
- `CLIPTextEncode` —— 1/12 个有
- `CompressImages` —— 1/12 个有
- `EmptyHunyuanLatentVideo` —— 1/12 个有
- `PathchSageAttentionKJ` —— 1/12 个有
- `PrimitiveString` —— 1/12 个有
- `RBGImageStitchPlus` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 12 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/12 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，12 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（27/12 个样本）：Steps较低可能导致细节不足
