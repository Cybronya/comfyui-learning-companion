---
name: text_to_image_sampler_clip_unet_43
type: Text To Image
frequency: 13
level: strong
coverage: 0.938615
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image文生图 基础版 lora模型加载_2001116171342577665.json, 图片生成/文生图/z-image文生图工作流_1998291742837366786.json, 图片生成/文生图/z-image文生图工作流_2001830276877697026.json, 图片生成/文生图/z-image文生图工作流_2002604407730630657.json, 图片生成/文生图/z-image文生图工作流_2009919536497168386.json, 图片生成/文生图/z-image文生图工作流_2089710476165992450.json, 图片生成/文生图/z-image文生图工作流_2098948533117345794.json, 图片生成/文生图/z-image文生图工作流_2101933018976968706.json, 图片生成/文生图/z-image文生图工作流（B02）_2056384805872431106.json, 图片生成/文生图/z-image文生图工作流（不油腻超写实）_2099020153999675394.json, 图片生成/文生图/z-image文生图工作流（不油腻超写实）_2099402532144635906.json, 图片生成/文生图/z-image文生图工作流（超写实）_2100510837722148865.json, 图片生成/文生图/提示词润色 文生图 图片编辑_2103111585429549057.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_43

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/z-image文生图 基础版 lora模型加载_2001116171342577665.json、图片生成/文生图/z-image文生图工作流_1998291742837366786.json、图片生成/文生图/z-image文生图工作流_2001830276877697026.json、图片生成/文生图/z-image文生图工作流_2002604407730630657.json、图片生成/文生图/z-image文生图工作流_2009919536497168386.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 5/13 个有
- `LoraLoaderModelOnly` —— 5/13 个有
- `UpscaleModelLoader` —— 4/13 个有
- `ImageFromBatch` —— 3/13 个有
- `LayerColor: BrightnessContrastV2` —— 3/13 个有
- `PreviewImage` —— 3/13 个有
- `easy promptList` —— 3/13 个有
- `AILab_QwenVL` —— 2/13 个有
- `CR Text` —— 2/13 个有
- `CR Text Concatenate` —— 2/13 个有
- `QWEN_TextDisplay` —— 2/13 个有
- `CFGNorm` —— 1/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/13 个有
- `LoadImage` —— 1/13 个有
- `RH_Nano_Banana_Image2Image` —— 1/13 个有
- `Upscale Model Loader` —— 1/13 个有
- `ZML_LoadImage` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 6 - 10 | 13 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 1024 | 1024 - 1920 | 13 | 78% |
| 高度 | 1536 | 720 - 1920 | 13 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 6 - 10，13 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1920，13 个样本
- 高度 中位数 1536，观测区间 720 - 1920，13 个样本
- 高发问题（9/13 个样本）：Steps较低可能导致细节不足
