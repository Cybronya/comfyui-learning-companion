---
name: unknown_workflow_sampler_clip_unet_14
type: Unknown Workflow
frequency: 29
level: weak
coverage: 0.85031
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/hidream_i1_dev.json, comfyui-workflow-templates-json/hidream_i1_fast.json, comfyui-workflow-templates-json/hidream_i1_full.json, 图片生成/图生图/Z-Image_turbo文生图-又快又好_2101288087241445378.json, 图片生成/图生图/Z-image-base文生图（新国风浮世绘）_2016739215698038785.json, 图片生成/图生图/qwen2512粗线条水墨_2070337251640434689.json, 图片生成/文生图/QwenImage 4K高清大图DyPE直出_2000788947687141378.json, 图片生成/文生图/Z-Image-Turbo 4K高清大图DyPE直出_2000758971898134529.json, 图片生成/文生图/qwen-image2512-q版风格动漫_2056048226654015490.json, 图片生成/文生图/qwen-image2512q版3d风格_2057869164727062530.json, 图片生成/文生图/qwen2512定格玩偶_2037359907288125442.json, 图片生成/文生图/qwen2512日系动漫素描_2032364402506211330.json, 图片生成/文生图/qwen2512水墨中式枯笔焦墨勾线插画_2062947076870336513.json, 图片生成/文生图/qwen2512水墨国风_2063805351761367042.json, 图片生成/文生图/qwen2512粗线条水墨_2067961144140197890.json, 图片生成/文生图/qwen2512粗线条水墨_2068857089002393601.json, 图片生成/文生图/qwen2512粗线条水墨_2069676975639326721.json, 图片生成/文生图/qwen2512粗线条水墨_2080477072551665665.json, 图片生成/文生图/qwen2512粗线条水墨_2080481494887391233.json, 图片生成/文生图/qwen2512粗线条水墨_2112167137883283458.json, 图片生成/文生图/qwen2512线条感动漫_2033458216113278977.json, 图片生成/文生图/qwen2512马克笔插画_2047576499305320449.json, 图片生成/文生图/qwen2512马克笔插画_2067421994693521410.json, 图片生成/文生图/qwen2512马克笔插画_2069671724421046273.json, 图片生成/文生图/qwen2512马克笔插画_2080470094504873985.json, 图片生成/文生图/qwen2512马克笔插画_2080472510591750146.json, 图片生成/文生图/qwen2512马克笔插画_2081934496953356289.json, 图片生成/文生图/手绘画本_2022488976958951425.json, 视频生成/图生视频/qwen-image2512q版3d风格_2067062569453576193.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_14

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（comfyui-workflow-templates-json/hidream_i1_dev.json、comfyui-workflow-templates-json/hidream_i1_fast.json、comfyui-workflow-templates-json/hidream_i1_full.json、图片生成/图生图/Z-Image_turbo文生图-又快又好_2101288087241445378.json、图片生成/图生图/Z-image-base文生图（新国风浮世绘）_2016739215698038785.json…）

- **类型**：Unknown Workflow
- **样本数**：29
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 29 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 26/29 个有
- `LoraLoaderModelOnly` —— 25/29 个有
- `ModelSamplingAuraFlow` —— 25/29 个有
- `Text Multiline` —— 24/29 个有
- `LatentUpscaleBy` —— 22/29 个有
- `Text Concatenate` —— 22/29 个有
- `EG_K_LATENT` —— 6/29 个有
- `ModelSamplingSD3` —— 3/29 个有
- `QuadrupleCLIPLoader` —— 3/29 个有
- `DyPE_FLUX` —— 2/29 个有
- `ConditioningZeroOut` —— 1/29 个有
- `LoraLoader` —— 1/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 8 - 50 | 29 | 24% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 29 | 28% |
| 采样算法 | euler_ancestral | - | 29 | 59% |
| 调度器 | simple | - | 29 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 29 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/29 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 8 - 50，29 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，29 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 euler_ancestral，29 个样本，一致性 59%
- 调度器 最常用 simple，29 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
