---
name: unknown_workflow_lora_sampler_unet_41
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.962357
common_nodes: [CLIPLoader, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Edit-2511文生图3D国漫CG风格_2079515568432046082.json, 图片生成/文生图/Qwen-Edit手机上的3D城市_2032281919450255362.json, 图片生成/文生图/Qwen-Image Edit Plus换装双人同框_1994201692587622402.json, 图片生成/文生图/Qwen_Edit_2509古书上的3D插画_1989311154684129281.json, 图片生成/文生图/Qwen_Edit_2509微缩城市鸟瞰_1988774900942909442.json, 图片生成/文生图/Qwen_Edit_2509手机上的3D人物_1989695013087047682.json, 图片生成/文生图/Qwen_Edit_2509手机上的3D城市_1989171870014517249.json, 图片生成/文生图/Qwen_Edit_2509手机上的3D城市_2046760188522274818.json, 图片生成/文生图/Qwen_Edit_2509手机上的3D城市_2082741081346764801.json, 图片生成/文生图/Qwen_Edit_2509胶囊城市_1988927261430648834.json, 图片生成/文生图/Qwen_Edit_3D城市3D微景观_2011800399782617090.json, 图片生成/文生图/上传图片+手动输入提示词来生成下一场景+全节点注释_2055618848560295937.json, 图片生成/文生图/换装同服装双人或者多人同框_1994237410244493314.json, 平台全量/图片转手绘 Qwen Image Edit 2509 真实图片转漫画卡通风格_1993150543153610753.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_41

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Qwen-Edit-2511文生图3D国漫CG风格_2079515568432046082.json、图片生成/文生图/Qwen-Edit手机上的3D城市_2032281919450255362.json、图片生成/文生图/Qwen-Image Edit Plus换装双人同框_1994201692587622402.json、图片生成/文生图/Qwen_Edit_2509古书上的3D插画_1989311154684129281.json、图片生成/文生图/Qwen_Edit_2509微缩城市鸟瞰_1988774900942909442.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 13/14 个有
- `EmptyLatentImage` —— 13/14 个有
- `ModelSamplingAuraFlow` —— 13/14 个有
- `ImageScaleToTotalPixels` —— 4/14 个有
- `LoadImage` —— 4/14 个有
- `ConstrainImage|pysssss` —— 3/14 个有
- `BiRefNetRMBG` —— 2/14 个有
- `LayerUtility: ExtendCanvas` —— 2/14 个有
- `CR Latent Input Switch` —— 1/14 个有
- `CR SDXL Aspect Ratio` —— 1/14 个有
- `CR Text` —— 1/14 个有
- `Image Comparer (rgthree)` —— 1/14 个有
- `RH_Translator` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 720 - 1920 | 13 | 77% |
| 高度 | 1280 | 720 - 1920 | 13 | 68% |
| 采样步数 | 4 | 4 - 8 | 14 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 720 - 1920，13 个样本
- 高度 中位数 1280，观测区间 720 - 1920，13 个样本
- 采样步数 中位数 4，观测区间 4 - 8，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（17/14 个样本）：Steps较低可能导致细节不足
