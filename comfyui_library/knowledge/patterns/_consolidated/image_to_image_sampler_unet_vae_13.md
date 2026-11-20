---
name: image_to_image_sampler_unet_vae_13
type: Image To Image
frequency: 12
level: weak
coverage: 0.85125
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/MOSS Image SFT洗图_2115238971512016897.json, 图片生成/图生图/87time QW 图生图_2054463234631061505.json, 图片生成/图生图/AI一键换脸-Qwen2511工作流_2094961251532234753.json, 图片生成/图生图/AI修手-Qwen-Edit指令修图工作流_2095002727083495426.json, 图片生成/图生图/GS-多视角人物场景都可_2061465943561293825.json, 图片生成/图生图/Krea2图生图重绘多张对比版本，一键无脑_2091851062343983106.json, 图片生成/图生图/Krea2图生图重绘多张对比，_2101865451822338049.json, 图片生成/图生图/QWEN一键单图直出多角度场景图生图_2061991338425536513.json, 图片生成/图生图/Qwen Edit 2509多图编辑_2001660412015853570.json, 图片生成/图生图/Qwen-Edit-一键角度编辑器_1990319553639051265.json, 图片生成/图生图/Qwen_Camera_Control_Pro_1990243371115573250.json, 平台全量/Qwen-Edit-多角度镜头切换-【2025-11-13】_2008801100790501377.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_13

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/反推提示词/MOSS Image SFT洗图_2115238971512016897.json、图片生成/图生图/87time QW 图生图_2054463234631061505.json、图片生成/图生图/AI一键换脸-Qwen2511工作流_2094961251532234753.json、图片生成/图生图/AI修手-Qwen-Edit指令修图工作流_2095002727083495426.json、图片生成/图生图/GS-多视角人物场景都可_2061465943561293825.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 10/12 个有
- `LoraLoaderModelOnly` —— 9/12 个有
- `TextEncodeQwenImageEditPlus` —— 8/12 个有
- `PrimitiveStringMultiline` —— 7/12 个有
- `CFGNorm` —— 6/12 个有
- `CLIPTextEncode` —— 6/12 个有
- `ModelSamplingAuraFlow` —— 6/12 个有
- `Image Comparer (rgthree)` —— 4/12 个有
- `AILab_QwenVL` —— 3/12 个有
- `Label (rgthree)` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `easy imageSize` —— 3/12 个有
- `CameraControlPromptNode` —— 2/12 个有
- `PreviewAny` —— 2/12 个有
- `Display Any (rgthree)` —— 1/12 个有
- `LayerUtility: PurgeVRAM` —— 1/12 个有
- `ReferenceLatent` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 10 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 10 | 50% |
| 采样算法 | euler | - | 10 | 80% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 0.3 - 1 | 10 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，10 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 80%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，10 个样本
- 高发问题（27/12 个样本）：Steps较低可能导致细节不足
