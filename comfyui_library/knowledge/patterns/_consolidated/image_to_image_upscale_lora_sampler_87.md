---
name: image_to_image_upscale_lora_sampler_87
type: Image To Image
frequency: 2
level: weak
coverage: 0.7325
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageScaleBy, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, TT_img_enc, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【动漫转真人】Qwen+Z-image_支持文本修改&去水印&加密_真实洗图_2030319073132814338.json, 图片生成/图生图/【楚心钟陌】Qwen+ZI二次元转真人，真实感洗图(本地API调用)_2001670288888721409.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_87

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【动漫转真人】Qwen+Z-image_支持文本修改&去水印&加密_真实洗图_2030319073132814338.json、图片生成/图生图/【楚心钟陌】Qwen+ZI二次元转真人，真实感洗图(本地API调用)_2001670288888721409.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `TT_img_enc`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `AILab_ImageStitch` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `DF_Text_Box` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `Int` —— 1/2 个有
- `JoinStrings` —— 1/2 个有
- `RH_ExecuteNode` —— 1/2 个有
- `RH_ImageUploaderNode` —— 1/2 个有
- `RH_NodeInfoListNode` —— 1/2 个有
- `RH_SettingsNode` —— 1/2 个有
- `ResizeImageNode` —— 1/2 个有
- `SaveLatent` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy boolean` —— 1/2 个有
- `easy imageSwitch` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6.5 | - | 2 | 77% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 50% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 50% |
| 重绘幅度 | 0.8 | - | 2 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6.5，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 50%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 50%
- 重绘幅度 中位数 0.8，样本不足，未给区间，2 个样本
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
